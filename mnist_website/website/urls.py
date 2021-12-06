from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('saveform', views.UserCreateView.as_view(), name='user_form'),
    path('check_username/', views.check_username, name="check-username"),
    path('result/', views.result, name="result"),
    path('userimages', views.userimages, name="images"),
    path('add_image', views.add_user_image, name='add-image'),
    path('image_form', views.UserImageCreateView.as_view(), name='image-form'),
    path('participants/<int:pk>', views.UserImageDetailView.as_view(), name='user_detail'),


]

