# users/admin.py
from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['email', 'username', 'first_name', 'last_name', 'user_type']

    fieldsets = (
        ('Personal info', {'fields': ('email', 'username', 'first_name', 'last_name', 'password', 'user_type')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'username', 'user_type')}
        ),
    )

admin.site.register(CustomUser, CustomUserAdmin)