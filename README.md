<header>
<title>Tournoi Suisse</title>
<h1>Présentaion</h1>
<p>Tournoi suisse est une application console écrit en python qui sert à la gestion et à l'organisation d'un tournoi d'échec.</p>
</header>

<body>
<section>
<h2>Fonctionnement</h2>

<p>L'utilisateur rentrer les données rélatifs à un tournoi ( nom, adresse, joueurs, date ...), l'application se charge de générer les paires de joueurs composant les matchs et les rounds du tournoi.
L'application fournit differentes fonctionnalités de gestion et d'afficage de données.
</p>
<p>
- Ajouter un tournoi
- Ajouter un joueur 
- Afficher des rapports 
	- Afficher la liste de tournoi
	- Afficher la liste de joueurs 
	- Afficher les matchs d'un tournoi
	- Afficher les rounds d'un tournoi
- Rentrer les resultats des matchs 
- Modifier le classement d'un joueur
- Règlages/gestion de la base de données
...
</p>
</section>
<section>
<h3>Installation</h3>
<p>
Assurez vous d'avoir installé en local le gestionnaire de version git et le gestionnaire de paquets python pip.
Ouvrez le terminal git et, suivez les étapes ci-dessous.
Initialise le répertoire courant
git init
Clonez le respository github en local
git clone https://github.com/mavamalonga/Tournoi-suisse.git
Placez vous dans le répertoire principal du projet et, créez un environnement virtuel
python -m venv env
Lancez l'environnement virtuel
env\Scripts\activate.bat
Installez les paquets python avec le gestionnaire de paquets pip
pip install -r requirements.txt
Lancez le programme avec le fichier run.py
python run.py
Les données du programme seront sauvegardés dans un  fichier format json dans le repertoire principal.
Pour toute autre question, contactez moi à l'adresse suivante : mavamalonga.alpha@gmail.com
</section>
</body>
