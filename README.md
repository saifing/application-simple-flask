# Application Web simple

Ceci est une application Web simple utilisant [Python Flask](http://flask.pocoo.org/) et la Base de données [MySQL](https://www.mysql.com/) . 
Ceci est utilisé dans la démonstration de développement de playbooks ansibles.
  
  Vous trouverez ci-dessous les étapes nécessaires pour obtenir ce travail sur un système de base Linux.
  
   - Installer toutes les dépendances requises
   - Installer et configurer le serveur Web
   - Démarrer le serveur Web
   
## 1. Installer toutes les dépendances requises
  
  Python et ses dépendances

    apt-get install -y python python-setuptools python-dev build-essential python-pip python-mysqldb

   
## 2. Installer et configurer le serveur Web

Installez la dépendance Python Flask 

    pip install flask
    pip install flask-mysql

- Copier app.py ou le télécharger du référentiel source
- Configurer les informations d'identification et les paramètres de base de données

## 3. Démarrer le serveur Web

Démarrer le serveur Web

    FLASK_APP=app.py flask run --host=0.0.0.0
    
## 4. Test

Ouvrez un navigateur et allez à l'URL

    http://<IP>:5000                            => Bienvenu
    http://<IP>:5000/how%20are%20you            => Je vais bien et toi?
