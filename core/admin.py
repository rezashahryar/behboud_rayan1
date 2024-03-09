from django.contrib import admin
from . import models
from django.contrib.auth.admin import UserAdmin
# Register your models here.


@admin.register(models.User)
class CustomUserAdmin(UserAdmin):
    model = models.User
    ordering = ('mobile',)
    search_fields = ('mobile', 'email')
    list_filter = ('is_active', 'is_superuser')
    list_display = ['email', 'is_superuser', 'is_staff', 'is_active', 'mobile']

    fieldsets = (
        ('Authentication', {
            "fields": (
                'mobile', 'email', 'password', 'first_name', 'last_name'
            ),
        }),
        ('group permissions', {
            'fields': (
                'user_permissions', 'groups',
            )
        }),
        ('Permissions', {
            'fields': (
                'is_staff', 'is_active', 'is_superuser'
            ),
        }),
        ('last login', {
            'fields': (
                'last_login',
                'date_joined',
            ),
        }),
    )

    add_fieldsets = (
        ('Create User', {
            'classes': ('wide',),
            'fields': ('mobile', 'password1', 'password2', 'is_staff', 'is_active', 'is_superuser')
        }),
    )
