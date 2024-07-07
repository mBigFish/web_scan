import os
import time
from concurrent.futures import ThreadPoolExecutor
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


def start_browser():
    # 创建一个参数对象，用来控制chrome以无界面模式打开
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')

    # 创建浏览器对象
    driver = webdriver.Chrome(options=chrome_options)
    # driver = webdriver.Chrome()  # 不加 chrome_options 参数就是正常的打开一个浏览器，进行操作
    # driver.implicitly_wait(10)

    return driver


def browser_thread(url):
    driver = start_browser()  # 每个线程独立启动浏览器
    try:
        driver.get(url)
        print(url, driver.title)

        # 创建截图保存目录
        screenshot_dir = 'screenshots'
        if not os.path.exists(screenshot_dir):
            os.makedirs(screenshot_dir)

        # 保存截图到指定目录
        screenshot_path = os.path.join(screenshot_dir, f"{url.replace('.', '_').replace('https://', '').replace('http://', '').replace('/', '_')}.png")
        driver.save_screenshot(screenshot_path)

        driver.quit()
        return True
    except Exception as e:
        print(f"Error in thread {url}: {e}")
        driver.quit()
        return False


def main(url_list):
    with ThreadPoolExecutor(max_workers=10) as executor:
        futures = [executor.submit(browser_thread, url) for url in url_list]

        # 等待所有任务执行完毕
        # for future in futures:
        #     result = future.result()
        #     print(f"Task completed with result: {result}")


if __name__ == "__main__":
    url_list = []
    start = time.time()
    with open("url.txt", "r") as fp:
        for line in fp.readlines():
            url_list.append(line.strip('\n'))

    main(url_list)

    end = time.time()
    print("time:", end - start)