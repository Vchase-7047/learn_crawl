import urllib.request
import urllib.parse
# 在请求中加入Headers

url = 'http://httpbin.org/post'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36',
    'Host': 'httpbin.org'
}

dict = {
    'name': 'vchase'
}

data = bytes(urllib.parse.urlencode(dict), encoding='utf8')  # 使用bytes()和urllib库中的parse模块中的urlencode()方法转成字节流
req = urllib.request.Request(url, data=data, headers=headers)  # 重新构造URL
response = urllib.request.urlopen(req)
print(response.read().decode('utf-8'))
