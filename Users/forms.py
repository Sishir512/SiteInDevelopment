from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import FocusUsUser


class FocusUsUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = FocusUsUser
        fields = ('email','username')


class FocusUsUserChangeForm(UserChangeForm):

    class Meta:
        model = FocusUsUser
        fields = ('email','username','password','is_admin','is_active')