#! /usr/bin/env python
# -*- coding: utf-8 -*-
from math import ceil
import gtk,webkit

import urllib2
from lxml import etree
from StringIO import StringIO

import re, htmlentitydefs

def unescape(text):
    return text
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


class ArgonDock(gtk.Window):
   def drawMessages(self,messages,*is_mul): #нельзя проверять тип messages потому что если мы даже
       ret=''                   #передадим один элемент - он все равно тоже будет листом
       if len(is_mul)>0:
          for message in messages:
             ret+=self.drawMessage(message)
       else:
          ret=self.drawMessage(messages)
       return ret
   def drawMessage(self,message):
       mes_num= message[0][1][0][0].text #number of message
       mes_uname= message[1][0][0][0].text #username
       print mes_uname
       #mes_mes= message[1][1][5] #message
       mes_mes=unescape(etree.tostring(message[1][1][5],method="html")) #exactly text of message!!
       mes_mes=mes_mes.replace('style="margin:20px; margin-top:5px; "','class="quote_frame"')
       return        mes_mes.split('\n')[0] \
            +        "<div class=message_head><b>"+mes_uname+"</b>&nbsp;<sup>["+mes_num+"]</sup>"\
            +             "<div class='button float-right'><span class='button_text hide_button'>-</span></div>"\
            +        "</div>" \
            +        "<div class='message_body'>"\
            +        '\n'.join((mes_mes.split('\n')+['</div>'])[1:])


   def __init__(self):
       gtk.Window.__init__(self,gtk.WINDOW_TOPLEVEL) 
       #self.set_type_hint(gtk.gdk.WINDOW_TYPE_HINT_DOCK)
       self.set_gravity(gtk.gdk.GRAVITY_EAST)
       self.set_size_request(2,100)
       self.set_decorated(False)
       self.set_accept_focus(True)
       width, height = self.get_size()
       self.move(int(ceil((gtk.gdk.screen_width() - width))), int(ceil(gtk.gdk.screen_height() - height)/2))
       
       self.page=""
       self.from_post=1
       eb = gtk.EventBox()
       
       self.add(eb)
       
       web = webkit.WebView()
       web.connect("navigation-requested", self.on_click_link)
       web.connect("enter-notify-event", self.enter_notify)
       
       html="<html style='background:#0000ff'><h1 style='background:#00ff00'>hello</h1></html>"

       localFile = open('jquery-min.js', 'r')
       jquery=localFile.read()
       localFile.close()
       
       localFile = open('panel_css.css', 'r')
       css=localFile.read()
       localFile.close()

       localFile = open('panel_jscript.js', 'r')
       jscript=localFile.read()
       localFile.close()

       ##################################
       forum_page=open('temp0.html','r')
       broken_html = forum_page.read()
       forum_page.close()
       ##################################
       """
       myHeaders = {'User-agent': 'Mozilla/5.0'}
       #myHeaders['Range']='bytes='+str(from_byte)+'-'
       #req = urllib2.Request('http://ololo.web',headers=myHeaders)
       page_url="http://127.0.0.1:8000/forum.html"
       req = urllib2.Request(page_url, None, headers=myHeaders)
       file_ = urllib2.urlopen(req)
       broken_html = file_.read()
       """
              ##################################
       parser = etree.HTMLParser()
       tree   = etree.parse(StringIO(broken_html), parser)
       result = etree.tostring(tree.getroot(),pretty_print=True, method="html")
       table = tree.xpath('//table[substring(@id,1,4)="post"]')
       
       invisible = """
       <div style="display:none" class="parse_from_form">
        <form action="program:/menu_form" method=get>
         <div class="button input_meaning float-left"><span class='button_text input_meaning'>page</span></div>
         <input type="text" class="parse_from float-left" name="set_page" value="set page" onfocus="this.value='';" onblur="if (this.value == '') this.value='set page';"/>
       </form>
       </div>
       """
       #print mes_mes
       html="<html><head>" \
            + invisible \
            + "<style type='text/css'>" + css + "</style><script>"+jquery+"</script>" \
            + '<meta http-equiv="Content-Type" content="text/html; charset=utf-8">' \
            + "</head><body>" \
            + "<div class='window_bookmark'></div>" \
            +     "<div class='all_messages'>"\
            + "<div class='menu'>>></div>"
       print len(table)
       #print self.drawMessages(table[0:3],'mul')
       #exit()
       html+=self.drawMessages(table,'mul')
       
            
       html+="</div>"\
            + "<script>"+ jscript+"</script></body></html>"
       ##################################
       localFile = open('test_for_browser.html', 'w')
       localFile.write(html)
       localFile.close()

       web.load_html_string(html,"file:///")
       web.show()
       eb.add(web)

       self.show_all()
       self.show()
   def enter_notify(self,*args):
       #self.set_type_hint(0)
       self.resize(300,300)
       #print 'enter'
   def leave_notify(self,*args):
       self.resize(2,100)
       #self.set_type_hint(gtk.gdk.WINDOW_TYPE_HINT_DOCK)
       #print 'leave'
   def set_page(self,page):
      print "page:",page
   def on_click_link(self, view, frame, req, data=None):
        """Describes what to do when a href link is clicked"""

        # As Ryan Paul stated he likes to use the prefix program:/ if the
        # link is being used like a button, the else will catch true links
        # and open them in the webbrowser
        uri = req.get_uri()
        if uri.startswith("file:///"):
            return False
        elif uri.startswith("program:/"):
            #print uri.split("/")[1]
            if uri.split("/")[1].startswith('body-click'):
               self.enter_notify();
            if uri.split("/")[1].startswith('hide'):
               self.leave_notify();
            if uri.split("/")[1].startswith('menu_form'):
               this.set_page( uri.split("set_page=")[1] ) 
            
            #view.execute_script('alert("alert");')
        else: 
            webbrowser.open(uri)
        return True

if __name__ == "__main__":
   ArgonDock()
   gtk.main()
#python -m SimpleHTTPServer &
#http://127.0.0.1:8000/

#<script src="http://code.jquery.com/jquery-1.7.2.min.js"></script>

"""
import urllib2

myHeaders = {'Range':'bytes=0-9'}

req = urllib2.Request('http://ololo.web',headers=myHeaders)

partialFile = urllib2.urlopen(req)

s2 = (partialFile.read())
"""
