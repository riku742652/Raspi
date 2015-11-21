# -*- coding: utf-8 -*-

import twython
import time
import datetime
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(26, GPIO.IN)

if __name__ == '__main__':
    consumerKey = 'BhPlGspnnrWfYZfeWN0tV5fu5'
    consumerSecret = 'G7MUno4Xe7spO8RKYXGa7kx1NBvd0Tqkxfp8UYUCWQTPnieu7o'
    accessToken = '2852882784-qzSN2DJKP4cRNesufx1Zl5AAsuAaoP6oKQUiPox'
    accessSecret = 'YFFZjzNRtKZmoWRoEwl9snGrC0P9n8XNjuunetSZhY2H2'

    api = twython.Twython(app_key=consumerKey,
                  app_secret=consumerSecret,
                  oauth_token=accessToken,
                  oauth_token_secret=accessSecret)
    test_tweet_str = '{0:%Y-%m-%d %H:%M:%S}\n'.format(datetime.datetime.now())+'Someone enter your room!'

    try:
	while True:
		inputValue = GPIO.input(26)
		if(inputValue == True):
			api.update_status(status=test_tweet_str)
			time.sleep(5000)

    except twython.TwythonError as e:
        print e
        