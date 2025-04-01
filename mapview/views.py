from django.shortcuts import render
from django.core.serializers import serialize
from django.http import JsonResponse
from .models import State, NIHCenter
import openrouteservice

def home(request):
    return render(request, 'map.html')

def states_geojson(request):
    data = serialize('geojson', State.objects.all(), geometry_field='geom', fields=['name'])
    return JsonResponse(data, safe=False)

def centers_geojson(request):
    data = serialize('geojson', NIHCenter.objects.all(), geometry_field='geom', fields=['name'])
    return JsonResponse(data, safe=False)
