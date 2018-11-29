import re


# match()_1
content1 = 'hello 123 4567 World_This is a Demo!'
result1 = re.match('^hello\s(\d{3})\s\d{4}.*', content1)  # 匹配成功则返回一个对象
print(result1.span())  # 输出匹配范围
print(result1.group())  # 输出匹配到的内容
print(result1.group(1))  # 使用分组索引，传入索引即可提取()中的对应结果

# 贪婪匹配--> .*会匹配尽可能多的字符，使留下的内容满足后面正则表达式的规则即可
content2 = 'Hello 1234567 World_This is a Demo!'
result2 = re.match('^He.*(\d+).*Demo!$', content2)
print(result2)
print(result2.group(1))  # 只打印出了7

# 非贪婪匹配--> .*?会匹配尽可能少的字符
content3 = 'Hello 1234567 World_This is a Demo!'
result3 = re.match('^He.*?(\d+).*Demo!$', content2)
print(result3)
print(result3.group(1))  # 打印出了1234567

# 修饰符
content4 = """hello 123 4567 
World_This is a Demo!"""  # 使用三引号来包含换行符
result4 = re.match('^hello\s(\d{3})\s\d{4}.*', content4, re.S)  # 添加一个修饰符来使得.*能够匹配换行符
print(result4.group())  # 输出匹配到的内容
print(result4.group(1))  # 使用分组索引，传入索引即可提取()中的对应结果