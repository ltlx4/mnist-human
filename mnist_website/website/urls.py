from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('saveform', views.save_form_views, name='save_user_form')

]
