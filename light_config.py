#!/usr/bin/python
from google.protobuf import text_format
from proto import config_pb2

class LightConfig(object):
  def __init__(self, config_file):
    self.config_file = config_file
    self.ReadConfigFromFile()

  def ReadConfigFromFile(self):
    f = open(self.config_file, 'r')
    self.config = config_pb2.AutoHueConfig()
    text_format.Merge(f.read(), self.config)
    f.close()

  def GetBridgeIp(self):
    return self.config.bridge_info.ip_address

