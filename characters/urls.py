from django.urls import path

from . import views

urlpatterns = [
    path('', views.combos),
    path('<str:legend_name>/', views.get_all_legend_info),
]