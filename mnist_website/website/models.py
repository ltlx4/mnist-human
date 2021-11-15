from django.db import models
from django.db.models.query import QuerySet
from .validators import validate_file_extension


class UserManager(models.Manager):
    def tries_number(self):
        return self.objects.all()
    

class User(models.Model):

    class Meta:
        verbose_name = 'Participant'
        verbose_name_plural = 'Participants'
        
    name = models.CharField(max_length=100, null=False, blank=False)
    degree = models.CharField(max_length=150, blank=False)
    age = models.IntegerField(blank=False, null=False)
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
        return self.name


def user_directory_path(instance, filename):
    return 'images/{0}_{1}/{2}'.format(instance.user.name, instance.user.id, filename)


class UserImageManager(models.Manager):
    def image_count(self):
        return self.objects.count()

class UserImage(models.Model):
    class Meta:
        verbose_name = 'Participant Image'
        verbose_name_plural = 'Participants Images'
        
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='images') #user.images.all
    image = models.FileField(upload_to=user_directory_path, validators=[validate_file_extension])
    human_guess = models.IntegerField()
    real_value = models.IntegerField()
    correct_guess = models.BooleanField(default=False)

    def __str__(self):
        return "{}'s picture ({}) ".format(str(self.user),str(self.id))


