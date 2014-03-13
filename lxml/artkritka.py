#!/usr/bin/python 
# -*- coding: utf-8 -*-
import urllib2
from lxml import etree
from StringIO import StringIO

art_url="http://atkritka.com"
main_url = 'http://atkritka.com/?&PAGEN_1='#NN from 29 to 
nn_from = 203
nn_to = 257
def get_images(page_url):
    req = urllib2.Request(page_url, None, {'User-agent': 'Mozilla/5.0'})
    file_ = urllib2.urlopen(req)
    broken_html = urllib2.urlopen(req).read()
    parser = etree.HTMLParser()
    tree   = etree.parse(StringIO(broken_html), parser)
    result = etree.tostring(tree.getroot(),pretty_print=True, method="html")
    print 'downloaded:',len(result),#//*[@id="allEntries"]/table
    table = tree.xpath('//*[@id="mainpage"]/ul/descendant::*/img') # Открываем раздел
    images = []
    href = []
    for node in table: # Перебираем элементы
        parent_href = node.xpath('..')[0].get('href')
        if parent_href.find('make')<0:
           href.append(parent_href)
    return href
def get_big(url):
    s=url.split('/')
    s[5]='2'
    #print s
    return '/'.join(s)
def get_name(url):
    s=url.split('/')
    return s[-1]
import gtk
class MainWin:

    def destroy(self, widget, data=None):
        gtk.main_quit()

    def __init__(self,image_url):
        self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
        self.window.connect("destroy", self.destroy)
        self.window.set_border_width(1)
        self.image=gtk.Image()
        response=urllib2.urlopen(image_url)
        loader=gtk.gdk.PixbufLoader()
        loader.write(response.read())
        loader.close()        
        self.image.set_from_pixbuf(loader.get_pixbuf())
        # This does the same thing, but by saving to a file
        # fname='/tmp/planet_x.jpg'
        # with open(fname,'w') as f:
        #     f.write(response.read())
        # self.image.set_from_file(fname)
        self.window.add(self.image)
        self.image.show()
        self.window.show()

    def main(self):
        gtk.main()
        
#MainWin(images[0]).main()
import os
#os.system("rm -rf ./artkritka/")
#os.system("mkdir ./artkritka/")
num = 1393
from urlparse import urlparse
def get_big_im_by_href(page_url):
   #//*[@id="mainpage"]/img
   req = urllib2.Request(page_url, None, {'User-agent': 'Mozilla/5.0'})
   file_ = urllib2.urlopen(req)
   broken_html = urllib2.urlopen(req).read()
   parser = etree.HTMLParser()
   tree   = etree.parse(StringIO(broken_html), parser)
   result = etree.tostring(tree.getroot(),pretty_print=True, method="html")
   print 'exactly page downloaded:',len(result),#//*[@id="allEntries"]/table
   table = tree.xpath('//*[@id="mainpage"]/img') # Открываем раздел
   return art_url+table[0].get('src')
    
for n in range(nn_from,nn_to+1):
    #print n
    
    print 'page #',n,';',
    images = get_images(main_url+str(n))
    print 'images:',len(images),
    #break
    for image in images:
        if (image.find('icon')>=0):
           continue
        print image
        try:
            u = urllib2.urlopen(get_big_im_by_href(art_url+image))
        except urllib2.HTTPError, e:
            pass
        localFile = open('./artkritka/'+str(num)+'.jpg', 'w')
        num+=1
        localFile.write(u.read())
        localFile.close()
        print num
        
