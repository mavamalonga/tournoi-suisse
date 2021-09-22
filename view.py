from model import Database

class View:
	def __init__(self):
		pass

	def home_page(self):
		print(f'{"#"*15} HOME')
		a = "1 : Add new tournament"
		b = "2 : Add new player"
		c = "3 : Read reports"
		d = "4 : Settings"
		e = "q : quit"
		lines = [a, b, c, d, e]
		for line in lines:
			print(f'{" "*15} {line}')
		
	def form_add_tournament(self):
		print(f'{"#"*15} ADD TOURNAMENT')
		form_values = []
		name = "name : "
		place = "place : "
		date = "date : "
		nb_of_turns = "nb of turns : "
		controller_time = "controller time : "
		description = "description : "
		lines = [name, place, date, nb_of_turns, controller_time, 
			description]
		for line in lines:
			value = input(f'{" "*15} {line}')
			form_values.append(value)
		return form_values

	def form_add_player(self):
		print(f'{"#"*15} ADD PLAYER')
		form_values = []
		name = "name : "
		firstname = "firstname : "
		birthday = "birthday : "
		gender = "gender : "
		ranking = "ranking : "
		lines = [name, firstname, birthday, gender, ranking]
		for line in lines:
			value = input(f'{" "*15} {line}')
			form_values.append(value)
		return form_values

	def reports(self):
		print(f'{"#"*15} REPORTS')
		a = "1 : List of all players"
		b = "2 : List of all tournaments"
		c = "q : quit"
		lines = [a, b, c]
		for line in lines:
			print(f'{" "*15} {line}')

	def tournament_add_players(self, id_list, instances):
		print(f'{" "*15} Add players : enter the id of 8 players separated by commas')
		print(f'{" "*17} Id  Firstname  Name  Gender  Birthday')
		for player_id, player_instance in zip(id_list, instances):
			print(f'{" "*17} {player_id} {player_instance["firstname"]} {player_instance["name"]}')
		ids = input(f'{" "*15} Choice ids : ')
		return ids

	def display_list_players(self, players, page_1=True, order_by_name="name"):
		"""Header"""
		if page_1:
			print(f'{"#"*15} List of all players \n')
		else:
			print(f'{"#"*15} List of all players in a tournament\n')
		"""Body"""
		print(f'{" "*15} Ranking {" "*3}Name Firstname')
		for player in players:
			print(f'{" "*15} {player["ranking"]}{" "*10}{player["name"]} {player["firstname"]}')
		"""Footer"""
		if order_by_name == "name":
			print("\n \
		2 : order by ranking")
		else:
			print("\n \
		1 : order by name")
		if page_1 == False:
			print(f'{" "*15} 3 : Modify player"s ranking')

	def display_list_tournaments(self, ids, instances):
		print("#"*15 + " List of all tournament \n")
		print(f"{' '*15} Id  Name    Date")
		for tournament_id, tournament_instance in zip(ids, instances):
			print(f"{' '*15} {tournament_id}   {tournament_instance['name']} {tournament_instance['date']}")

	def tournament_menu(self, instance):
		print(f"{'#'*15} Tournament {instance['name']} \n")
		for attr in instance:
			if attr != "name" and attr != "rounds" and attr != "players":
				print(f"{' '*15} {attr} : {instance[str(attr)]}")
		print(end="\n")
		a = "1 : List of all players in a tournament"
		b = "2 : List of all rounds in a tournament"
		c = "3 : List of all matchs in tournament"
		d = "q : quit"
		lines = [a, b, c, d]
		for line in lines:
			print(f'{" "*15} {line}')

	def display_rounds(self, round_list):
		print(f"{'#'*15} List of all rounds in a tournament \n")
		for round_instance in round_list:
			print(f"{' '*15} {round_instance['name']}")
			print(f"{' '*15}  Start : {round_instance['start_date']}")
			print(f"{' '*15}  End : {round_instance['end_date']}")
			for match in round_instance['matchs']:
				player1, player2 = match['match']
				print(f"{' '*20} {player1[0]['name']} {player1[1]} vs {player2[1]} {player2[0]['name']}")
			print(f'{" "} \n')
		print(f"{' '*15} To enter the results press the key 'r'")

	def display_matchs(self, round_list):
		print(f"{'#'*15} List of all matchs in tournament \n")
		for round_instance in round_list:
			for match in round_instance['matchs']:
				player1, player2 = match['match']
				print(f"{' '*20} {player1[0]['name']} {player1[1]} vs {player2[1]} {player2[0]['name']}")

	def display_form_results(self, round_list):
		latest_round = round_list[-1]
		print(f"{'#'*15} Results \n")
		list_pts = []
		for match in latest_round['matchs']:
			player1, player2 = match['match']
			print(f"{' '*20} {player1[0]['name']} {player1[1]} vs {player2[1]} {player2[0]['name']}")
			pts = input(f"{' '*20} {player1[0]['name']} points : ")
			list_pts.append(pts)
			pts = input(f"{' '*20} {player2[0]['name']} points : ")
			list_pts.append(pts)
		return list_pts

	def error(self, error_list):
		print(f'{" "*15} ERROR')
		for error in error_list:
			print(f'{error}')
		print(end='\n')