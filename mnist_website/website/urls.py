from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('saveform', views.UserCreateView.as_view(), name='user_form'),
    path('create/', views.UserImageCreate.as_view(), name='user_image_form'),
    path('detail/', views.ImageViwe.as_view(), name='view_user_image'),
    path('htmx/create-image-form', views.create_image_form, name='create_image_form'),


]
