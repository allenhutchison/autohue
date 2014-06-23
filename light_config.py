#!/usr/bin/python
import ConfigParser

class LightConfig(object):
  def __init__(self, config_file):
    self.config = ConfigParser.SafeConfigParser()
    self.config.read('testdata/lights_test.config')
  
  def GetBridgeIp(self):
    return self.config.get('Bridge', 'ip')