import commands
import pywapi
result = pywapi.get_weather_from_yahoo('JAXX0030')

str =  result['location']['city']+result['condition']['text']
check = commands.getoutput('/home/pi/aquestalkpi/AquesTalkPi "%s"|aplay'%str)

print str
temp = result['condition']['temp']
check2 = commands.getoutput('/home/pi/aquestalkpi/AquesTalkPi -t "%s"'% temp)
print check2
print temp
