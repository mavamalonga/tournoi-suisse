

class Ulrs:

	def __init__(self):
		Controller.__init__(self)
		Database.__init__(self)
		View.__init__(self)

	def path_add_tournament(self):
		tournament_values = View.form_add_tournament(self)
		validator_tournament = Controller.check_form_add_tournament(tournament_values)
		if validator_tournament == True:
			id_list, instances = Database.select_from_player_table(self, get_id=True, get_instance=True)
			selection_of_players = View.tournament_add_players(self, id_list, instances)
			selection_of_players = Controller.parse_select_of_players(selection_of_players)
			validator_selection_of_players = Controller.check_selection_of_players(selection_of_players)
			if validator_selection_of_players:
				instances = Database.select_from_player_table(self, get_instance=True, where_id=selection_of_players)
				validator_instances = Controller.check_instances_players(selection_of_players, instances)
				if validator_instances:
					instances = Controller.round_classification(instances, first_round=True)
					list_match_id = Controller.pairing_add_match(instances)
					list_match_instance = Database.select_from_match_table(self, get_instance=True, where_id=list_match_id)
					round_id = Database.add_round(self, list_match_instance)
					round_instance = Database.select_from_round_table(self, get_instance=True, where_id=round_id)
					Database.add_tournament(self, tournament_values[0], tournament_values[1], tournament_values[2],
					tournament_values[3], round_instance[0], selection_of_players, tournament_values[4], tournament_values[5])
		View.home_page()

	def path_add_player(self):
		add_again = "yes"
		while add_again == "yes":
			player = View.form_add_player(self)
			validator_player = self.check_form_add_player(player)
			if validator_player:
				Database.add_player(self, player[0], player[1], player[2], player[3], player[4])
				add_again = input("Add again ? yes/not : ")
		View.home_page()

	def path_reports(self):
		View.reports(self)
