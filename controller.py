from model import Tournoi, Player
from view import View
import os


class Controller(View, Player):
	def __init__(self):
		self.matchs = "0"
		View.__init__(self)
		Player.__init__(self)

	def home(self):
		View.home_page(self)

	def check_form_player(self, data):
		if data[0] is not None:
			if len(data[0] > 16):
				
		else:
			print("Error name")

		

	def create_player(self):
		data = View.form_player(self)
		if data[0] is not None:
			if len(data[0]) > 16:
				print("Error name")

		if len(data[1]) > 16:
			print("Error firstname")
		if len(data[2]) > 10:
			sep_data = data[2].split("/")



	def main(self):
		var = 0
		self.home()
		while True:
			if var == 'q':
				quit()
			if var == "0":
				self.home()
			if var == "1":
				data = self.create_player()


			var = input("Response : ")




if __name__ == '__main__':
	c = Controller()
	c.main()



""""
Download_image.__init__(self, self.home_page, 
						data[0], data[3], self.category_name)
"""