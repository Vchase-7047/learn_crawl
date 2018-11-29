from lxml import etree


text = """
<div>
<ul>
<li class="item-0"><a href="link1.html">first item</a></li>
<li class="item-1"><a href="link2.html">second item</a></li>
<li class="item-inactive"><a href="link3.html">third item</a></li>
<li class="item-1"><a href="link4.html">fourth item</a></li>
<li class="item-0"><a href="link5.html">fifth item</a></li>
</ul>
</div>
"""
filename = './test.html'


def use_Xpath(filename, string):
    html = etree.parse(filename, etree.HTMLParser())  # 直接读取文本文件进行解析
    result = html.xpath(string)
    print(result)

html1 = etree.HTML(text)  # 构造一个XPath解析对象
result1 = etree.tostring(html1)  # 调用tostring()方法可输出修正后的HTML代码，结果是bytes类型
print(result1.decode('utf-8'))

# 输出所有节点
use_Xpath(filename, '//*')
use_Xpath(filename, '//li')  # 匹配li节点

# 子节点
use_Xpath(filename, '//li/a')
use_Xpath(filename, '//ul//a')  # 查找ul节点下所有的子孙节点，必须使用//

# 父节点
use_Xpath(filename, '//a[@href="link4.html"]/../@class')

# 属性匹配
use_Xpath(filename, '//li[@class="item-0"]')

# 文本获取
use_Xpath(filename, '//li[@class="item-0"]//text()')
use_Xpath(filename, '//li[@class="item-0"]/a/text()')

# 属性获取
use_Xpath(filename, '//li/a/@href')

# 属性多值匹配
use_Xpath(filename, '//li[contains(@class, "li")]/a/text()')  # 属性中包含li的就匹配

# 多属性匹配
use_Xpath(filename, '//li[contains(@class, "li") and @name="item"]/a/text()')

# 按序选择
use_Xpath(filename, '//li[1]/a/text()')  # 选取匹配的第一个节点
use_Xpath(filename, '//li[last()]/a/text()')  # 选取最后一个
use_Xpath(filename, '//li[position()<3]/a/text()')  # 选取前两个
use_Xpath(filename, '//li[last()-2]/a/text()')  # 选取倒数第三个

# 节点轴选择
use_Xpath(filename, '//li[1]/ancestor::*')  # 获取所有祖先节点
use_Xpath(filename, '//li[1]/ancestor::div')  # 获取只有div这个祖先节点
use_Xpath(filename, '//li[1]/attribute::*')  # 获取li界定啊的所有属性
use_Xpath(filename, '//li[1]/child::a[@href="link1.html"]')  # 选取子节点带有xxx属性的节点
use_Xpath(filename, '//li[1]/descendant::span')  # 获取所有子孙节点
use_Xpath(filename, '//li[1]/following::*[2]')  # 获取当前节点之后的所有节点
use_Xpath(filename, '//li[1]/following-sibling::*')  # 获取当前节点之后的所有同级节点