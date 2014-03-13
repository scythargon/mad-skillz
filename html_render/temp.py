myHeaders = {'User-agent': 'Mozilla/5.0'}
from_byte=43000
def get_page():
    global result
    #myHeaders['Range']='bytes='+str(from_byte)+'-'+str(from_byte+100)
    myHeaders['Range']='bytes=10-50'    
    print myHeaders
    #page_url="http://wool/forum.html"
    #page_url="http://forum.fxclub.org/showthread.php?t=60981&page=23"
    req = urllib2.Request(page_url, None, headers=myHeaders)
    file_ = urllib2.urlopen(req)
    broken_html = file_.read()
    print "++++++++++"+broken_html
    parser = etree.HTMLParser()
    tree   = etree.parse(StringIO(broken_html), parser)
    result = etree.tostring(tree.getroot(),pretty_print=True, method="html")
    print len(result)

page_url="http://argon.freevar.com/get_fx_page.php?page=http%3A//forum.fxclub.org/showthread.php%3Ft%3D60981%26page%3D23"
    
get_page()

import urllib2
page_url="http://argon.freevar.com/get_fx_page.php?page=http%3A//forum.fxclub.org/showthread.php%3Ft%3D60981%26page%3D23"
print urllib2.urlopen(urllib2.Request(page_url,None,{'Range':'bytes=10-50'})).read()


def get_page():
    myHeaders = {'Range':'bytes=0-30'}
    print myHeaders
    page_url="http://127.0.0.1:8000/forum.html"
    #page_url='http://argon.freevar.com'
    req = urllib2.Request(page_url,headers=myHeaders)
    partialFile = urllib2.urlopen(req)
    global s2
    s2 = (partialFile.read())
    print s2
    

get_page()
