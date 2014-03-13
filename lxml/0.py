#!/usr/bin/python 
import urllib,lxml.html,lxml.etree 
 
page = urllib.urlopen("http://ithappens.ru/story/1") 
doc = lxml.html.document_fromstring(page.read()) 
print '[' + page.read() + ']'
header = doc.cssselect("h3")[0] 
print '[' + header.text + ']' 
 
date = doc.cssselect("p.date")[0] 
print date.text 
 
rating = doc.cssselect("p.date")[1] 
print "rating: "+rating.text[9:] 
 
text = doc.cssselect("p.text") 
print lxml.etree.tostring(text[0],encoding="utf8",method="html") 
 
tags = doc.cssselect("p.storytags")[0] 
for tag in tags.iterchildren(): 
    print tag.text
