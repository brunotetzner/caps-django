from django.urls import path
from .views import AnimeView, AnimeIdView, RetrieveAnimeView

urlpatterns = [
    path("animes/", AnimeView.as_view()),
    path("animes/<str:anime_id>/", AnimeIdView.as_view()),
    path("animes/one/<str:pk>/", RetrieveAnimeView.as_view()),
]
