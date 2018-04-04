from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from movie_log.movies import models, serializers
from movie_log.users import models as user_models, serializers as user_serializers


class Movies(APIView):

    def get(self, request, format=None):
        all_movies = models.Movie.objects.all()
        serializer = serializers.MovieSerializer(all_movies, many=True)
        return Response(data=serializer.data)


class MovieDetail(APIView):

    def get(self, request, movie_id, format=None):
        try:
            found_movie = models.Movie.objects.get(id=movie_id)
        except models.Movie.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = serializers.MovieDetailSerializer(found_movie, context={"request": request})
        return Response(data=serializer.data, status=status.HTTP_200_OK)


class LikeMovie(APIView):
    permission_classes = (IsAuthenticated, )

    def get(self, request, movie_id, format=None):
        likes = models.MovieLike.objects.filter(id=movie_id)
        like_creator_ids = likes.values('creator')
        users = user_models.User.objects.filter(id__in=like_creator_ids)
        serializer = user_serializers.ListUserSerializer(users, many=True)

        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def post(self, request, movie_id, format=None):
        user = request.user

        try:
            found_movie = models.Movie.objects.get(id=movie_id)
        except models.Movie.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        try:
            models.MovieLike.objects.get(creator=user, movie=found_movie)
            return Response(status=status.HTTP_304_NOT_MODIFIED)
        except models.MovieLike.DoesNotExist:
            new_like = models.MovieLike.objects.create(creator=user, movie=found_movie)
            new_like.save()
            return Response(status=status.HTTP_201_CREATED)


class UnlikeMovie(APIView):
    permission_classes = (IsAuthenticated, )

    def delete(self, request, movie_id, format=None):
        user = request.user

        try:
            found_movie = models.Movie.objects.get(id=movie_id)
        except models.Movie.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        try:
            preexisting_like = models.MovieLike.objects.get(creator=user, movie=found_movie)
            preexisting_like.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except models.MovieLike.DoesNotExist:
            return Response(status=status.HTTP_304_NOT_MODIFIED)


class SimpleReview(APIView):
    permission_classes = (IsAuthenticated, )

    def post(self, request, movie_id, format=None):
        user = request.user

        try:
            found_movie = models.Movie.objects.get(id=movie_id)
        except models.Movie.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = serializers.SimpleReviewSerializer(data=request.data)

        if (serializer.is_valid()):
            serializer.save(creator=user, movie=found_movie)
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LikeSimpleReview(APIView):
    permission_classes = (IsAuthenticated, )

    def post(self, request, sreview_id, format=None):
        user = request.user

        try:
            found_sreview = models.SimpleReview.objects.get(id=sreview_id)
        except models.SimpleReview.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        try:
            models.SimpleReviewLike.objects.get(creator=user, review=sreview_id)
            return Response(status=status.HTTP_304_NOT_MODIFIED)
        except models.SimpleReviewLike.DoesNotExist:
            new_like = models.SimpleReviewLike.objects.create(creator=user, review=found_sreview)
            new_like.save()
            return Response(status=status.HTTP_201_CREATED)


class UnlikeSimpleReview(APIView):
    permission_classes = (IsAuthenticated, )

    def delete(self, request, sreview_id, format=None):
        user = request.user

        try:
            found_sreview = models.SimpleReview.objects.get(id=sreview_id)
        except models.SimpleReview.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        try:
            preexisting_like = models.SimpleReviewLike.objects.get(creator=user, review=found_sreview)
            preexisting_like.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except models.SimpleReviewLike.DoesNotExist:
            return Response(status=status.HTTP_304_NOT_MODIFIED)
