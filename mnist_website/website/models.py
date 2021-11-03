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
    tries = models.IntegerField(default=10)
    accuracy = models.FloatField(default=0.0, blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    objects = UserManager()

    def __str__(self):
        return self.name


    def add_user_image(self, UserImage):
        if self.userimage_set.count() >= self.tries:
            raise Exception("Too many images on this account")
        self.userimage_set.add(UserImage)


            

    # def save(self, *args, **kwargs):
    #     return super.save(*args, **kwargs)


class UserImage(models.Model):
    class Meta:
        verbose_name = 'Participant Image'
        verbose_name_plural = 'Participants Images'
        
    user = models.ForeignKey(User, default=None, on_delete=models.CASCADE)
    image = models.FileField(upload_to='images')
    human_guess = models.IntegerField()
    real_value = models.IntegerField()
    correct_guess = models.BooleanField(default=False)

    def __str__(self):
        return "{}'s picture ({}) ".format(str(self.user),str(self.id))

    @property
    def check_correct(self):
        return True if self.human_guess == self.real_value else False