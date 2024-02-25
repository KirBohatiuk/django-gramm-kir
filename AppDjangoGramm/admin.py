from django.contrib import admin
from .models import MyUser, PostModel, ProfileModel
# Register your models here.


admin.site.register(MyUser)
admin.site.register(PostModel)
admin.site.register(ProfileModel)
