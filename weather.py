# -*- coding: utf-8 -*-

import commands
import pywapi
result = pywapi.get_weather_from_yahoo('JAXX0030')

str =  result['condition']['text']
location = result['location']['city']
temp = result['condition']['temp']
commands.getoutput('/home/pi/aquestalkpi/AquesTalkPi "%s"|aplay'%location)
commands.getoutput('/home/pi/aquestalkpi/AquesTalkPi "の天気は"|aplay')

if('Cloudy' in str):
	commands.getoutput('/home/pi/aquestalkpi/AquesTalkPi "曇り"|aplay')
if('Sunny' in str):
	commands.getoutput('/home/pi/aquestalkpi/AquesTalkPi "晴れ"|aplay')
if('Rain' in str):
	commands.getoutput('/home/pi/aquestalkpi/AquesTalkPi "雨"|aplay')
commands.getoutput('/home/pi/aquestalkpi/AquesTalkPi "です。"|aplay')
print str
commands.getoutput('/home/pi/aquestalkpi/AquesTalkPi "平均気温は"|aplay')
commands.getoutput('/home/pi/aquestalkpi/AquesTalkPi "%s"|aplay'%temp)
commands.getoutput('/home/pi/aquestalkpi/AquesTalkPi "どです。"|aplay')
print temp
