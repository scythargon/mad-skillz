#!/usr/bin/python 
import pygtk
pygtk.require('2.0')
import gtk
import urllib2

class MainWin:

    def destroy(self, widget, data=None):
        print "destroy signal occurred"
        gtk.main_quit()

    def __init__(self):
        self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
        self.window.connect("destroy", self.destroy)
        self.window.set_border_width(10)
        self.image=gtk.Image()
        response=urllib2.urlopen(
            'http://www.dailygalaxy.com/photos/uncategorized/2007/05/05/planet_x.jpg')
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

if __name__ == "__main__":
    MainWin().main()
