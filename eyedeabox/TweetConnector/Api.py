import tweepy
import itertools

# TODO: Remove duplicate worded tweets (i.e retweets)
"""
Class to run queries and interface with the core tweepy twitter api    
"""


class TwitterApi:
    _hashtags = [
        'I need an app to',
        'I wish there was a way to',
        'Why is process so complicated',
        'Is there a business',
        'What I need is',
    ]

    def __init__(self,
                 consumer_key: str,
                 consumer_secret: str,
                 access_token: str,
                 access_token_secret: str):
        self.__ck = consumer_key
        self.__cs = consumer_secret
        self.__at = access_token
        self.__ats = access_token_secret
        self.__tapi: tweepy.API = None

    def connect(self):
        authorization = tweepy.OAuthHandler(self.__ck, self.__cs)
        authorization.set_access_token(self.__at, self.__ats)

        self.__tapi = tweepy.API(authorization, wait_on_rate_limit=True)

    def runQuery(self):
        if self.__tapi:
            tweets = [self.__tapi.search(query, tweet_mode="extended") for query in self._hashtags]
            return list(itertools.chain.from_iterable(tweets))
        raise ValueError("Did not connect before executing query")

    def disconnect(self):
        raise RuntimeError("Not implemented yet")
