import argparse
import configparser
import csv
import datetime
import os
import sys
import re
import socket
import sys
import time
import json
import urllib
import urllib.parse
from concurrent.futures import ALL_COMPLETED, ThreadPoolExecutor, wait, as_completed
import requests
import urllib3
from certifi.__main__ import args

from CSHeaderGenerator import HeaderGenerator
from CSCallBack import CallBack

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
DEBUG = False



class CSGetResponseWEB(object):
    def __init__(self, url_list):

        # 从config读取配置信息
        config = configparser.ConfigParser()
        config.read("config.ini")
        config_section = "request"
        self.ALLOW_REDIRECT = config.getboolean(config_section, "ALLOW_REDIRECT")
        self.OUTFILE = config.getboolean(config_section, "OUTFILE")
        self.VERITY = config.getboolean(config_section, "VERITY")
        self.RANDOM_HEADER = config.getboolean(config_section, "RANDOM_HEADER")

        self.TRYAGAIN = config.getint(config_section, "TRYAGAIN")
        self.THREAD_POOL_SIZE = config.getint(config_section, "THREAD_POOL_SIZE")
        self.TIMEOUT = config.getint(config_section, "TIMEOUT")
        self.PROXY = json.loads(config.get(config_section, "PROXY"))

        self.CALLBACK = CallBack()

        self.URL_LIST = url_list
        self.tableheader = ['no', 'url', 'ip', 'state',
                            'state_code', 'title', 'server', 'length', 'other']  # CSV 输出的表头
        self.TOTAL_URL = len(self.URL_LIST)  # 待扫描的 URL 总数
        self.completed_url = -1  # 已完成扫描的 URL 计数器

        if self.OUTFILE:
            self.timenow = time.strftime("%Y%m%d%H%M%S", time.localtime(time.time()))  # 当前时间戳
            self.outfilename = f'{self.timenow}.csv'  # 输出的 CSV 文件名
            self.errorfilename = f'error_{self.timenow}.txt'  # 错误日志文件名

    def run(self):
        start_time = datetime.datetime.now()
        print(f'total {self.TOTAL_URL}')

        self.completed_url += 1
        if self.OUTFILE:
            self.__writetofile(self.tableheader)  # 写入 CSV 文件头部

        result_list = []
        with ThreadPoolExecutor(max_workers=self.THREAD_POOL_SIZE) as t:
            tasklist = []
            for url_id, url in enumerate(self.URL_LIST):
                tasklist.append(t.submit(self.__scan, url, url_id + 1)) # 提交 URL 扫描任务
            for task_result in as_completed(tasklist):
                result_list.append(task_result.result())

            if wait(tasklist, return_when=ALL_COMPLETED):
                end_time = datetime.datetime.now()
                print(f'--------------------------------\nDONE, use {(end_time - start_time).seconds} seconds')
                if self.OUTFILE:
                   info_print_outfile = f'outfile: {os.path.join(os.path.abspath(os.path.dirname(__file__)), "result", self.outfilename)}'

    def __callback(self):
        pass

    def __scan(self, url, url_id):
        self.completed_url += 1
        header = self.__getheader()
        progress =
        try:
            # 发送HTTP请求判断网站是否存活
            if self.ALLOW_REDIRECT:
                # 允许重定向时的处理逻辑
                r = requests.get(url=url, headers=header,
                                 timeout=self.TIMEOUT, verify=self.VERITY, proxies=self.PROXY)
                state = r.status_code

            else:
                # 不允许重定向时的处理逻辑
                r = requests.get(url=url, headers=header, allow_redirects=self.ALLOW_REDIRECT,
                                 timeout=self.TIMEOUT, verify=self.VERITY, proxies=self.PROXY)
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


    def __getheader(self):
        if self.RANDOM_HEADER:
            header = HeaderGenerator.get_headers()
        else:
            header = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36',
        }  # 请求的 HTTP 头部信息
        return header


if __name__ == '__main__':
    with open("../url.txt", "r") as fp:
        urls = [line.strip("\n") for line in fp.readlines()]
    w = CSGetResponseWEB(urls)
    w.run()
