#!/usr/bin/env python
import gtk, unittest

from transparent import Transparent

class MainWindow(gtk.Window,Transparent):
    def __init__(self):
        gtk.Window.__init__(self)
        Transparent.__init__(self)
class TestArgon (unittest.TestCase):

    def setUp(self):
		self.window = MainWindow()
    def testUnPaintable(self):
        default_window = gtk.Window()
        self.assertFalse(default_window.get_app_paintable())
    def testPaintable(self):
        self.assertTrue(self.window.get_app_paintable())

if __name__ == "__main__":
	unittest.main()
