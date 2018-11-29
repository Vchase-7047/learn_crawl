from urllib import error, request


# try:
#     response = request.urlopen('https://cuiqingcai.com/index.htm')
# except error.URLError as e:
#     print(e.reason)

# 同时使用HTTPError类和URLError类，先选择捕获子类信息
try:
    response1 = request.urlopen('https://cuiqingcai.com/index.htm')

except error.HTTPError as e1:
    print(e1.code, e1.reason, e1.headers, sep='\n')
except error.URLError as e2:
    print(e2.reason)
else:
    print('Request successful!')


# # 有时候reason返回的是可能是一个对象
# import socket
# import urllib.request
# import urllib .error
# try:
#     response2 = urllib.request.urlopen('https://www.baidu.com', timeout=0.01)
# except urllib.error.URLError as e:
#     print(type(e.reason))
# if isinstance(e.reason, socket.timeout):
#     print(' TIME OUT')