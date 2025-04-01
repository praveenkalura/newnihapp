from django.urls import path
from . import views
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import IndiaStateViewSet

urlpatterns = [
    path('', views.home, name='home'),
    path('geojson/states/', views.states_geojson, name='states_geojson'),
    path('geojson/nih_centers/', views.centers_geojson, name='centers_geojson'),
    path('get_route/', views.get_route, name='get_route'),
]


router = DefaultRouter()
router.register(r'india-states', IndiaStateViewSet)

urlpatterns = [
    path("api/", include(router.urls)),
]
