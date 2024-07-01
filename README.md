"# portfolio.github.io" 
Description du projet :
Site portfolio

Instructions d'installation :
    python manage.py migrate
    python manage.py runserver 0.0.0.0:8000(remplacer l'adresse ip par l'adresse ip du server)

Exemples d'utilisation :
    Des exemples de code ou d'utilisation montrant comment utiliser votre projet dans différentes situations.

Documentation :
    docs.djangoproject.com
    django-admin startproject mysite
    python manage.py startapp polls(pour les apps du projet)
    python manage.py check --deploy


Contributions :
    Des instructions sur la manière de contribuer à votre projet, y compris les normes de codage, les processus de demande de tirage, etc.

Crédits et licences :
    Les crédits pour les contributeurs et les bibliothèques tierces utilisées, ainsi que des informations sur la licence du projet.
Bonus : Github :
    Résolution problème de connexion en ssh à github:
        ssh-keygen -t rsa -b 4096 -C "votre_email@example.com"

        cat ~/.ssh/id_rsa.pub(on récupère la clé publique pour la coller sur le serveur distant)

        eval `ssh-agent -s`(vérifie si l'agent ssh est en cours d'exécution, et si ce n'est pas le cas : ssh-agent)

        ssh-add ~/.ssh/id_rsa(ajout de la clé privée à l'agent ssh)

        ssh -T git@github.com(vérification de la connexion)




