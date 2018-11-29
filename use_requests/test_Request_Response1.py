# import requests
#
#
# headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'}
# response = requests.get('https://www.baidu.com/img/baidu_jgylogo3.gif',headers=headers)
# # print(response.text,'\n')
# # print(response.headers)
# # print(response.status_code)
# print(response.content) #获取响应体的二进制格式
# with open('./baidu.gif','wb') as f:
#     f.write(response.content) #保存为图片
#     f.close()

# 利用selenium解决JavaScript渲染问题
from selenium import webdriver


driver=webdriver.Chrome()
# driver.get('http://www.taobao.com')
print(driver.page_source)