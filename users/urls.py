from django.urls import path
from django.contrib.auth.views import LogoutView

from . import views

urlpatterns = [
    path('register/', views.register),
    path('login/', views.login),
    path('profile/', views.profile),
    path('profile/combos', views.user_combos),
    path('logout/', views.logout, name='logout'),
]