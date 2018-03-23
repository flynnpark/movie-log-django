from django.db import models


class Movie(models.Model):

    title = models.CharField(max_length=512)
    subtitle = models.CharField(max_length=512, null=True)
    naver_link = models.URLField(null=True)
    image = models.ImageField()
    pub_date = models.IntegerField(null=True)
    director = models.CharField(max_length=128, null=True)
    actor = models.CharField(max_length=256, null=True)
    user_rating = models.FloatField(null=True)
