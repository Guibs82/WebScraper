#encoding:utf-8

from urllib2 import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://www.pythonscraping.com/pages/page3.html")
bsObj = BeautifulSoup(html.read())

# 使用lambda 设置判定条件, 筛选属性数量为2 的标签
tagList = bsObj.findAll(lambda tag: len(tag.attrs) == 2)
for tag in tagList:
    print tag.attrs