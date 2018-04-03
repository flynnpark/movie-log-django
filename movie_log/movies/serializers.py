from rest_framework import serializers
from movie_log.movies import models
from movie_log.users import serializers as user_serializers


class MovieSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Movie
        fields = (
            'title',
            'image',
            'pub_date',
            'genre'
        )


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


class MovieLikeSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.MovieLike
        fields = '__all__'


class SimpleReviewSerializer(serializers.ModelSerializer):

    creator = user_serializers.UserSerializer(read_only=True)

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


class MovieDetailSerializer(serializers.ModelSerializer):

    simple_reviews = SimpleReviewSerializer(many=True, required=False)

    class Meta:
        model = models.Movie
        fields = ('__all__')
