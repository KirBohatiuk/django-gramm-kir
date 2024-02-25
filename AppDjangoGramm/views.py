from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .models import MyUser, PostModel, ProfileModel
from django.contrib.auth.decorators import login_required
from . import forms
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.core.mail import EmailMessage
from django.contrib import messages
from .tokens import account_activation_token



def index(request):
    users = MyUser.objects.all()
    return render(request, 'AppDjangoGramm/index.html', {"users": users})


def register(request):
    if request.method == 'POST':
        form = forms.RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            next = request.GET.get('next')
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            if next:
                return redirect(next)
            elif user:
                login(request, user)
                return redirect('verify-email')
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
            post = form.save(commit=False)
            post.owner = request.user
            post.save()
            return redirect('feed')
    else:
        form = forms.PostForm()
    return render(request, 'AppDjangoGramm/post.html', {'form': form})

@login_required
def feed(request):
    posts = PostModel.objects.order_by('-post_creation_date')[:5]
    return render(request, 'AppDjangoGramm/feed.html', {'posts': posts})


def verify_email(request):
    if request.method == "POST":
        if request.user.email_is_verified != True:
            current_site = get_current_site(request)
            user = request.user
            email = request.user.email
            subject = "Verify Email"
            message = render_to_string('AppDjangoGramm/verify_email_message.html', {
                'request': request,
                'user': MyUser,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            email = EmailMessage(
                subject, message, to=[email]
            )
            email.content_subtype = 'html'
            email.send()
            return redirect('verify-email-done')
        else:
            return redirect('signup')
    return render(request, 'AppDjangoGramm/verify_email.html')


def verify_email_done(request):
    return render(request, 'AppDjangoGramm/verify_email_done.html')


def verify_email_confirm(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = MyUser.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, MyUser.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.email_is_verified = True
        user.save()
        messages.success(request, 'Your email has been verified.')
        return redirect('create-profile')
    else:
        messages.warning(request, 'The link is invalid.')
    return render(request, 'AppDjangoGramm/verify_email_confirm.html')


def create_profile(request):
    if request.method == 'POST':
        form = forms.ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            user_profile = form.save(commit=False)
            user_profile.owner = request.user
            user_profile.save()
            return redirect('own-profile')
        return redirect('create-profile')
    else:
        form = forms.ProfileForm()
    return render(request, 'AppDjangoGramm/create_profile.html', {'form': form})


def own_profile(request):
    user = request.user
    user_profile = user.profile
    context = {
        'username': user.username,
        'profile': user_profile,
    }
    return render(request, 'AppDjangoGramm/own_profile.html', context)
