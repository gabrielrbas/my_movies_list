from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:movie_id>", views.detail, name="detail"),
    path("new_movie", views.new_movie, name="new_movie"),
    path("update/<int:movie_id>", views.update, name="update"),
    path("delete/<int:movie_id>", views.delete, name="delete"),
]
