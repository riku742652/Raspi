import  pywapi
import string

result = pywapi.get_weather_from_yahoo('JAXX0030')

print '---'
print result['title']
print 'city: ' + result['location']['city']
print 'date_time: ' + result['condition']['date']
print 'condition: ' + result['condition']['text']
print 'temp: ' + result['condition']['temp'] + '('+ result['units']['temperature'] + ')'
print 'geo(lat,long): ' + result['geo']['lat'] + ',' + result['geo']['long']
print '---'
