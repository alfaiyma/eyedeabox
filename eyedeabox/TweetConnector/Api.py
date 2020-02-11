import tweepy
import itertools

class twitterApi():
    _queries = [
        'I need an app',
        'Is there an app to',
        'Give me an app'
    ]

    def __init__(self, 
    consumer_key: str,
    consumer_secret:str,
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
        if self.__tapi  :
            tweets = [self.__tapi.search(query) for query in self._queries] 
            return list(itertools.chain.from_iterable(tweets))
        raise ValueError("Did not connect before executing query")

    def disconnect(self):
        raise RuntimeError("Not implemented yet")
