import  pywapi
import string

yahoo_result = pywapi.get_weather_from_yahoo('10001')

print "Yahoo says: It is " + string.lower(yahoo_result['condition']['text']) + " and " + yahoo_result['condition']['temp'] + "C now in New York.\n\n"

#coding: UTF-8
import pywapi
import string
fp = open("location_result.dat", "w")
fp.write("location ID   Name   Geodata(lat,long)\n")

for num in xrange(10000):
        tag_num = '{0:04}'.format(num+1)
        tag_name = "JAXX" + str(tag_num)
        try:
            result = pywapi.get_weather_from_yahoo(tag_name)
            fp.write(tag_name + " " + result['location']['city'] + " " + result['geo']['lat'] + "," + result['geo']['long'])
            fp.write("\n")
        except:
            fp.write(tag_name + " N/A" + " N/A,N/A")
            fp.write("\n")
fp.close()
