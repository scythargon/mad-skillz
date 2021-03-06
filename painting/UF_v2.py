#! /usr/bin/env python
# -*- coding: utf-8 -*-
import os
import thread
import sys
import gtk
import gobject
from DrawingGetRegion import DrawingGetRegion,Handler
from transparent import Transparent
import time

showbig,showsmall = False,False
windows=[]
window_work_with=0
winGetReg=None
class Win:
    #x,y,name,id,region
    def __init__(self):
        pass
class impHandler(Handler):
    def __init__(self,nextHandler=None):
        self.nextHandler=nextHandler
        pass
        #self.win=win
    def handle(self,region_):
        global windows
        windows[window_work_with].region=region_
        #region = region_
        if self.nextHandler!=None:
            self.nextHandler()
def placeSmallWin():
    global windows
    win=windows[window_work_with]
    try:
        #print win.get_screen().get_width(),region[2]
        w=win.win.get_screen().get_width()
        h=win.win.get_screen().get_height()
        x,y=win.region[2],win.region[3]
        #print x,y
        if w-x<=2:
            x=w-win.reg_w
        if h-y<=2:
            y=h-win.reg_h
        #print x,y
        win.win.move(x,y)
    except:
        win.win = gtk.Window()
        win.win.set_type_hint(gtk.gdk.WINDOW_TYPE_HINT_DOCK)
        image =gtk.Image()
        image.set_from_pixbuf(win.pixbuf)
        win.image=image
        win.win.add(image)
        win.win.set_decorated(False)
        win.win.set_accept_focus(False)
        
        w=win.win.get_screen().get_width()
        h=win.win.get_screen().get_height()
        x,y=win.region[2],win.region[3]
        #print x,y
        if w-x<=2:
            x=w-reg_w
        if h-y<=2:
            y=h-reg_h
        #print x,y
        win.win.move(x,y)
        win.win.show_all()
    
    
def soWeGotRegionAndWindow():
    print 'Taking screenshot, one moment...'
    global windows
    temp_file = time.time()
    windows[window_work_with].temp_file=temp_file
    os.system('echo '+str(temp_file)+' > dafuck')
    os.system('import -window '+windows[window_work_with].id+' '+str(temp_file)+'.png')
    if showbig:
        print 'Ok, just close next window.'
        raw_input('ready? press enter')

        window = gtk.Window(gtk.WINDOW_TOPLEVEL)
        image=gtk.Image()
        f=open(str(temp_file)+'.png','r')
        loader=gtk.gdk.PixbufLoader()
        loader.write(f.read())
        loader.close()
        f.close()
        image.set_from_pixbuf(loader.get_pixbuf())
        window.add(image)
        window.connect("delete_event", previewDestroyed)
        window.set_position(gtk.WIN_POS_CENTER)
        image.show()
        window.show()
    else:
        previewDestroyed_afterPause()
def previewDestroyed(widget,event):
    print 'Just in case wait 0.5 second for really window closing'
    gobject.timeout_add(500,previewDestroyed_afterPause)
def makeAbiggerB(a,b):
    if a<b:
        t=a
        a=b
        b=t
def previewDestroyed_afterPause(*a):
    global windows
    #global true_x,true_y,reg_w,reg_h,region
    #print region, win_x,win_y
    region=windows[window_work_with].region
    win=windows[window_work_with]
    print region
    makeAbiggerB(region[2],region[0])
    makeAbiggerB(region[3],region[1])
    print region,'-normalized'
    true_x= region[0]-win.x
    if true_x<0:
        true_x=0
    true_y= region[1]-win.y
    if true_y<0:
        true_y=0
    win.true_x,win.true_y=true_x,true_y
    reg_w,reg_h=region[2]-region[0],region[3]-region[1]
    print reg_w,reg_h
    win.region=None

    f=open(str(win.temp_file)+'.png','r')
    loader=gtk.gdk.PixbufLoader()
    loader.write(f.read())
    loader.close()
    f.close()
    #global pixbuf
    pb=loader.get_pixbuf()
    if reg_w>pb.get_width():
        reg_w=pb.get_width()
    if reg_h>pb.get_height():
        reg_h=pb.get_height()
    print reg_w,reg_h,'-normalized'
    win.reg_w,win.reg_h=reg_w,reg_h
    win.pixbuf=pb.subpixbuf(true_x,true_y,reg_w,reg_h)
        
    if showsmall:
        print 'So lets see preview of piece of window'
        raw_input('just close the window again. now press enter')
        #print true_x,true_y,region[2],region[3]
        #global window
        window = gtk.Window(gtk.WINDOW_TOPLEVEL)
        image=gtk.Image()
        window.img=image
        image.set_from_pixbuf(win.pixbuf)
        window.add(image)
        window.connect("delete_event", smallPreviewDestroyed)
        window.set_position(gtk.WIN_POS_CENTER)
        image.show()
        window.show()
    else:
        smallPreviewDestroyed_afterPause()
