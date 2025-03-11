from django.urls import path
from . import views

urlpatterns = [
    path('emodji/', views.emodji),
    path('text/', views.text),
    path('image/', views.image),
    path('', views.films_list, name='films'),
    path('film_list/<int:id>/', views.film_detail),
]
