import requests
import logging


# 平时访问12306会出现证书问题导致无法访问，添加参数使其忽略该问题，但会报错，需要处理警告信息到日志中
logging.captureWarnings(True)
r1 = requests.get('https://www.12306.cn', verify=False)
print(r1.status_code)

# 指定一个本地证书用作客户端证书，可以是单个文件，也可以是一个包含两个文件路径的元组
r2 = requests.get('https://www.12306.cn', cert=('/ path/server.crt', '/path/key'))
print(r2.status_code)