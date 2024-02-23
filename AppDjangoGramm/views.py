from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .models import MyUser, PostModel
from django.contrib.auth.decorators import login_required
from . import forms


def index(request):
    users = MyUser.objects.all()
    return render(request, 'AppDjangoGramm/index.html', {"users": users})


def register(request):
    if request.method == 'POST':
        form = forms.RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect('index')
            return redirect('register')
    else:
        form = forms.RegistrationForm()
    return render(request, 'AppDjangoGramm/register.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect('index')
    else:
        form = forms.LoginForm()
    return render(request, 'AppDjangoGramm/login.html', {'form': form})


def user_logout(request):
    logout(request)
    return redirect('index')

@login_required
def create_post(request):
    if request.method == 'POST':
        form = forms.PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('feed')
    else:
        form = forms.PostForm()
    return render(request, 'AppDjangoGramm/post.html', {'form': form})

@login_required
def feed(request):
    posts = PostModel.objects.all()
    return render(request, 'AppDjangoGramm/feed.html', {'posts': posts})
