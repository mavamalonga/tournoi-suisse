from model import Database

class View:
	def __init__(self):
		self.error_404 = "		page not found"

	def controller_page(self, error_404=False):
		page = "1"
		print("#"*15 + " controller page")
		if error_404:
			self.error([self.error_404])
		text_controller_page = "\n \
		1 : Create new tournement \n \
		2 : Add new player in database \n \
		3 : Read reports \n \
		4 : Settings \n \
		q : quit "
		print(text_controller_page)
		
	def form_add_tournement(self):
		print("#"*15 + " form create tournement")
		print("		2 to 16 characters.")
		name = input("		name : ")
		print("		66 max characters.")
		place = input("		place : ")
		print("		Format dd/mm/yyyy")
		date = input("		date : ")
		print("		Integer, defect = 4")
		nb_of_turns = input("		nb_of_turns : ")
		print("		bullet, blitz or rapide")
		control_time = input("		controller_time : ")
		print("		234 max characters.")
		description = input("		description : ")
		# players
		# rounds
		return [name, place, date, nb_of_turns, control_time, description]

	def form_add_player(self):
		print("#"*15 + " Form player")
		print("		2 to 16 characters.")
		name = input("		name : ")
		print("		2 to 16 characters.")
		firstname = input("		firstname : ")
		print("		Format dd/mm/yyyy")
		birthday = input("		birthday : ")
		print("		M/F")
		gender = input("		gender : ")
		#ranking = input("		ranking : ")
		return [name, firstname, birthday, gender]

	def read_reports(self):
		print("#"*15 + " Read reports")
		text_read_reports = "\n \
		1 : List of all players\n \
		2 : List of all players in a tournament \n \
		3 : List of all tournaments \n \
		4 : Liste de tous les tours d'un tournoi \n \
		5 : List of all matches in a tournament \n \
		q : quit "
		print(text_read_reports)

	def display_players(self, players, order_by_name=True):
		print("#"*15 + " List of all players \n")
		print(" "*15 + " Ranking" +" "+"Name"+" "+"Firstname"+" "+"Gender"+" "+"Birthday")
		for player in players:
			print("		" + player["ranking"] +" "+ player["name"]
				+" "+player["firstname"]+ " "+player["gender"]+" "+player["birthday"])
		if order_by_name == True:
			print("\n \
		2 : order by ranking")
		else:
			print("\n \
		1 : order by name")

	def error(self, error_list):
		print("\n \
		ERROR")
		for error in error_list:
			print(error)
		print("\n \
			")
