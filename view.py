from model import Database

class View:
	def __init__(self):
		pass

	def home_page(self):
		print(end="\n")
		page = "1"
		print(f'{" "*60} HOME')
		a = "1 : Add new tournament"
		b = "2 : Add new player"
		c = "3 : Read reports"
		d = "e : Exit the application"
		lines = [a, b, c, d]
		for line in lines:
			print(f'{" "*60} {line}')
		return page, None
		
	def form_add_tournament(self):
		print(f'{" "*60} ADD TOURNAMENT')
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
			value = input(f'{" "*60} {line}')
			form_values.append(value)
		return form_values

	def form_add_player(self):
		print(f'{" "*60} ADD PLAYER')
		form_values = []
		name = "name : "
		firstname = "firstname : "
		birthday = "birthday : "
		gender = "gender : "
		ranking = "ranking : "
		lines = [name, firstname, birthday, gender, ranking]
		for line in lines:
			value = input(f'{" "*60} {line}')
			form_values.append(value)
		return form_values

	def reports(self):
		print(f'{" "*60} REPORTS')
		a = "1 : List of all players"
		b = "2 : List of all tournaments"
		c = "p : Previous page"
		d = "e : Exit the application"
		lines = [a, b, c, d]
		for line in lines:
			print(f'{" "*60} {line}')

	def tournament_add_players(self, id_list, instances):
		print(f'{" "*60} Add players : enter the id of 8 players separated by commas')
		print(f'{" "*60} Id  Firstname  Name  Gender  Birthday')
		for player_id, player_instance in zip(id_list, instances):
			print(f'{" "*62} {player_id} {player_instance["firstname"]} {player_instance["name"]}')
		ids = input(f'{" "*60} Choice ids : ')
		return ids

	def display_list_players(self, players, page_1=True, order_by_name="name"):
		"""Header"""
		if page_1:
			print(f'{" "*60} LIST OF ALL PLAYERS')
		else:
			print(f'{" "*60} LIST OF ALL PLAYERS IN A TOURNAMENT')
		"""Body"""
		print(f'{" "*60} Ranking {" "*1}Name Firstname')
		for player in players:
			print(f'{" "*62} {player["ranking"]}{" "*6}{player["name"]} {player["firstname"]}')
		"""Footer"""
		if order_by_name == "name":
			print(f'{" "*60} r : Order by ranking')
			print(f'{" "*60} p : Previous page')
		else:
			print(f'{" "*60} n : Order by name')
			print(f'{" "*60} p : Previous page')
		if page_1 == False:
			print(f'{" "*60} m : Modify player"s ranking')

	def display_list_tournaments(self, ids, instances):
		print(" "*60 + " LIST OF ALL TOURNAMENT")
		print(f"{' '*60} Id  Name    Date")
		for tournament_id, tournament_instance in zip(ids, instances):
			print(f"{' '*60} {tournament_id}   {tournament_instance['name']} {tournament_instance['date']}")
		c = "p : Previous page"
		d = "e : Exit the application"
		print(end="\n")
		lines = [c, d]
		for line in lines:
			print(f'{" "*60} {line}')

	def tournament_menu(self, instance):
		print(f"{' '*60} Tournament {instance['name']} \n")
		for attr in instance:
			if attr != "name" and attr != "rounds" and attr != "players":
				print(f"{' '*60} {attr} : {instance[str(attr)]}")
		print(end="\n")
		a = "1 : List of all players in a tournament"
		b = "2 : List of all rounds in a tournament"
		c = "3 : List of all matchs in tournament"
		d = "b : Previous page"
		e = "e : Exit the application"
		lines = [a, b, c, d, e]
		for line in lines:
			print(f'{" "*60} {line}')

	def display_rounds(self, round_list):
		print(f"{' '*60} LIST OF ALL ROUNDS IN A TOURNAMENT")
		for round_instance in round_list:
			print(f"{' '*60} {round_instance['name']}")
			print(f"{' '*60}  Start : {round_instance['start_date']}")
			print(f"{' '*60}  End : {round_instance['end_date']}")
			for match in round_instance['matchs']:
				player1, player2 = match['match']
				print(f"{' '*65} {player1[0]['name']} {player1[1]} vs {player2[1]} {player2[0]['name']}")
			print(f'{" "} \n')
		if len(round_list) == 7 and round_list[-1]['end_date'] != None:
			print(f"{' '*65}Tournament ended on {round_list[-1]['end_date']}")
		else:
			print(f"{' '*65} To enter the results press the key 'r'")

	def display_matchs(self, round_list):
		print(f"{' '*60} LIST OF ALL MATCHS IN TOURNAMENT")
		for round_instance in round_list:
			for match in round_instance['matchs']:
				player1, player2 = match['match']
				print(f"{' '*65} {player1[0]['name']} {player1[1]} vs {player2[1]} {player2[0]['name']}")

	def display_form_results(self, round_list):
		latest_round = round_list[-1]
		print(f"{' '*60} RESULTS \n")
		list_pts = []
		for match in latest_round['matchs']:
			player1, player2 = match['match']
			print(f"{' '*65} {player1[0]['name']} {player1[1]} vs {player2[1]} {player2[0]['name']}")
			pts = input(f"{' '*65} {player1[0]['name']} points : ")
			list_pts.append(pts)
			pts = input(f"{' '*65} {player2[0]['name']} points : ")
			list_pts.append(pts)
		return list_pts

	def form_modify_ranking(self):
		name = input(f'{" "*60} name of player : ')
		ranking = input(f'{" "*60} new ranking : ')
		return name, ranking

	def error(self, error_list):
		print(f'{" "*60} ERROR')
		for error in error_list:
			print(f'{" "*65}- {error}')
		print(end='\n')

	def notification(self, notif):
		print(f'{" "*60} {notif}')
		print(end="\n")