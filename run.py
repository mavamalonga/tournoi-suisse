from urls import Urls


def main():
    urls = Urls()
    page = urls.home_page()
    while True:
        print(end="\n")
        request = input(f'{" "*45} Request : ')
        if request == "e":
            exit()
        elif page == "1":
            if request == "1":
                page = urls.add_tournament()
                urls.home_page()
            elif request == "2":
                page = urls.add_player()
                page = urls.home_page()
            elif request == "3":
                page = urls.reports_menu()
            elif request == "4":
                page = urls.settings_menu()
            else:
                urls.page_not_found()
        elif page == "13":
            if request == "p":
                page = urls.home_page()
            elif request == "1":
                page = urls.players_order_name()
            elif request == "2":
                page = urls.tournament_list()
            else:
                urls.page_not_found()
        elif page == "131":
            if request == "p":
                page = urls.reports_menu()
            elif request == "n":
                urls.players_order_name()
            elif request == "r":
                urls.players_order_ranking()
            else:
                urls.page_not_found()
        elif page == "132":
            if request == "p":
                page = urls.reports_menu()
            else:
                page, tournament_id, tournament_instance = urls.tournament_menu(request)
                if tournament_id is None:
                    page = urls.tournament_list()
        elif page == "132t":
            if request == "p":
                page = urls.tournament_list()
            elif request == "1":
                page = urls.players_from_tournament_order_name(tournament_instance)
            elif request == "2":
                page = urls.rounds_from_tournament(tournament_instance)
            elif request == "3":
                page = urls.matchs_from_tournament(tournament_instance)
            elif request == "4":
                urls.add_new_date_tournament(tournament_id)
                page, tournament_id, tournament_instance = urls.tournament_menu(tournament_id)
            else:
                urls.page_not_found()
        elif page == "132t1":
            if request == "p":
                page, tournament_id, tournament_instance = urls.tournament_menu(tournament_id)
            elif request == "n":
                page = urls.players_from_tournament_order_name(tournament_instance)
            elif request == "r":
                page = urls.players_from_tournament_order_ranking(tournament_instance)
            elif request == "m":
                urls.modify_player_ranking_from_tournament()
                page, tournament_id, tournament_instance = urls.tournament_menu(tournament_id)
            else:
                urls.page_not_found()
        elif page == "132t2":
            if request == "p":
                page, tournament_id, tournament_instance = urls.tournament_menu(tournament_id)
            elif request == "r":
                urls.enter_results_of_tournament(tournament_id, tournament_instance)
                page, tournament_id, tournament_instance = urls.tournament_menu(tournament_id)
            else:
                urls.page_not_found()
        elif page == "132t3":
            if request == "p":
                page, tournament_id, tournament_instance = urls.tournament_menu(tournament_id)
            else:
                urls.page_not_found()
        elif page == "14":
            if request == "p":
                page = urls.home_page()
            elif request == "1":
                urls.drop_database()
            elif request == "2":
                page = urls.drop_table()
            else:
                urls.page_not_found()
        elif page == "142":
            if request == "p":
                page = urls.settings_menu()
            elif request == "1":
                table = "Tournament"
                page = urls.table_selected_drop_table(table)
            elif request == "2":
                table = "Player"
                page = urls.table_selected_drop_table(table)
            elif request == "3":
                table = "Match"
                page = urls.table_selected_drop_table(table)
            elif request == "4":
                table = "Rounds"
                page = urls.table_selected_drop_table(table)
            else:
                urls.page_not_found()


if __name__ == '__main__':
    main()
