from rest_framework import serializers
from . import models


class MovieSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Movie
        fields = (
            'title',
            'image',
            'pub_date',
            'genre'
        )


class MovieDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Movie
        fields = ('__all__')


class InputMovieSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Movie
        fields = (
            'title',
            'subtitle',
            'image',
            'pub_date',
            'genre',
            'nation',
            'director',
            'company',
            'actors'
        )


class SimpleReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.SimpleReview
        fields = '__all__'


class SimpleReviewLikeSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.SimpleReviewLike
        fields = '__all__'


class ReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Review
        fields = '__all__'


class ReviewLikeSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.ReviewLike
        fields = '__all__'


class ReviewCommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.ReviewComment
        fields = '__all__'
