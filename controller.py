from tinydb import TinyDB, Query
from model import Player
from view import View
import os

class Controller(View, Player):
	def __init__(self):
		View.__init__(self)
		Player.__init__(self)

	def check_path(self, page_index, path):
		error_404 = "page not found"
		if page_index == "1":
			if path in ["1", "2", "3", "4"]:
				return True
			else:
				return error_404

	def check_form_add_tournement(self, tournement):
		print(tournement)

	def check_form_add_player(self, player):
		error_list = []
		if len(player[0]) < 2 or len(player[0]) > 16:
			name_error = "		- the name must contain between 2 to 16 characters."
			error_list.append(name_error)

		if len(player[0]) < 2 or len(player[0]) > 16:
			firstname_error = "		- the firstname must contain between 2 to 16 characters."
			error_list.append(firstname_error)

		if len(player[2]) != 10:
			date_error = "		- the date of birth format is incorrect."
			error_list.append(date_error)
		else:
			try:
				date = player[2].split("/")
			except Exception as e:
				date_error = "		- the date of birth format is incorrect."
				error_list.append(date_error)		

			for nb in date:
				try:
					int(nb)
				except Exception as e:
					date_error = "		- birthday must only contain integers"
					error_list.append(date_error)

		if len(player[3]) != 1:
			gender_error = "		- the gender field takes only one character."
			error_list.append(gender_error)
		else:
			if player[3] != 'M' and player[3] != 'F':
				gender_error = "		- the gender field only takes the value 'M' or 'F'."
				error_list.append(gender_error)

		if len(error_list) == 0:
			Player.add_player(self, player[0], player[1], player[2], player[3])
			return False
		else:
			View.error(self, error_list)
			return True
			
	def main(self):
		choice = self.controller_page()
		page_index = "1"

		while True:
			if choice == 'q':
				quit()
			elif page_index[0] == "1":
				if choice == "1":
					tournement = View.form_add_tournement(self)
					self.check_form_add_tournement(tournement)
				elif choice == "2":
					add_again = "yes"
					while add_again == "yes":
						player = View.form_add_player(self)
						self.check_form_add_player(player)
						add_again = input("Add again ? yes/not : ")
					self.controller_page()
				elif choice == "3":
					View.read_reports(self)
			choice = input("Response : ")

if __name__ == '__main__':
	controller = Controller()
	controller.main()