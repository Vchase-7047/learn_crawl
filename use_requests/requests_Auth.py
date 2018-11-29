import requests
from requests.auth import HTTPBasicAuth


# 一般方法
r1 = requests.get('http://localhost:5000', auth=HTTPBasicAuth('username', 'password'))
# 简化方法
r2 = requests.get('http://localhost:5000', auth=('username', 'password'))

# 使用OAuth
# pip3 install requests_oauthlib
# from requests_oauthlib import OAuth1
# url = 'https ://api .twitter.com/1. 1/account/verify credentials.json'
# auth = OAuth1('YOUR_APP_KEY', 'YOUR_APP_SECRET', 'USER_OAUTH_TOKEN', 'USER_OAUTH_TOKEN_SECRET')
# requests.get(url, auth=auth)