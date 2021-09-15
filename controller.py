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

	def pairing_and_add_match(self, instances):
		instances_order_by_ranking = sorted(instances, key=lambda k: k['ranking'])
		part_one = instances_order_by_ranking[:4]
		part_two = instances_order_by_ranking[4:]
		match_list = []
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
						selection_of_players = View.display_players_1(self, id_list, instances)
						selection_of_players = self.parse_select_of_players(selection_of_players)
						validator_selection_of_players = self.check_selection_of_players(selection_of_players)
						if validator_selection_of_players:
							instances = Database.select_from_player_table(self, get_instance=True, where_id=selection_of_players)
							validator_instances = self.check_instances_players(selection_of_players, instances)
							if validator_instances:
								list_match_id = self.pairing_and_add_match(instances)
								print("list match id")
								print(list_match_id)
								list_match_instance = Database.select_from_match_table(self, get_instance=True, where_id=list_match_id)
								print("list match instance")
								print(list_match_instance)
								round_id = Database.add_round(self, list_match_instance, name="Round 1", status="in progress")
								round_instance = Database.select_from_round_table(self, get_instance=True, where_id=round_id)
								print("0" + tournament_values[0])
								print("1" + tournament_values[1])
								print("2" + tournament_values[2])
								print("3" + tournament_values[3])
								print("4" + tournament_values[4])
								print("5" + tournament_values[5])
								print(round_instance[0])
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
					View.read_reports(self)
				else:
					self.home_page(error_404=True)
			elif page == "13":
				if next_page == "1":
					page = page + next_page
					players = Database.select_players(self)
					View.display_players(self, players)
				elif next_page == "2":
					page = page + next_page
					tournaments = Database.select_tournament(self)
					View.display_tournament(self, tournaments[0], tournaments[1])
			elif page == "131":
				if next_page == "1":
					players = Database.select_players(self)
					View.display_players(self, players)
				elif next_page == "2":
					players = Database.select_players(self, order_by_name=False)
					View.display_players(self, players, order_by_name=False)
				else:
					pass
			elif page == "132":
				validator = self.check_next_page(page, next_page)
				if validator:
					page = page + next_page
					tournament_id = next_page
					View.reports_tournament(self)
				else:
					pass
			elif page == "1321":
				if next_page == "1":
					tournament = Database.select_tournament_id(self, tournament_id)
					player_instances = Database.select_player_instances(self, tournament['players'])
					View.display_rounds(self, player_instances)
				elif next_page == "2":
					tournament = Database.select_tournament_id(self, tournament_id)
					View.display_rounds(self, tournament['rounds'])
					# select all rounds in tournament
				else:
					pass
			else:
				pass

if __name__ == '__main__':
	controller = Controller()
	controller.main()