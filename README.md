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
	<ul>
		<li>Initialise le répertoire courant avec la commande<br> 
			<mark>git init</mark></li>
		<li>Clonez le respository github en local <br>
			<mark>git clone https://github.com/mavamalonga/Tournoi-suisse.git</mark>
		<li>Placez vous dans le répertoire principal du projet et, créez un environnement virtuel
			<br><mark>python -m venv env</mark></li>
		<li>Lancez l'environnement virtuel<br>
			<mark>env\Scripts\activate.bat</mark></li>
		<li>Installez les paquets python avec le gestionnaire de paquets pip<br>
			<mark>pip install -r requirements.txt</mark></li>
		<li>Lancez le programme avec le fichier run.py<br>
			<mark>py python run.py</mark></li>
	</ul>
<p>
Les données du programme seront sauvegardés dans un  fichier format json dans le repertoire principal.
</p>
<p>Pour effectuer le peluchage du code et génener le rapport html tapez la commande suivante : <br>
	<mark>flake8 --max-line-length=119 --format=html --htmldir=flake-report<mark>
<p>
<p>
Pour toute autre question, contactez moi à l'adresse suivante : mavamalonga.alpha@gmail.com
</p>
</article>
</section>
</body>
