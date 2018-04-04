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

    @property
    def like_count(self):
        return self.likes.all().count()


class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class MovieLike(TimeStampedModel):
    creator = models.ForeignKey(user_models.User, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='likes')


class SimpleReview(TimeStampedModel):
    creator = models.ForeignKey(user_models.User, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='simple_reviews')
    rating = models.FloatField()
    message = models.TextField()

    def __str__(self):
            return '[{}] {}'.format(self.rating, self.message)

    @property
    def like_count(self):
        return self.likes.all().count()


class SimpleReviewLike(TimeStampedModel):
    creator = models.ForeignKey(user_models.User, on_delete=models.CASCADE)
    review = models.ForeignKey(SimpleReview, on_delete=models.CASCADE, related_name='likes')


class Review(TimeStampedModel):
    creator = models.ForeignKey(user_models.User, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='reviews')
    rating = models.FloatField()
    title = models.TextField(null=True)
    message = models.TextField()


class ReviewLike(TimeStampedModel):
    creator = models.ForeignKey(user_models.User, on_delete=models.CASCADE)
    review = models.ForeignKey(Review, on_delete=models.CASCADE, related_name='likes')


class ReviewComment(TimeStampedModel):
    creator = models.ForeignKey(user_models.User, on_delete=models.CASCADE)
    review = models.ForeignKey(Review, on_delete=models.CASCADE, related_name='comments')
    message = models.TextField()
