from django.db import models
from movie_log.users import models as user_models


class Movie(models.Model):
    title = models.CharField(max_length=512)
    subtitle = models.CharField(max_length=512, null=True)
    image = models.ImageField(blank=True)
    pub_date = models.CharField(max_length=32, null=True)
    genre = models.CharField(max_length=128, null=True)
    nation = models.CharField(max_length=32, null=True)
    director = models.CharField(max_length=128, null=True)
    company = models.CharField(max_length=256, null=True)
    actors = models.TextField(null=True)

    def __str__(self):
        return '{}({})'.format(self.title, self.pub_date)


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

    def __str__(self):
            return '[{}] {}'.format(self.rating, self.message)


class SimpleReviewLike(TimeStampedModel):
    creator = models.ForeignKey(user_models.User, on_delete=models.CASCADE)
    review = models.ForeignKey(SimpleReview, on_delete=models.CASCADE)


class Review(TimeStampedModel):
    creator = models.ForeignKey(user_models.User, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    rating = models.FloatField()
    title = models.TextField(null=True)
    message = models.TextField()


class ReviewLike(TimeStampedModel):
    creator = models.ForeignKey(user_models.User, on_delete=models.CASCADE)
    review = models.ForeignKey(Review, on_delete=models.CASCADE)


class ReviewComment(TimeStampedModel):
    creator = models.ForeignKey(user_models.User, on_delete=models.CASCADE)
    review = models.ForeignKey(Review, on_delete=models.CASCADE)
    message = models.TextField()
