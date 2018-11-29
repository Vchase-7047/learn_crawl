from requests import Request, Session


url = 'http://httpbin.org/post'
data = {
    'name': 'vchase'
}
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/70.0.3538.77 Safari/537.36'
}

s = Session()
req = Request('POST', url, data=data, headers=headers)  # 构造一个Request对象
prepped = s.prepare_request(req)  # 使用prepare_request()方法将其转换为一个Prepared Request对象
r = s.send(prepped)  # 调用send发送
print(r.text)