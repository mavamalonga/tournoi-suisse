from tinydb import TinyDB, Query
from model import Database
from view import View
import os

class Controller(View, Database):
	def __init__(self):
		View.__init__(self)
		Database.__init__(self)

	def check_next_page(self, page, next_page):
		if page == "1":
			if next_page in ["1", "2", "3", "4"]:
				return True
			else:
				return False
		if page == "13":
			if next_page in ["1", "2", "3", "4", "5"]:
				return True
			else:
				return False
		if page == "131":
			if next_page in ["1", "2"]:
				return True
			else:
				return False

	def check_form_add_tournement(self, tournement):
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
			control_time_error = "		- control time must only contain following values : bullet, blitz, rapide"
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
			except Exception as e:
				date_error = "		- the date of birth format is incorrect."
				error_list.append(date_error)		

			for nb in date:
				try:
					int(nb)
				except Exception as e:
					date_error = "		- birthday must only contain integers"
					error_list.append(date_error)

		if len(player[3]) != 1:
			gender_error = "		- the gender field takes only one character."
			error_list.append(gender_error)
		else:
			if player[3] != 'M' and player[3] != 'F':
				gender_error = "		- the gender field only takes the value 'M' or 'F'."
				error_list.append(gender_error)

		if len(error_list) == 0:
			Database.add_player(self, player[0], player[1], player[2], player[3])
			return False
		else:
			View.error(self, error_list)
			return True

	def parse_and_check_player_id(self, Ids):
		error_list = []
		players = []
		Ids.replace(' ', '')
		Id_list = Ids.split(",")
		if len(Id_list) != 8:
			Id_error = "		- incorrect number of player_id"
			error_list.append(Id_error)
		else:
			for player_id in Id_list:
				try:
					int(player_id)
					players.append(player_id)
				except Exception as e:
					Id_error = "		- player_id list must only contain integers."
					error_list.append(Id_error)
		
		if len(error_list) == 0:
			return [True, players]
		else:
			View.error(self, error_list)
			return [False, players]

	def check_player_instance(self, id_list, player_instance):
		error_list = []
		for Id, player in zip(id_list, player_instance):
			if player == None:
				player_error = "		- there is no player with the following id :{0}".format(Id)
				error_list.append(player_error)
		if len(error_list) == 0:
			return True
		else:
			View.error(self, error_list)
			return False

	def pairing(self, player_instance):
		part_one = player_instance[:4]
		part_two = player_instance[4:]
		match_list = []
		for player1, player2 in zip(part_one, part_two):
			match_id = Database.add_match(self, player1, player2)
			match_list.append(match_id)
		return match_list

	def main(self):
		page = "1"
		self.home_page()
		while True:
			next_page = input("Response : ")
			if next_page.lower() == "q":
				quit()
			elif page == "1":
				validator = self.check_next_page(page, next_page)
				if validator:
					if next_page == "1":
						tournement = View.form_add_tournement(self) #we enter and retrieve the we enter with a single request
						validator_tournement = self.check_form_add_tournement(tournement)
						if  validator_tournement == True:
							players = Database.select_players_for_tournement(self)
							select_player_id = View.display_players_for_tournement(self, players[0], players[1])
							validator_player_id = self.parse_and_check_player_id(select_player_id)
							if validator_player_id[0]:
								player_instances = Database.select_player_instances(self, validator_player_id[1])
								validator_instances = self.check_player_instance(validator_player_id[1], player_instances)
								if validator_instances:
									match_list = self.pairing(player_instances)
									round_id = Database.add_round(self, match_list)
									round_instance = Database.select_round(self, round_id)
									tournement_id = Database.add_tournement(self, tournement[0], tournement[1], tournement[2],
										tournement[3], [round_instance], validator_player_id[1], tournement[4], tournement[5])
									tournement_instance = Database.select_tournement(self, tournement_id)
									#View.display_tournement(self, tournement_instance)
									print(tournement_instance)
								else:
									pass
							else:
								self.home_page()
						else:
							self.home_page()
					elif next_page == "2":
						add_again = "yes"
						while add_again == "yes":
							player = View.form_add_player(self)
							self.check_form_add_player(player)
							add_again = input("Add again ? yes/not : ")
						self.home_page()
					elif next_page == "3":
						page = page + next_page
						View.read_reports(self)
				else:
					self.home_page(error_404=True)
			elif page == "13":
				validator = self.check_next_page(page, next_page)
				if validator:
					if next_page == "1":
						page = page + next_page
						players = Database.select_players(self)
						View.display_players(self, players)
					elif next_page == "2":
						page = page + next_page
						tournaments = Database.select_tournament(self)
						tournament_choice = View.display_tournament(self, tournaments[0], tournaments[1])
					elif next_page == "3":
						pass
					elif next_page == "4":
						pass
					elif next_page == "5":
						pass
			elif page == "131":
				validator = self.check_next_page(page, next_page)
				if validator:
					if next_page == "1":
						players = Database.select_players(self)
						View.display_players(self, players)
					elif next_page == "2":
						players = Database.select_players(self, order_by_name=False)
						View.display_players(self, players, order_by_name=False)
				else:
					pass
		

if __name__ == '__main__':
	controller = Controller()
	controller.main()