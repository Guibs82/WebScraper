#encoding:utf-8
from urllib2 import urlopen
from urllib2 import HTTPError, URLError
from bs4 import BeautifulSoup

def getTitle(url):
    """获取指定url 网页中的title"""
    try:
        html = urlopen(url)
    except (HTTPError, URLError) as e:
        print e.message
        return None
    else:
        try:
            bsObj = BeautifulSoup(html.read())
            title = bsObj.body.h1
        except AttributeError as e:
            print e.message
            return None
        else:
            return title

title = getTitle("http://pythonscraping.com/pages/page1.html")

if title is None:
    print "你的url里找不到title"
else:
    print title