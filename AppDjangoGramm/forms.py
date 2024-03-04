from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import MyUser, Post, Profile


class RegistrationForm(UserCreationForm):
    class Meta:
        model = MyUser
        fields = ['username', 'email', 'password1', 'password2']


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['text', 'image']


class ProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ('avatar', 'full_name', 'bio')
