from django.urls import reverse
from django.db  import models
from django.contrib.auth.models import User

# Create your models here.
class Sites(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    site_photo = models.ImageField(upload_to='users_photos/')
    html_file = models.FileField(upload_to='users_files/')
    user = models.ForeignKey(User, on_delete=models.CASCADE)    

    class Meta:
        verbose_name = 'сайт'
        verbose_name_plural = 'сайты'

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("site", kwargs={"pk": self.pk})
    

    

