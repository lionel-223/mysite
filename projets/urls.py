from django.urls import path
from django.contrib import admin
from django.urls import include
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('index.html', views.index, name='index'),
    path('about.html', views.about, name='about'),
    path('services.html', views.services, name='services'),
    path('operations.html', views.operations, name='operations'),
    path('personnalite.html', views.personnalite, name='personnalite'),
    path('cv.html', views.cv, name='cv'),
    path('blogs.html', views.blogs, name='blogs'),
    path('article_IA.html', views.article_IA, name='article_IA'),
    path('resultat.html', views.resultat, name='resultat'),
    path('veille.html', views.veille, name='veille'),
    path('design-graphique.html', views.designgraphique, name='design-graphique'),  
    path('developpement-web.html', views.developpementweb, name='developpement-web'),
    path('redaction-de-contenu.html', views.redactiondecontenu, name='redaction-de-contenu'),
    path('contact.html', include('contact.urls')),
    path('change_password.html', views.change_password, name='change_password'),
    path('change_profile_picture.html', views.change_profile_picture, name='change_profile_picture'),
    path('delete_account.html', views.delete_account, name='delete_account'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup.html', views.signup_view, name='signup'),
    path('change_password.html', auth_views.PasswordChangeView.as_view(template_name='change_password.html'), name='change_password'),
    path('password_change_done.html', auth_views.PasswordChangeDoneView.as_view(template_name='password_change_done.html'), name='password_change_done'),
    path('logout.html', views.logout_view, name='logout'),
    path('privacy_policy.html', views.privacy_policy, name='privacy_policy'),
]
