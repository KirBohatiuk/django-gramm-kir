from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from cloudinary import CloudinaryImage


class MyUser(AbstractUser):
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(unique=True)
    email_is_verified = models.BooleanField(default=False)
    date_joined = models.DateTimeField(verbose_name="Creation date", auto_now_add=True)
    pass


class PostModel(models.Model):
    owner = models.ForeignKey(
        MyUser,
        on_delete=models.CASCADE,
        blank=True,
    )
    text = models.CharField(max_length=200)
    image = models.ImageField(blank=True, null=True)
    post_creation_date = models.DateTimeField(auto_now_add=True, verbose_name="Creation date")
