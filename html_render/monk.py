#! /usr/bin/env python
# -*- coding: utf-8 -*-
from math import ceil
import gtk,webkit
window=0
web = 0
label = 0
eb=0
import cairo,math

class YouJustCantGoogle(object):
   def __init__(self):
       global window,web,label,eb
       window = gtk.Window(gtk.WINDOW_TOPLEVEL)
       #window.set_title("Just learn to google")
       eb = gtk.EventBox()
       window.add(eb)
       
#       eb.add_events(gtk.gdk.ENTER_NOTIFY)
#       eb.add_events(gtk.gdk.LEAVE_NOTIFY)
       #eb.modify_bg(gtk.STATE_NORMAL, gtk.gdk.color_parse("blue")) 
       window.set_size_request(1,100)
       window.set_decorated(False)
       label = gtk.Label("Stop smoking shit!")
       
       window.set_gravity(gtk.gdk.GRAVITY_EAST)
       width, height = window.get_size()
       window.move(int(ceil((gtk.gdk.screen_width() - width))), int(ceil(gtk.gdk.screen_height() - height)/2))

       
       
       web = webkit.WebView()

       eb.connect("enter-notify-event", self.enter_notify)
       eb.connect("leave-notify-event", self.leave_notify)

       html="<html style='background:#0000ff'><h1 style='background:#00ff00'>hello</h1></html>"
       web.load_html_string(html,"file:///")
       web.show()
       eb.add(web)
       #eb.add(label)
  
       window.show_all()
       
       
       window.show()
       """ может потом пригодится всякое рисование
       window.set_app_paintable(True)
       #web.connect('expose-event', self.expose)
       print 'dafuck EXP event connected'
       
   def expose (self,widget, event):
       #print 'web expose'
       
       self.context = widget.window.cairo_create()
       self.context.rectangle(event.area.x, event.area.y,
                               event.area.width, event.area.height)
       self.context.clip()
        
       self.draw(self.context)
       
       return False 
       
   def draw(self, context):
        rect = window.get_allocation()
        x = rect.x + rect.width / 2
        y = rect.y + rect.height / 2
        
        radius = min(rect.width / 2, rect.height / 2) - 5
        
        # clock back
        context.arc(x, y, radius, 0, 2 * math.pi)
        context.set_source_rgb(1, 5, 5)
        context.fill_preserve()
        context.set_source_rgb(0, 0, 0)
        context.stroke()
        print 'drow'
"""        

   def enter_notify(self,*args):
       window.resize(100,100)
       #eb.remove(label)
       #eb.add(web)
       print 'enter'
   def leave_notify(self,*args):
       window.resize(1,100)
       #eb.remove(web)
       #eb.add(label)
       print 'leave'


if __name__ == "__main__":
   YouJustCantGoogle()
   gtk.main()
