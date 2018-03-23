from django.db import models
from movie_log.users import models as user_models


class Movie(models.Model):
    title = models.CharField(max_length=512)
    subtitle = models.CharField(max_length=512, null=True)
    naver_link = models.URLField(null=True)
    image = models.ImageField()
    pub_date = models.IntegerField(null=True)
    director = models.CharField(max_length=128, null=True)
    actor = models.CharField(max_length=256, null=True)
    user_rating = models.FloatField(null=True)


class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class SimpleReview(TimeStampedModel):
    creator = models.ForeignKey(user_models.User, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    rating = models.FloatField()
    message = models.TextField()


class Review(TimeStampedModel):
    creator = models.ForeignKey(user_models.User, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    rating = models.FloatField()
    message = models.TextField()
