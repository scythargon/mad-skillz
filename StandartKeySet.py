#!/usr/bin/env python
import gtk
from Button import button
class StandartKeySet(gtk.VBox):
    def __init__(self,size,parent_):
        self.a_parent=parent_
        row0 = ('Ecscape','F1','F2','F3','F4','F5','F6','F7','F8','F9','F10',
                'F11','F12','PrtScr','Pause','Insert','Delete')
        row1 = (('`','~'),('1','!'),('2','@'),('3','#'),('4','$'),('5','%'),('6','^'),
                ('7','&'),('8','*'),('9','('),('0',')'),('-','_'),('=','+'),'BackSpace')
        row2 = ('Tab','q','w','e','r','t','y','u','i','o','p',('[','{'),(']','}'),'Return')
        row3 = ('CapsLock','a','s','d','f','g','h','j','k','l',(';',':'),('"',"'"),("'",'|'))
        row4 = ('Shift',('<','>'),'z','x','c','v','b','n','m',(',','<'),('.','>'),('/','?'),'Shift','Up')
        row5 = ('Ctrl','Super','Alt','space','Alt','Sub','Ctrl','Left','Down','Right')
        gtk.VBox.__init__(self)
        self.show()
        self.holdKeys = []
        #self.set_size_request(size[0],size[1])
        #print size[0],size[1]
        self.rows = []
        buttonsAmount = [17,14,14,14,14,14]
        for i in range(6):
            self.rows.append(gtk.HBox())
            self.rows[i].show()
            #self.rows[i].set_size_request(int(ceil(size[0])),int(ceil(size[1])))
            #self.pack_start(self.rows[i],False,False,4)
            self.pack_start(self.rows[i],True,True,4)
        self.parseRow(row1,0)
        self.parseRow(row2,1)
        self.parseRow(row3,2)
        self.parseRow(row4,3)
        self.parseRow(row5,4)
        btn = gtk.Button('Hide')
        btn.show()
        btn.connect('clicked',self.a_parent.hideAndThenShow)
        btn.set_size_request(50,50)
        #self.fixed = gtk.Fixed()
        #self.fixed.put(btn,100,100)
        #self.fixed.show()
        #self.a_parent.add(self.fixed)
        self.rows[4].pack_start(btn,True,True,5)    
        return
    def parseRow(self,row,num):
        for j in range(len(row)):
            if isinstance(row[j], tuple):
                char_ = row[j][0]
            else:
                char_ = row[j]
        #    print char_
            self.rows[num].pack_start(button(self,char_),True,True,5)
