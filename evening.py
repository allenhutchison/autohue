#!/usr/bin/python
from phue import Bridge

import sys

b = Bridge('10.0.1.24') # Enter bridge IP here.

#If running for the first time, press button on bridge and run with b.connect() uncommented
#b.connect()

lights = b.get_light_objects()

if sys.argv[1] == "on":
  for light in lights:
    light.on = True
    light.brightness = 254
    light.xy = [0.4448,0.4066]
else:
  for light in lights:
    light.on = False

