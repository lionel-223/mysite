from django.db import models

class ArticlesDePresse(models.Model):
    Id_Articles = models.AutoField(primary_key=True)
    Libelle_AP = models.CharField(max_length=50)
    Description = models.CharField(max_length=50)
    Auteur = models.CharField(max_length=50)
    Date_publication = models.DateField()
    Date_Syndication = models.DateField()

class Mailing(models.Model):
    Id_Mailing = models.AutoField(primary_key=True)
    Notification = models.CharField(max_length=50)
    Date_Envoi = models.DateField()
    Destinataires = models.CharField(max_length=50)

class MesArticles(models.Model):
    Id_Mes_Articles = models.AutoField(primary_key=True)
    Libelle_MA = models.CharField(max_length=50)
    Description = models.CharField(max_length=50)
    Date_publication = models.DateField()
    Date_Miseajour = models.DateField()

class Utilisateurs(models.Model):
    Id_Utilisateurs = models.AutoField(primary_key=True)
    utilisateur = models.CharField(max_length=50)
    mdp = models.CharField(max_length=50)
    date_souscription = models.DateField()
    mailng = models.BooleanField()
    Id_Mailing = models.ForeignKey(Mailing, on_delete=models.CASCADE)

class Simulations(models.Model):
    Id_Simulations = models.AutoField(primary_key=True)
    exercice = models.CharField(max_length=500)
    Date_Sim = models.DateField()
    graph = models.TextField()
    Id_Utilisateurs = models.ForeignKey(Utilisateurs, on_delete=models.CASCADE)

class Evaluations(models.Model):
    Id_Evaluations = models.AutoField(primary_key=True)
    Date_Com = models.DateField()
    commentaires = models.CharField(max_length=50)
    Note = models.CharField(max_length=50)
    Id_Utilisateurs = models.ForeignKey(Utilisateurs, on_delete=models.CASCADE)
