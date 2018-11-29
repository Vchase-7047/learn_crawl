from bs4 import BeautifulSoup


html = """
    <html>
    <head>
        <title>The Dormouse's story</title>
    </head>
    <body>
    <p class="story">
        Once upon a time there were three little sisters; and their names were
        <a href="http://example.com/elsie" class="sister" id="link1">
    <span>Elsie</span>
    </a>
    hello
    <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a>
    and
    <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
    and they lived at the bottom of a well.
    </p>
    <p class="story">...</p>
"""

# 小试牛刀
soup1 = BeautifulSoup(html, 'lxml')  # 创建一个对象
print(soup1.prettify())  # 调用该方法，把要解析的字符串以标准的缩进格式输出
print(soup1.title.string)  # 输出title节点的文本内容
print(soup1.title.txet)

# 节点选择器
# 选择元素-该方法只返回匹配的第一个元素
soup2 = BeautifulSoup(html, 'lxml')
print(type(soup2.title), soup2.title)  # 返回<class 'bs4.element.Tag'>类型
print(soup2.title.get_text())
print(soup2.head)
print(soup2.p)

# 提取信息-获取节点名称
print(soup2.title.name)
# 提取信息-获取属性
print(soup2.p.attrs)
print(soup2.p.attrs['name'])
print(soup2.p['class'])  # class属性不唯一，所以返回的是一个列表
print(soup2.p['name'])  # name属性唯一，返回的是string
# 提取信息-获取内容
print(soup2.p.string)

# 嵌套选择
print(soup2.head.title)
print(soup2.head.title.string)

# 关联选择
# 子节点和孙节点
print(soup2.p.contents)  # 返回直接子节点的列表
print(soup2.p.children)  # 返回一个迭代器类型
for i, child in enumerate(soup2.p.children):  # 使用enumerate()方法来添加索引
    print(i, child)
for i1, child1 in enumerate(soup2.p.descendants):  # 获取所有子孙节点
    print(i1, child1)

# 父节点和祖先节点
print(type(soup2.a.parent))  # 返回<class 'bs4.element.Tag'>
print(type(soup2.a.parents))  # 返回一个生成器
for i in soup2.a.parents:
    print(i)

# 兄弟节点(同级节点)
print(soup2.a.next_sibling)  # 返回下一个同级节点的字符串
print(soup2.a.next_sibling.string) # 提取信息
print(type(soup2.a.previous_sibling))
print(soup2.a.next_siblings)  # 返回后面所有同级节点的生成器generator类型
print(type(soup2.a.previous_siblings))
print(list(soup2.a.parents)[0].attrs['class'])
