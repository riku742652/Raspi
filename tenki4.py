# -*- coding: utf-8 -*-
import pywapi

result = pywapi.get_weather_from_yahoo('JAXX0085')

tomorrow = '---\n' + \
            u'明日(' + result['forecasts'][1]['date'] + u')の' + \
            result['location']['city'] + u'の天気をお知らせします。\n' + \
            u'天気は' + result['forecasts'][1]['text'] + u'で、\n' + \
            u'最高気温は' + result['forecasts'][1]['high'] + u'℃、\n' + \
            u'最低気温は' + result['forecasts'][1]['low'] + u'℃です。\n' + \
            '---' 

print (tomorrow)