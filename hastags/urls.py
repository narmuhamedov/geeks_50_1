from django.urls import path
from . import views

urlpatterns = [
    path('all_hashtags_films/', views.all_category_film, name='all'),
    path('comedy_hashtags_films/', views.comedy_category_film, name='comedy'),
    path('fantastic_hashtags_films/', views.fantastic_category_film, name='fantastic'),
]