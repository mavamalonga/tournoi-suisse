from tinydb import TinyDB, Query

class Database:
	def __init__(self):
		self.db = TinyDB('db.json')
		self.Query = Query() 
		self.tournament_table = self.db.table('Tournament')
		self.player_table = self.db.table('Player')
		self.match_table = self.db.table('Match')
		self.round_table = self.db.table('Rounds')

	def add_tournement(self, name, place, date, number_of_turns, rounds, 
		players, time_control, description):
		tournement = {
			"name": name,
			"place": place,
			"date": date,
			"number_of_turns": number_of_turns,
			"rounds": rounds,
			"players": players,
			"time_control": time_control,
			"description": description
		}
		tournament_id = self.tournament_table.insert(tournement)
		return tournament_id

	def add_player(self, name, firstname, birthday, gender):
		player = {
			"name": name,
			"firstname": firstname,
			"birthday":birthday,
			"gender": gender,
			"ranking": 0
		}
		self.player_table.insert(player)

	def update_ranking(self, player_id):
		self.player_table.update({'ranking': 0}, doc_id=player_id)

	def remove_player(self, player_id):
		self.player_table.remove(doc_id=player_id)

	def select_players(self, order_by_name=True):
		players = self.player_table.all()
		if order_by_name:
			players_order = sorted(players, key=lambda k: k['name'])
		else:
			players_order = sorted(players, key=lambda k: k['ranking'])
		return players_order

	def select_players_id_and_instance(self):
		id_list = []
		players = self.player_table.all()
		for player in players:
			id_list.append(player.doc_id)
		return [id_list, players]

	def select_player_instance(self, player_id_list):
		player_instances = []
		for player_id in player_id_list:
			instance = self.player_table.get(doc_id = int(player_id))
			player_instances.append(instance)
		return player_instances

	def add_match(self, player1_id, player2_id):
		match = {
			"Match": ([player1_id, 0], [player2_id, 0])
		}
		match_id = self.match_table.insert(match)
		return match_id

	def select_match_id(self, match_id):
		match_instance = self.match_table.get(doc_id = match_id)
		return match_instance

	def select_round(self, round_id):
		round_instance = self.round_table.get(doc_id = round_id)
		return round_instance

	def add_round(self, match_list, name="Round1"):
		match_instances_list = []
		for match_id in match_list:
			match_instance = self.select_match_id(match_id)
			match_instances_list.append(match_instance)
		Round = {
			"name": name,
			"matchs": match_instances_list
		}
		round_id = self.round_table.insert(Round)
		return round_id

	def select_tournament(self):
		tournament_id_list = []
		tournament_instances = self.tournament_table.all()
		for tournament in tournament_instances:
			tournament_id_list.append(tournament.doc_id)
		return [tournament_id_list, tournament_instances]

	def select_tournament_id(self, tournament_id):
		tournament = self.tournament_table.get(doc_id = int(tournament_id))
		return tournament

	def drop_database(self, table):
		self.db.drop_table(table)

	def remove_player(self):
		self.player_table.remove(doc_ids=[3, 11, 12, 13, 14])
