import requests


# 获取Cookies
r1 = requests.get("http://www.baidu.com")
print(type(r1.cookies))  # 返回一个RequestsCookieJar对象
for key, value in r1.cookies.items():  # items可以将其类型转化为由元组组成的列表
    print(key + '=' + value)

# 直接用Cookies维持登录状态
headers = {
    'cookie': 'l_n_c=1; q_c1=dc691aef7e33447ca73ff5dbefdb096e|1541078505000|1541078505000; '
              '_xsrf=8d1d33d2a9c5233149508416816c9622; '
              'r_cap_id="OWNiZmVjY2YxMzJjNDU2ZTgwMWMxYzY3NDRiMGY3MWU=|1541078505|891ae06bf3ee1570d65d84250c1e25f12c8f6cdd"; '
              'cap_id="N2U2ZDgwNDJkOGU5NGFhYjgxOTE4NTAxZDhhMjdlYTY=|1541078505|5e7dbacd6ac0c27a73520d9518a553e43d10ba6d"; '
              'l_cap_id="NzJlNDhiNzVhNjQxNDFlOGI2MDc1Yzg1N2MxNTU1ZGU=|1541078505|996153ea58bcf6c987c0082ba4d517cbc85db894"; '
              'n_c=1; d_c0="AJDmXKTvcw6PTrBCNtnjZoys-Ep44ghnIdU=|1541078508"; _zap=bf91152a-1906-4442-859b-0b2b2d63a11b; '
              '__utmc=51854390; _xsrf=XVwcF7q8lf6t43MRlLwwrpBByqUqsqOg; tgw_l7_route=23ddf1acd85bb5988efef95d7382daa0; '
              'capsion_ticket="2|1:0|10:1541080726|14:capsion_ticket|44:MjdlMzdkMTQ2OTc2NDUxNjlhZGEwNGQ1ZTExMDEwZjA=|0629f121abbec79c9564e5d2c5fa14108c461b00f3fc44f65bd598c7b696657e"; '
              'z_c0="2|1:0|10:1541080823|4:z_c0|92:Mi4xM1o4OEJnQUFBQUFBa09aY3BPOXpEaWNBQUFDRUFsVk45NU1DWEFEeTR6UGZHcHV6X214YXFkaDFYYzM2WVJTU2xn|dd6718243a34fe82ce7928d16669944d25a28c307445cbe1850fb0ae4c94efa0";'
              ' __utma=51854390.1320427146.1541078513.1541078513.1541080830.2; __utmb=51854390.0.10.1541080830; __utmz=51854390.1541080830.2.2.utmcsr=zhihu.com|utmccn=(referral)|utmcmd=referral|utmcct=/signin;'
              ' __utmv=51854390.100--|2=registration_date=20171018=1^3=entry_date=20171018=1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/70.0.3538.77 Safari/537.36',
    'Host': 'www.zhihu.com'
}
r2 = requests.get("http://www.zhihu.com", headers=headers)
print(r2.text)

# Cookie的缺陷
requests.get('http://httpbin.org/cookies/set/number/123456789')
r2 = requests.get('http://httpbin.org/cookies')
print(r2.text)  # -->无法获取到Cookies信息

# 使用Session来维持会话状态-相当于在同一个浏览器打开了一个选项卡，不用为了维持登录而每次都设置Cookie
s = requests.Session()
s.get('http://httpbin.org/cookies/set/number/123456789')
r3 = s.get('http://httpbin.org/cookies')
print(r3.text)