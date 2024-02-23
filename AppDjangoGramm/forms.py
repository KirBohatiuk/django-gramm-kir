from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import MyUser, PostModel


class RegistrationForm(UserCreationForm):
    class Meta:
        model = MyUser
        fields = ['username', 'email', 'password1', 'password2']


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class PostForm(forms.ModelForm):
    class Meta:
        model = PostModel
        fields = ['text', 'image']
