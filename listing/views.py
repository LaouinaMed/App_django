from django.shortcuts import render
from django.http import HttpResponse
from math import *
from .models import Placement
from django.shortcuts import render
import geopy.distance

from django.contrib.auth.decorators import login_required

@login_required(login_url='home')


def great_circle_distance(latitude1, longitude1, latitude2, longitude2):
  d = pi / 180  # factor to convert degrees to radians
  return acos(sin(float(longitude1)*d) * sin(float(longitude2)*d) + cos(float(longitude1)*d) * cos(float(longitude2)*d) * cos((float(latitude1) - float(latitude2)) * d)) / d
# Create your views here.
def home(request):

    query_dict=request.GET
    lng = query_dict.get("lng")
    lat = query_dict.get("lat")
    place = Placement.objects.all()
    context={place : "place"}
    in_range={}
    coords_2 = (lng,lat)
    print(coords_2)
    for places in place:
        coords_1 = (places.latitude,places.longtitude)
        print(geopy.distance.distance(coords_1, coords_2).km)
        if geopy.distance.distance(coords_1, coords_2).km <10:
            in_range[places.id]=places
    return render(request,'listing.html',{'data': sorted(in_range.items())})







from django.shortcuts import render