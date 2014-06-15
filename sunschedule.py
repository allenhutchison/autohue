import ephem
import datetime

now = datetime.datetime.utcnow()
pad = datetime.timedelta(minutes=30)
evening_off = datetime.datetime

obs = ephem.Observer()
obs.lat = '37.33'
obs.long= '-121.9'
obs.date = now

sun = ephem.Sun()

rise_time = obs.next_rising(sun).datetime()
set_time = obs.next_setting(sun).datetime()

print "local rise: ", ephem.localtime(obs.next_rising(sun))
print "local set: ", ephem.localtime(obs.next_setting(sun))

print "UTC Now: ", now
print "UTC Set: ", set_time
print "Diff: ", set_time - now

if (set_time - now) <= pad:
  print "turn on the lights"
