#!/usr/bin/env python
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

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
DEBUG = False

class whichAlive(object):
    def __init__(self, file, THREAD_POOL_SIZE=10, allow_redirect=False, TRYAGAIN=False, PROXY={}, nooutfile=False, timeout=10):
        self.script_path = os.path.dirname(__file__)
        self.file = file
        self.nooutfile = nooutfile
        if not self.nooutfile: self.timenow = time.strftime("%Y%m%d%H%M%S", time.localtime(time.time()))
        if not self.nooutfile: self.outfilename = f'{self.timenow}.csv'
        if not self.nooutfile: self.errorfilename = f'error_{self.timenow}.txt'
        self.urllist = self.__urlfromfile()
        self.tableheader = ['no', 'url', 'ip', 'state',
                            'state_code', 'title', 'server', 'length', 'other']
        self.HEADER = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36',
        }
        self.THREAD_POOL_SIZE = THREAD_POOL_SIZE
        self.TRYAGAIN = TRYAGAIN
        self.allurlnumber = len(self.urllist)
        self.completedurl = -1
        self.allow_redirect = allow_redirect
        self.PROXY = PROXY
        self.timeout = timeout

    def run(self):
        self.completedurl += 1
        if not self.nooutfile:
            self.__writetofile(self.tableheader)
        tasklist = []
        start_time = datetime.datetime.now()
        t = ThreadPoolExecutor(max_workers=self.THREAD_POOL_SIZE)
        for k, url in enumerate(self.urllist):
            tasklist.append(t.submit(self.__scan, url, k+1, self.TRYAGAIN))
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
        ip = ''
        state = ''
        state_code = -1
        title = ''
        server = ''
        length = -1
        other = ''

        try:
            # 调试模式下输出调试信息
            if DEBUG:
                print(f'[debug] {no} {url}')

            # 如果URL不以'http://'或'https://'开头，则默认加上'http://'
            if not url.startswith('http://') and not url.startswith('https://'):
                url = 'http://' + url

            # 解析URL获取域名部分，并通过域名获取IP地址
            u = urllib.parse.urlparse(url)
            ip = self.__getwebip(u.netloc.split(':')[0])

            # 发送HTTP请求判断网站是否存活
            if self.allow_redirect:
                # 允许重定向时的处理逻辑
                r = requests.get(url=url, headers=self.HEADER,
                                 timeout=self.timeout, verify=False, proxies=self.PROXY)
                state = 'alive'
                state_code = '->'.join([str(i.status_code)
                                        for i in r.history] + [str(r.status_code)])
                """
                # 获取所有重定向历史的状态码列表
                redirect_statuses = [str(i.status_code) for i in r.history]
                
                # 获取最终响应的状态码，并加入列表末尾
                final_status = str(r.status_code)
                redirect_statuses.append(final_status)
                
                # 将状态码列表用 '->' 连接成一个字符串
                state_code = '->'.join(redirect_statuses)
                """
                title = '->'.join([self.__getwebtitle(i)
                                   for i in r.history] + [self.__getwebtitle(r)])
                length = '->'.join([str(self.__getweblength(i))
                                    for i in r.history] + [str(self.__getweblength(r))])
                server = '->'.join([self.__getwebserver(i)
                                    for i in r.history] + [self.__getwebserver(r)])
            else:
                # 不允许重定向时的处理逻辑
                r = requests.get(url=url, headers=self.HEADER, allow_redirects=False,
                                 timeout=self.timeout, verify=False, proxies=self.PROXY)
                state = 'alive'
                state_code = str(r.status_code)
                title = self.__getwebtitle(r)
                length = str(self.__getweblength(r))
                server = self.__getwebserver(r)

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
                state = '未知错误'
            # 调用回调函数，通知处理结果
            callback(no, url, ip, state, state_code, title, server, length, 'e')

    def __getwebtitle(self, r) -> str:
        try:
            # 检查响应头中是否包含 Content-Type
            if r.headers.get('Content-Type'):
                try:
                    # 尝试从 Content-Type 中获取字符集信息
                    if r.headers.get('Content-Type').split('charset=')[1]:
                        charset = r.headers.get('Content-Type').split('charset=')[1]
                    # 如果 Content-Type 中没有字符集信息，尝试从 meta 标签中获取
                    elif re.findall(r'<meta charset=(.*?)>', r.text)[0].replace('\'', '').replace('"', ''):
                        charset = re.findall(r'<meta charset=(.*?)>', r.text)[0].replace('\'', '').replace('"', '')
                    else:
                        charset = 'utf8'
                except:
                    charset = 'utf8'
            else:
                charset = 'utf8'  # 如果没有 Content-Type，默认使用 utf-8 编码

            # 使用获取到的字符集解码响应内容，并从中提取网页标题
            return re.findall(r'<title>(.*?)</title>', r.content.decode(charset))[0]

        except:
            return ''  # 发生任何异常时返回空字符串

    def __getwebip(self, domain) -> str:
        try:
            ip = socket.getaddrinfo(domain, 'http')
            return ip[0][4][0]
        except:
            return ''

    def __getweblength(self, r) -> int:
        try:
            return len(r.content)
        except:
            return -1

    def __getwebserver(self, r) -> str:
        try:
            return r.headers.get('server') if r.headers.get('server') else ''
        except:
            return ''

    def __urlfromfile(self) -> str:
        tmp_list = [i.replace('\n', '').replace('\r', '')
                    for i in self.file.readlines()]
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


