# -*- coding: utf-8 -*-

import commands
import pywapi
import RPi.GPIO as GPIO
import time
result = pywapi.get_weather_from_yahoo('JAXX0030')

BLUE = 17
GREEN = 22
RED = 23

GPIO.setmode(GPIO.BCM)

GPIO.setup(RED, GPIO.OUT)
GPIO.setup(GREEN, GPIO.OUT)


str =  result['condition']['text']
location = result['location']['city']
temp = result['condition']['temp']
commands.getoutput('/home/pi/aquestalkpi/AquesTalkPi "%s"|aplay'%location)
commands.getoutput('/home/pi/aquestalkpi/AquesTalkPi "の天気は"|aplay')

#if('Cloudy' in str):
#	commands.getoutput('/home/pi/aquestalkpi/AquesTalkPi "曇り"|aplay')
#	GPIO.output(RED,True)
#	GPIO.output(BLUE,True)
#	GPIO.output(GREEN,True)
	
#if('Sunny' in str):
commands.getoutput('/home/pi/aquestalkpi/AquesTalkPi "晴れ"|aplay')
GPIO.output(RED,True)
GPIO.output(GREEN,True)
#if('Rain' in str):
#	commands.getoutput('/home/pi/aquestalkpi/AquesTalkPi "雨"|aplay')
#	GPIO.output(BLUE,True)
#commands.getoutput('/home/pi/aquestalkpi/AquesTalkPi "です。"|aplay')
print str
commands.getoutput('/home/pi/aquestalkpi/AquesTalkPi "平均気温は"|aplay')
commands.getoutput('/home/pi/aquestalkpi/AquesTalkPi "%s"|aplay'%temp)
commands.getoutput('/home/pi/aquestalkpi/AquesTalkPi "どです。"|aplay')
print temp
GPIO.cleanup()
