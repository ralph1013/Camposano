from django import forms
from .models import Poste

class PostForm(forms.ModelForm):
    class Meta:
        model = Poste
        fields = ['title', 'users', 'body']
