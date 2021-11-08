from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.urls import reverse
from django.forms import inlineformset_factory
from django.contrib.gis.geoip2 import GeoIP2
from .utils import *
from .models import User, UserImage
from .forms import UserForm


def get_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip



def save_form_views(request):
    if request.method != "POST":
        return HttpResponseRedirect(reverse(''))
    else:
        name = request.POST.get('name')
        degree = request.POST.get('degree')
        age = request.POST.get('age')
        for lis in request.POST.get(''):
            print(lis)
        ip = 'localhost'
        locator = GeoIP2().city(ip)
        country = locator['country_name']
        city = locator['city']
        continent = locator['continent_name']
        try:
            user = User(name=name, degree=degree, age=age, country=country, city=city,continent=continent, ip_address=ip)
            user.save()
            return HttpResponseRedirect(reverse('home'))

        except Exception as e:
            print(e)
            return HttpResponseRedirect(reverse('home'))
        
        
        
class Home(TemplateView):
    template_name = 'website/index.html'
    
    def get_context_data(self, *args, **kwargs):
        InlineForm = inlineformset_factory(User, UserImage, 
            fields=('human_guess',), exclude=('pk',), can_delete=False, extra=25,    
        )
        context = super(Home, self).get_context_data(*args, **kwargs)
        context['form'] = UserForm()
        context['inline_form'] = InlineForm()

        return context