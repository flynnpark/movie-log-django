from django.urls import path
from . import views

app_name = 'movies'
urlpatterns = [
    path('', views.Movies.as_view(), name='all_movies'),
    path('<int:movie_id>/', views.MovieDetail.as_view(), name='movie_detail'),
    path('<int:movie_id>/like/', views.LikeMovie.as_view(), name='like_movie'),
    path('<int:movie_id>/unlike/', views.UnlikeMovie.as_view(), name='unlike_movie'),
    path('<int:movie_id>/sreviews/', views.SimpleReview.as_view(), name='simple_review'),
    path('<int:movie_id>/reviews/', views.ReviewAtMovie.as_view(), name='review_at_movie'),
    path('sreviews/<int:sreview_id>/like/', views.LikeSimpleReview.as_view(), name='like_sreview'),
    path('sreviews/<int:sreview_id>/unlike/', views.UnlikeSimpleReview.as_view(), name='unlike_sreview'),
]
