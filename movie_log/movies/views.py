from rest_framework import status
from rest_framework import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from movie_log.movies import models, serializers
from movie_log.users import models as user_models


class Movies(APIView):

    def get(self, request, format=None):
        all_movies = models.Movie.objects.all()
        serializer = serializers.MovieSerializer(all_movies, many=True)
        return Response(data=serializer.data)


class LikeMovie(APIView):

    def get(self, request, movie_id, format=None):
        likes = models.MovieLike.objects.filter(movie__id=movie_id)
        like_creator_ids = likes.values('creator_id')
        users = user_models.User.objects.filter(id__in=like_creator_ids)

        serializer = user_ser
