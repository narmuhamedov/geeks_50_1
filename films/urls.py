from django.urls import path
from . import views

urlpatterns = [
    path('emodji/', views.emodji),
    path('text/', views.text),
    path('image/', views.image)
]

