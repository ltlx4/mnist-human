from django.db import models


class UserManager(models.Manager):
    def tries_number(self):
        return self.userimage_set.count()

class User(models.Model):


    class Meta:
        verbose_name = 'Participant'
        verbose_name_plural = 'Participants'
        
    name = models.CharField(max_length=100, null=False, blank=False)
    degree = models.CharField(max_length=150, blank=False)
    age = models.IntegerField(blank=False, null=False)
    country = models.CharField(max_length=100, blank=True)
    city = models.CharField(max_length=100, blank=True)
    continent = models.CharField(max_length=100, blank=True)
    ip_address = models.CharField(max_length=220, blank=True)
    accuracy = models.FloatField(default=0.0, blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    objects = UserManager()

    def __str__(self):
        return self.name

    # def save(self, *args, **kwargs):
    #     return super.save(*args, **kwargs)

def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'images/{0}_{1}/{2}'.format(instance.user.name, instance.user.id, filename)


class UserImage(models.Model):
    class Meta:
        verbose_name = 'Participant Image'
        verbose_name_plural = 'Participants Images'
        
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='images') #user.images.all
    image = models.FileField(upload_to=user_directory_path)
    human_guess = models.IntegerField()
    real_value = models.IntegerField()
    correct_guess = models.BooleanField(default=False)

    def __str__(self):
        return "{}'s picture ({}) ".format(str(self.user),str(self.id))