BANNER = """\
           __    _      __    ___    ___
 _      __/ /_  (_)____/ /_  /   |  / (_)   _____
| | /| / / __ \/ / ___/ __ \/ /| | / / / | / / _ \\
| |/ |/ / / / / / /__/ / / / ___ |/ / /| |/ /  __/
|__/|__/_/ /_/_/\___/_/ /_/_/  |_/_/_/ |___/\___/  \033[95mFAST\033[0m

\033[90mAbout: https://github.com/abelche/whichalive\033[0m
"""

HELP_MESSAGE = """FAST detect alive targets
  python whichalive-air.py -u url.txt
  cat url.txt | python whichalive-air.py\
"""

if __name__ == '__main__':
    # 打印程序的横幅信息
    print(BANNER)

    # 创建参数解析器对象，并设置其使用帮助消息为 HELP_MESSAGE
    parser = argparse.ArgumentParser(usage=HELP_MESSAGE)

    # 添加命令行参数
    parser.add_argument('-f', '--file', metavar='FILE', nargs='?',
                        type=argparse.FileType('r'), default=sys.stdin, help='URL lists file.')
    # --file 参数用于指定包含URL列表的文件，可以通过标准输入重定向，默认从标准输入读取

    parser.add_argument('--proxy', default='',
                        help='Set proxy, such as http://127.0.0.1:8080 or socks5://127.0.0.1:7777')
    # --proxy 参数用于设置代理，支持 http 和 socks5 协议

    parser.add_argument('-t', '--thread', default=20,
                        type=int, help='Set max threads, default 20')
    # -t 或 --thread 参数用于设置最大线程数，默认为 20

    parser.add_argument('--timeout', default=10,
                        type=int, help='Set request timeout value, default 10s')
    # --timeout 参数用于设置请求超时时间，默认为 10 秒

    parser.add_argument('-d', '--debug', default=False,
                        action='store_true', help='print some debug information')
    # -d 或 --debug 参数，如果设置了该参数，则打印一些调试信息

    parser.add_argument('--no-redirect', default=False,
                        action='store_true', help='Set to disallow redirect', dest='noredirect')
    # --no-redirect 参数，如果设置了该参数，则禁止重定向

    parser.add_argument('--try-again', default=False, action='store_true',
                        help='If some error, try again scan that url once', dest='tryagain')
    # --try-again 参数，如果设置了该参数，则在遇到错误时尝试再次扫描该 URL 一次

    parser.add_argument('--no-outfile', default=False, action='store_true',
                        help='Set to NOT output results to file', dest='nooutfile')
    # --no-outfile 参数，如果设置了该参数，则不将结果输出到文件

    # 解析命令行参数
    args = parser.parse_args()

    # 检查是否有标准输入，并且是 TTY
    if args.file == sys.stdin and sys.stdin.isatty():
        parser.print_help()
        sys.exit()

    # 根据命令行参数设置调试模式、重试标志和不输出到文件标志
    DEBUG = args.debug
    TRYAGAIN = args.tryagain
    NOOUTFILE = args.nooutfile

    # 创建 whichAlive 类的实例 w，并传入命令行参数解析后的相关设置
    w = whichAlive(
        file=args.file,  # 文件对象或标准输入流
        THREAD_POOL_SIZE=args.thread,  # 线程池大小
        allow_redirect=(not args.noredirect),  # 是否允许重定向
        PROXY={'http': args.proxy, 'https': args.proxy},  # 代理设置
        nooutfile=NOOUTFILE,  # 是否输出到文件
        timeout=args.timeout  # 请求超时时间
    )

    # 运行 whichAlive 实例的主程序逻辑
    w.run()
