from django.urls import path

from . import views

urlpatterns = [
    path('', views.all_legends),
    path('<str:legend_name>/', views.get_all_legend_info),
]