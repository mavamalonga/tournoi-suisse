class Controller:

    def check_form_add_tournament(self, values):
        error_list = []
        if len(values[0]) < 2 or len(values[0]) > 16:
            name_error = "the name must contain between 2 to 16 characters."
            error_list.append(name_error)
        if len(values[1]) < 8 or len(values[1]) > 66:
            place_error = "the place value must contain between 8 to 66 characters."
            error_list.append(place_error)
        if len(values[2]) != 10:
            date_error = "the date format is incorrect."
            error_list.append(date_error)
        else:
            try:
                date = values[2].split("/")
                for nb in date:
                    try:
                        int(nb)
                    except Exception:
                        date_error = "date must only contain integers"
                        error_list.append(date_error)
            except Exception:
                date_error = "the date format is incorrect."
                error_list.append(date_error)

        try:
            int(values[3])
        except Exception:
            nb_of_turns = "nb of turns must only contain integers"
            error_list.append(nb_of_turns)

        if values[4] != "bullet" and values[4] != "blitz" and values[4] != "rapide":
            time_error = "control time must only contain following values : bullet || blitz ||rapide"
            error_list.append(time_error)

        if len(values[5]) > 234:
            description_error = "the description value must contain 234 characters."
            error_list.append(description_error)

        if len(error_list) > 0:
            return False, error_list
        else:
            return True, None

    def parse_select_of_players(self, id_selected):
        id_selected.replace(' ', '')
        id_list = id_selected.split(",")
        return id_list

    def check_selection_of_players(self, id_list):
        error_list = []
        list_verified_id = []
        if len(id_list) != 8:
            nb_selected_error = "incorrect number of player id"
            error_list.append(nb_selected_error)
        else:
            for player_id in id_list:
                try:
                    int(player_id)
                    list_verified_id.append(player_id)
                except Exception:
                    type_error = "player_id list must only contain integers."
                    error_list.append(type_error)

        if len(error_list) > 0:
            return False, error_list
        else:
            return True, None

    def check_instances_players(self, id_list, instances):
        error_list = []
        for player_id, player_instance in zip(id_list, instances):
            if player_instance is None:
                player_error = "there is no player with the following id :{0}".format(player_id)
                error_list.append(player_error)

        if len(error_list) > 0:
            return False, error_list
        else:
            return True, None

    def round_classification(self, instances, first_round=True):
        winner = []
        looser = []
        zero = []
        if first_round is True:
            instances = sorted(instances, key=lambda k: k['ranking'])
        else:
            for match in instances:
                player1, player2 = match['match']
                if int(player1[1]) > int(player2[1]):
                    winner.append(player1[0])
                    looser.append(player2[0])
                elif player1[1] == player2[1]:
                    zero.append(player1[0])
                    zero.append(player2[0])
                else:
                    winner.append(player2[0])
                    looser.append(player1[0])
            winner = sorted(winner, key=lambda k: k['ranking'])
            looser = sorted(looser, key=lambda k: k['ranking'])
            zero = sorted(zero, key=lambda k: k['ranking'])
            instances = winner + zero + looser
        return instances

    def pairing_first_round(self, instances):
        pairing_list = []
        nb_players = len(instances)
        part_one = instances[:nb_players // 2]
        part_two = instances[nb_players // 2:]
        for player1, player2 in zip(part_one, part_two):
            pairing_list.append((player1, player2))
        return pairing_list

    def check_form_add_player(self, player):
        error_list = []
        if len(player[0]) < 2 or len(player[0]) > 16:
            name_error = "the name must contain between 2 to 16 characters."
            error_list.append(name_error)

        if len(player[0]) < 2 or len(player[0]) > 16:
            firstname_error = "the firstname must contain between 2 to 16 characters."
            error_list.append(firstname_error)

        if len(player[2]) != 10:
            date_error = "the date of birth format is incorrect."
            error_list.append(date_error)
        else:
            try:
                date = player[2].split("/")
                for nb in date:
                    try:
                        int(nb)
                    except Exception:
                        date_error = "birthday must only contain integers"
                        error_list.append(date_error)
            except Exception:
                date_error = "the date of birth format is incorrect."
                error_list.append(date_error)
        if len(player[3]) != 1:
            gender_error = "the gender field takes only one character."
            error_list.append(gender_error)
        else:
            if player[3] != 'M' and player[3] != 'F':
                gender_error = "the gender field only takes the value 'M' or 'F'."
                error_list.append(gender_error)

        try:
            if int(player[4]) > 0:
                player[4] = int(player[4])
            else:
                error_ranking = "ranking this is a positive number"
                error_list.append(error_ranking)
        except Exception:
            ranking_error = "ranking must only contain integers"
            error_list.append(ranking_error)

        if len(error_list) > 0:
            return False, error_list
        else:
            return True, None

    def check_modify_ranking(self, instances, name, ranking):
        error_list = []
        try:
            ranking = int(ranking)
            ranking_int = True
        except Exception:
            ranking_int = False
            ranking_error = "ranking must only contain integers"
            error_list.append(ranking_error)

        if len(instances) != 0 and ranking_int:
            player_id = instances[0].doc_id
        else:
            name_error = f'there is no user with the name {name}'
            error_list.append(name_error)

        if len(error_list) > 0:
            return False, None, error_list
        else:
            return True, player_id, None

    def check_select_tournament(self, tournament_id):
        error_list = []
        try:
            int(tournament_id)
        except Exception:
            id_error = "tournament_id must only contain integers."
            error_list.append(id_error)
        if len(error_list) > 0:
            return False, error_list
        else:
            return True, None

    def convert_points(self, list_points):
        new_list_points = []
        error_list = []
        for pts in list_points:
            try:
                value = int(pts)
                int_validator = "True"
            except Exception:
                int_validator = "False"
                try:
                    value = float(pts)
                    float_validator = "True"
                except Exception:
                    float_validator = "False"

            if int_validator == "True" or float_validator == "True":
                new_list_points.append(value)
            else:
                error_type = "'{0}' value is incorrect, points only accept values of type int and float".format(pts)
                error_list.append(error_type)
        if len(error_list) > 0:
            return False, None, error_list
        else:
            return True, new_list_points, None

    def check_points_values(self, pts_list):
        error_list = []
        for value in pts_list:
            if value == 0 or value == 0.5 or value == 1:
                pass
            else:
                error = f"{value}' value is incorrect, points only accept the following values : 0, 0.5, 1"
                error_list.append(error)

        if len(error_list) > 0:
            return False, error_list
        else:
            return True, None

    def transform_matchs_scores_tuple(self, list_points):
        size_list = len(list_points)
        index1, index2, match = (0, 1, 0)
        new_list = []
        while match < size_list / 2:
            score1 = list_points[index1]
            score2 = list_points[index2]
            new_list.append((score1, score2))
            index1 += 2
            index2 += 2
            match += 1
        return new_list

    def check_pairings(self, dict_1, dict_2, round_list):
        for key1_name in dict_1:
            player1 = dict_1[key1_name]
            for key2_name in dict_2:
                player2 = dict_2[key2_name]
                if self.check_match_exits(player1['name'], player2['name'], round_list):
                    continue
                else:
                    return player1['name'], player2['name']

    """check if the match already exists"""
    def check_match_exits(self, player1_name, player2_name, round_list):
        for round_instance in round_list:
            for match in round_instance['matchs']:
                player1, player2 = match['match']
                if player1_name == player1[0]['name'] or player2[0]['name'] == player1_name:
                    if player2_name == player1[0]['name'] or player2[0]['name'] == player2_name:
                        return True
                    else:
                        pass
                else:
                    pass
        return False

    def check_date_tournament(self, new_date):
        error_list = []
        if len(new_date) != 10:
            date_error = "the date format is incorrect."
            error_list.append(date_error)
        else:
            try:
                date = new_date.split("/")
                for nb in date:
                    try:
                        int(nb)
                    except Exception:
                        date_error = "date must only contain integers"
                        error_list.append(date_error)
            except Exception:
                date_error = "the date format is incorrect."
                error_list.append(date_error)

        if len(error_list) > 0:
            return False, error_list
        else:
            return True, None

    def new_round_pairing_algo(self, instances_order, tournament_instance):
        dict_1 = {}
        dict_2 = {}
        pairing_list = []
        for player in instances_order:
            p = {player['name']: player}
            dict_1.update(p)
            dict_2.update(p)
        for i in range(4):
            try:
                name1, name2 = self.check_pairings(self, dict_1, dict_2, tournament_instance['rounds'])
            except Exception:
                name1, name2 = list(dict_1)[-1], list(dict_1)[-2]
            pairing_list.append((dict_1[name1], dict_2[name2]))
            del dict_1[name1]
            del dict_1[name2]
            del dict_2[name1]
            del dict_2[name2]
        return pairing_list
