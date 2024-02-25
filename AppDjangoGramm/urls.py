from django.urls import path
from . import views
from DjangoGramm import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('post/', views.create_post, name='post'),
    path('feed/', views.feed, name='feed'),
    path('verify-email/', views.verify_email, name='verify-email'),
    path('verify-email/done/', views.verify_email_done, name='verify-email-done'),
    path('verify-email-confirm/<uidb64>/<token>/', views.verify_email_confirm, name='verify-email-confirm'),
    path('create-profile/', views.create_profile, name='create-profile'),
    path('own-profile/', views.own_profile, name='own-profile'),
]
