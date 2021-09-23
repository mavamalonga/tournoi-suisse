def main(self):

	Urls = {
		"1": ([View.home_page(self)],["1", "2", "3"]),
		"11": ([Controller.patch_add_tournament(self)], ["1", "e"]),
		"12": ([Controller.path_add_player(self)], ["1", "e"]),
		"13": ([Controller.path_reports(self)], ["1", "131", "132", "e"]),
		"131": ([Controller.path_list_of_players(self)], ["13", "e"]),
		"132": ([Controller.path_list_of_tournament(self)], ["13", "int(&)", "e"]),
		"132t": ([Controller.path_tournament(self)], ["132", "132t1", "132t2", "132t3", "e"]),
		"132t1": ([Controller.path_list_players_tournament(self)], ["132t", "132t1", "132t1m", "e"]),
		"132t1m": ([Controller.path_modify_ranking(self)], ["132t1", "e"]),
		"132t2": ([Controller.path_rounds(self)], ["132t", "132t2r", "e"]),
		"132t3": ([Controller.path_matchs(self)], ["132t", "e"])
	}
	page = View.home_page(self) # page = "1"
	while True:
		next_page = input(f'{" "*45} Next page : ')
		for   in Urls:
			if next_page == "e":
				exit()
			elif next_page == url:
				Urls[next_page]



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
				self.path_upgrade_results(instance)
				View.home_page(self)
			else:
				pass
		else:
			pass

if __name__ == '__main__':
	controller = Controller()
	controller.main()