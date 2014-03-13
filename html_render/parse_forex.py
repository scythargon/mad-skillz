#!/usr/bin/python 
# -*- coding: utf-8 -*-

import urllib2
from lxml import etree
from StringIO import StringIO
#page_url="http://forum.fxclub.org/showthread.php?t=60981&page=23"
#req = urllib2.Request(page_url, None, {'User-agent': 'Mozilla/5.0'})
#file_ = urllib2.urlopen(req)
#broken_html = urllib2.urlopen(req).read()
forum_page=open('/home/argon/forum_page','r')
broken_html = forum_page.read()
forum_page.close()

parser = etree.HTMLParser()
tree   = etree.parse(StringIO(broken_html), parser)
result = etree.tostring(tree.getroot(),pretty_print=True, method="html")
table = tree.xpath('//table[substring(@id,1,4)="post"]')
print table[0][0][1][0][0].text #number of message
print table[0][1][0][0][0].text #username
print table[0][1][1][5] #message

import re, htmlentitydefs
##
# Removes HTML or XML character references and entities from a text string.
#
# @param text The HTML (or XML) source text.
# @return The plain text, as a Unicode string, if necessary.
def unescape(text):
    def fixup(m):
        text = m.group(0)
        if text[:2] == "&#":
            # character reference
            try:
                if text[:3] == "&#x":
                    return unichr(int(text[3:-1], 16))
                else:
                    return unichr(int(text[2:-1]))
            except ValueError:
                pass
        else:
            # named entity
            try:
                text = unichr(htmlentitydefs.name2codepoint[text[1:-1]])
            except KeyError:
                pass
        return text # leave as is
    return re.sub("&#?\w+;", fixup, text)

print unescape(etree.tostring(table[0][1][1][5],method="html")) #exactly text of message!!
