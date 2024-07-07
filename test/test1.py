import os
from concurrent.futures import ThreadPoolExecutor
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


def start_browser():
    options = Options()
    options.headless = True  # 设置无头模式
    options.add_argument("--disable-gpu")  # 适用于Windows操作系统
    options.add_argument("--no-sandbox")  # 适用于Linux操作系统
    options.add_argument("--disable-dev-shm-usage")  # 适用于Linux操作系统

    service = ChromeService(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
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
    with open("../file/url.txt", "r") as fp:
        for line in fp.readlines():
            url_list.append(line.strip('\n'))

    main(url_list)