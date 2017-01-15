#encoding:utf-8

from urllib2 import urlopen
from bs4 import BeautifulSoup
import re

# 对于标签对象, 可以用以下方法获得全部属性
#   myTag.attrs
#   返回一个属性字典

html = urlopen("http://www.pythonscraping.com/pages/page3.html")
bsObj = BeautifulSoup(html)

images = bsObj.findAll("img",{"src":re.compile("\.\.\/img\/gifts\/img.*\.jpg")})
for image in images:
    print(image["src"])