# -*- coding: utf-8 -*-
import pywapi

result = pywapi.get_weather_from_yahoo('JAXX0085')

weather = '---\n' + \
    result['title'] + '\nåªç›ÇÃ' + \
    result['location']['city'] + u'ÇÃìVãC:' + \
    result['condition']['text'] + u'\n' +\
    u'---'

print weather