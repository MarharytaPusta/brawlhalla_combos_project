from django.urls import path

from . import views

urlpatterns = [
    path('', views.combos),
    path('choose_character', views.combos),
]