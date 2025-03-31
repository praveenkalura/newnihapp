from django.urls import path
from . import views

urlpatterns = [
    path('geojson/states/', views.states_geojson, name='states_geojson'),
    path('geojson/nih_centers/', views.centers_geojson, name='centers_geojson'),
    path('get_route/', views.get_route, name='get_route'),
]
