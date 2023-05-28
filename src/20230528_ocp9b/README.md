# OCP9b

<< mettre une miniature du site ici >>

## Objectif
Ce programme est un exercice proposé par [OpenClassRooms](https://openclassrooms.com/fr/) dans le cadre de la formation :
Développeur d'applications Python. Description courte du projet

<< mettre une  image d'une page ici >>

## Fonctionnalités


## Technologie utilisée


## Creation d'un environnement virtuel
* -> Télécharger le package de l'application depuis github : git clone https://github.com/Slb59/Oc-P9.git
* -> Creer un environnement virtuel : python -m venv .venv
* -> Activer l'environnement virtuel : .venv\Scripts\activate.bat
* -> Installer la dernière version de pip: python -m pip install --upgrade pip
* -> Installer les bibliothèques externes de Python: pip install -r requirements.txt

## Utilisation

* -> L'environnement virtuel doit être activé
* -> Lancer le serveur:
```bash
cd litreview
python manage.py runserver
```
* -> Depuis votre navigateur, vous accédez à l'application via : http:/127.0.0.1:8000
* -> Créez un compte pour pouvoir vous connecter et accéder au site.
* -> Le mot de passe doit avoir au moins 8 caractères, des chiffres dans le désordre et des lettres. Il ne doit pas être commun.
* -> Pour accéder à l'administration de django: http://127.0.0.1:8000/admin
* -> Pour créer un nouvel administrateur dans le terminal: python manage.py createsuperuser

