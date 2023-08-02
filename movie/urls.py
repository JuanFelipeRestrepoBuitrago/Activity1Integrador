from django.urls import path
from . import views as movie_views

urlpatterns = [
    path("", movie_views.home, name="home"),
]