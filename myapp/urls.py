from django.urls import path
from . import views

urlpatterns = [
    path('wind-data/', views.handle_wind_data, name='handle_wind_data'),
    path('dashboard/', views.dashboard, name='dashboard'),
]