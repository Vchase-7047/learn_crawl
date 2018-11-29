import requests
import re
import json


# GET_1普通请求
r1 = requests.get('http://httpbin.org/get')
print(type(r1))  # 返回一个对象
print(type(r1.text))  # 返回str类型
print(r1.json())  # 调用json()返回一个字典格式的数据，若返回的结果不是JSON格式就会出现解析错误
# 或者使用json库
print(json.loads(r1.text))

# GET_2带参数访问
data = {
    'name': 'vchase',
    'age': '21'
}
r2 = requests.get('http://httpbin.org/get', params=data)
print(r2.text)

# GET_3加入headers抓取知乎->发现页面
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/70.0.3538.77 Safari/537.36'
}

r3 = requests.get('https://www.zhihu.com/explore', headers=headers)
pattern = re.compile('explore-feed.*?question_link.*?>(.*?)</a>', re.S)
titles = re.findall(pattern, r3.text)
print(titles)

# GET_4抓取二进制数据
r4 = requests.get("http://github.com/favicon.ico")
print(type(r4.content))  # 返回bytes类型的数据
with open('favicon.ico', 'wb') as f:
    f.write(r4.content)
