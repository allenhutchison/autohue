#!/usr/bin/python
import ConfigParser

class LightConfig(object):
  def __init__(self, config_file):
    self.config = ConfigParser.SafeConfigParser()
    self.config.read('testdata/lights_test.config')
  
  def GetBridgeIp(self):
    return self.config.get('Bridge', 'ip')

  def GetGroups(self):
    groups = []
    for x in self.config.items('Groups'):
      groups.append(x[0])
    return sorted(groups)