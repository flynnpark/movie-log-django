from django.urls import path
from . import views

app_name = 'movies'
urlpatterns = [
    path('', views.Movies.as_view(), name='all_movies'),
    # 영화 상세 정보 및 간단 리뷰 조회
    path('<int:movie_id>/', views.MovieDetail.as_view(), name='movie_detail'),
    # 영화 좋아요 리스트
    path('<int:movie_id>/likes/', views.MovieLikeList.as_view(), name='movie_like_list'),
    # 영화 좋아요
    path('<int:movie_id>/like/', views.LikeMovie.as_view(), name='like_movie'),
    # 영화 좋아요 취소
    path('<int:movie_id>/unlike/', views.UnlikeMovie.as_view(), name='unlike_movie'),
    # 간단 리뷰 작성
    path('<int:movie_id>/sreview/', views.SimpleReview.as_view(), name='simple_review'),
    # 리뷰 리스트 및 작성
    path('<int:movie_id>/review/', views.ReviewAtMovie.as_view(), name='review_at_movie'),
    # 간단 리뷰 좋아요
    path('sreview/<int:sreview_id>/like/', views.LikeSimpleReview.as_view(), name='like_sreview'),
    # 간단 리뷰 좋아요 취소
    path('sreview/<int:sreview_id>/unlike/', views.UnlikeSimpleReview.as_view(), name='unlike_sreview'),
    # 리뷰 조회
    path('review/<int:review_id>/', views.ReviewDetail.as_view(), name='review_detail'),
    # 리뷰 좋아요 리스트
    path('review/<int:review_id>/likes/', views.ReviewLikeList.as_view(), name='review_like_list'),
    # 리뷰 좋아요
    path('review/<int:review_id>/like/', views.LikeReview.as_view(), name='like_review'),
    # 리뷰 좋아요 취소
    path('review/<int:review_id>/unlike/', views.UnlikeReview.as_view(), name='unlike_review'),
]
