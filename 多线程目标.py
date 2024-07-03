import time

import requests
from concurrent.futures import ThreadPoolExecutor, as_completed, wait, ALL_COMPLETED
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
# 线程池大小
THREAD_POOL_SIZE = 100

# 爬取网页的函数
def fetch_url(url):
    try:
        r = requests.get(url, verify=False, timeout=10).status_code
        print(url, r)
        a = url, r
    except requests.RequestException as e:
        print(url, "eeeeeeeeeeeeeee")
        a = f"Error fetching {url}: {e}"
    return a

# 主函数，用于执行爬取任务
def main():
    start = time.time()
    with open("./more_url1.txt", "r") as fp:
        urls = [line.strip("\n") for line in fp.readlines()]

    total = len(urls)
    # 使用线程池
    with ThreadPoolExecutor(max_workers=THREAD_POOL_SIZE) as executor:
        # 提交每个任务到线程池
        futures = [executor.submit(fetch_url, url) for url in urls]

        completed = 0
        # 等待所有任务完成
        # for future in as_completed(futures):
        #     completed += 1
        #     bf = '%.2f' % {completed / total * 100}
        #     print(f"[{bf}]%{future.result()}")

        if wait(futures, return_when=ALL_COMPLETED):
            end = time.time()
            print(start - end)
if __name__ == "__main__":
    main()
