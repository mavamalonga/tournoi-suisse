from tinydb import TinyDB, Query
from model import Database
from view import View
import os

class Controller(Database, View):
	def __init__(self):
		View.__init__(self)
		Database.__init__(self)

	def check_form_add_player(self, player):
		error_list = []
		if len(player[0]) < 2 or len(player[0]) > 16:
			name_error = "the name must contain between 2 to 16 characters."
			error_list.append(name_error)

		if len(player[0]) < 2 or len(player[0]) > 16:
			firstname_error = "the firstname must contain between 2 to 16 characters."
			error_list.append(firstname_error)

		if len(player[2]) != 10:
			date_error = "the date of birth format is incorrect."
			error_list.append(date_error)
		else:
			try:
				date = player[2].split("/")
				for nb in date:
					try:
						int(nb)
					except Exception as e:
						date_error = "birthday must only contain integers"
						error_list.append(date_error)
			except Exception as e:
				date_error = "the date of birth format is incorrect."
				error_list.append(date_error)		

		if len(player[3]) != 1:
			gender_error = "the gender field takes only one character."
			error_list.append(gender_error)
		else:
			if player[3] != 'M' and player[3] != 'F':
				gender_error = "the gender field only takes the value 'M' or 'F'."
				error_list.append(gender_error)

		try:
			if int(player[4]) > 0: 
				player[4] = int(player[4])
			else:
				error_ranking = "ranking this is a positive number"
				error_list.append(error_ranking)
		except Exception as e:
			ranking_error = "ranking must only contain integers"
			error_list.append(ranking_error)

		return self.check_errors(error_list)

	def parse_select_of_players(self, id_selected):
		id_selected.replace(' ', '')
		id_list = id_selected.split(",")
		return id_list

	def check_selection_of_players(self, id_list):
		error_list = []
		list_verified_id = []
		if len(id_list) != 8:
			nb_selected_error = "incorrect number of player id"
			error_list.append(nb_selected_error)
		else:
			for player_id in id_list:
				try:
					int(player_id)
					list_verified_id.append(player_id)
				except Exception as e:
					type_error = "player_id list must only contain integers."
					error_list.append(type_error)
		return self.check_errors(error_list)

	def check_instances_players(self, id_list, instances):
		error_list = []
		for player_id, player_instance in zip(id_list, instances):
			if player_instance == None:
				player_error = "there is no player with the following id :{0}".format(player_id)
				error_list.append(player_error)
		return self.check_errors(error_list)

	def check_select_tournament(self, tournament_id):
		error_list = []
		try:
			int(tournament_id)
		except Exception as e:
			id_error = "tournament_id must only contain integers. :{0}".format(tournament_id)
			error_list.append(id_error)
		return self.check_errors(error_list)

	def convert_points(self, list_points):
		new_list_points = []
		error_list = []
		for pts in list_points:
			try:
				value = int(pts)
				int_validator = "True"
			except Exception as e:
				int_validator = "False"
				try:
					value = float(pts)
					float_validator = "True"
				except Exception as e:
					float_validator = "False"

			if int_validator == "True" or float_validator == "True":
				new_list_points.append(value)
			else:
				error_type = "'{0}' value is incorrect, points only accept values of type int and float".format(pts)
				error_list.append(error_type)
		return self.check_errors(error_list), new_list_points

	def check_points_values(self, list_points):
		error_list = []
		for value in list_points:
			if value == 0 or value == 0.5 or value == 1:
				pass
			else:
				error = f"{value}' value is incorrect, points only accept the following values : 0, 0.5, 1"
				error_list.append(error)
		return self.check_errors(error_list)

	def transform_matchs_scores_tuple(self, list_points):
		size_list = len(list_points)
		index1, index2, match = (0, 1, 0)
		new_list = []
		while match < size_list/2:
			score1 = list_points[index1]
			score2 = list_points[index2]
			new_list.append((score1, score2))
			index1 += 2
			index2 += 2
			match += 1
		return new_list

	def round_classification(self, instances, first_round=True):
		winner =[]
		looser =[]
		zero =[]
		match_list = []

		if first_round == True:
			instances = sorted(instances, key=lambda k: k['ranking'])
		else:
			for match in instances:
				player1, player2 = match['match']
				if int(player1[1]) > int(player2[1]):
					winner.append(player1[0])
					looser.append(player2[0])
				elif player1[1] == player2[1]:
					zero.append(player1[0])
					zero.append(player2[0])
				else:
					winner.append(player2[0])
					looser.append(player1[0])
			winner = sorted(winner, key=lambda k: k['ranking'])
			looser = sorted(looser, key=lambda k: k['ranking'])
			zero = sorted(zero, key=lambda k: k['ranking'])
			instances = winner + zero + looser
		return instances

	def pairing(self, instances, first_round=True, round_list=None):
		pairing_list = []
		if first_round == True:
			nb_players = len(instances)
			part_one = instances[:nb_players//2]
			part_two = instances[nb_players//2:]
			for player1, player2 in zip(part_one, part_two):
				pairing_list.append(player1, player2)
			return pairing_list
		else:
			dict_1 = {}
			dict_2 = {}
			for player in instances:
				p = {player['name']: player}
				dict_1.update(p)
				dict_2.update(p)

			for i in range(4):
				name1, name2 = self.check_pairings(dict_1, dict_2, round_list)
				match_id = Database.add_match(self, dict_1[name1], dict_2[name2])
				matchs.append(match_id)
				del dict_1[name1]
				del dict_1[name2]
				del dict_2[name1]
				del dict_2[name2]
		return matchs

	def check_pairings(self, dict_1, dict_2, round_list):
		for key1_name in dict_1:
			player1 = dict_1[key1_name]
			for key2_name in dict_2:
				player2 = dict_2[key2_name]
				if self.check_match_exits(player1['name'], player2['name'], round_list):
					continue
				else:
					return player1['name'], player2['name']

	"""check if the match already exists"""
	def check_match_exits(self, player1_name, player2_name, round_list):
		for round_instance in round_list:
			for match in round_instance['matchs']:
				player1, player2 = match['match']
				if player1_name == player1[0]['name'] or player2[0]['name'] == player1_name:
					if player2_name == player1[0]['name'] or player2[0]['name'] == player2_name:
						return True
					else:
						pass
				else:
					pass
		return False

	def check_modify_ranking(self, name, ranking):
		error_list = []
		instances = Database.from_player_table_search_player(self, name)

		try:
			ranking = int(ranking)
			ranking_int = True
		except Exception as e:
			ranking_int = False
			ranking_error = "ranking must only contain integers"
			error_list.append(ranking_error)

		if len(instances) != 0 and ranking_int:
			player_id = instances[0].doc_id
			Database.from_player_table_update_ranking(self, ranking, [int(player_id)])
		else:
			name_error = f'there is no user with the name {name}'
			error_list.append(name_error)
		return self.check_errors(error_list)

	""" next Class Urls """

	def patch_add_tournament(self):
		tournament_values = View.form_add_tournament(self)
		validator_tournament = self.check_form_add_tournament(tournament_values)
		if validator_tournament == True:
			id_list, instances = Database.select_from_player_table(self, get_id=True, get_instance=True)
			selection_of_players = View.tournament_add_players(self, id_list, instances)
			selection_of_players = self.parse_select_of_players(selection_of_players)
			validator_selection_of_players = self.check_selection_of_players(selection_of_players)
			if validator_selection_of_players:
				instances = Database.select_from_player_table(self, get_instance=True, where_id=selection_of_players)
				validator_instances = self.check_instances_players(selection_of_players, instances)
				if validator_instances:
					instances = self.round_classification(instances, first_round=True)
					list_match_id = self.pairing_add_match(instances, first_round=True, round_list=None)
					list_match_instance = Database.select_from_match_table(self, get_instance=True, where_id=list_match_id)
					round_id = Database.add_round(self, list_match_instance)
					round_instance = Database.select_from_round_table(self, get_instance=True, where_id=round_id)
					Database.add_tournament(self, tournament_values[0], tournament_values[1], tournament_values[2],
						tournament_values[3], round_instance[0], selection_of_players, tournament_values[4], tournament_values[5])
		View.home_page(self)

	def path_add_player(self):
		add_again = "yes"
		while add_again == "yes":
			player = View.form_add_player(self)
			validator_player = self.check_form_add_player(player)
			if validator_player:
				Database.add_player(self, player[0], player[1], player[2], player[3], player[4])
			add_again = input(f'{" "*45}Add again ? yes/not : ')
		View.home_page(self)

	def path_upgrade_results(self, tournament_id, instance):
		list_points = View.display_form_results(self, instance['rounds'])
		validator_convert, new_list_points = self.convert_points(list_points)
		if validator_convert:
			validator_points = self.check_points_values(new_list_points)
			if validator_points:
				new_list_points = self.transform_matchs_scores_tuple(new_list_points)
				update_matchs = Database.update_match_score(self, tournament_id, new_list_points)
				if len(instance['rounds']) < 7:
					instances_order = self.round_classification(update_matchs, first_round=False)
					list_match_id = self.pairing_add_match(instances_order, first_round=False, round_list=instance['rounds'])
					list_match_instance = Database.select_from_match_table(self, get_instance=True, where_id=list_match_id)
					round_id = Database.add_round(self, list_match_instance)
					round_instances = Database.select_from_round_table(self, get_instance=True, where_id=round_id)
					Database.update_tournament_round(self, tournament_id, round_instances[0])
				else:
					pass

	def main(self):
		page = "1"
		View.home_page(self)
		while True:
			next_page = input(f'{" "*45} Next page : ')
			if next_page.lower() == "e":
				exit()
			elif page == "1": 
				if next_page == "1":
					self.patch_add_tournament()
					View.home_page(self)
				elif next_page == "2":
					self.path_add_player()
					View.home_page(self)
				elif next_page == "3":
					page = page + next_page
					View.reports(self)
				else:
					View.home_page(self)
			elif page == "13":
				if next_page == "1":
					page = page + next_page
					players = Database.select_from_player_table(self, get_instance=True, order_by_name="name")
					View.display_list_players(self,  players, page_1=True, order_by_name="name")
				elif next_page == "2":
					page = page + next_page
					ids, instances = Database.select_from_tournament_table(self, 
						get_id=True, get_instance=True)
					View.display_list_tournaments(self, ids, instances)
			elif page == "131":
				if next_page == "1":
					players = Database.select_from_player_table(self, get_instance=True, order_by_name="name")
					View.display_list_players(self,  players, page_1=True, order_by_name="name")
				elif next_page == "2":
					players = Database.select_from_player_table(self, get_instance=True, order_by_name="ranking")
					View.display_list_players(self, players, page_1=True, order_by_name="ranking")
				else:
					print("j'ai pas compris !")
			elif page == "132":
				validator_tournament = self.check_select_tournament(next_page)
				tournament_id = next_page
				if validator_tournament:
					page = page + "t"
					instance = Database.select_from_tournament_table(self, get_instance=True, where_id=tournament_id)
					View.tournament_menu(self, instance)
				else:
					pass
			elif page == "132t":
				if next_page == "1":
					page = page + next_page
					players = Database.select_from_player_table(self, get_instance=True, where_id=instance['players'], 
						order_by_name="name")
					View.display_list_players(self, players, page_1=False, order_by_name="name")
				elif next_page == "2":
					page = page + next_page
					View.display_rounds(self, instance['rounds'])
				elif next_page == "3":
					View.display_matchs(self, instance['rounds'])
				else:
					print("j'ai pas compris")
			elif page == "132t1":
				if next_page == "1":
					players = Database.select_from_player_table(self, get_instance=True, where_id=instance['players'], 
					order_by_name="name")
					View.display_list_players(self, players, page_1=False, order_by_name="name")
				elif next_page == "2":
					players = Database.select_from_player_table(self, get_instance=True, where_id=instance['players'],
						order_by_name="ranking")
					View.display_list_players(self, players, page_1=False, order_by_name="ranking")
				elif next_page == "3":
					name, ranking = View.form_modify_ranking(self)
					validator_modify_ranking = self.check_modify_ranking(name, ranking)
			elif page == '132t2':
				if next_page == 'r':
					self.path_upgrade_results(tournament_id, instance)
					View.home_page(self)
				else:
					pass
			else:
				pass

class Manager:

	def check_form_add_tournament(self, tournement):
		error_list = []
		if len(tournement[0]) < 2 or len(tournement[0]) > 16:
			name_error = "the name must contain between 2 to 16 characters."
			error_list.append(name_error)
		if len(tournement[1]) < 8 or len(tournement[1]) > 66:
			place_error = "the place value must contain between 8 to 66 characters."
			error_list.append(place_error)
		if len(tournement[2]) != 10:
			date_error = "the date format is incorrect."
			error_list.append(date_error)
		else:
			try:
				date = tournement[2].split("/")
				for nb in date:
					try:
						int(nb)
					except Exception as e:
						date_error = "date must only contain integers"
						error_list.append(date_error)
			except Exception as e:
				date_error = "the date format is incorrect."
				error_list.append(date_error)

		try:
			int(tournement[3])
		except Exception as e:
			nb_of_turns = "nb of turns must only contain integers"
			error_list.append(nb_of_turns)

		if tournement[4].lower() != "bullet" and tournement[4].lower() != "blitz" and tournement[4].lower() != "rapide":
			control_time_error = "control time must only contain following values : bullet || blitz ||rapide"
			error_list.append(control_time_error)

		if len(tournement[5]) > 234:
			description_error = "the description value must contain 234 characters."
			error_list.append(description_error)

		if len(error_list) > 0:
			return False, error_list
		else:
			return True, None

	def parse_select_of_players(self, id_selected):
		id_selected.replace(' ', '')
		id_list = id_selected.split(",")
		return id_list

	def check_selection_of_players(self, id_list):
		error_list = []
		list_verified_id = []
		if len(id_list) != 8:
			nb_selected_error = "incorrect number of player id"
			error_list.append(nb_selected_error)
		else:
			for player_id in id_list:
				try:
					int(player_id)
					list_verified_id.append(player_id)
				except Exception as e:
					type_error = "player_id list must only contain integers."
					error_list.append(type_error)
		if len(error_list) > 0:
			return False, error_list
		else:
			return True, None

	def check_instances_players(self, id_list, instances):
		error_list = []
		for player_id, player_instance in zip(id_list, instances):
			if player_instance == None:
				player_error = "there is no player with the following id :{0}".format(player_id)
				error_list.append(player_error)

		if len(error_list) > 0:
			return False, error_list
		else:
			return True, None

	def round_classification(self, instances, first_round=True):
		winner =[]
		looser =[]
		zero =[]
		match_list = []

		if first_round == True:
			instances = sorted(instances, key=lambda k: k['ranking'])
		else:
			for match in instances:
				player1, player2 = match['match']
				if int(player1[1]) > int(player2[1]):
					winner.append(player1[0])
					looser.append(player2[0])
				elif player1[1] == player2[1]:
					zero.append(player1[0])
					zero.append(player2[0])
				else:
					winner.append(player2[0])
					looser.append(player1[0])
			winner = sorted(winner, key=lambda k: k['ranking'])
			looser = sorted(looser, key=lambda k: k['ranking'])
			zero = sorted(zero, key=lambda k: k['ranking'])
			instances = winner + zero + looser
		return instances

	def pairing(self, instances, first_round=True, round_list=None):
		pairing_list = []
		if first_round == True:
			nb_players = len(instances)
			part_one = instances[:nb_players//2]
			part_two = instances[nb_players//2:]
			for player1, player2 in zip(part_one, part_two):
				pairing_list.append((player1, player2))
			return pairing_list
		else:
			dict_1 = {}
			dict_2 = {}
			for player in instances:
				p = {player['name']: player}
				dict_1.update(p)
				dict_2.update(p)

			for i in range(4):
				name1, name2 = self.check_pairings(dict_1, dict_2, round_list)
				match_id = Database.add_match(self, dict_1[name1], dict_2[name2])
				matchs.append(match_id)
				del dict_1[name1]
				del dict_1[name2]
				del dict_2[name1]
				del dict_2[name2]
		return matchs

	def check_form_add_player(self, player):
		error_list = []
		if len(player[0]) < 2 or len(player[0]) > 16:
			name_error = "the name must contain between 2 to 16 characters."
			error_list.append(name_error)

		if len(player[0]) < 2 or len(player[0]) > 16:
			firstname_error = "the firstname must contain between 2 to 16 characters."
			error_list.append(firstname_error)

		if len(player[2]) != 10:
			date_error = "the date of birth format is incorrect."
			error_list.append(date_error)
		else:
			try:
				date = player[2].split("/")
				for nb in date:
					try:
						int(nb)
					except Exception as e:
						date_error = "birthday must only contain integers"
						error_list.append(date_error)
			except Exception as e:
				date_error = "the date of birth format is incorrect."
				error_list.append(date_error)		

		if len(player[3]) != 1:
			gender_error = "the gender field takes only one character."
			error_list.append(gender_error)
		else:
			if player[3] != 'M' and player[3] != 'F':
				gender_error = "the gender field only takes the value 'M' or 'F'."
				error_list.append(gender_error)

		try:
			if int(player[4]) > 0: 
				player[4] = int(player[4])
			else:
				error_ranking = "ranking this is a positive number"
				error_list.append(error_ranking)
		except Exception as e:
			ranking_error = "ranking must only contain integers"
			error_list.append(ranking_error)

		if len(error_list) > 0:
			return False, error_list
		else:
			return True, None

	def check_modify_ranking(self, instances, name, ranking):
		error_list = []
		try:
			ranking = int(ranking)
			ranking_int = True
		except Exception as e:
			ranking_int = False
			ranking_error = "ranking must only contain integers"
			error_list.append(ranking_error)

		if len(instances) != 0 and ranking_int:
			player_id = instances[0].doc_id
		else:
			name_error = f'there is no user with the name {name}'
			error_list.append(name_error)

		if len(error_list) > 0:
			return False, None, error_list
		else:
			return True, player_id, None

if __name__ == '__main__':
	controller = Controller()
	controller.main()