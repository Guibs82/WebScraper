#encoding:utf-8

from urllib2 import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://www.pythonscraping.com/pages/page3.html")
bsObj = BeautifulSoup(html)

# 1. 处理子标签和后代标签
#   Dealing with children and other descendants

# 使用.children 找出子标签
print "===.children==="
for child in bsObj.find("table", {"id":"giftList"}).children:
    print child

# 使用.descendants 找出后代标签
print "===.descendant==="
for descendant in bsObj.find("table", {"id":"giftList"}).descendants:
    print descendant


# 2. 处理兄弟标签
#   Dealing with siblings
#   .next_siblings 获取在他之后的所有兄弟标签
#   .previous_siblings 获取在他之前的所有兄弟标签
print "===.next_sibings==="
for sibling in bsObj.find("table", {"id":"giftList"}).tr.next_siblings:
    print sibling

# 3. 父标签处理
#   Dealing with your parents
print "===.parent==="
print bsObj.find("img",{"src":"../img/gifts/img1.jpg"}).parent.previous_sibling.get_text()

