import  pywapi
import string
import pprint
pp = pprint.PrettyPrinter(indent=4)
 
result = pywapi.get_weather_from_yahoo('JAXX5868')
 
print '---'
print result['title']
print 'city: ' + result['location']['city']
print 'date_time: ' + result['condition']['date']
print 'condition: ' + result['condition']['text']
print 'temp: ' + result['condition']['temp'] + '('+ result['units']['temperature'] + ')'
print 'geo(lat,long): ' + result['geo']['lat'] + ',' + result['geo']['long']
print '---'
pp.pprint(result)
print '---'
