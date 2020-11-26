from django import forms
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

class EditUsernameForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = ['username']
        labels = {
            'username': _(''),
        }

        widgets = {
            'username' : forms.TextInput(attrs={'class':'validate' , 'id':'username'})
        }
        