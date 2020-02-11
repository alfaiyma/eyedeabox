import tweepy

# Setup keys to authenticate requests

consumer_key= 'GeoyOlLBm85Y4VroHHklBVn1i'
consumer_secret= 'JtCdxEumajgcRPcEXZWq9TxQKl7UmDg8MlF6mn2hTzNCstZiRb'
access_token= '224138640-3fA4V37Eve9OCYHwLYfGd9BoGKwe7BfdQhRq8jqe'
access_token_secret= '93hvjOo8wEEh2JUGkDhOOOTnTcWaAdL1APv6sUu08EhXp'

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
