from django.db import models
from django.contrib.auth.models import AbstractUser


class MyUser(AbstractUser):
    username = models.CharField(max_length=100, unique=True)
    pass


class PostModel(models.Model):
    text = models.CharField(max_length=200)

# Create your models here.
