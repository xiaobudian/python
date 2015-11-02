from django.shortcuts import render
from django.http import HttpResponse
import requests
from .models import Province, City, Town, Air, Weather
import json

# Create your views here.
baseUri = "http://apis.baidu.com/3023/weather/"

def getareadata(url):

    headers = {
        'apikey':'fb655c55aed101b68d2e1f3bf5534738',
    }

    response = requests.get(url, headers=headers)
    return response

def updatearea(model, url):
    
    data = getareadata(baseUri+url)
    all = ""
    for d in data.json():
        m = model()
        m.name = d[0]
        m.code = d[1]
        m.save()
        all += m.name + " "
    
    return all

def index(request):
           
    return HttpResponse("Welcome to ls weather info services.")
    
def getweather(request, code):
    air = Air.objects.first()
    needupdate = True
    if (air is not None):
        if(air.time != '000'):
            needupdate = False
    if needupdate:
        url = baseUri + "weather?id=" + code
        weather = getareadata(url)
        air_new = Air(**json.loads(weather.text))
        return HttpResponse(air_new.time)
    return HttpResponse(air)
    
def updateprovince(request):
    Province.objects.all().delete()
    
    url = "province"
  
    return HttpResponse(updatearea(Province, url))

def updatecity(request):
    City.objects.all().delete()
    
    all = ""
    for p in Province.objects.all():
        url = "city?id=" + p.code
        all += updatearea(City, url)

    return HttpResponse(all)
 
def updatetown(request):
    Town.objects.all().delete()
    
    all = ""
    for c in City.objects.all():
        url = "town?id=" + c.code
        all += updatearea(Town, url)

    return HttpResponse(all)
