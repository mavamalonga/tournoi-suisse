from model import Database

class View:
	def __init__(self):
		self.error_404 = "		page not found"

	def home_page(self, error_404=False):
		page = "1"
		print("#"*15 + "home page")
		if error_404:
			self.error([self.error_404])
		text_controller_page = "\n \
		1 : Add new tournament \n \
		2 : Add new player \n \
		3 : Read reports \n \
		4 : Settings \n \
		q : quit "
		print(text_controller_page)
		
	def form_add_tournament(self):
		print("#"*15 + " form create tournement")
		name = input("		name : ")
		place = input("		place : ")
		date = input("		date : ")
		nb_of_turns = input("		nb_of_turns : ")
		control_time = input("		controller_time : ")
		description = input("		description : ")
		return [name, place, date, nb_of_turns, control_time, description]

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
		print("#"*15 + " Read reports")
		text_read_reports = "\n \
		1 : List of all players\n \
		2 : List of all tournaments \n \
		q : quit "
		print(text_read_reports)

	def reports_tournament(self):
		print("#"*15 + " tournament reports")
		text_read_reports = "\n \
		1 : List of all players in a tournament \n \
		2 : List of all rounds in a tournament \n \
		q : quit "
		print(text_read_reports)


	def display_list_players(self, players, order_by_name):
		print("#"*15 + " List of all players \n")
		print(" "*15 + " Ranking" +" "+"Name"+" "+"Firstname"+" "+"Gender"+" "+"Birthday")
		for player in players:
			print("		" + str(player["ranking"]) +" "+ player["name"]
				+" "+player["firstname"]+ " "+player["gender"]+" "+player["birthday"])
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
			print(f"		{tournament_id}   {tournament_instance['name']} {tournament_instance['date']}")

	def display_tournament(self, instance):
		print(f"{'#'*15} {instance['name']} \n")
		for attr in instance:
			if attr != "rounds" and attr != "players":
				print(f"{' '*15} {attr} {instance[str(attr)]}")
		"""Display round and matchs"""
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
		print("\n \
		ERROR")
		for error in error_list:
			print(error)
		print("\n \
			")
