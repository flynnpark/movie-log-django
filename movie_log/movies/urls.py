from django.conf.urls import url
from . import views

app_name = 'movies'
urlpatterns = [
    url(r'^all/$', views.ListAllMovies.as_view(), name='all_movies'),
]
