from django.urls import path
from . import views

urlpatterns = [
    path('', views.show_genres, name="home"),
    path('create/<int:id>/', views.create, name="create"),
    path('rename', views.rename, name="rename"),
    path('delete', views.delete, name="delete"),
]
