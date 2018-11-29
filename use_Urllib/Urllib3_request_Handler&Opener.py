# 导入类
from urllib.request import HTTPPasswordMgrWithDefaultRealm, HTTPBasicAuthHandler, build_opener
from urllib.error import URLError


username = 'username'
password = 'password'
url = 'http://localhost:5000/'  # 这里指一个需要验证的网站

# 提供验证
p = HTTPPasswordMgrWithDefaultRealm()  # 实例化一个对象
p.add_password(None, url, username, password)  # 利用该方法传入用户名和密码
auth_handler = HTTPBasicAuthHandler()   # 从而建立一个处理验证的Handler
# 使用bulid_opener()建立一个Opener时传入验证信息
opener = build_opener(auth_handler)

try:
    result = opener.open(url)
    html = result.read().decode('utf-8')
    print(html)
except URLError as e:
    print(e.reason)