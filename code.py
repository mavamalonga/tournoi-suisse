def main(self):
		choice = 0
		self.controller_page()
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