def showBoard(select_what_):
    global winGetReg
    win = gtk.Window()
    winGetReg = win
    win.set_events(gtk.gdk.KEY_PRESS_MASK)
    global select_what
    select_what = select_what_
    win.connect("key_press_event", keyPressed)
    Transparent.makeTransparent(win)
    
    if select_what_=='region':
        onlyClick=False
        handler = impHandler()
    else:
        onlyClick=True
        handler = impHandler(placeSmallWin)
    getReg = DrawingGetRegion(handler,rgba=(1,1,0,0.2),border=(1,0,0,1),onlyClick=onlyClick)
    #win.set_size_request(win.get_screen().get_width(), win.get_screen().get_height())
    win.set_decorated(False)
    win.set_keep_above(True)
    #win.set_type_hint(gtk.gdk.WINDOW_TYPE_HINT_DOCK)
    win.fullscreen()
    win.add(getReg)
    win.getReg=getReg
    win.show_all()
    win.show()
    gtk.main()
def smallPreviewDestroyed(*a):
    print 'Just in case wait 0.5 second for really window closing'
    gobject.timeout_add(500,smallPreviewDestroyed_afterPause)
def smallPreviewDestroyed_afterPause(*a):
    print "Okeeey, on this step lets deside where we want to place our panel.\n"+\
    "Just click on screen and Enter/Escape again."
    showBoard('point')
select_what=0
def keyPressed(widget,event):
    #print event.hardware_keycode
    if event.hardware_keycode==36:#'Return':
        if windows[window_work_with].region==None:
            print 'at first - select '+ select_what
        else:
    #        print win_x
            winGetReg.hide()
            if select_what=='region':
                soWeGotRegionAndWindow()
            else:
                soWeGotPlace()
    if event.hardware_keycode==9:#'Escape':
        exit()
def refreshSmallWin(win_num):
    win=windows[win_num]
    os.system('import -window '+win.id+' '+str(win.temp_file)+'.png')
    f=open(str(win.temp_file)+'.png','r')
    loader=gtk.gdk.PixbufLoader()
    loader.write(f.read())
    loader.close()
    f.close()
    pixbuf=loader.get_pixbuf().subpixbuf(win.true_x,win.true_y,win.reg_w,win.reg_h)
    win.image.set_from_pixbuf(pixbuf)
    print 'refreshed ',win_num
    return True
def soWeGotPlace():
    thread.start_new_thread( (lambda x,y: gobject.timeout_add(2000,refreshSmallWin,window_work_with)) ,  (0,0))
    while 1: 
        command=raw_input('command: ')
        if command=='q':
            print 'exit'
            exit()
        elif command=='+':
            print 'Ok, lets add one more region in the other window.'
            global window_work_with
            window_work_with+=1
            main()
            pass
        else:
            print """supported commands:
            + - add one more region in the OTHER window
            q - exit
            """
if len(sys.argv)==1:
    print "for help use: "+sys.argv[0]+" --help"
else:
    if sys.argv[1]=='--help' or sys.argv[1]=='-h':
        print """
  This program allows you to place a refreshed in time area of some window's screenshot anywhere upon your screen above all the other windows.
  This may be helpfull if you want to see progress of something for example.
  Version 0.1
  Author: Argon  [scythargon@gmail.com]
        """
        exit()
def main():
    print "Now select window."
    f=open('dafuck','r')
    prev_img=f.read()
    #print '__'+img[:-1]+'__'
    #os.system('rm '+prev_img[:-1]+'.png')
    f.close()
    p = os.popen('xwininfo')
    resp = p.read()
    global my_windows
    win = Win()
    #global win_x, win_y, win_name, win_id
    win.x = int(resp.split('\n')[7].split('  ')[2]) #x-coord
    win.y =  int(resp.split('\n')[8].split('  ')[2]) #y-coord
    win.name = resp.split('\n')[5].split(' ')[4] # window name
    win.id = resp.split('\n')[5].split(' ')[3] # window id
    win.region=None
    global windows
    windows.append(win)
    print "Window: " + win.name \
        + "\nid: " + win.id \
        + "\ncoords: " + str((win.x,win.y))

    print "Now select window region and press Enter for accept or Escape for exit."
    showBoard('region')
import atexit
def deletePic():
    if temp_file!=None:
        os.system('rm '+str(temp_file)+'.png')
        os.system('echo deleted >> dafuck')
#atexit.register(deletePic)
    
    
main()
#sys.path.insert(0,'/home/blablabla')
