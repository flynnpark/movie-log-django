from django.contrib import admin
from movie_log.movies import models


@admin.register(models.Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'subtitle',
        'image',
        'genre',
        'pub_date',
        'director',
    )


@admin.register(models.MovieLike)
class MovieLikeAdmin(admin.ModelAdmin):
    list_display = (
        'movie',
        'creator',
        'created_at'
    )


@admin.register(models.SimpleReview)
class SimpleReviewAdmin(admin.ModelAdmin):
    list_display = (
        'movie',
        'creator',
        'rating',
        'message',
    )


@admin.register(models.SimpleReviewLike)
class SimpleReviewLikeAdmin(admin.ModelAdmin):
    list_display = (
        'creator',
        'review',
    )


@admin.register(models.Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = (
        'movie',
        'creator',
        'rating',
        'title',
        'message',
    )


@admin.register(models.ReviewLike)
class ReviewLikeAdmin(admin.ModelAdmin):
    list_display = (
        'creator',
        'review',
    )


@admin.register(models.ReviewComment)
class ReviewCommentAdmin(admin.ModelAdmin):
    list_display = (
        'creator',
        'review',
        'message',
    )
