# -*- coding: utf-8 -*-
import pywapi

result = pywapi.get_weather_from_yahoo('JAXX0085')

weather = '---\n' + \
    result['title'] + '\n���݂�' + \
    result['location']['city'] + u'�̓V�C:' + \
    result['condition']['text'] + u'\n' +\
    u'---'

print weather