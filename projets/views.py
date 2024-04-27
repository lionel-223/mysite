from django.shortcuts import render
from django.views.generic import TemplateView
from flask import Flask
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import parametres
from projets.models import MesArticles

from django.http import HttpResponse



def about(request):
    return render(request,'about.html',)
def services(request):
    return render(request,'services.html',)

def index(request):
    return render(request, 'index.html')

def portfolio(request):
    article = MesArticles(Libelle_MA='Mon article', Description='Ceci est mon article', Date_publication='2022-03-28', Date_Miseajour='2022-03-28')
    article.save()
    articles = MesArticles.objects.all()
    return render(request, 'portfolio.html', {'articles': articles})

def contact(request):
    return render(request, 'contact.html')
def cv(request):
    return render(request, 'cv.html')
def blogs(request):
    return render(request, 'blogs.html')
def resultat(request):
    print('/thanks/')
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
class QuadraticEquationView(TemplateView):
    template_name = 'quadratic_equation.html'

    def post(self, request):
        a = float(request.POST.get('a'))
        b = float(request.POST.get('b'))
        c = float(request.POST.get('c'))

        # Calculer les racines de l'équation du second degré
        delta = b**2 - 4*a*c
        if delta < 0:
            result = "Pas de solution réelle"
        elif delta == 0:
            x = -b / (2*a)
            result = f"Une solution réelle unique: x = {x}"
        else:
            x1 = (-b + delta**0.5) / (2*a)
            x2 = (-b - delta**0.5) / (2*a)
            result = f"Deux solutions réelles: x1 = {x1}, x2 = {x2}"
        
        # Passer le résultat à la page
        context = {'result': result}
        return render(request, self.template_name, context)
