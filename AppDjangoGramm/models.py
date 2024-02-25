from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from cloudinary import CloudinaryImage


class MyUser(AbstractUser):
    username = models.CharField(verbose_name='username', max_length=100, unique=True)
    email = models.EmailField(verbose_name='email', unique=True)
    email_is_verified = models.BooleanField(verbose_name='email_is_verified', default=False)
    date_joined = models.DateTimeField(verbose_name="Creation date", auto_now_add=True)
    pass


class PostModel(models.Model):
    owner = models.ForeignKey(
        MyUser,
        on_delete=models.CASCADE,
    )
    text = models.CharField(verbose_name="post text", max_length=200)
    image = models.ImageField(verbose_name="post image", blank=True, null=True)
    post_creation_date = models.DateTimeField(auto_now_add=True, verbose_name="Creation date")


class ProfileModel(models.Model):
    owner = models.OneToOneField(
        MyUser,
        on_delete=models.CASCADE,
        related_name='profile'
    )
    full_name = models.CharField(verbose_name="full name", max_length=64, blank=True)
    bio = models.TextField(verbose_name="bio", blank=True)
    avatar = models.ImageField('avatar', default='blank_avatar.png')
