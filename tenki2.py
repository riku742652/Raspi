# -*- coding: utf-8 -*-
import pywapi

result = pywapi.get_weather_from_yahoo('JAXX0085')

weather = '---\n' + \
    result['title'] + '\n現在の' + \
    result['location']['city'] + u'の天気:' + \
    result['condition']['text'] + u'\n' +\
    u'---'

print weather
