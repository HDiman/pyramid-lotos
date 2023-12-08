from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="home"),
    path('edit/<int:id>/', views.edit, name="edit"),
    path('relocate/<int:id>/', views.relocate, name="relocate"),
    path('create', views.create, name="create"),
    path('rename', views.rename, name="rename"),
    path('delete', views.delete, name="delete"),
    path('show_genres', views.show_genres, name="show_genres"),
    path('get_posts/', views.get_posts, name='get_posts'),
]
