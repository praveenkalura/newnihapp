from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('geojson/states/', views.states_geojson, name='states_geojson'),
    path('geojson/nih_centers/', views.centers_geojson, name='centers_geojson'),
    path('get_route/', views.get_route, name='get_route'),
]
