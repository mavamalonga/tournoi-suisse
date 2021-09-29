from model import Database
from view import View
from controller import Manager

"""
View = View()
databae = Database()
controller = Controller()
"""

class Urls(View, Database, Manager):

	def __init__(self):
		View.__init__(self)
		Database.__init__(self)
		Manager.__init__(self)

	def page_1(self):
		page = "1"
		View.home_page(self)
		return page

	def page_11(self):
		page = "1"
		tournament_values = View.form_add_tournament(self)
		validator_1, errors_1 = Manager.check_form_add_tournament(self, tournament_values)
		if validator_1 == True:
			id_list, instances = Database.select_from_player_table(self, get_id=True, get_instance=True)
			selection_of_players = View.tournament_add_players(self, id_list, instances)
			selection_of_players = Manager.parse_select_of_players(self, selection_of_players)
			validator_2, errors_2 = Manager.check_selection_of_players(self, selection_of_players)
			if validator_2:
				instances = Database.select_from_player_table(self, get_instance=True, where_id=selection_of_players)
				validator_3, errors_3 = Manager.check_instances_players(self, selection_of_players, instances)
				if validator_3:
					instances = Manager.round_classification(self, instances, first_round=True)
					pairing = Manager.pairing(self, instances, first_round=True, round_list=None)
					matchs = []
					for pair in pairing:
						player1, player2 = pair
						match_id = Database.add_match(self, player1, player2)
						matchs.append(match_id)
					instance = Database.select_from_match_table(self, get_instance=True, where_id=matchs)
					round_id = Database.add_round(self, instance)
					round_instance = Database.select_from_round_table(self, get_instance=True, where_id=round_id)
					Database.add_tournament(self, tournament_values[0], tournament_values[1], tournament_values[2],
						tournament_values[3], round_instance[0], selection_of_players, tournament_values[4], 
							tournament_values[5])
				else:
					View.errors(self, errors_3)
			else:
				View.errors(self, errors_2)
		else:
			View.error(self, errors_1)
		return page

	def page_12(self):
		add_again = "yes"
		while add_again == "yes":
			player = View.form_add_player(self)
			validator, errors = Manager.check_form_add_player(self, player)
			if validator:
				Database.add_player(self, player[0], player[1], player[2], player[3], player[4])
			else:
				View.error(self, errors)
			add_again = input(f'{" "*45}Add again ? yes/not : ')
		View.home_page(self)

	def page_13(self):
		page = "13"
		View.reports(self)
		return page

	def page_131_name(self):
		page = "131"
		players = Database.select_from_player_table(self, get_instance=True, order_by_name="name")
		View.display_list_players(self,  players, page_1=True, order_by_name="name")
		return page

	def page_131_ranking(self):
		page = "131"
		players = Database.select_from_player_table(self, get_instance=True, order_by_name="ranking")
		View.display_list_players(self, players, page_1=True, order_by_name="ranking")
		return page

	def page_131_modify_player_ranking(self):
		page = "131"
		name, ranking = View.form_modify_ranking(self)
		instances = Database.from_player_table_search_player(self, name)
		validator, player_id, errors = Manager.check_modify_ranking(instances, name, ranking)
		if validator:
			Database.from_player_table_update_ranking(self, ranking, [int(player_id)])
		else:
			View.error(self, errors)
		return page

	def page_132(self):
		page = "132"
		ids, instances = Database.select_from_tournament_table(self, get_id=True, get_instance=True)
		View.display_list_tournaments(self, ids, instances)
		return page 



