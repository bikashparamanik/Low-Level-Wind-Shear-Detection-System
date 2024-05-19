from django.contrib import admin
from django.urls import path
from myapp.views import handle_wind_data, dashboard

urlpatterns = [
    path('admin/', admin.site.urls),
    path('wind-data/', handle_wind_data, name='wind_data'),
    path('', dashboard, name='dashboard'),
]