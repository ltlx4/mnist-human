from django.shortcuts import render, redirect       
from django.contrib.gis.geoip2 import GeoIP2
from .utils import *
from .forms import UserForm


def home(request):
    images, labels = zip(*shuffle_samples())
    user_ip = '176.63.3.126'
    g = GeoIP2()
    country = g.city(user_ip)
    
    context ={
        'form': UserForm(),
        'country': country['country_code'],
        'continent': country['continent_name'],
        'images': images,
        'labels': labels,
        'userlist': {1,2,3}
    }
    return render(request, 'website/index.html', context)    


def get_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip



