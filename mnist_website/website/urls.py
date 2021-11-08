from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('saveform', views.save_form_views, name='save_user_form')

]
