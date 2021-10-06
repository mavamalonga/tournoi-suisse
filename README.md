<header>
<h1>Présentaion</h1>
<p>Tournoi suisse est une application console écrit en python qui sert à la gestion et à l'organisation d'un tournoi d'échec.</p>
</header>

<body>
<section>
<h2>Fonctionnement</h2>

<p>L'utilisateur rentrer les données rélatifs à un tournoi ( nom, adresse, joueurs, date ...), l'application se charge de générer les paires de joueurs composant les matchs et les rounds du tournoi. <br>L'application fournit differentes fonctionnalités de gestion et d'afficage de données.
</p>
<article>
	<ul>
		<li>Ajouter un tournoi</li>
		<li>Ajouter un joueur</li> 
		<li>Afficher des rapports</li>
		<ul>
			<li>Afficher la liste de tournoi</li>
			<li>Afficher la liste de joueurs</li>
			<li>Afficher les matchs d'un tournoi</li>
			<li>Afficher les rounds d'un tournoi</li>
		</ul>
		<li>Rentrer les resultats des matchs</li>
		<li>Modifier le classement d'un joueur</li>
		<li>Règlages/gestion de la base de données</li>
		...
	</ul>
</article>
</section>
<section>
<h3>Installation</h3>
<p>
Assurez vous d'avoir installé en local le gestionnaire de version git et le gestionnaire de paquets python pip. <br>Ouvrez le terminal git et, suivez les étapes ci-dessous.<br>
</p>
<article>
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
</article>
</section>
</body>
