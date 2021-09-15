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

	def display_report_player(self, players, order_by_name=True):
		print("#"*15 + " List of all players \n")
		print(" "*15 + " Ranking" +" "+"Name"+" "+"Firstname"+" "+"Gender"+" "+"Birthday")
		for player in players:
			print("		" + str(player["ranking"]) +" "+ player["name"]
				+" "+player["firstname"]+ " "+player["gender"]+" "+player["birthday"])
		if order_by_name == True:
			print("\n \
		2 : order by ranking")
		else:
			print("\n \
		1 : order by name")

	def display_tournament(self, tournament_ids, tournament_instances):
		print("#"*15 + " List of all tournaments \n")
		print(" "*15 + " Id Name")
		for Id, tournament in zip(tournament_ids, tournament_instances):
			print("		{0} {1}".format(Id, tournament["name"]))

	def display_rounds(self, round_instance):
		print("#"*15 + " List of rounds \n")
		for single_round in round_instance:
			print("		{0}".format(single_round['name']))
			for match in single_round['matchs']:
				player1 = match['Match'][0]
				player1_instance = player1[0]
				player1_score = player1[1]
				player2 = match['Match'][1]
				player2_instance = player2[0]
				player2_score = player2[1]
				print("		{0} {1} vs {2} {3}".format(player1_instance['name'], player1_score,
					player2_instance['name'], player2_score))

	def error(self, error_list):
		print("\n \
		ERROR")
		for error in error_list:
			print(error)
		print("\n \
			")
