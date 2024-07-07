import argparse
import csv
import datetime
import os
import sys
import re
import socket
import sys
import time
import urllib
import urllib.parse
from concurrent.futures import ALL_COMPLETED, ThreadPoolExecutor, wait
import requests
import urllib3
from certifi.__main__ import args

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
DEBUG = False


"""
文件  file
最大线程
允许跳转
错误重扫次数
代理
输出文件
超时时间
输出标题


"""


class whichAlive(object):
    def __init__(self, file, THREAD_POOL_SIZE=10, allow_redirect=False, TRYAGAIN=False, PROXY={}, nooutfile=False, timeout=10):
        """
        初始化 whichAlive 类，设置必要的属性。

        Args:
        - file: 包含 URL 的文件对象或标准输入流。
        - THREAD_POOL_SIZE: 最大线程数，用于并发请求（默认为 10）。
        - allow_redirect: 是否允许 HTTP 重定向（默认为 False）。
        - TRYAGAIN: 如果发生错误，是否重试扫描 URL（默认为 False）。
        - PROXY: 字典，指定 HTTP/HTTPS 代理（默认为空字典）。
        - nooutfile: 是否禁止输出到文件（默认为 False）。
        - timeout: 请求超时时间，单位为秒（默认为 10）。

        初始化各种属性，包括文件处理、从文件中提取 URL、线程池大小、重试设置、代理配置和超时设置。
        """
        self.script_path = os.path.dirname(__file__)  # 脚本所在目录路径
        self.file = file  # 包含 URL 的文件对象或标准输入流
        self.nooutfile = nooutfile  # 是否禁止输出到文件的标志
        if not self.nooutfile:
            self.timenow = time.strftime("%Y%m%d%H%M%S", time.localtime(time.time()))  # 当前时间戳
            self.outfilename = f'{self.timenow}.csv'  # 输出的 CSV 文件名
            self.errorfilename = f'error_{self.timenow}.txt'  # 错误日志文件名
        self.urllist = self.__urlfromfile()  # 从文件/流中提取的 URL 列表
        self.tableheader = ['no', 'url', 'ip', 'state',
                            'state_code', 'title', 'server', 'length', 'other']  # CSV 输出的表头
        self.HEADER = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36',
        }  # 请求的 HTTP 头部信息
        self.THREAD_POOL_SIZE = THREAD_POOL_SIZE  # 最大并发线程数
        self.TRYAGAIN = TRYAGAIN  # 失败时是否重试的标志
        self.allurlnumber = len(self.urllist)  # 待扫描的 URL 总数
        self.completedurl = -1  # 已完成扫描的 URL 计数器
        self.allow_redirect = allow_redirect  # 是否允许 HTTP 重定向的标志
        self.PROXY = PROXY  # 代理配置字典
        self.timeout = timeout  # 请求超时时间

    def run(self):
        """
        执行主要的扫描过程。
        """
        self.completedurl += 1
        if not self.nooutfile:
            self.__writetofile(self.tableheader)  # 写入 CSV 文件头部
        tasklist = []
        start_time = datetime.datetime.now()
        t = ThreadPoolExecutor(max_workers=self.THREAD_POOL_SIZE)
        for k, url in enumerate(self.urllist):
            tasklist.append(t.submit(self.__scan, url, k + 1, self.TRYAGAIN))  # 提交 URL 扫描任务
        print(f'total {self.allurlnumber}')
        if wait(tasklist, return_when=ALL_COMPLETED):
            end_time = datetime.datetime.now()
            print(f'--------------------------------\nDONE, use {(end_time - start_time).seconds} seconds')
            if not self.nooutfile:
                print(f'outfile: {os.path.join(os.path.abspath(os.path.dirname(__file__)), "result", self.outfilename)}')


    def __scan(self, url, no, tryagainflag=False):
        """
        扫描单个URL并输出扫描结果。

        Parameters:
        - url (str): 要扫描的URL。
        - no (int): URL在列表中的编号。
        - tryagainflag (bool, optional): 是否重试标志。

        Returns:
        - None

        Raises:
        - ConnectTimeout: 连接超时异常。
        - ReadTimeout: 读取超时异常。
        - ConnectionError: 连接错误异常。
        - Exception: 其他未处理的异常。
        """

        def callback(no, url, ip, state, state_code, title, server, length, other):
            """
            回调函数，处理扫描结果并输出。

            Parameters:
            - no (int): URL在列表中的编号。
            - url (str): 扫描的URL。
            - ip (str): IP地址。
            - state (str): 状态，'alive' 表示存活，'dead' 表示不存活。
            - state_code (str): 状态码。
            - title (str): 网页标题。
            - server (str): 服务器信息。
            - length (str): 内容长度。
            - other (str): 其他信息。

            Returns:
            - None
            """
            self.completedurl += 1
            thisline = [no, url, ip, state, state_code,
                        title, server, length, other]
            nowpercent = '%.2f' % ((self.completedurl / self.allurlnumber) * 100)
            if state == 'alive':
                print(f'[{nowpercent}%] {url} | {ip} | \033[0;32;40m{state}\033[0m | {title} | {length}')
            else:
                print(f'[{nowpercent}%] {url} | {ip} | \033[0;31;40m{state}\033[0m | {title} | {length}')
            if not self.nooutfile:
                self.__writetofile(thisline)

        # 初始化各变量
        ip = '-1'
        state = '-1'
        state_code = -1
        title = '-1'
        server = '-1'
        length = -1
        other = '-1'

        try:
            # 调试模式下输出调试信息
            if DEBUG:
                print(f'[debug] {no} {url}')

            # 如果URL不以'http://'或'https://'开头，则默认加上'http://'
            if not url.startswith('http://') and not url.startswith('https://'):
                url = 'http://' + url

            # 解析URL获取域名部分，并通过域名获取IP地址
            u = urllib.parse.urlparse(url)
            # ip = self.__getwebip(u.netloc.split(':')[0])

            # 发送HTTP请求判断网站是否存活
            if self.allow_redirect:
                # 允许重定向时的处理逻辑
                r = requests.get(url=url, headers=self.HEADER,
                                 timeout=self.timeout, verify=False, proxies=self.PROXY)
                state = r.status_code

            else:
                # 不允许重定向时的处理逻辑
                r = requests.get(url=url, headers=self.HEADER, allow_redirects=False,
                                 timeout=self.timeout, verify=False, proxies=self.PROXY)
                state = r.status_code

            # 调用回调函数处理扫描结果
            callback(no, url, ip, state, state_code, title, server, length, other)

        # 处理各种异常情况
        except requests.exceptions.ConnectTimeout as e:
            # 如果开启了 DEBUG 模式，则打印连接超时的错误信息
            if DEBUG:
                print(f'[ERROR][SCAN][ConnectTimeout] {url} {e}')
            # 记录错误信息到错误报告中
            self.__errorreport(str(e))
            # 标记状态为 'dead'，表示连接失败
            state = '连接超时'
            # 调用回调函数，通知处理结果
            callback(no, url, ip, state, state_code, title, server, length, 'ConnectTimeout')

        except requests.exceptions.ReadTimeout as e:
            # 如果开启了 DEBUG 模式，则打印读取超时的错误信息
            if DEBUG:
                print(f'[ERROR][SCAN][ReadTimeout] {url} {e}')
            # 记录错误信息到错误报告中
            self.__errorreport(str(e))
            # 标记状态为 'dead'，表示读取失败
            state = '读取超时'
            # 调用回调函数，通知处理结果
            callback(no, url, ip, state, state_code, title, server, length, 'ReadTimeout')

        except requests.exceptions.ConnectionError as e:
            # 如果开启了 DEBUG 模式，则打印连接错误的错误信息
            if DEBUG:
                print(f'[ERROR][SCAN][ConnectionError] {url} {e}')
            # 记录错误信息到错误报告中
            self.__errorreport(str(e))
            # 标记状态为 'dead'，表示连接失败
            state = '连接错误'
            # 调用回调函数，通知处理结果
            callback(no, url, ip, state, state_code, title, server, length, 'ConnectionError')

        except Exception as e:
            # 如果开启了 DEBUG 模式，则打印其他未知异常的错误信息
            if DEBUG:
                print(f'[ERROR][SCAN][other] {no} {url} {e}')
            # 记录错误信息到错误报告中
            self.__errorreport(str(e))
            # 如果设置了重试标志，尝试再次扫描该 URL
            if tryagainflag:
                self.__scan(url, no, True)
            else:
                state = "未知错误"
            # 调用回调函数，通知处理结果
            callback(no, url, ip, state, state_code, title, server, length, 'e')


    def __urlfromfile(self) -> str:
        # tmp_list = [i.replace('\n', '').replace('\r', '')
        #             for i in self.file.readlines()]
        with open(self.file, "r") as fp:
            tmp_list = [line.strip('\n') for line in fp.readlines()]
        return tmp_list

    def __writetofile(self, data: list):
        if not self.nooutfile:
            f = open(f'{os.path.join(os.path.abspath(os.path.dirname(__file__)), "result", self.outfilename)}', 'a')
            writer = csv.writer(f)
            writer.writerow(data)
            f.close()

    def __errorreport(self, message):
        if not self.nooutfile:
            f = open(f'{os.path.join(os.path.abspath(os.path.dirname(__file__)), "error", self.errorfilename)}', 'a')
            f.write(message+'\n')
            f.close()

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    # 添加命令行参数
    parser.add_argument('-f', '--file', metavar='FILE', nargs='?',
                        type=argparse.FileType('r'), default="../url.txt", help='URL lists file.')

    file_path = "file/more_url1.txt"
    # fp.close()
    w = whichAlive(
        file=file_path,  # 文件对象或标准输入流
        THREAD_POOL_SIZE=100,  # 线程池大小
        # allow_redirect=(not args.noredirect),  # 是否允许重定向
        # PROXY={'http': args.proxy, 'https': args.proxy},  # 代理设置
        nooutfile=True,  # 是否输出到文件
        # timeout=10  # 请求超时时间
    )

    # 运行 whichAlive 实例的主程序逻辑
    w.run()
