from django.shortcuts import render, redirect
from keras.datasets import mnist
from .forms import UserForm
import numpy as np
from PIL import Image
import random
from django.contrib.gis.geoip2 import GeoIP2
import matplotlib.pyplot as plt



def get_shuffled_samples():
    (x_train, y_train), (x_test, y_test) = mnist.load_data()
    images = x_train
    labels = y_train
    images_with_labels = list(zip(images,labels))
    random.shuffle(images_with_labels)
    return images_with_labels[:15]

def home(request):
    images, labels = zip(*get_shuffled_samples())
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

def gen_image(arr):
    two_d = (np.reshape(arr, (28, 28)) * 255).astype(np.uint8)
    img = Image.fromarray(two_d, 'L')
    return img