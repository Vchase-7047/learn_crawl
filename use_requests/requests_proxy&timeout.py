import requests


# 普通方式
proxies1 = {
    "http": "http://127.0.0.1:59576",
    "https": "https://127.0.0.1:59576"
}
requests.get("https://www.baidu.com", proxies=proxies1)

# 代理需要认证
proxies2 = {
    "http": "http://user:password@127.0.0.1:59576/",
}
requests.get("https://www.taobao.com", proxies=proxies2)

# 使用SOCKS协议代理
# pip install 'requests[socks]'
proxies3 = {
    "http": "socks5://user:password@127.0.0.1:59576/",
}
requests.get("https://www.taobao.com", proxies=proxies3, timeout=None)

