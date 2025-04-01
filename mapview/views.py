from django.core.serializers import serialize
from django.http import JsonResponse
from .models import State, NIHCenter
import openrouteservice

def states_geojson(request):
    data = serialize('geojson', State.objects.all(), geometry_field='geom', fields=['name'])
    return JsonResponse(data, safe=False)

def centers_geojson(request):
    data = serialize('geojson', NIHCenter.objects.all(), geometry_field='geom', fields=['name'])
    return JsonResponse(data, safe=False)

def get_route(request):
    coords = request.GET.getlist('coords[]')
    client = openrouteservice.Client(key='YOUR_API_KEY')
    route = client.directions(
        coordinates=[[float(coords[0]), float(coords[1])], [float(coords[2]), float(coords[3])]],
        profile='driving-car',
        format='geojson'
    )
    return JsonResponse(route)
