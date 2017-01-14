#encoding:utf-8
from urllib2 import urlopen
from bs4 import BeautifulSoup

# BeautifulSoup4 初体验2
#   增加异常处理
try:
    html = urlopen("http://pythonscraping.com/pages/page1.html")
except Exception as e:
    # 如果程序返回 HTTP 错误代码，程序就会显示错误内容，不再执行 else 语句后面的代码
    # 异常处理
    #   此时urlopen 返回null
    print e.message
else:
    # 无异常时执行的代码
    if html is None:
        # 如果服务器不存在, 则urlopen 返回None
        print 'URL IS NOT FOUND'
    else:
        bsObj = BeautifulSoup(html.read())
        try:
            print bsObj.h1 # <h1>An Interesting Title</h1>
            # 如果想要调用不存在的标签, BeautifulSoup 就会返回None
            print bsObj.nonExistentTag # None
            print bsObj.nonExistentTag.someTag # AttributeError: 'NoneType' object has no attribute 'someTag'
        except AttributeError as e:
            print e.message # 'NoneType' object has no attribute 'someTag'
