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
import warnings
from urllib3.exceptions import NotOpenSSLWarning
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
warnings.filterwarnings("ignore", category=NotOpenSSLWarning)
# DEBUG = True
DEBUG = False


class CSGetResponseWEB(object):
    def __init__(self, url_list):

        # 从config读取request配置信息
        config = configparser.ConfigParser()
        config.read("config.ini")
        config_section = "request"
        self.ALLOW_REDIRECT = config.getboolean(config_section, "ALLOW_REDIRECT")
        self.OUTFILE = config.getboolean(config_section, "OUTFILE")
        self.VERITY = config.getboolean(config_section, "VERITY")
        self.RANDOM_HEADER = config.getboolean(config_section, "RANDOM_HEADER")
        self.TRYAGAIN = config.getboolean(config_section, "TRYAGAIN")
        self.THREAD_POOL_SIZE = config.getint(config_section, "THREAD_POOL_SIZE")
        self.TIMEOUT = config.getint(config_section, "TIMEOUT")
        self.PROXY = json.loads(config.get(config_section, "PROXY"))
        # 从config读取function配置信息
        config_section = "function"
        self.GET_WEB_TITLE = config.getboolean(config_section, "GET_WEB_TITLE")
        self.GET_WEB_LENGTH = config.getboolean(config_section, "GET_WEB_LENGTH")
        self.GET_WEB_SERVER =  config.getboolean(config_section, "GET_WEB_SERVER")

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
                tasklist.append(t.submit(self.__scan, url_id + 1, url))# 提交 URL 扫描任务
            for task_result in as_completed(tasklist):
                result_list.append(task_result.result())
                if not DEBUG:
                    print(f"已完成：{len(result_list)}")
                    print(task_result.result())

            if wait(tasklist, return_when=ALL_COMPLETED):
                end_time = datetime.datetime.now()
                print(f'--------------------------------\nDONE, use {(end_time - start_time).seconds} seconds')
                if self.OUTFILE:
                   info_print_outfile = f'outfile: {os.path.join(os.path.abspath(os.path.dirname(__file__)), "result", self.outfilename)}'

    def __callback(self, url_id, url, state, response, progress):
        result = {"网站状态": state}
        if response:
            if self.GET_WEB_TITLE:
                result["网站标题"] = self.__get_web_title(response)
            if self.GET_WEB_LENGTH:
                result["网页长度"] = self.__get_web_length(response)
            if self.GET_WEB_SERVER:
                result["网站服务"] = self.__get_web_server(response)
        else:
            if self.GET_WEB_TITLE:
                result["网站标题"] = ''
            if self.GET_WEB_LENGTH:
                result["网页长度"] = ''
            if self.GET_WEB_SERVER:
                result["网站服务"] = ''
        # print(url_id, url, progress, result)
        # print(f"[{progress}%] | {url} | {result}")
        return url_id, url, progress, result

    def __scan(self, url_id, url):
        self.completed_url += 1
        header = self.__get_header()
        progress = '%.2f' % ((self.completed_url / self.TOTAL_URL) * 100)
        response = None
        try:
            response = requests.get(
                url=url, headers=header, allow_redirects=self.ALLOW_REDIRECT,
                timeout=self.TIMEOUT, verify=self.VERITY, proxies=self.PROXY
            )
            state = response.status_code

            # 调用回调函数处理扫描结果
            # self.__callback(url_id, url, state, response, progress)
            print(url)
            return url_id, url, state, response, progress

        # 处理各种异常情况
        except requests.exceptions.ConnectTimeout as e:
            if DEBUG:
                print(f"[ERROR] | [连接超时] | {url} | [原因{e}]")
            # 记录错误信息到错误报告中
            # self.__errorreport(str(e))
            state = '连接超时'
            # 调用回调函数，通知处理结果
            self.__callback(url_id, url, state, response, progress)

        except requests.exceptions.ReadTimeout as e:
            if DEBUG:
                print(f"[ERROR] | [读取超时] | {url} | [原因{e}]")
            # 记录错误信息到错误报告中
            # self.__errorreport(str(e))
            state = '读取超时'
            # 调用回调函数，通知处理结果
            self.__callback(url_id, url, state, response, progress)

        except requests.exceptions.ConnectionError as e:
            if DEBUG:
                print(f"[ERROR] | [连接错误] | {url} | [原因{e}]")
            # 记录错误信息到错误报告中
            # self.__errorreport(str(e))
            state = '连接错误'
            # 调用回调函数，通知处理结果
            self.__callback(url_id, url, state, response, progress)

        except Exception as e:
            if DEBUG:
                print(f"[ERROR] | [其他错误] | {url} | [原因{e}]")
            # 记录错误信息到错误报告中
            # self.__errorreport(str(e))
            # 如果设置了重试标志，尝试再次扫描该 URL
            # if self.TRYAGAIN:
            #     print(self.TRYAGAIN)
            #     self.completed_url -= 1
            #     self.TRYAGAIN = False
            #     self.__scan(url_id, url)
            state = "未知错误"
            self.__callback(url_id, url, state, response, progress)


    def __get_header(self):
        if self.RANDOM_HEADER:
            header = HeaderGenerator.get_headers()
        else:
            header = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36',
        }  # 请求的 HTTP 头部信息
        return header

    @staticmethod
    def __get_web_title(r) -> str:
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
                except Exception as e:
                    if DEBUG:
                        print(f"[ERROR] ｜ [获取标题错误] | [原因{e}]")
                    charset = 'utf8'
            else:
                charset = 'utf8'  # 如果没有 Content-Type，默认使用 utf-8 编码

            # 使用获取到的字符集解码响应内容，并从中提取网页标题
            return re.findall(r'<title>(.*?)</title>', r.content.decode(charset))[0]
        except Exception as e:
            if DEBUG:
                print(f"[ERROR] ｜ [获取标题错误] | [原因{e}]")
            return "未获取到网站标题"

    @staticmethod
    def __get_web_length(r) -> str:
        try:
            return str(len(r.content))
        except AttributeError:
            return "未获取到网页长度"

    @staticmethod
    def __get_web_server(r) -> str:
        try:
            return r.headers.get('server')
        except AttributeError:
            return "未获取到网站服务"


if __name__ == '__main__':
    with open("./url.txt", "r") as fp:
        urls = [line.strip("\n") for line in fp.readlines()]
    w = CSGetResponseWEB(urls)
    w.run()
