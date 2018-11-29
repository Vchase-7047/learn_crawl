import re


# 使用sub()方法来替换匹配到的字符串
content = '54aKS4yrsoiRS4ixSL2g'
result = re.sub('\d+', '', content)
print(result)

# 使用compile()方法来实现预编译
content1 = '2016-12-15 12:00'
content2 = '2016-12-17 12:55'
content3 = '2016-12-22 13:21'
pattern = re.compile('\d{2}:\d{2}')
result1 = re.sub(pattern, '', content1)
result2 = re.sub(pattern, '', content2)
result3 = re.sub(pattern, '', content3)
print(result1, result2, result3, sep='\n')