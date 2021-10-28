from django.db import models

# Create your models here.
class User(models.Model):
    class Meta:
        verbose_name = 'Participant'
        verbose_name_plural = 'Participants'
        
    name = models.CharField(max_length=100, null=False, blank=False)
    degree = models.CharField(max_length=150, blank=False)
    age = models.IntegerField(blank=False, null=False)
    region = models.CharField(max_length=100, blank=False, null=False)
    image = models.ImageField(upload_to='images')
    result = models.BooleanField(default=None)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)

    # def save(self, *args, **kwargs):
    #     return super.save(*args, **kwargs)