#!/usr/bin/env python
import ConfigParser
import AsettingsContainer
class SettingsController:
    def __init__(self,settingsContainer_):
        self.settingsContainer = settingsContainer_
        #self.loadSettings()
        
    def loadSettings(self):
        config = ConfigParser.RawConfigParser()
        config.read('config.cfg')
    def applySettings(self):
        return
