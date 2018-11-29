import requests


# 响应处理
r1 = requests.get('http://www.jianshu.com')
if not r1.status_code == requests.codes.ok:  # ok为响应代码
    exit()
else:
    print('Request successful!')
