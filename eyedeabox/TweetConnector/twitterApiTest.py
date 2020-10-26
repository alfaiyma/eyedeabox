import tweepy

# Setup keys to authenticate requests

consumer_key= 'consumer_key'
consumer_secret= 'consumer_secret'
access_token= 'token'
access_token_secret= 'token_secret'

def vimTest(number: int):
    print(number)

def main():
    print('YOLO')

    authorization = tweepy.OAuthHandler(consumer_key, consumer_secret)
    authorization.set_access_token(access_token, access_token_secret)

    api = tweepy.API(authorization, wait_on_rate_limit=True)

    for tweet in api.home_timeline():
        print(tweet.text)

def connect_and_get_tweets():
    authorization = tweepy.OAuthHandler(consumer_key, consumer_secret)
    authorization.set_access_token(access_token, access_token_secret)

    api = tweepy.API(authorization, wait_on_rate_limit=True)

    # for tweet in api.home_timeline():
    #     print(tweet.text)
    return api.home_timeline()


if (__name__ == '__main__'):
    main()
