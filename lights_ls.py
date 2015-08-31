#!/usr/bin/python
import light_config

from phue import Bridge

import sys

config = light_config.LightConfig("testdata/lights_test.config")

b = Bridge(config.GetBridgeIp())

def print_light(light):
  if light.on:
    label = "On"
  else:
    label = "Off"
  print 'ID: {:<3}'.format(light.light_id),
  print 'Name: {:<15}'.format(light.name),
  print 'Status: {:<4}'.format(label),
  print 'Brightness: {:<4}'.format(light.brightness),
  print 'Hue: {:<3}'.format(light.hue)


lights = b.get_light_objects('id')

for l in lights:
  print_light(lights[l])

