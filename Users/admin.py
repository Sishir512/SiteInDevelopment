# For information check  https://testdriven.io/blog/django-custom-user-model/ && last section of https://docs.djangoproject.com/en/3.1/topics/auth/customizing/


from django.contrib import admin

# Register your models here.

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import FocusUsUserCreationForm, FocusUsUserChangeForm
from .models import FocusUsUser


class FocusUsUserAdmin(UserAdmin):
    add_form = FocusUsUserCreationForm
    form = FocusUsUserChangeForm
    model = FocusUsUser
    list_display = ('email','username','fullname', 'is_admin', 'is_active',)
    list_filter = ('email', 'is_admin', 'is_active',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Permissions', {'fields': ('is_admin', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'fullname' , 'password1', 'password2', 'is_admin', 'is_active')}
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)


admin.site.register(FocusUsUser, FocusUsUserAdmin)