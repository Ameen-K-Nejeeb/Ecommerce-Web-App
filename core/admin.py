from django.contrib import admin
from .models import AbstractUser
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

# Register your models here.

class CustomUserAdmin(UserAdmin):
    add_fieldsets = (
        (None,{
            'classes': ('wide',),
            'fields': ('username', 'email', 'first_name', 'last_name', 'password1', 'city', 'state', 'address', 'phone' , 'is_staff', 'is_active')}
            ), 
    )
admin.site.register(CustomUser, CustomUserAdmin)