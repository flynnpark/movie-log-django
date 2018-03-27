from rest_framework import serializers
from . import models


class MovieSerializer(serializers.Serializer):

    class Meta:
        model = models.Movie
        fields = '__all__'


class SimpleReviewSerializer(serializers.Serializer):

    class Meta:
        model = models.SimpleReview
        fields = '__all__'


class SimpleReviewLikeSerializer(serializers.Serializer):

    class Meta:
        model = models.SimpleReviewLike
        fields = '__all__'


class ReviewSerializer(serializers.Serializer):

    class Meta:
        model = models.Review
        fields = '__all__'


class ReviewLikeSerializer(serializers.Serializer):

    class Meta:
        model = models.ReviewLike
        fields = '__all__'


class ReviewCommentSerializer(serializers.Serializer):

    class Meta:
        model = models.ReviewComment
        fields = '__all__'
