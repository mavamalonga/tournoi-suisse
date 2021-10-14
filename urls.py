from model import Database
from view import View
from controller import Controller


class Urls(View, Database, Controller):

    def __init__(self):
        View.__init__(self)
        Database.__init__(self)
        Controller.__init__(self)

    def home_page(self):
        page = "1"
        View.home_page(self)
        return page

    def add_tournament(self):
        page = "1"
        data = View.form_add_tournament(self)
        validator_1, errors_1 = Controller.check_form_add_tournament(self, data)
        if validator_1 is True:
            id_list, instances = Database.select_from_player_table(self, get_id=True, get_instance=True)
            select = View.tournament_add_players(self, id_list, instances)
            select = Controller.parse_select_of_players(self, select)
            validator_2, errors_2 = Controller.check_selection_of_players(self, select)
            if validator_2:
                instances = Database.select_from_player_table(self, get_instance=True, where_id=select)
                validator_3, errors_3 = Controller.check_instances_players(self, select, instances)
                if validator_3:
                    instances = Controller.round_classification(self, instances, first_round=True)
                    pairing = Controller.pairing_first_round(self, instances)
                    matchs = []
                    for pair in pairing:
                        player1, player2 = pair
                        match_id = Database.add_match(self, player1, player2)
                        matchs.append(match_id)
                    instance = Database.select_from_match_table(self, get_instance=True, where_id=matchs)
                    round_id = Database.add_round(self, instance)
                    round_i = Database.select_from_round_table(self, get_instance=True, where_id=round_id)
                    tournament_values = (data[0], data[1], data[2], data[3], round_i[0], select, data[4], data[5])
                    Database.add_tournament(self, tournament_values)
                else:
                    View.error(self, errors_3)
            else:
                View.error(self, errors_2)
        else:
            View.error(self, errors_1)
        return page

    def add_player(self):
        add_again = "yes"
        while add_again == "yes":
            player = View.form_add_player(self)
            validator, errors = Controller.check_form_add_player(self, player)
            if validator:
                Database.add_player(self, player[0], player[1], player[2], player[3], player[4])
            else:
                View.error(self, errors)
            add_again = input(f'{" "*45}Add again ? yes/not : ')

    def reports_menu(self):
        page = "13"
        View.reports(self)
        return page

    def players_order_name(self):
        page = "131"
        players = Database.select_from_player_table(self, get_instance=True, order="name")
        View.display_list_players(self, players, page_1=True, order_by_name="name")
        return page

    def players_order_ranking(self):
        page = "131"
        players = Database.select_from_player_table(self, get_instance=True, order="ranking")
        View.display_list_players(self, players, page_1=True, order_by_name="ranking")
        return page

    def tournament_list(self):
        page = "132"
        ids, instances = Database.select_from_tournament_table(self, get_id=True, get_instance=True)
        View.display_list_tournaments(self, ids, instances)
        return page

    def tournament_menu(self, tournament_id):
        page = "132t"
        validator, errors = Controller.check_select_tournament(self, tournament_id)
        if validator:
            tournament = Database.select_from_tournament_table(self, get_instance=True, where_id=tournament_id)
            if tournament is not None:
                View.tournament_menu(self, tournament)
                return page, tournament_id, tournament
            else:
                page = "132"
                View.error(self, [f'there is no tournament with the following id {tournament_id}'])
                return page, None, None
        else:
            page = "132"
            View.error(self, errors)
            return page, None, None

    def players_from_tournament_order_name(self, data):
        page = "132t1"
        players = Database.select_from_player_table(self, get_instance=True, where_id=data['players'], order="name")
        View.display_list_players(self, players, page_1=False, order_by_name="name")
        return page

    def players_from_tournament_order_ranking(self, data):
        page = "132t1"
        players = Database.select_from_player_table(self, get_instance=True, where_id=data['players'], order="ranking")
        View.display_list_players(self, players, page_1=False, order_by_name="ranking")
        return page

    def modify_player_ranking_from_tournament(self):
        page = "132t1"
        name, ranking = View.form_modify_ranking(self)
        instances = Database.from_player_table_search_player(self, name)
        validator, player_id, errors = Controller.check_modify_ranking(self, instances, name, ranking)
        if validator:
            Database.from_player_table_update_ranking(self, ranking, [int(player_id)])
            View.notification(self, "change success !!")
        else:
            View.error(self, errors)
        return page

    def rounds_from_tournament(self, tournament_instance):
        page = "132t2"
        View.display_rounds(self, tournament_instance['rounds'])
        return page

    def enter_results_of_tournament(self, tournament_id, tournament_instance):
        """Update round score"""
        pts_list = View.display_form_results(self, tournament_instance['rounds'])
        validator_1, new_pts_list, errors_1 = Controller.convert_points(self, pts_list)
        if validator_1:
            validator_2, errors_2 = Controller.check_points_values(self, new_pts_list)
            if validator_2:
                new_pts_list = Controller.transform_matchs_scores_tuple(self, new_pts_list)
                update_matchs = Database.update_match_score(self, tournament_id, new_pts_list)
                if len(tournament_instance['rounds']) < 7:
                    instances_order = Controller.round_classification(self, update_matchs, first_round=False)
                    pairing_list = Controller.new_round_pairing_algo(self, instances_order, tournament_instance)
                    matchs = []
                    for pair in pairing_list:
                        p1, p2 = pair
                        match_id = Database.add_match(self, p1, p2)
                        matchs.append(match_id)
                    match_instances = Database.select_from_match_table(self, get_instance=True, where_id=matchs)
                    round_id = Database.add_round(self, match_instances)
                    round_instances = Database.select_from_round_table(self, get_instance=True, where_id=round_id)
                    Database.update_tournament_round(self, tournament_id, round_instances[0])
                    View.notification(self, "change success !!")
                else:
                    """the tournament has reached its maximum number of matches"""
                    pass
            else:
                View.error(self, errors_2)
        else:
            View.error(self, errors_1)

    def matchs_from_tournament(self, tournament_instance):
        page = "132t3"
        View.display_matchs(self, tournament_instance['rounds'])
        return page

    def add_new_date_tournament(self, tournament_id):
        new_date = View.add_new_date_tournament(self)
        validator, errors = Controller.check_date_tournament(self, new_date)
        if validator:
            Database.update_date_tournament(self, tournament_id, new_date)
            View.notification(self, "Add new date success !")
        else:
            View.error(self, errors)

    def settings_menu(self):
        page = "14"
        View.settings(self)
        return page

    def drop_database(self):
        to_confirm = View.confirm(self)
        if to_confirm:
            Database.drop_database(self)
            View.notification(self, "drop database successful !")
        else:
            View.notification(self, "drop database canceled.")

    def drop_table(self):
        page = View.drop_table(self)
        return page

    def table_selected_drop_table(self, table):
        Database.drop_table(self, table)
        print_table = f'drop table {table} successful !'
        View.notification(self, print_table)
        page = self.page_14()
        return page

    def page_not_found(self):
        View.page_404(self)
        return None
