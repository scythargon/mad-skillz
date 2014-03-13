#!/usr/bin/env python
class SettingsController:
    def __init__(self,settingsContainer:SettingsContainer):
        
        #self.loadSettings()
        
    def loadSettings(self):
        config = ConfigParser.RawConfigParser()
        config.read('config.cfg')
    def applySettings(self):
