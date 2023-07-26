from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from rest_framework import viewsets

from .models import WashroomData
from .serializers import WashroomDataSerializer

# Create your views here.

# def index(request):
#     washroom_list = WashroomData.objects.order_by("-_id")[:5]
#     template = loader.get_template("basicmap/index.html")
#     context = {
#         "washroom_list": washroom_list,
#     }
#     return HttpResponse(template.render(context, request))

def index(request):
    washroom_list = WashroomData.objects.order_by("opendata_id")[:5]
    context = {
        "washroom_list": washroom_list,
    }
    context = {
        "washroom_list": [{ "type": "Feature", "properties": { "opendata_id": 778, "id": 70, "asset_id": 29421, "location": "Greenwood Park", "alternative_name": "Greenwood Park Fieldhouse Washroom", "type": "Washroom Building", "location_details": "Located in the fieldhouse east of the skate trail, south of the playground.", "url": "https:\/\/www.toronto.ca\/data\/parks\/prd\/facilities\/complex\/70\/index.html", "address": "150 Greenwood Ave  " }, "geometry": { "type": "MultiPoint", "coordinates": [ [ -79.328683485008398, 43.669449113634101 ] ] } }],
    }
    # context = {'test': 123, }
    return render(request, 'basicmap/index.html', context)
    
class WashroomDataView(viewsets.ModelViewSet):
    serializer_class = WashroomDataSerializer
    queryset = WashroomData.objects.all()
