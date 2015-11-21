# -*- coding: utf-8 -*-
import pywapi
import pprint

result = pywapi.get_weather_from_yahoo('JAXX0085')

pp = pprint.PrettyPrinter(indent=4)

pp.pprint(result)
