# -*- coding: utf-8 -*-

import twython

if __name__ == '__main__':
    consumerKey = 'BhPlGspnnrWfYZfeWN0tV5fu5'
    consumerSecret = 'G7MUno4Xe7spO8RKYXGa7kx1NBvd0Tqkxfp8UYUCWQTPnieu7o'
    accessToken = '2852882784-qzSN2DJKP4cRNesufx1Zl5AAsuAaoP6oKQUiPox'
    accessSecret = 'YFFZjzNRtKZmoWRoEwl9snGrC0P9n8XNjuunetSZhY2H2'

    api = twython.Twython(app_key=consumerKey,
                  app_secret=consumerSecret,
                  oauth_token=accessToken,
                  oauth_token_secret=accessSecret)
    test_tweet_str = '防御固めのローラーは最強'

    try:
        api.update_status(status=test_tweet_str)
    except twython.TwythonError as e:
        print e
