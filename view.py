from model import Tournoi
from model import Player
from model import Match

class View:
	def __init__(self):
		pass

	def home_page(self):
		print("1 : Create a tournament")
		print("2 : Create a player")

	def form_player(self):
		name = input("name : ")
		firstname = input("firstname : ")
		birthday = input("birthday : ")
		gender = input("sexe : ")
		ranking = input("ranking : ")
		return name, firstname, birthday, gender, ranking


def create_player():
	player = input("")
	player_1 = Player("Affane", "Jean", "00/07/1997","M", "1")
	player_2 = Player("Candas", "Ma2t", "00/07/1997","M", "5")
	player_3 = Player("Ben", "Yass", "00/07/1999","M", "7")
	player_4 = Player("Maro", "MOMO", "00/07/1997","M", "8")
	player_5 = Player("Cartajena", "Felipe", "00/07/1997","M", "1")
	player_6 = Player("Mister", "Flow", "00/07/1998","M", "9")
	player_7 = Player("Hilal", "Hilary", "00/07/1999","F", "11")
	player_8 = Player("Ben", "Islace", "00/07/1997","M", "1")
	return [player_1.name, player_2.name, player_3.name, 
		player_4.name, player_5.name, player_6.name, 
		player_7.name, player_8.name]
	
	