import time

import httpx
import requests
from concurrent.futures import ThreadPoolExecutor, as_completed, wait, ALL_COMPLETED
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
# 线程池大小
THREAD_POOL_SIZE = 100

start = time.time()

# 爬取网页的函数
# def fetch_url(url):
#     try:
#         r = requests.get(url, allow_redirects=True, verify=False, timeout=10).status_code
#         # print(url, r)
#         a = url, r
#     except requests.RequestException as e:
#         # print(url, "eeeeeeeeeeeeeee")
#         a = f"Error fetching {url}: {e}"
#     return a
m = []
def fetch_url(url):
    try:
        with httpx.Client(follow_redirects=True, verify=False) as client:
            response = client.get(url, timeout=10)
            # print(response.headers)
            status_code = response.status_code
            if status_code == 200:
                m.append(url)
            return status_code
    except httpx.TimeoutException:
        return "请求超时"
    except httpx.RequestError as e:
        return f"请求出错: {e}"


# 主函数，用于执行爬取任务
def main():
    with open("./url.txt", "r") as fp:
        urls = [line.strip("\n") for line in fp.readlines()]

    start = time.time()

    total = len(urls)
    # 使用线程池
    with ThreadPoolExecutor(max_workers=THREAD_POOL_SIZE) as executor:
        # 提交每个任务到线程池
        futures = [executor.submit(fetch_url, url) for url in urls]

        completed = 0
        # 等待所有任务完成
        for future in as_completed(futures):
            completed += 1
            bf = round(completed / total * 100, 2)
            print(f"[{bf}%], {future.result()}")

        if wait(futures, return_when=ALL_COMPLETED):
            end = time.time()
            print(start - end)
if __name__ == "__main__":
    main()
    print(len(m))
