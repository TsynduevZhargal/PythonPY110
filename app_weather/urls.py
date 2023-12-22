from django.urls import path, include
from .views import weather_view


urlpatterns = [
    path('', weather_view),
]
