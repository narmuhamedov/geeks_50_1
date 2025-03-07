from django.urls import path
from . import views

urlpatterns = [
    path('emodji/', views.emodji),
    path('text/', views.text),
    path('image/', views.image),
    path('film_list/', views.films_list),
    path('film_list/<int:id>/', views.film_detail),
]
