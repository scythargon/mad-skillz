#!/usr/bin/python 
# -*- coding: utf-8 -*-
#//*[@id="allEntries"]/table/tbody
# //*[@id="allEntries"]/table/tbody/tr[1]
#http://bfolder.ru/photo/vse_podrjad/2
#phtTdMain
import urllib2
from lxml import etree
from StringIO import StringIO

main_url = 'http://bfolder.ru/photo/skrinshoty/48-'
mu_end = '-0-0-2'
    
def get_images(page_url):
   req = urllib2.Request(page_url, None, {'User-agent': 'Mozilla/5.0'})
   file_ = urllib2.urlopen(req)
   broken_html = urllib2.urlopen(req).read()
   parser = etree.HTMLParser()
   tree   = etree.parse(StringIO(broken_html), parser)
   result = etree.tostring(tree.getroot(),pretty_print=True, method="html")
   print 'downloaded:',len(result),#//*[@id="allEntries"]/table
   table = tree.xpath('//*[@id="allEntries"]/table/descendant::*/a/img') # Открываем раздел
   images = []
   for node in table: # Перебираем элементы
        images.append(node.get('src'))
   return images
"""
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~    
req = urllib2.Request("http://bfolder.ru/photo/vse_podrjad/2", None, {'User-agent': 'Mozilla/5.0'})
file_ = urllib2.urlopen(req)
broken_html = urllib2.urlopen(req).read()
#print page 
from lxml import etree
from StringIO import StringIO
parser = etree.HTMLParser()
tree   = etree.parse(StringIO(broken_html), parser)
result = etree.tostring(tree.getroot(),pretty_print=True, method="html")
print len(result)#//*[@id="allEntries"]/table
#//*[@id="entryID20204"]/div[1]/a/img

""""""table = tree.xpath('//*[@id="allEntries"]/table')[0] # Открываем раздел

for tr in table: # Перебираем элементы
    for td in tr:
        for div in td:
            for div2 in div:
                node = div2
                print node.tag,node.keys(),node.values()
                print 'name =',node.get('name') # Выводим параметр name
                print 'text =',[node.text] # Выводим текст элемента
   """"""         #//*[@id="entryID20204"]/div[1]/a/img
table = tree.xpath('//*[@id="allEntries"]/table/descendant::*/a/img') # Открываем раздел
#print table
images = []
for node in table: # Перебираем элементы
    t= node.get('src')
    #print t
    images.append(t)
    """
"""print node.tag,node.keys(),node.values()
    print 'name =',node.get('name') # Выводим параметр name
    print 'text =',[node.text] # Выводим текст элемента
   """
def get_big(url):
    s=url.split('/')
    del s[5]
    #print s
    return '/'.join(s)
def get_medium(url):
    s=url.split('/')
    #del s[5]
    #print s
    s[5]='2'
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

#cropped_buffer=pixbuf.subpixbuf(x,y,width,height)

#MainWin(images[0]).main()
import os
os.system("rm ./bfolder/tredshots/*")

num = 0
from urlparse import urlparse
for n in range(6):
    print 'page #',n+1,';'
    images = get_images(main_url+str(n+1)+mu_end)
    print 'images:',len(images),
    for image in images:
        #print image
        rash='jpg'
        while True:
           try:
               #print image, get_big(image)
               #exit()
               if(rash=='jpg'):
                  u = urllib2.urlopen(get_big(image))
               else:
                  u = urllib2.urlopen(get_big(image[:-3]+'png'))
           except urllib2.HTTPError, e:
               try:
                  if(rash=='jpg'):
                     u = urllib2.urlopen(get_medium(image))
                  else:
                     u = urllib2.urlopen(get_medium(image[:-3]+'png'))
               except urllib2.HTTPError, e:
                  print "ERROR БЛЯТЬ"
                  rash="png"
                  continue
           if(rash!='jpg'):
              print 'found png'
           break
        localFile = open('./bfolder/tredshots/'+'%05d' % num + "."+rash, 'w')
        num+=1
        localFile.write(u.read())
        localFile.close()
        #print 'блять'
        print num,' '
        
