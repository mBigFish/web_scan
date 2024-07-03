import re
import socket
from urllib.parse import urlparse


class HandleURL:
    def __init__(self):
        pass

    @classmethod
    def check_url_protocol(cls, url):
        """判断url是否含有http/https"""
        pattern = r'^https?://'
        return bool(re.match(pattern, url))

    @classmethod
    def get_host_port_from_url(cls, url):
        """从url中获取host和端口"""
        pattern = r"(?P<scheme>http[s]?://)?(?P<host>[\w.-]+)(:(?P<port>\d+))?(/.*)?"
        match = re.match(pattern, url)
        if match:
            host = match.group("host")
            port = match.group("port")
            if not port:
                port = None
            return True, {"host": host, "port": port}
        else:
            return False, f"{url} 匹配失败！"

    @classmethod
    def is_valid_url(cls, url):
        """判断url是否正确"""
        # 定义URL的正则表达式模式
        url_pattern = re.compile(
            r'^(?:http|ftp)s?://'  # http:// or https://
            r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'  # domain...
            r'localhost|'  # localhost...
            r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}|'  # ...or ipv4
            r'\[?[A-F0-9]*:[A-F0-9:]+\]?)'  # ...or ipv6
            r'(?::\d+)?'  # optional port
            r'(?:/?|[/?]\S+)$', re.IGNORECASE)

        return bool(re.match(url_pattern, url))

    @classmethod
    def is_ip_or_domain(cls, url):
        """判断是域名还是ip"""
        ip_pattern = re.compile(r'^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$')
        domain_pattern = re.compile(r'^(?:[a-zA-Z0-9-]+\.)+[a-zA-Z]{2,}$')
        if ip_pattern.match(urlparse(url).hostname):
            return 'IP'
        if domain_pattern.match(urlparse(url).hostname):
            return 'Domain'
        return None

    @classmethod
    def get_ip_from_url(cls, url):
        flag, result = cls.get_host_port_from_url(url)
        if flag:
            domain = result["host"]
            try:
                ip = socket.getaddrinfo(domain, 'http')
                return ip[0][4][0]
            except socket.gaierror as e:
                return '获取IP失败'
        else:
            return "解析URL错误"

# # 测试示例
# urls = [
#     "http://114.116.116.102:8099",
#     "http://123.183.157.15:90/pictures/ncuyqhwen.jsp",
#     "https://sxcgzxkj.yyu8c.com/servlet/RegisterServlet",
#     "example.com;'",        # 只有域名
#     "example.com:80",       # 域名和端口号
#     "122.122.122.1:30",     # IP 地址和端口号
#     "www.example.com;'",    # 包含额外的分号
#     "www.example.com:80;",  # 包含额外的分号和端口号
#     "122.122.122.1;30",     # 包含额外的分号和端口号
# ]
#
# for url in urls:
#     print(f"URL: {url}")
#     print(f"是否含有http/https: {HandleURL.check_url_protocol(url)}")
#     valid, info = HandleURL.get_host_port_from_url(url)
#     if valid:
#         print(f"Domain/IP: {info['domain_ip']}")
#         print(f"Port: {info['port']}")
#         print(f"是否是域名还是IP: {HandleURL.is_ip_or_domain(url)}")
#     else:
#         print(f"不是正确的链接！详情： {info}")
#     print("=" * 20)
