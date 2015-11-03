from django.shortcuts import render
from django.http import HttpResponse
import requests
from .models import Province, City, Town

# Create your views here.
baseUri = "http://apis.baidu.com/3023/weather/"

def getareadata(url):

    headers = {
        'apikey':'fb655c55aed101b68d2e1f3bf5534738',
    }

    response = requests.get(url, headers=headers)
    return response.json()

def updatearea(model, url):
    
    data = getareadata(baseUri+url)
    all = ""
    for d in data:
        m = model()
        m.name = d[0]
        m.code = d[1]
        m.save()
        all += m.name + " "
    
    return all

def index(request):
           
    return HttpResponse("Welcome to ls weather info services.")
    
def getweather(request, code):
    url = baseUri + "weather?id=" + code
    
    weather = getareadata(url)
    return HttpResponse(str(weather))
    
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
