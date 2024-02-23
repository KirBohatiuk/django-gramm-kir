from django.db import models
from django.contrib.auth.models import AbstractUser
from cloudinary import CloudinaryImage


class MyUser(AbstractUser):
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(unique=True)
    email_is_verified = models.BooleanField(default=False)
    pass


class PostModel(models.Model):
    text = models.CharField(max_length=200)
    image = models.ImageField(blank=True, null=True)

# Create your models here.
