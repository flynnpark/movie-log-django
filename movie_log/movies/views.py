from rest_framework.views import APIView
from rest_framework.response import Response
from . import models, serializers


class ListAllMovies(APIView):

    permission_classes = []

    def get(self, request, format=None):
        all_movies = models.Movie.objects.all()
        serializer = serializers.MovieSerializer(all_movies, many=True)
        return Response(data=serializer.data)
