
from distutils.command.upload import upload
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=14)
    surname = models.CharField(max_length=14)
    profile_image = models.ImageField(upload_to='profile_images/')
    bio = models.TextField()
    email = models.EmailField()
    
    
    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("user", kwargs={"pk": self.pk})

