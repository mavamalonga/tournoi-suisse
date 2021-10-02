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
					pairing = Manager.pairing_first_round(self, instances)
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
					View.error(self, errors_3)
			else:
				View.error(self, errors_2)
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

	def page_132(self):
		page = "132"
		ids, instances = Database.select_from_tournament_table(self, get_id=True, get_instance=True)
		View.display_list_tournaments(self, ids, instances)
		return page 

	def page_132t(self, tournament_id):
		page = "132t"
		validator, errors = Manager.check_select_tournament(self, tournament_id)
		if validator:
			tournament_instance = Database.select_from_tournament_table(self, 
				get_instance=True, where_id=tournament_id)
			if tournament_instance != None:
				View.tournament_menu(self, tournament_instance)
				return page, tournament_id, tournament_instance
			else:
				page = "132"
				View.error(self, [f'there is no tournament with the following id {tournament_id}'])
				return page, None, None
		else:
			page = "132"
			View.error(self, errors)
			return page, None, None

	def page_132t1_name(self, tournament_instance):
		page = "132t1"
		players = Database.select_from_player_table(self, get_instance=True, where_id=tournament_instance['players'], 
			order_by_name="name")
		View.display_list_players(self, players, page_1=False, order_by_name="name")
		return page

	def page_132t1_ranking(self, tournament_instance):
		page = "132t1"
		players = Database.select_from_player_table(self, get_instance=True, 
			where_id=tournament_instance['players'], order_by_name="ranking")
		View.display_list_players(self, players, page_1=False, order_by_name="ranking")
		return page

	def page_132t1_modify_ranking(self):
		page = "132t1"
		name, ranking = View.form_modify_ranking(self)
		instances = Database.from_player_table_search_player(self, name)
		validator, player_id, errors = Manager.check_modify_ranking(self, instances, name, ranking)
		if validator:
			Database.from_player_table_update_ranking(self, ranking, [int(player_id)])
			View.notification(self, "change success !!")
		else:
			View.error(self, errors)
		return page

	def page_132t2(self, tournament_instance):
		page = "132t2"
		View.display_rounds(self, tournament_instance['rounds'])
		return page

	def page_132t2r(self, tournament_id, tournament_instance):
		"""Update round score"""
		pts_list = View.display_form_results(self, tournament_instance['rounds'])
		validator_1, new_pts_list, errors_1 = Manager.convert_points(self, pts_list)
		if validator_1:
			validator_2, errors_2 = Manager.check_points_values(self, new_pts_list)
			if validator_2:
				new_pts_list = Manager.transform_matchs_scores_tuple(self, new_pts_list)
				update_matchs = Database.update_match_score(self, tournament_id, new_pts_list)
				""" create new rounds"""
				if len(tournament_instance['rounds']) < 7:
					instances_order = Manager.round_classification(self, update_matchs, first_round=False)
					""" create pairing and add new match"""
					matchs = []
					dict_1 = {}
					dict_2 = {}
					for player in instances_order:
						p = {player['name']: player}
						dict_1.update(p)
						dict_2.update(p)

					for i in range(4):
						try:
							name1, name2 = Manager.check_pairings(self, dict_1, dict_2, tournament_instance['rounds'])
						except Exception as e:
							name1, name2 = list(dict_1)[-1], list(dict_1)[-2]
						match_id = Database.add_match(self, dict_1[name1], dict_2[name2])
						matchs.append(match_id)
						del dict_1[name1]
						del dict_1[name2]
						del dict_2[name1]
						del dict_2[name2]
					match_instances = Database.select_from_match_table(self, get_instance=True, where_id=matchs)
					round_id = Database.add_round(self, match_instances)
					round_instances = Database.select_from_round_table(self, get_instance=True, where_id=round_id)
					Database.update_tournament_round(self, tournament_id, round_instances[0])
					View.notification(self, "change success !!")
				else:
					"""the tournament has reached its maximum number of matches"""
					pass
			else:
				View.error(self, errors_2)
		else:
			View.error(self, errors_1)

	def page_132t3(self, tournament_instance):
		page = "132t3"
		View.display_matchs(self, tournament_instance['rounds'])
		return page 

	def page_132t4(self, tournament_id):
		new_date = View.add_new_date_tournament(self)
		validator, errors = Manager.check_date_tournament(self, new_date)
		if validator:
			Database.update_date_tournament(self, tournament_id, new_date)
			View.notification(self, "Add new date success !")
		else:
			View.error(self, errors)

	def page_14(self):
		page = "14"
		View.settings(self)
		return page

	def page_drop_database(self):
		to_confirm = View.confirm(self)
		if to_confirm:
			Database.drop_database(self)
			View.notification(self, "drop database successful !")
			page = self.page_14()
		else:
			View.notification(self, "drop database canceled.")
			page = self.page_14()

	def page_drop_table(self):
		page = View.drop_table(self)
		return page

	def page_drop_table_1(self, table):
		Database.drop_table(self, table)
		print_table = f'drop table {table} successful !'
		View.notification(self, print_table)
		page = self.page_14()
		return page 

	def page_404(self):
		View.page_404(self)
		return None
