from django.contrib import admin
from . import models


@admin.register(models.Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'subtitle',
        'image',
        'pub_date',
        'director',
        'actor',
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
