from re import template
import base64
from PIL import Image
from django.contrib import auth
from django.db.models import fields
from django.http import request
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.urls import reverse
from django.contrib.gis.geoip2 import GeoIP2
from django.contrib.auth import authenticate, login
from django.core.files.base import ContentFile
from .utils import *
from .models import User, UserImage
from .forms import *
import uuid



path = '/home/oiz/programming/mnist-human/mnist_website/media/images'

class UserCreateView(CreateView):
    model = User
    form_class = UserImageForm
    context_object_name = 'user_form'

    def get_context_data(self, *args, **kwargs):
        context = super(User, self).get_context_data(*args, **kwargs)
        context['user_form'] = UserForm()
        return context


    def post(self, request, *args, **kwargs):
        form = UserForm(request.POST or None)
        # human_guess = list(request.POST.getlist('human_guess'))
        # print(human_guess)
        if form.is_valid():
            username = form.cleaned_data['username']
            age = form.cleaned_data['age']
            request.session['username'] = username
            request.session['age'] = age
            user = form.save()
            user.save() 
            return redirect('result')
        return redirect('home')

        
        
        
class Home(TemplateView):
    template_name = 'website/index.html'


    def get_context_data(self, *args, **kwargs):
        context = super(Home, self).get_context_data(*args, **kwargs)
        
        context['user_form'] = UserForm()
        context['image_form'] = UserImageForm()
        
        return context



class UserImageCreate(CreateView):
    
    model = UserImage
    template_name = 'partials/image_form.html'
    fields = ('human_guess')
    success_url = "game"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(UserImageCreate, self).form_valid(form)



    def post(self, request, *args, **kwargs):
        form = UserImageForm(request.POST)
        if form.is_valid():
            image = form.save()
            form['real_value'] = 2
            form['image'] = None
            form['correct_guess'] = False

            image.save()
        return render(request, 'partials/image_form.html', {'user_form':form})


    


def create_image_form(request): 
    context = {
        'form': UserImageForm()
    }
    return render(request, "partials/user_form.html", context)


def check_username(request):
    username = request.POST.get('username')
    pattern = re.compile(r'^[a-zA-Z0-9]([._-](?![._-])|[a-zA-Z0-9]){1,18}[a-zA-Z0-9]$')
    if not pattern.match(username) or User.objects.filter(username=username).exists():
        return HttpResponse("<div id='username-error' class='danger'>Invalid Username</div>")
    else:
        return HttpResponse("<div id='username-error' class='normal'>This user name is available</div>")


def result(request):
    if request.session.has_key('username'):
        username = request.session['username']
        age = request.session['age']
        
        if username_exists(username):
            return render(request, 'website/result.html', {'username': username, 'age': age})
        return render(request, 'website/result.html', {})
    return render(request, 'website/result.html', {})


def userimages(request):
    username = request.POST.get('username')
    age = request.POST.get('age')
    user = User.objects.filter(username=username, age=age).first()
    
    if user:
        images = UserImage.objects.filter(user=user).all()
        request.session['username'] = username
        request.session['age'] = age
        context = {
            'user': user,
            'images': images
        }
        return render(request, 'partials/user_found.html', context)
    else:
        del request.session['username']
        del request.session['age'] 
        return render(request, 'partials/user_not_found.html')


def add_user_image(request):
    if request.method == 'POST':
        
        image_data = request.POST.get('image')
        user_image = UserImage()
        user_image.image = image_data


        username = request.session['username']
        user = User.objects.get(username=username)
        user_image.user = user
        
        if user.images.count() <= 30:

            user_image.human_guess = request.POST.get('human_guess')
            user_image.real_value = request.POST.get('real_value') 
            user_image.correct_guess = user_image.human_guess == user_image.real_value
            
            user_image.save()

            return result(request)
        else:
            return HttpResponse('<h1>Cannot add more than 30 images. Thanks<h1>')

    


    return redirect('result')


class UserImageCreateView(CreateView):
    model = UserImage
    fields = ['human_guess', 'image', 'real_value', 'correct_guess']
    template_name = 'partials/image_form.html'

    def get_context_data(self, *args, **kwargs):
        context = super(UserImageCreateView, self).get_context_data(*args, **kwargs)
        image, label = get_sample()
        context['image'] = image
        context['label'] = label
        
        return context




class UserImageDetailView(DetailView):
    model = UserImage