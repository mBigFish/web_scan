from asyncio import as_completed

from CSHandleURL import HandleURL
import datetime
import socket
from concurrent.futures import ALL_COMPLETED, ThreadPoolExecutor, wait

DEBUG = False


class GetIpURL(object):
    def __init__(self, urllist, THREAD_POOL_SIZE):

        self.urllist = urllist
        self.HEADER = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36',
        }  # 请求的 HTTP 头部信息
        self.THREAD_POOL_SIZE = THREAD_POOL_SIZE  # 最大并发线程数
        self.allurlnumber = len(self.urllist)  # 待扫描的 URL 总数
        self.completedurl = -1  # 已完成扫描的 URL 计数器

    def run(self):
        self.completedurl += 1
        tasklist = []
        start_time = datetime.datetime.now()
        t = ThreadPoolExecutor(max_workers=self.THREAD_POOL_SIZE)
        for k, url in enumerate(self.urllist):
            tasklist.append(t.submit(self.__scan, url, k + 1))  # 提交 URL 扫描任务
        # for future in as_completed(tasklist):
        #     print(future)
            # completed += 1
            # bf = round(completed / total * 100, 2)
            # print(f"[{bf}%], {future.result()}")

        print(f'total {self.allurlnumber}')
        if wait(tasklist, return_when=ALL_COMPLETED):
            end_time = datetime.datetime.now()
            print(f'--------------------------------\nDONE, use {(end_time - start_time).seconds} seconds')



    def __scan(self, url, no):


        def callback(no, url, ip):

            self.completedurl += 1
            nowpercent = '%.2f' % ((self.completedurl / self.allurlnumber) * 100)
            print(f'[{nowpercent}%] {url} | {ip}')

        flag, result = HandleURL.get_host_port_from_url(url)
        if flag:
            domain = result["host"]
            try:
                ip_result = socket.getaddrinfo(domain, 'http')
                ip =  ip_result[0][4][0]
            except socket.gaierror as e:
                ip =  '获取IP失败'
        else:
            ip = "解析URL错误"

        # 调用回调函数处理扫描结果
        callback(no, url, ip)
        return 1

    # def __errorreport(self, message):
    #     if not self.nooutfile:
    #         f = open(f'{os.path.join(os.path.abspath(os.path.dirname(__file__)), "error", self.errorfilename)}', 'a')
    #         f.write(message+'\n')
    #         f.close()

if __name__ == '__main__':

    file_path = "../url.txt"
    with open(file_path, "r") as fp:
        url_list = [line.strip("\n") for line in fp.readlines()]

    w = GetIpURL(
        urllist=url_list,  # 文件对象或标准输入流
        THREAD_POOL_SIZE=100,  # 线程池大小
    )

    w.run()
