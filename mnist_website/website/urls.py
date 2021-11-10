from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('saveform', views.UserCreateView.as_view(), name='save_user_form'),
    path('create/', views.UserImageCreate.as_view(), name='create_user_image')

]
