from django.urls import reverse
from django.db import models
from django.db.models.query import QuerySet
from django.core.validators import RegexValidator
from .validators import validate_file_extension
import urllib
import os

class UserManager(models.Manager):
    def tries_number(self):
        return self.images.count()
    

class User(models.Model):

    class Meta:
        verbose_name = 'Participant'
        verbose_name_plural = 'Participants'
        
    name = models.CharField(max_length=100, null=False, blank=False)
    degree = models.CharField(max_length=150, blank=False)
    age = models.IntegerField(blank=False, null=False)
    username = models.CharField(max_length=24, unique=True)
    country = models.CharField(max_length=100, blank=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    continent = models.CharField(max_length=100, blank=True)
    ip_address = models.CharField(max_length=220, blank=True)
    accuracy = models.FloatField(default=0.0, blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    images: QuerySet['UserImage']

    objects = UserManager()

    def __str__(self):
        return self.name or str(self.name)



def user_directory_path(instance, filename):
    return 'images/{0}_{1}/{2}'.format(instance.user.name, instance.user.id, filename)


class UserImageManager(models.Manager):
    def image_count(self):
        return self.objects.count()

    def create_userimage(self, username, human_guess , real):
        user_image = self.create(user=username, human_guess=human_guess, real_value=real)
        return user_image

class UserImage(models.Model):
    class Meta:
        verbose_name = 'Participant Image'
        verbose_name_plural = 'Participants Images'
        
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='images') #user.images.all
    image = models.URLField(max_length=600)
    human_guess = models.IntegerField()
    real_value = models.IntegerField(null=True, blank=True)
    correct_guess = models.BooleanField(default=False)

    def __str__(self):
        return "{}'s guess ({}) ".format(str(self.user),str(self.id))

    def get_absolute_url(self):
        return reverse('user_detail', kwargs={'pk': self.pk})

    objects = UserImageManager()



