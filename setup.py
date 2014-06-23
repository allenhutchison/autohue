#!/usr/bin/python
import ConfigParser

from phue import Bridge

config = ConfigParser.SafeConfigParser()

config.read('testdata/lights_test.config')

ip = config.get('Bridge', 'ip')

b = Bridge(ip)

print "Push the button on your bridge."
b.connect()
