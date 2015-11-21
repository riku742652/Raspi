#!/usr/bin/env python
#coding:utf-8

import os
from twython import Twython


CONSUMER_KEY = 'BhPlGspnnrWfYZfeWN0tV5fu5'
CONSUMER_SECRET = 'G7MUno4Xe7spO8RKYXGa7kx1NBvd0Tqkxfp8UYUCWQTPnieu7o'
ACCESS_KEY = '2852882784-qzSN2DJKP4cRNesufx1Zl5AAsuAaoP6oKQUiPox'
ACCESS_SECRET ='YFFZjzNRtKZmoWRoEwl9snGrC0P9n8XNjuunetSZhY2H2'

api = Twython(CONSUMER_KEY,CONSUMER_SECRET,ACCESS_KEY,ACCESS_SECRET)

cmd = '/opt/vc/bin/vcgencmd measure_temp'
line = os.popen(cmd).readline().strip()
temp = line.split('=')[1].split("‘")[0]

api.update_status(status='CPUtemp:'+temp)
