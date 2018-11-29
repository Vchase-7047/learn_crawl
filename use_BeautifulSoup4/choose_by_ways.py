from bs4 import BeautifulSoup
import re


html = """
    <div class="panel">
        <div class="panel-heading">
            <h4>Hello</h4>
        </div>
        <div class="panel-body">
            <ul class="list" id="list-1" name="elements">
                <li class="element">Foo</li>
                <li class="element">Bar</li>
                <li class="element">Jay</li>
            </ul>"
            <ul class="list list-small" id="list-2">
                <li class="element">Foo</li>
                <li class="element">Bar</li>
            </ul>
        </div>
    </div>
"""
# find_all()：查询所有符合条件的元素标签
# API：find_a ll(narne , attrs , recursive , text , **kwargs)
soup1 = BeautifulSoup(html, 'lxml')
# name
print(soup1.find_all(name='ul'))  # 返回一个列表
for i in soup1.find_all(name='ul'):
    print(i.find_all(name='li')[0].text)  # 嵌套查找
    print(i.find_all(name='li')[0].string)

# attrs
print(soup1.find_all(attrs={'id': 'list-1'}))
print(soup1.find_all(attrs={'name': 'elements'}))  # 参数类型为字典
# 也可以使用另外一种方法
print(soup1.find_all(id='list-1'))
print(soup1.find_all(class_='element'))

# text-传入的形式可以是string也可以是正则表达式对象
print(soup1.find_all(text=re.compile('Foo')))

# find()：返回第一个匹配的单个元素，用法与find_all()类似
