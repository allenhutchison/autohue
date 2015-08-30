#!/usr/bin/python
import light_config

from phue import Bridge

import sys

config = light_config.LightConfig("testdata/lights_test.config")

b = Bridge(config.GetBridgeIp())

for l in b.lights:
  print "Name:", l.name, "\tOn:",l.on