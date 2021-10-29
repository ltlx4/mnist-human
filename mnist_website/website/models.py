from django.db import models


# Create your models here.
class User(models.Model):
    class Meta:
        verbose_name = 'Participant'
        verbose_name_plural = 'Participants'
        
    name = models.CharField(max_length=100, null=False, blank=False)
    degree = models.CharField(max_length=150, blank=False)
    age = models.IntegerField(blank=False, null=False)
    region = models.CharField(max_length=20, blank=False, default='Europe') 
    accuracy = models.FloatField(default=0.0)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

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
        return "{}'s guess ({}) ".format(str(self.user),str(self.id))

    @property
    def check_correct(self):
        return True if self.human_guess == self.real_value else False