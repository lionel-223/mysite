from django import forms
from .models import MesArticles
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import PasswordChangeForm
from .models import Utilisateurs


class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Requis. Entrez une adresse email valide.')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class ProfilePictureChangeForm(forms.ModelForm):
    class Meta:
        model = Utilisateurs
        fields = ['profile_picture']

class parametres(forms.Form):
    param = forms.CharField(label='param', max_length=100)
class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, label='Nom')
    email = forms.EmailField(label='Email')
    message = forms.CharField(widget=forms.Textarea, label='Message')


