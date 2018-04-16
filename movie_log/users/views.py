from rest_framework import status
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from movie_log.users import models, serializers


class UserProfile(APIView):
    permission_classes = (IsAuthenticated, )

    def get_user(self, username):
        try:
            found_user = models.User.objects.get(username=username)
            return found_user
        except models.User.DoesNotExist:
            return None

    def get(self, request, username, format=None):
        found_user = self.get_user(username)
        if found_user is None:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = serializers.UserSerializer(found_user)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
