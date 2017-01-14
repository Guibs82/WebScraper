#encoding:utf-8
from urllib2 import urlopen

# 输 出 http://pythonscraping.com/pages/page1.html 这 个 网 页 的 全 部 HTML 代 码
html = urlopen("http://pythonscraping.com/pages/page1.html")
print html.read()