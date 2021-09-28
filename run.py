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
				page = urls.page_131()
			elif request == "2":
				page = urls.page_132()
		elif page == "131":
			pass



		"""
		elif page == "12":
			validator = check_next_page(urls)
		elif page == "13":
			validator = check_next_page(urls)
		elif page == "131":
			validator = check_next_page(urls)
		elif page == "132":
			validator = check_next_page(urls)
		elif page == "132t":
			validator = check_next_page(urls)
		elif page == "132t1":
			validator = check_next_page(urls)
		elif page == "132t1m":
			validator = check_next_page(urls)
		elif page == "132t2":
			validator = check_next_page(urls)
		elif page == "132t3":
			validator = check_next_page(urls)
		"""

if __name__ == '__main__':
	main(urls)
