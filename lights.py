#!/usr/bin/python
from phue import Bridge

import sys

b = Bridge('10.0.1.24') # Enter bridge IP here.

#If running for the first time, press button on bridge and run with b.connect() uncommented
#b.connect()

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

