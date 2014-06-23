#!/usr/bin/python
import unittest

import light_config

class TestLightConfig(unittest.TestCase):
  def setUp(self):
    self.config_file = 'testdata/lights_test.config'
  
  def test_ip(self):
    lc = light_config.LightConfig(self.config_file)
    self.assertEqual('192.168.1.143', lc.GetBridgeIp())

if __name__ == '__main__':
  unittest.main()