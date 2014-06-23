#!/usr/bin/python
import unittest

import light_config

class TestLightConfig(unittest.TestCase):
  def setUp(self):
    self.config_file = 'testdata/lights_test.config'
    self.lc = light_config.LightConfig(self.config_file)
  
  def test_ip(self):
    self.assertEqual('192.168.1.143', self.lc.GetBridgeIp())

  def test_groups(self):
    self.assertEqual(['kitchen', 'living_room', 'porch'], self.lc.GetGroups())


if __name__ == '__main__':
  unittest.main()