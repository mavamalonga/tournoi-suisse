from model import Tournoi
from model import Player
from model import Match

def create_player():
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

def create_tournoi(player_list):
	t1 = Tournoi("Les petits princes", "Paris 14", 
		"29/08/2021", "5", "4", player_list, "06:00:00",
		 "Putains de tournoi")
	return t1

def create_matchs(player_list):
	m = Match(player_list)
	matchs = m.main()
	print(matchs)

def main():
	player_list = create_player()
	t1 = create_tournoi(player_list)
	create_matchs(player_list)

	
if __name__ == '__main__':
	main()