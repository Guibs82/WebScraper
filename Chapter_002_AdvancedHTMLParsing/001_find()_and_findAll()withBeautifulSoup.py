#encoding:utf-8
from urllib2 import urlopen
from bs4 import BeautifulSoup

"""
    findAll(tag, attributes, recursive, text, limit, keywords)
    find(tag, attributes, recursive, text, keywords)
        tag 一个标签的名称或多个标签名称组成的Python 列表做标签参数
        attributes 是用一个 Python 字典封装一个标签的若干属性和对应的属性值 {'class': {'red', 'green'}}
        recursive 默认True，findAll 就会根据你的要求去查找标签参数的所有子标签
        text 用标签的文本内容去匹配(完全一致)
        limit 按网页上的顺序爬取前n 个
        keywords 你选择那些具有指定属性的标签
"""
html = urlopen("http://www.pythonscraping.com/pages/warandpeace.html")
bsObj = BeautifulSoup(html.read())

print "===tag==="
h1_2 = bsObj.findAll(("h1","h2"))
for h in h1_2:
    print h.get_text()

print "===attributes==="
nameAndWordList = bsObj.findAll("span", {'class':{"green", "red"}})
for nameAndWord in nameAndWordList:
    print nameAndWord.get_text() # get_text() 获得标签中的内容

print "===text==="
include_tp = bsObj.findAll(text="the")
print len(include_tp)
print include_tp

print "===limit==="
nameAndWordList = bsObj.findAll("span", {'class':{"green", "red"}}, limit=2)
for nameAndWord in nameAndWordList:
    print nameAndWord.get_text()

print "===keywords==="
# 两者效果相同
textList = bsObj.findAll(id="text")
textList = bsObj.findAll("", {"id":"text"})
for text in textList:
    print text
# 因为class 是Python 中的关键字, 所以当要使用class 的属性值来进行查找时, 需要使用以下方案
bsObj.findAll(class_="green")
bsObj.findAll("", {"class":"green"})