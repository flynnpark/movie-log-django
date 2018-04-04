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
            'genre',
            'like_count'
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
        fields = (
            'id',
            'creator',
            'movie',
            'rating',
            'message',
            'like_count'
        )


class SimpleReviewLikeSerializer(serializers.ModelSerializer):

    creator = user_serializers.UserSerializer(read_only=True)

    class Meta:
        model = models.SimpleReviewLike
        fields = (
            'id',
            'creator',
            'movie',
            'rating',
            'title',
            'message'
        )


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
        fields = (
            'title',
            'subtitle',
            'image',
            'pub_date',
            'genre',
            'nation',
            'director',
            'company',
            'actors',
            'like_count',
            'simple_reviews'
        )


class ReviewAtMovieSerializer(serializers.ModelSerializer):

    reviews = ReviewSerializer(many=True, required=False)

    class Meta:
        model = models.Movie
        fields = (
            'title',
            'reviews'
        )
