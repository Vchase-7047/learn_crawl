from bs4 import BeautifulSoup


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

soup1 = BeautifulSoup(html, 'lxml')
print(soup1.select('.panel .panel-heading'))  # 需要注意空格，这里使用.来查找拥有class属性的节点
print(soup1.select('ul li'))
print(soup1.select('#list-2 .element'))  # 使用#找到拥有该id值的标签，之后在寻找拥有符合该class值的标签
# 获取文本
print(soup1.select('ul'))  # 返回一个列表
print(soup1.select('ul')[0].get_text())  # 返回<class 'bs4.element.Tag'>类型
print(soup1.select('ul')[0].text)

# 嵌套选择
for ul in soup1.select('ul'):
    print(ul.select('li'))

# 获取属性-两种方法
for ul1 in soup1.select('ul'):
    print(ul1['id'])
    print(ul1.attrs['id'])