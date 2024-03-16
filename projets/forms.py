from django import forms
from .models import MesArticles

class parametres(forms.Form):
    param = forms.CharField(label='param', max_length=100)
