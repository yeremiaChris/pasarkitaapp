from django.db import models
from django.conf import settings

# Create your models here.


class Image(models.Model):
    image = models.FileField(upload_to='gambar/')

