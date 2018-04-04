from django.urls import path
from . import views

app_name = 'movies'
urlpatterns = [
    path('', views.Movies.as_view(), name='all_movies'),
    path('<int:movie_id>/', views.MovieDetail.as_view(), name='movie_detail'),
    path('<int:movie_id>/like/', views.LikeMovie.as_view(), name='like_movie'),
    path('<int:movie_id>/unlike/', views.UnlikeMovie.as_view(), name='unlike_movie'),
    path('<int:movie_id>/sreview/', views.SimpleReview.as_view(), name='simple_review')
]
