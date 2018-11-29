import socket
import urllib.request
import urllib.parse
import urllib.error
# 实现请求，down下源代码

# response=urllib.request.urlopen(url='',data=None,timeout=None,cafile=None,capath=None,cadefault=False,context=None)

# GET请求
response = urllib.request.urlopen('http://www.baidu.com')
# print(response.read().decode('utf-8'))


# POST请求-加入data参数
data = bytes(urllib.parse.urlencode({'world': 'hello'}), encoding='utf8')
response1 = urllib.request.urlopen('https://httpbin.org/post', data=data)
# print(response1.read().decode('utf-8'))
print(response1.status)  # 返回状态码信息
print(response1.getheaders())  # 以字典形式返回一个response-headers信息

# 使用timeout及处理报错信息
try:
    response2=urllib.request.urlopen('http://httpbin.org/get',timeout=0.1)
except urllib.error.URLError as e:
    if isinstance(e.reason,socket.timeout):
        print('TIME OUT')
