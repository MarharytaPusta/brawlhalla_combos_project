from django.urls import path

from . import views

urlpatterns = [
    path('', views.all_legends),
    path('api/save-combo/', views.SaveComboAPIView.as_view(), name='api_save_combo'),
    path('<str:legend_name>/', views.get_all_legend_info),
]