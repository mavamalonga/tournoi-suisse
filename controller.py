from tinydb import TinyDB, Query
from model import Database
from view import View
import os

class Controller(View, Database):
	def __init__(self):
		View.__init__(self)
		Database.__init__(self)

	def check_form_add_tournament(self, tournement):
		error_list = []
		if len(tournement[0]) < 2 or len(tournement[0]) > 16:
			name_error = "		- the name must contain between 2 to 16 characters."
			error_list.append(name_error)
		if len(tournement[1]) < 8 or len(tournement[1]) > 66:
			place_error = "		- the place value must contain between 8 to 66 characters."
			error_list.append(place_error)
		if len(tournement[2]) != 10:
			date_error = "		- the date format is incorrect."
			error_list.append(date_error)
		else:
			try:
				date = tournement[2].split("/")
				for nb in date:
					try:
						int(nb)
					except Exception as e:
						date_error = "		- date must only contain integers"
						error_list.append(date_error)
			except Exception as e:
				date_error = "		- the date format is incorrect."
				error_list.append(date_error)

		try:
			int(tournement[3])
		except Exception as e:
			nb_of_turns = "		- nb of turns must only contain integers"
			error_list.append(nb_of_turns)

		if tournement[4].lower() != "bullet" and tournement[4].lower() != "blitz" and tournement[4].lower() != "rapide":
			control_time_error = "		- control time must only contain following values : bullet || blitz ||rapide"
			error_list.append(control_time_error)

		if len(tournement[5]) > 234:
			description_error = "		- the description value must contain 234 characters."
			error_list.append(description_error)

		if len(error_list) == 0:
			return True
		else:
			View.error(self, error_list)
			return False
			

	def check_form_add_player(self, player):
		error_list = []
		if len(player[0]) < 2 or len(player[0]) > 16:
			name_error = "		- the name must contain between 2 to 16 characters."
			error_list.append(name_error)

		if len(player[0]) < 2 or len(player[0]) > 16:
			firstname_error = "		- the firstname must contain between 2 to 16 characters."
			error_list.append(firstname_error)

		if len(player[2]) != 10:
			date_error = "		- the date of birth format is incorrect."
			error_list.append(date_error)
		else:
			try:
				date = player[2].split("/")
				for nb in date:
					try:
						int(nb)
					except Exception as e:
						date_error = "		- birthday must only contain integers"
						error_list.append(date_error)
			except Exception as e:
				date_error = "		- the date of birth format is incorrect."
				error_list.append(date_error)		

		if len(player[3]) != 1:
			gender_error = "		- the gender field takes only one character."
			error_list.append(gender_error)
		else:
			if player[3] != 'M' and player[3] != 'F':
				gender_error = "		- the gender field only takes the value 'M' or 'F'."
				error_list.append(gender_error)

		try:
			int(player[4])
		except Exception as e:
			ranking_error = "		- ranking must only contain integers"
			error_list.append(ranking_error)

		if len(error_list) == 0:
			return True
		else:
			View.error(self, error_list)
			return False

	def parse_select_of_players(self, id_selected):
		id_selected.replace(' ', '')
		id_list = id_selected.split(",")
		return id_list

	def check_selection_of_players(self, id_list):
		error_list = []
		list_verified_id = []
		if len(id_list) != 8:
			nb_selected_error = "		- incorrect number of player id"
			error_list.append(nb_selected_error)
		else:
			for player_id in id_list:
				try:
					int(player_id)
					list_verified_id.append(player_id)
				except Exception as e:
					type_error = "		- player_id list must only contain integers."
					error_list.append(type_error)
		
		if len(error_list) == 0:
			return True
		else:
			View.error(self, error_list)
			return False

	def check_instances_players(self, id_list, instances):
		error_list = []
		for player_id, player_instance in zip(id_list, instances):
			if player_instance == None:
				player_error = "		- there is no player with the following id :{0}".format(player_id)
				error_list.append(player_error)
		if len(error_list) == 0:
			return True
		else:
			View.error(self, error_list)
			return False

	def check_select_tournament(self, tournament_id):
		error_list = []
		try:
			int(tournament_id)
			return True
		except Exception as e:
			id_error = "		- tournament_id must only contain integers. :{0}".format(tournament_id)
			error_list.append(id_error)
			View.error(self, error_list)
			return False

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
				error_type = "		- '{0}' value is incorrect, points only accept values of type int and float".format(pts)
				error_list.append(error_type)
		
		if len(error_list) == 0:
			return True, new_list_points
		else:
			View.error(self, error_list)
			return False, None

	def check_points_values(self, list_points):
		error_list = []
		for value in list_points:
			if value == 0 or value == 0.5 or value == 1:
				pass
			else:
				error = f"{' '*15} {value}' value is incorrect, points only accept the following values : 0, 0.5, 1"
				error_list.append(error)
		if len(error_list) == 0:
			return True
		else:
			View.error(self, error_list)
			return False

	def transform_matchs_scores_tuple(self, list_points):
		size_list = len(list_points)
		index1 = 0
		index2 = 1
		new_list = []
		match = 0
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

	def pairing_add_match(self, instances):
		match_list = []
		nb_players = len(instances)
		part_one = instances[:nb_players//2]
		part_two = instances[nb_players//2:]
		
		for player1, player2 in zip(part_one, part_two):
			match_id = Database.add_match(self, player1, player2)
			match_list.append(match_id)
		return match_list

	def main(self):
		page = "1" #Home page
		self.home_page()
		while True:
			next_page = input("Response : ")
			if next_page.lower() == "q":
				quit()
			elif page == "1": 
				if next_page == "1":
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
								list_match_id = self.pairing_add_match(instances)
								list_match_instance = Database.select_from_match_table(self, get_instance=True, where_id=list_match_id)
								round_id = Database.add_round(self, list_match_instance)
								round_instance = Database.select_from_round_table(self, get_instance=True, where_id=round_id)
								Database.add_tournament(self, tournament_values[0], tournament_values[1], tournament_values[2],
									tournament_values[3], round_instance[0], selection_of_players, tournament_values[4], tournament_values[5])
							else:
								self.home_page()
						else:
							self.home_page()
					else:
						self.home_page()
				elif next_page == "2":
					add_again = "yes"
					while add_again == "yes":
						player = View.form_add_player(self)
						validator_player = self.check_form_add_player(player)
						if validator_player:
							Database.add_player(self, player[0], player[1], player[2], player[3], player[4])
						add_again = input("Add again ? yes/not : ")
					self.home_page()
				elif next_page == "3":
					page = page + next_page
					View.reports(self)
				else:
					self.home_page()
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
					# select_players 
					# display players
					# usr select player 
					# usr enter ranking
					# check value 
					# update ranking value 
				elif next_page == "2":
					page = page + next_page
					View.display_rounds(self, instance['rounds'])
				elif next_page == "3":
					View.display_matchs(self, instance['rounds'])
				else:
					print("j'ai pas compris")
			elif page == "132t1":
				if next_page == "1":
					page = page + next_page
					players = Database.select_from_player_table(self, get_instance=True, where_id=instance['players'], 
					order_by_name="name")
					View.display_list_players(self, players, page_1=False, order_by_name="name")
				elif next_page == "2":
					players = Database.select_from_player_table(self, get_instance=True, where_id=instance['players'],
						order_by_name="ranking")
					View.display_list_players(self, players, page_1=False, order_by_name="ranking")
			elif page == '132t2':
				if next_page == 'r':
					list_points = View.display_form_results(self, instance['rounds'])
					validator_convert, new_list_points = self.convert_points(list_points)
					if validator_convert:
						validator_points = self.check_points_values(new_list_points)
						if validator_points:
							new_list_points = self.transform_matchs_scores_tuple(new_list_points)
							update_matchs = Database.update_match_score(self, tournament_id, new_list_points)
							instances = self.round_classification(update_matchs, first_round=False)
							list_match_id = self.pairing_add_match(instances)
							list_match_instance = Database.select_from_match_table(self, get_instance=True, where_id=list_match_id)
							round_id = Database.add_round(self, list_match_instance)
							round_instances = Database.select_from_round_table(self, get_instance=True, where_id=round_id)
							Database.update_tournament_round(self, tournament_id, round_instances[0])
						else:
							pass
					else:
						pass
				else:
					pass
			else:
				pass

if __name__ == '__main__':
	controller = Controller()
	controller.main()