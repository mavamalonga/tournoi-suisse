from urls import Urls

urls = Urls()

def main(urls):
	page = urls.page_1()
	while True:
		print(end="\n")
		request = input(f'{" "*45} Next page : ')
		if request == "e":
			exit()
		elif page == "1":
			if request == "1":
				page = urls.page_11()
				urls.page_1()
			elif request == "2":
				page = urls.page_12()
			elif request == "3":
				page = urls.page_13()
			else:
				urls.page_404()
		elif page == "13":
			if request == "p":
				page = urls.page_1()
			elif request == "1":
				page = urls.page_131_name()
			elif request == "2":
				page = urls.page_132()
		elif page == "131":
			if request == "p":
				page = urls.page_13()
			elif request == "n":
				page = urls.page_131_name()
			elif request == "r":
				page = urls.page_131_ranking()
			"""
			elif request == "m":
				page = urls.page_131_modify_player_ranking()
			"""
		elif page == "132":
			if request == "p":
				page = urls.page_13()
			else:
				page, tournament_id, tournament_instance = urls.page_132t(request)
		elif page == "132t":
			if request == "p":
				page = urls.page_132()
			elif request == "1":
				page = urls.page_132t1_name(tournament_instance)
			elif request == "2":
				page = urls.page_132t2(tournament_instance)
			elif request == "3":
				page = urls.page_132t3(tournament_instance)
			else:
				# page 404
				pass
		elif page == "132t1":
			if request == "p":
				page, tournament_id, tournament_instance = urls.page_132t(tournament_id)
			elif request == "n":
				page = urls.page_132t1_name(tournament_instance)
			elif request == "r":
				page = urls.page_132t1_ranking(tournament_instance)
			elif request == "m":
				urls.page_132t1_modify_ranking()
				page = urls.page_132t(tournament_id)
			else:
				pass
				# 404
		elif page == "132t2":
			if request == "p":
				page, tournament_id, tournament_instance = urls.page_132t(tournament_id)
			elif request == "r":
				urls.page_132t2r(tournament_id, tournament_instance)
				page = urls.page_132t(tournament_id)
			else:
				pass
		elif page == "132t3":
			if request == "p":
				page, tournament_id, tournament_instance = urls.page_132t(tournament_id)
			else:
				pass





if __name__ == '__main__':
	main(urls)
