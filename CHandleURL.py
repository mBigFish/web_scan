import ipaddress
import re
from urllib.parse import urlparse

class HandleURL:
    def __init__(self):
        pass

    def check_url_protocol(self):
        """判断url是否含有http/https"""
        pattern = r'^https?://'
        return bool(re.match(pattern, self.value))

    def get_domain_ip_port_from_url(self):
        """从url中获取域名/ip和端口"""
        pattern = r"(?P<scheme>http[s]?://)?(?P<domain_ip>[\w.-]+)(:(?P<port>\d+))?(/.*)?"
        match = re.match(pattern, self.value)
        if match:
            domain_ip = match.group("domain_ip")
            port = match.group("port")
            if not port:
                port = None
            return True, {"domain_ip": domain_ip, "port": port}
        else:
            return False, f"{self.value} 匹配失败！"

    def extract_domain_and_ip_from_host(self):
        """清理host，获取域名/IP 和 端口"""
        cleaned_str = re.sub(r'[^\w.:]', '', self.value)
        if ":" in cleaned_str:
            parts = cleaned_str.split(":")
            domain_or_ip = parts[0]
            port = parts[1]
            try:
                ipaddress.ip_address(domain_or_ip)
                return None, domain_or_ip, port
            except ValueError:
                return domain_or_ip, None, port
        else:
            try:
                ipaddress.ip_address(cleaned_str)
                return None, cleaned_str, None
            except ValueError:
                return cleaned_str, None, None

    def is_valid_url(self):
        """判断url是否正确"""
        try:
            result = urlparse(self.value)
            if result.scheme and result.netloc:
                if result.scheme.startswith('http') or result.scheme.startswith('https'):
                    domain, ip, port = self.extract_domain_and_ip_from_host()
                    return True, {"scheme": result.scheme, "domain": domain, "ip": ip, "port": port}
                else:
                    return False, "不是正确的链接！"
            else:
                return False, "不是正确的链接！"
        except ValueError:
            return False, "不是正确的链接！"

    def is_ip_or_domain(self):
        """判断是域名还是ip"""
        ip_pattern = re.compile(r'^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$')
        domain_pattern = re.compile(r'^(?:[a-zA-Z0-9-]+\.)+[a-zA-Z]{2,}$')
        if ip_pattern.match(self.value):
            return 'IP'
        if domain_pattern.match(self.value):
            return 'Domain'
        return None

# 测试示例
urls = [
    "http://114.116.116.102:8099",
    "http://123.183.157.15:90/pictures/ncuyqhwen.jsp",
    "https://sxcgzxkj.yyu8c.com/servlet/RegisterServlet",
    "example.com;'",        # 只有域名
    "example.com:80",       # 域名和端口号
    "122.122.122.1:30",     # IP 地址和端口号
    "www.example.com;'",    # 包含额外的分号
    "www.example.com:80;",  # 包含额外的分号和端口号
    "122.122.122.1;30",     # 包含额外的分号和端口号
]

# handler = URLHandle()
#
# for url in urls:
#     handler.value = url
#     print(f"URL: {url}")
#     print(f"是否含有http/https: {handler.check_url_protocol()}")
#     valid, info = handler.is_valid_url()
#     if valid:
#         print(f"Domain/IP: {info['domain']}")
#         print(f"IP: {info['ip']}")
#         print(f"Port: {info['port']}")
#         print(f"是否是域名还是IP: {handler.is_ip_or_domain()}")
#     else:
#         print(f"不是正确的链接！详情： {info}")
#     print("=" * 20)
