#!/usr/bin/env python
import os,gobject, unittest
#pygtk.require('2.0')
from transparent import Transparent
from MainWindow import MainWindow
from math import ceil
from abc import ABCMeta, abstractmethod, abstractproperty
import gtk, sys, cairo, ConfigParser
#from AsettingsController import SettingsController
#from AsettingsContainer import SettingsContainer

class Application:
    def __init__(self):
        global gwin
        #self.settingsContainer = SettingsContainer()
        #self.settingsController = SettingsController(self.settingsContainer)
        #self.settingsController.loadSettings()
        self.mainWindow = MainWindow()
        self.mainWindow.setupWindow()
        
        gwin = self.mainWindow
        self.journal = Journal()
        self.wordsHint = WordsHint()

class WordsHint:
    def __init__(self):
        return
class Journal:
    def __init__(self):
        return
class Settings:
    def __init__(self):
        return

        
                    
        
    
def main (argc):
    application = Application()
    
    win = application.mainWindow
    win.show()
    return win
        
win = main(0)
gtk.main()
