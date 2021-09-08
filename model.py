from tinydb import TinyDB, Query

class Database:
	def __init__(self):
		self.db = TinyDB('db.json')
		self.Query = Query() 
		self.tournament_table = self.db.table('Tournament')
		self.player_table = self.db.table('Player')
		self.match_table = self.db.table('Match')
		self.rounds_table = self.db.table('Rounds')

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
			"ranking": 0
		}
		self.player_table.insert(data)

	def select_players(self, order_by_name=True):
		players = self.player_table.all()
		if order_by_name:
			players_order = sorted(players, key=lambda k: k['name'])
		else:
			players_order = sorted(players, key=lambda k: k['ranking'])
		return players_order

	def select_players_for_tournement(self):
		id_list = []
		players = self.player_table.all()
		for player in players:
			id_list.append(player.doc_id)
		return [id_list, players]

	def select_player_where_id(self, player_id):
		player = self.player_table.get(doc_id = player_id)
		return player

	def add_match(self, player1, ranking1, player2, ranking2):
		Match = {
			"Match": ([player1, ranking1], [player2, ranking2])
		}
		self.match_table.insert(Match)

	def add_rounds(self, name, matchs):
		Round = {
			"name": name,
			"matchs": matchs
		}
		self.rounds_table.insert(Round)

	def drop_database(self):
		pass