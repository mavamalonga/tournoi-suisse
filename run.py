from urls import Urls

urls = Urls()

def main(urls):
	page = urls.page_1()
	while True:
		print(end="\n")
		request = input(f'{" "*45} Request : ')
		if request == "e":
			exit()
		elif page == "1":
			if request == "1":
				page = urls.page_11()
				urls.page_1()
			elif request == "2":
				page = urls.page_12()
				page = urls.page_1()
			elif request == "3":
				page = urls.page_13()
			elif request == "4":
				page = urls.page_14()
			else:
				urls.page_404()
		elif page == "13":
			if request == "p":
				page = urls.page_1()
			elif request == "1":
				page = urls.page_131_name()
			elif request == "2":
				page = urls.page_132()
			else:
				urls.page_404()
		elif page == "131":
			if request == "p":
				page = urls.page_13()
			elif request == "n":
				urls.page_131_name()
			elif request == "r":
				urls.page_131_ranking()
			else:
				urls.page_404()
		elif page == "132":
			if request == "p":
				page = urls.page_13()
			else:
				page, tournament_id, tournament_instance = urls.page_132t(request)
				if tournament_id == None:
					page = urls.page_132()
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
				urls.page_404()
		elif page == "132t1":
			if request == "p":
				page, tournament_id, tournament_instance = urls.page_132t(tournament_id)
			elif request == "n":
				page = urls.page_132t1_name(tournament_instance)
			elif request == "r":
				page = urls.page_132t1_ranking(tournament_instance)
			elif request == "m":
				urls.page_132t1_modify_ranking()
				page, tournament_id, tournament_instance = urls.page_132t(tournament_id)
			else:
				urls.page_404()
		elif page == "132t2":
			if request == "p":
				page, tournament_id, tournament_instance = urls.page_132t(tournament_id)
			elif request == "r":
				urls.page_132t2r(tournament_id, tournament_instance)
				page, tournament_id, tournament_instance = urls.page_132t(tournament_id)
			else:
				urls.page_404()
		elif page == "132t3":
			if request == "p":
				page, tournament_id, tournament_instance = urls.page_132t(tournament_id)
			else:
				urls.page_404()
		elif page == "14":
			if request == "p":
				page = urls.page_1()
			elif request == "1":
				urls.page_drop_database()
			elif request == "2":
				page = urls.page_drop_table()
			else:
				urls.page_404()
		elif page == "142":
			if request == "p":
				page = urls.page_14()
			elif request == "1":
				page = urls.page_drop_table_1(request)
			elif request == "2":
				page = urls.page_drop_table_1(request)
			elif request == "3":
				page = urls.page_drop_table_1(request)
			elif request == "4":
				page = urls.page_drop_table_1(request)
			else:
				urls.page_404()

if __name__ == '__main__':
	main(urls)
