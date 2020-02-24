from django.db import models

# Register your models here.
class TweetRef(models.Model):
    tweet_text = models.CharField(max_length=280)
    tweet_date = models.DateField()
    tweet_user = models.CharField(max_length=256, blank=True, null=True)
    tweet_id = models.IntegerField(primary_key=True)
