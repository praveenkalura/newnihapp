from django.urls import path
from .views import map_home

urlpatterns = [
    path('', map_home, name='map-home'),  # Loads map.html at root
]
