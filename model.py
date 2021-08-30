from tinydb import TinyDB, Query

class Tournoi:

 	def __init__(self, name, place, date, nb_rounds, tournees,
 		players, time, description):
 		self.db = TinyDB('Tournoi.json')
 		tournoi = { 
 			"name": name,
 			"place": place,
 			"date": date,
 			"nb_rounds": nb_rounds,
 			"tournees": tournees,
 			"players": players,
 			"time": time,
 			"description": description
 		}
 		self.db.insert(tournoi)

 	def create_tournoi(self):
 		self.db.insert(tournoi)


class Player:
	def __init__(self, name, firstname, birthday, 
		gender, ranking):
		db = TinyDB("Player.json")
		player = {
			"name":name,
			"firstname":firstname,
			"birthday":birthday,
			"gender":gender,
			"ranking":ranking,
			"points":0
		}
		db.insert(player)


class Match:
	def __init__(self, player_list):
		self.number = "1"
		self.player_list = player_list
		self.matchs = []

	def random_draw(self):
		for player_one, player_two in zip(self.player_list[0:4], 
			self.player_list[4:8]):
			self.matchs.append((player_one, player_two))

	def main(self):
		self.random_draw()
		return self.matchs

