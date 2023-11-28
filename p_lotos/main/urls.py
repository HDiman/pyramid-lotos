from django.urls import path
from . import views

urlpatterns = [
    path('', views.show_genres, name="home"),
    path('rename', views.rename, name="rename"),
]
