from django.http.response import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.gis.geoip2 import GeoIP2
from .utils import *
from .forms import UserForm


def home(request):
    context ={}
    
    return render(request, 'website/index.html', context)    


def get_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip



def save_form_views(request):
    if request.method != "POST":
        return HttpResponseRedirect(reverse('/'))
    else:
        name = request.POST.get('name')
        degree = request.POST.get('degree')
        age = request.POST.get('age')
        tries_number = request.POST.get('tries')
        ip = get_ip(request)
        locator = GeoIP2().city(ip)
        country = locator['country_name']
        city = locator['city']
        continent = locator['continent_name']
        
        
        
        
