import http.cookiejar, urllib.request


cookie = http.cookiejar.CookieJar()  # 声明CookieJar对象
handler = urllib.request.HTTPCookieProcessor(cookie)  # 传入上面的对象来构造Handler
opener = urllib.request.build_opener(handler)
response = opener.open('http://www.baidu.com')
for item in cookie:
    print(item.name + '=' + item.value)

# 将Cookie存入成文件
filename = 'cookie.txt'
cookie1 = http.cookiejar.MozillaCookieJar(filename)  # 声明火狐浏览器的CookieJar对象
# cookie = http. cookiejar. LWPCookieJar (filename) -->LWP格式
handler1 = urllib.request.HTTPCookieProcessor(cookie1)  # 传入上面的对象来构造Handler
opener1 = urllib.request.build_opener(handler1)
response = opener1.open('http://www.baidu.com')
cookie1.save(ignore_discard=True, ignore_expires=True)

# 读取已生成的Cookie文件
cookie2 = http.cookiejar.MozillaCookieJar()
cookie2.load('cookie.txt', ignore_expires=True, ignore_discard=True)
handler2 = urllib.request.HTTPCookieProcessor(cookie2)
opener = urllib.request.build_opener(handler2)
response2 = opener.open('http://www.baidu.com')
print(response2.read().decode('utf-8'))