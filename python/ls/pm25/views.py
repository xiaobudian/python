from django.shortcuts import render
from django.http import HttpResponse
import requests
from .models import Province, City, Town

# Create your views here.
def index(requst):
    all = ""
    for p in Province.objects.all():
        all += p.name + "\n"
    return HttpResponse(all)

def getareadata(url):

    headers = {
        'apikey':'fb655c55aed101b68d2e1f3bf5534738',
    }

    response = requests.get(url, headers=headers)
    return response.json()


def updateprovince(requst):
    for p in Province.objects.all():
        p.delete()

    url = "http://apis.baidu.com/3023/weather/province"
    data = getareadata(url)
    all = ""
    for d in data:
        p = Province()
        p.name = d[0]
        p.code = d[1]
        p.save()
        all += p.name + " "

    return HttpResponse(all)

def updatecity(requst):
    for c in City.objects.all():
        c.delete()
    all = ""
    for p in Province.objects.all():
        url = "http://apis.baidu.com/3023/weather/city?id=" + p.code
        data = getareadata(url)

        for d in data:
            c = City()
            c.name = d[0]
            c.code = d[1]
            c.save()
            all += c.name + " "

    return HttpResponse(all)
 
def updatetown(requst):
    for t in Town.objects.all():
        t.delete()
    all = ""
    for c in City.objects.all():
        url = "http://apis.baidu.com/3023/weather/town?id=" + c.code
        data = getareadata(url)

        for d in data:
            t = Town()
            t.name = d[0]
            t.code = d[1]
            t.save()
            all += t.name + " "

    return HttpResponse(all)
