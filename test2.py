#!/usr/bin/env python
import gtk, unittest,gobject

from MainWindow import MainWindow

class TestArgon (unittest.TestCase):

    def setUp(self):
        self.window = MainWindow()
        self.window.show()
    def test1(self):
        self.assertTrue(self.window.get_visible())
    def testHide(self):
        self.window.hideAndThenShow(None)
        self.assertFalse(self.window.get_visible())
    def testShow(self):
        print 'we see that comment'
        self.window.hideAndThenShow(None)
        gobject.timeout_add(1500,self.part2)
    
    def part2(self):#dont work exactly
        print 'we dont see that, wtf? so next gainsaying each other string alarms nothing'
        self.assertFalse(self.window.get_visible())
        self.assertTrue(self.window.get_visible())
        return False

if __name__ == "__main__":
	unittest.main()
