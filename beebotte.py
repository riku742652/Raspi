#!/usr/bin/env python

############################################################
# This code uses the Beebotte API, you must have an account.
# You can register here: http://beebotte.com/register
############################################################

import time
import Adafruit_DHT
from beebotte import *

### Replace API_KEY and SECRET_KEY with those of your account
bbt = BBT('6ded29ec204c17e1d077388f7ce01497', '03ace8ed92b0119217662352f5481e2d09640c8e4b4cf50836180130ae68aa39')

period = 60 ## Sensor data reporting period (1 minute)
pin = 4 ## Assuming the DHT11 sensor is connected to GPIO pin number 4

### Change channel name and resource names as suits you
temp_resource   = Resource(bbt, 'RaspberryPi', 'temperature')
humid_resource  = Resource(bbt, 'RaspberryPi', 'humidity')

def run():
  while True:
    ### Assume 
    humidity, temperature = Adafruit_DHT.read_retry( Adafruit_DHT.DHT11, pin )
    if humidity is not None and temperature is not None:
#        print "Temp={0:f}*C  Humidity={1:f}%d".format(temperature, humidity)
        try:
          #Send temperature to Beebotte
          temp_resource.write(temperature)
          #Send humidity to Beebotte
          humid_resource.write(humidity)
        except Exception:
          ## Process exception here
          print ("Error while writing to Beebotte")
    else:
        print ("Failed to get reading. Try again!")

    #Sleep some time
    time.sleep( period )

run()
