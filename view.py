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
			description, description]
		for line in lines:
			value = input(f'{" "*15} {line}')
			form_values.append(value)
		return form_values

	def display_list_players(self, id_list, players):
		print("		Add players : enter the id of 8 players separated by commas")
		print("		Id  Firstname  Name  Gender  Birthday")
		for player_id, player in zip(id_list,players):
			print('		 {0}  {1}  {2}  {3}  {4}'.format(player_id, 
				player["firstname"], player["name"], player["gender"], player["birthday"]))
		Id = input("		Choice Id : ")
		return Id 

	def form_add_player(self):
		print("#"*15 + " Form player")
		name = input("		name : ")
		firstname = input("		firstname : ")
		birthday = input("		birthday : ")
		gender = input("		gender : ")
		ranking = input("		ranking : ")
		return [name, firstname, birthday, gender, ranking]

	def read_reports(self):
		print(f'{"#"*15} Read reports')
		text_read_reports = "\n \
		1 : List of all players\n \
		2 : List of all tournaments \n \
		q : quit "
		print(text_read_reports)

	def reports_tournament(self):
		print(f'{"#"*15} tournament reports')
		text_read_reports = "\n \
		1 : List of all players in a tournament \n \
		2 : List of all rounds in a tournament \n \
		q : quit "
		print(text_read_reports)

	def display_list_players(self, players, order_by_name):
		print(f'{"#"*15} List of all players \n')
		print(f'{" "*15} Ranking Name Firstname')
		for player in players:
			print(f'{" "*15} {player["ranking"]} {player["name"]} {player["firstname"]}')
		if order_by_name == "name":
			print("\n \
		2 : order by ranking")
		else:
			print("\n \
		1 : order by name")

	def display_list_tournaments(self, ids, instances):
		print("#"*15 + " List of all tournament \n")
		print(f"{' '*15} Id  Name    Date")
		for tournament_id, tournament_instance in zip(ids, instances):
			print(f"{' '*15} {tournament_id}   {tournament_instance['name']} {tournament_instance['date']}")

	def display_tournament(self, instance):
		print(f"{'#'*15} {instance['name']} \n")
		for attr in instance:
			if attr != "rounds" and attr != "players":
				print(f"{' '*15} {attr} {instance[str(attr)]}")
		print(f"{' '*15} {instance['rounds']['name']}")
		for match in instance['rounds']['matchs']:
			player1, player2 = match['match']
			print(f"{' '*20} {player1[0]['name']} {player1[1]} vs {player2[1]} {player2[0]['name']}")
		print(f"{' '*15} To enter the results press the key 'r'")
		print(f"{' '*15} To display all the players of the tournament press the key 'p'")

	def display_form_results(self, instance):
		print(f"{'#'*15} Results \n")
		list_pts = []
		for match in instance['rounds']['matchs']:
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