from .Api import TwitterApi
from homepage.models import TweetRef

class DataRefresh():
    def __init__(self):
        self.__twapi: TwitterApi = TwitterApi(
            'GeoyOlLBm85Y4VroHHklBVn1i',
            'JtCdxEumajgcRPcEXZWq9TxQKl7UmDg8MlF6mn2hTzNCstZiRb',
            '224138640-3fA4V37Eve9OCYHwLYfGd9BoGKwe7BfdQhRq8jqe',
            '93hvjOo8wEEh2JUGkDhOOOTnTcWaAdL1APv6sUu08EhXp')
        self.__twapi.connect()

    def refresh(self):
        for tweet in self.__twapi.runQuery():
            if not TweetRef.objects.filter(pk=tweet.id).exists():
                newModel = TweetRef()
                newModel.tweet_text = tweet.full_text
                newModel.tweet_id = tweet.id
                newModel.tweet_date = tweet.created_at
                newModel.tweet_user = tweet.user.screen_name
                newModel.save()
