from django import forms
from django.contrib.auth import get_user_model


class EditUsernameForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = {
            'username',
            
        }
        widgets = {
            'username' : forms.TextInput(attrs={'class': 'validate'})
        }
        