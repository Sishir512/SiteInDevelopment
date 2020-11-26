from django import forms
from .models import BlogComment
from django.utils.translation import gettext_lazy as _

class CommentForm(forms.ModelForm):
    class Meta:
        model = BlogComment

        fields = ['content']
        
        labels = {
            'content': _(''),
        }
        
        widgets = {
            'content' : forms.TextInput(attrs={'id' : 'commentarea'})
        }
