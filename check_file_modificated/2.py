#! /usr/bin/env python
# -*- coding: utf-8 -*-

import gtk,webkit,pyinotify,thread,os,Image,time,gobject,cairo
from blessings import Terminal
from transparent import Transparent
t=Terminal()
win = gtk.Window(gtk.WINDOW_TOPLEVEL)
#win.set_type_hint(gtk.gdk.WINDOW_TOPLEVEL)
win.set_keep_above(True)
web = webkit.WebView()
web.set_transparent(True)
file_='/home/argon/Desktop/clean_business/index.html'
Transparent.makeTransparent(win)
Transparent.makeTransparent(web)
win.add(web)
def reload_html():
    #print '/'.join(os.path.abspath( __file__ ).split('/')[:-1])
    #exit()
    #web.open('file://'+'/'.join(os.path.abspath( __file__ ).split('/')[:-1])+'/'+file_)
    web.open(file_)
    #f=open('html.html')
    #web.load_html_string(f.read(),"file://html.html/")
    #f.close()
    
win.set_size_request(300,300)
win.resize(300,300)
win.move(650,30)
win.set_decorated(False)
#d=gtk.gdk.Drawable()
win.show_all()
class OnWriteHandler(pyinotify.ProcessEvent):
    def my_init(self, file_):
        self.file_=file_
    def process_IN_CLOSE_WRITE(self, event):
        global last_t
        print t.green_bold+'RELOAD'+t.normal
        web.reload()
def monitor(path,recurs):
    wm = pyinotify.WatchManager()
    handler = OnWriteHandler(file_=file_)
    notifier = pyinotify.Notifier(wm, default_proc_fun=handler)
    wm.add_watch(path, pyinotify.ALL_EVENTS,rec=recurs)
    print '==> Start monitoring %s (type c^c to exit)' % path
    notifier.loop()
thread.start_new(monitor,('/home/argon/Desktop/clean_business/',True))
reload_html()
gtk.main()
