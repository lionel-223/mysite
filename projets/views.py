from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import parametres
from .forms import SignUpForm
from django.contrib.auth import login, authenticate
from projets.models import MesArticles
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from .forms import  ProfilePictureChangeForm
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages
from .models import Utilisateurs
from django.http import HttpResponse
from django.core.mail import send_mail
from django.urls import reverse
from .forms import ContactForm
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import redirect
from django.contrib.auth import logout



def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('index')  # Redirigez l'utilisateur vers la page d'accueil ou une autre page après l'inscription
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})
def about(request):
    return render(request,'about.html',)
def services(request):
    return render(request,'services.html',)

def index(request):
    return render(request, 'index.html')

def operations(request):
    return render(request, 'operations.html')

def contact(request):
    return render(request, 'contact.html')
def cv(request):
    return render(request, 'cv.html')
def blogs(request):
    return render(request, 'blogs.html')
def article_IA(request):
    return render(request, 'article_IA.html')
def resultat(request):
    return render(request, 'resultat.html')
def veille(request):
    return render(request, 'veille.html')
def personnalite(request):
    return render(request, 'personnalite.html')
def developpementweb(request):
    return render(request, 'developpement-web.html')
def redactiondecontenu(request):
    return render(request, 'redaction-de-contenu.html')
def designgraphique(request):
    return render(request, 'design-graphique.html')

@csrf_protect
def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            # Envoi de l'email
            send_mail(
                f'Message de {name} via votre portfolio',
                message,
                email,
                ['daviddelouest@gmail.com'],
            )

            return HttpResponseRedirect(reverse('contact:success'))
    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form': form})

def success_view(request):
    return render(request, 'success.html')

@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Votre mot de passe a été changé avec succès!')
            return redirect('change_password')
        else:
            messages.error(request, 'Veuillez corriger l\'erreur ci-dessous.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'change_password.html', {'form': form})

@login_required
def change_profile_picture(request):
    user_profile = Utilisateurs.objects.get(user=request.user)
    if request.method == 'POST':
        form = ProfilePictureChangeForm(request.POST, request.FILES, instance=user_profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Votre photo de profil a été changée avec succès!')
            return redirect('change_profile_picture')
    else:
        form = ProfilePictureChangeForm(instance=user_profile)
    return render(request, 'change_profile_picture.html', {'form': form})

@login_required
def delete_account(request):
    if request.method == 'POST':
        request.user.delete()
        messages.success(request, 'Votre compte a été supprimé avec succès!')
        return redirect('home')
    return render(request, 'delete_account.html')

def logout_view(request):
    logout(request)
    return redirect('index')

def privacy_policy(request):
    return render(request, 'privacy_policy.html')
