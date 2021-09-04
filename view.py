from model import Player

class View:
	def __init__(self):
		pass

	def controller_page(self):
		print("#"*15 + " controller page")
		text_controller_page = "\n \
		1 : Create new tournement \n \
		2 : Add new player in database \n \
		3 : Read reports \n \
		4 : Settings \n \
		q : quit "
		print(text_controller_page)

	def form_add_tournement(self):
		print("#"*15 + " form create tournement")
		name = input("		name : ")
		place = input("		place : ")
		date = input("		date : ")
		nb_of_turns = input("		nb_of_turns : ")
		control_time = input("		controller_time : ")
		description = input("		description : ")
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

	def error(self, error_list):
		print("\n \
		ERROR WHEN ENTERING IT.")
		for error in error_list:
			print(error)
		print("\n \
			")
