#encoding:utf-8
from urllib2 import urlopen
from bs4 import BeautifulSoup

# BeautifulSoup4 初体验
html = urlopen("http://pythonscraping.com/pages/page1.html")
bsObj = BeautifulSoup(html.read())
print bsObj.h1