import requests


# POST_1
data = {
    'name': 'vchase',
    'age': '21'
}
r1 = requests.post("http://httpbin.org/post", data=data)
print(r1.text)

# 文件上传
files = {'file': open('favicon.ico', 'rb')}
r2 = requests.post("http://httpbin.org/post", files=files)
print(r2.text)