from tinydb import TinyDB, Query

class Database:
	def __init__(self):
		self.db = TinyDB('db.json')
		self.tournament_table = self.db.table('Tournament')
		self.player_table = self.db.table('Player')
		self.match_table = self.db.table('Match')
		self.rounds_table = self.db.table('Rounds')

	def add_tournament(self, data):
		self.tournament_table.insert(data)

	def add_player(self, data):
		self.player_table.insert(data)

	def add_match(self, data):
		self.match_table.insert(data)

	def add_rounds(self, data):
		self.rounds_table.insert(data)

class Tournement:
	def __init__(self):
		Database.__init__(self)

	def add_tournement(self, name, place, date, number_of_turns, 
		players, time_control, description):
		Tournement = {
			"name": name,
			"place": place,
			"date": date,
			"number_of_turns": number_of_turns,
			"rounds": "empty",
			"players": players,
			"time_control": time_control,
			"description": description
		}
		Database.add_tournament(Tournement)


class Player(Database):
	def __init__(self):
		Database.__init__(self)

	def add_player(self, name, firstname, birthday, gender):
		Player = {
			"name": name,
			"firstname": firstname,
			"birthday":birthday,
			"gender": gender,
			"ranking": "NA"
		}
		Database.add_player(self, Player)

class Match:
	def __init__(self):
		Database.__init__(self)

	def add_match(self, player1, player2):
		Match = {
			"player1": [player1, score1],
			"player2": [player2, score2]
		}
		Database.add_Match(self, Match)


class Rounds:
	def __init__(self):
		Database.__init__(self)

	def add_rounds(self, name, matchs):
		Round = {
			"name": name,
			"matchs": matchs
		}
		Database.add_round(self, Round)