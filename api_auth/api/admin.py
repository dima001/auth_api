from django.contrib import admin
from models import *
# Register your models here.


class UserAdmin(admin.ModelAdmin):
    model = User
    #fields = ('first_name', 'email')

admin.site.register(User,UserAdmin)