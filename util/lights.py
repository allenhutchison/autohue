#!/usr/bin/python
import light_config

from phue import Bridge

import sys

config = light_config.LightConfig("testdata/lights_test.config")

b = Bridge(config.GetBridgeIp())

lights = b.get_light_objects()

if sys.argv[1] == "off":
  for light in lights:
    light.on = False

if sys.argv[1] == "evening":
  for light in lights:
    light.on = True
    light.brightness = 254
    light.xy = [0.4448,0.4066]
elif sys.argv[1] == "morning":
  for light in lights:
    light.on = True
    light.brightness = 254
    light.xy = [0.368,0.3686]

