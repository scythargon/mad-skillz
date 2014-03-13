#!/usr/bin/env python
import gtk
win=gtk.Window()

loader=gtk.gdk.PixbufLoader()
img_file=open("/home/argon/py/html_render/terminal.jpg","r")
loader.write(img_file.read())
loader.close()
img_file.close()
image=gtk.Image()
image.set_from_pixbuf(loader.get_pixbuf())
image.show()

vb=gtk.VBox()
#win.add(vb)
vb.show()
#vb.pack_start(image,False,False,0)


table = gtk.Table(1,1,False)
label=gtk.Label("aaaaaaaaaaaaaaaaaaaaaaaaa")
label.show()
table.attach(label, 0, 1, 0, 1,
                     gtk.SHRINK, gtk.SHRINK,
                     5, 5)
table.show()
win.add(table)
win.show()
win.set_resizable(True)
gtk.main()
