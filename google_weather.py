
# coding: UTF-8
import  pywapi
import urllib2, re
from xml.dom import minidom
from urllib import quote


 
result = pywapi.get_weather_from_google('takatsuki, osaka, japan', 'ja')
 
print result['forecast_information']['city']
print result['forecast_information']['current_date_time']
print result['current_conditions']['condition']
print result['current_conditions']['temp_c']
