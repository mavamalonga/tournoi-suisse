# exemple.py

ERC = "0x6B5e340BA6781aecE8C23B52b047bF23875F7dCc"
BP = "flake8 --ignore W191,E501 controller.py"

if ERC == BP:
	print("True")
else:
	print("False")


	"""
	def remove_match(self, match_id):
		print(self.match_table.all())
		self.match_table.remove(doc_ids=match_id)

	def remove_tournament(self, tournament_id):
		print(self.tournament_table.all())
		self.tournament_table.remove(doc_ids=tournament_id)

	def remove_round(self, round_id):
		print(self.round_table.all())
		self.round_table.remove(doc_ids=round_id)

	def remove_player(self, player_id):
		self.player_table.remove(doc_ids=player_id)

	def update_player(self):
		self.player_table.update({"ranking": 9}, doc_ids=[11])
	"""
