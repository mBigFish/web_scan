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
import urllib
import urllib.parse
from asyncio import as_completed
from concurrent.futures import ALL_COMPLETED, ThreadPoolExecutor, wait
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
        self.config = configparser.ConfigParser()
        self.config.read("config.ini")
        self.config = self.class_config.section_config("request")
        self.THREAD_POOL_SIZE = self.config[0][1]
        self.ALLOW_REDIRECT = self.config[1][1]
        self.TRYAGAIN = self.config[2][1]
        self.OUTFILE = self.config[3][1]
        self.TIMEOUT = self.config[4][1]
        self.PROXY = self.config[5][1]

        self.CALLBACK = CallBack()

        self.RANDOM_HEADER = self.config[6][1]
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

        self.completedurl += 1
        if self.OUTFILE:
            self.__writetofile(self.tableheader)  # 写入 CSV 文件头部

        result_list = []
        with ThreadPoolExecutor(max_workers=self.THREAD_POOL_SIZE) as t:
            for url_id, url in enumerate(self.URL_LIST):
                tasklist = [t.submit(self.__scan, url, url_id + 1, self.TRYAGAIN)] # 提交 URL 扫描任务

            for task_result in as_completed(tasklist):
                result_list.append(task_result.result())
            print(f'total {self.allurlnumber}')

            if wait(tasklist, return_when=ALL_COMPLETED):
                end_time = datetime.datetime.now()
                print(f'--------------------------------\nDONE, use {(end_time - start_time).seconds} seconds')
                if self.OUTFILE:
                   info_print_outfile = f'outfile: {os.path.join(os.path.abspath(os.path.dirname(__file__)), "result", self.outfilename)}'

    def __scan(self):
        self.completedurl += 1
        header = self.__getheader()



    def __getheader(self):
        if self.RANDOM_HEADER:
            header = HeaderGenerator.get_headers()
        else:
            header = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36',
        }  # 请求的 HTTP 头部信息
        return header


if __name__ == '__main__':

    w = CSGetResponseWEB()
    w.run()