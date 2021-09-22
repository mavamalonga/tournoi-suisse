from tinydb import TinyDB, Query
from datetime import datetime

class Database:
	def __init__(self):
		self.db = TinyDB('db.json')
		self.Query = Query() 
		self.tournament_table = self.db.table('Tournament')
		self.player_table = self.db.table('Player')
		self.match_table = self.db.table('Match')
		self.round_table = self.db.table('Rounds')

	def add_tournament(self, name, place, date, number_of_turns, rounds, 
		players, time_control, description):
		tournament = {
			"name": name,
			"place": place,
			"date": date,
			"number_of_turns": number_of_turns,
			"rounds": [rounds],
			"players": players,
			"time_control": time_control,
			"description": description
		}
		tournament_id = self.tournament_table.insert(tournament)
		return tournament_id

	def add_player(self, name, firstname, birthday, gender, ranking):
		player = {
			"name": name,
			"firstname": firstname,
			"birthday":birthday,
			"gender": gender,
			"ranking": int(ranking)
		}
		self.player_table.insert(player)

	def add_match(self, player1, player2, score1=0, score2=0):
		match = {
			"match": ([player1, score1], [player2, score2])
		}
		match_id = self.match_table.insert(match)
		return match_id

	def select_from_match_table(self, get_id=None, get_instance=None, where_id=None):
		""" get_id and get_instances takes boolean values, where_id take list value"""
		match_list = []
		if get_instance == True and where_id != None:
			for match_id in where_id:
				match_instance = self.match_table.get(doc_id = match_id)
				match_list.append(match_instance)
			return match_list

	def add_round(self, match_list):
		name = input(" Round name : ")
		Round = {
			"name": name,
			"start_date": datetime.now().strftime("%d/%m/%Y/%H %H:%M:%S"),
			"end_date": "NA",
			"matchs": match_list
		}
		round_id = self.round_table.insert(Round)
		return [round_id]

	def select_from_round_table(self, get_id=None, get_instance=None, where_id=None):
		""" get_id and get_instances takes boolean values, where_id take list value"""
		round_instances = []
		if get_instance==True and where_id != None:
			for round_id in where_id:
				round_instance = self.round_table.get(doc_id = round_id)
				round_instances.append(round_instance)
		return round_instances

	def update_ranking(self, ranking, player_id): #player_id list
		self.player_table.update({'ranking': ranking}, doc_ids=player_id)

	def select_from_player_table(self, get_id=None, get_instance=None, where_id=None, order_by_name=None):
		"""toutes les requêtes select sur la table player"""
		instances = self.player_table.all()

		if get_id == True and  get_instance == True and order_by_name == None:
			id_list = []
			for player in instances:
				id_list.append(player.doc_id)
			return id_list, instances
		elif get_instance == True and order_by_name != None:
			if order_by_name == "name":
				instances = sorted(instances, key=lambda k: k['name'])
			else:
				instances = sorted(instances, key=lambda k: k['ranking'])
			return instances
		elif get_instance == True and where_id != None:
			instances = []
			for player_id in where_id:
				player_instance = self.player_table.get(doc_id = int(player_id))
				instances.append(player_instance)
			return instances
		elif get_instance == True and where_id!=None and order_by_name!=None:
			if order_by_name == "name":
				instances = sorted(instances, key=lambda k: k['name'])
			else:
				instances = sorted(instances, key=lambda k: k['ranking'])
			return instances

	def remove_from_player_table(self, player_id):
		self.player_table.remove(doc_id=player_id)

	def select_from_tournament_table(self, get_id=None, get_instance=None, where_id=None):
		if get_id == True and get_instance == True and where_id == None:
			tournament_ids = []
			tournament_instances = self.tournament_table.all()
			for instance in tournament_instances:
				tournament_ids.append(instance.doc_id)
			return tournament_ids, tournament_instances
		elif get_instance == True and where_id != None:
			instance = self.tournament_table.get(doc_id = int(where_id))
			return instance
		else:
			return None

	def update_match_score(self, tournament_id, list_points):
		tournament_instance = self.select_from_tournament_table(get_instance=True, where_id=tournament_id)
		round_list = tournament_instance['rounds']
		latest_round = round_list[-1]
		update_matchs = []

		for match, score in zip(latest_round['matchs'], list_points):
			instance_player1 = match['match'][0][0]
			instance_player2 = match['match'][1][0]
			score_player1, score_player2 = score
			match['match'][0][1] = score_player1
			match['match'][1][1] = score_player2
			update_matchs.append({'match':([instance_player1, match['match'][0][1]], 
				[instance_player2, match['match'][1][1]])})

		update_round = {
			"name": latest_round['name'],
			"start_date": latest_round['start_date'],
			"end_date": datetime.now().strftime("%d/%m/%Y/%H %H:%M:%S"),
			"matchs": update_matchs
		}

		del round_list[-1]
		round_list.append(update_round)
		self.tournament_table.update({'rounds': round_list }, doc_ids=[int(tournament_id)])
		return update_matchs

	def update_tournament_round(self, tournament_id, round_instance):
		tournament_instance = self.select_from_tournament_table(get_instance=True, where_id=int(tournament_id))
		round_list = tournament_instance['rounds']
		round_list.append(round_instance)
		self.tournament_table.update({'rounds': round_list }, doc_ids=[int(tournament_id)])


	def drop_table(self, table):
		self.db.drop_table(table)

	def remove_match(self, match_id):
		print(self.match_table.all())
		self.match_table.remove(doc_ids=match_id)

	def remove_tournament(self, tournament_id):
		print(self.tournament_table.all())
		self.tournament_table.remove(doc_ids=tournament_id)

	def remove_round(self, round_id):
		print(self.round_table.all())
		self.round_table.remove(doc_ids=round_id)

	def remove_player(self, player_id):
		self.player_table.remove(doc_ids=player_id)

	def update_player(self):
		self.player_table.update({"ranking": 9}, doc_ids=[11])
