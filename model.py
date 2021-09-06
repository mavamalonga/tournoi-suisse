from tinydb import TinyDB, Query

class Database:
	def __init__(self):
		self.db = TinyDB('db.json')
		self.query = Query() 
		self.tournament_table = self.db.table('Tournament')
		self.player_table = self.db.table('Player')
		self.match_table = self.db.table('Match')
		self.rounds_table = self.db.table('Rounds')

	def exemple(self):
		Database.player_table.search(self.query.name == 't')

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
		self.tournament_table.insert(data)

	def add_player(self, name, firstname, birthday, gender):
		Player = {
			"name": name,
			"firstname": firstname,
			"birthday":birthday,
			"gender": gender,
			"ranking": "NA"
		}
		self.player_table.insert(data)

	def select_players(self):
		players = self.player_table.all()
		return players

	def add_match(self, player1, player2):
		Match = {
			"player1": [player1, score1],
			"player2": [player2, score2]
		}
		self.match_table.insert(Match)

	def add_rounds(self, name, matchs):
		Round = {
			"name": name,
			"matchs": matchs
		}
		self.rounds_table.insert(Round)