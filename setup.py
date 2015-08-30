#!/usr/bin/python
import light_config

from phue import Bridge

config = light_config.LightConfig("testdata/lights_test.config")

b = Bridge(config.GetBridgeIp())

print "Push the button on your bridge."
b.connect()