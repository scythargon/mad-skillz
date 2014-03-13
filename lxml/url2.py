#!/usr/bin/python 
import urllib2
req = urllib2.Request("http://ithappens.ru/story/1", None, {'User-agent': 'Mozilla/5.0'})
page = urllib2.urlopen(req).read()
print page
