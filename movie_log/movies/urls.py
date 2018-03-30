from django.conf.urls import url
from django.urls import path
from . import views

app_name = 'movies'
urlpatterns = [
    path('', views.Movies.as_view(), name='all_movies'),
]
