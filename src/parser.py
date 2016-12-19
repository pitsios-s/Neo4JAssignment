import re

# A dictionary keeping all the unique players
players = {}

# An integer variable that keeps the number of all unique players
num_of_players = 0

# A dictionary keeping all the unique events
events = {}

# An integer variable that keeps the number of all unique events
num_of_events = 0

# A dictionary keeping all the unique games
games = {}

# An integer variable that keeps the number of all unique games
num_of_games = 0

# A dictionary keeping all the unique moves
moves = {}

# An integer variable that keeps the number of all unique moves
num_of_moves = 0

if __name__ == '__main__':
    with open('../res/chessData.txt', 'r') as in_file:

        # A boolean flag variable that indicates if we have found a game "tag"
        game_found = False

        # An integer flag indicating which attribute we are parsing
        attribute_number = 0

        for line in in_file:

            if line.strip() == '':
                continue

            if re.match(r'([=]+)', line):
                if game_found:
                    game_found = False
                    games[game_number] = (game_number, game_date, game_result, game_eco, game_opening, game_half_moves, game_moves, game_white_elo, game_black_elo, game_round, num_of_events - 1, first_move)
                else:
                    game_found = True
                    attribute_number = 0
                    first_move = None

            if game_found:

                if attribute_number == 0:
                    attribute_number += 1
                    continue

                elif attribute_number == 1:
                    parts = line.strip().split(":")
                    player_name_1 = parts[1].lower().replace(" ", "")
                    player_color_1 = parts[0].lower().strip()

                    if player_name_1 not in players:
                        players[player_name_1] = (parts[1].strip(), num_of_players)
                        num_of_players += 1

                    attribute_number += 1

                elif attribute_number == 2:
                    parts = line.strip().split(":")
                    player_name_2 = parts[1].lower().replace(" ", "")
                    player_color_2 = parts[0].lower().strip()

                    if player_name_2 not in players:
                        players[player_name_2] = (parts[1].strip(), num_of_players)
                        num_of_players += 1

                    attribute_number += 1

                elif attribute_number == 3:
                    parts = line.strip().split(":")
                    game_date = parts[1].strip()
                    attribute_number += 1

                elif attribute_number == 4:
                    parts = line.strip().split(":")
                    game_half_moves = parts[1].strip()
                    attribute_number += 1

                elif attribute_number == 5:
                    parts = line.strip().split(":")
                    game_moves = parts[1].strip()
                    attribute_number += 1

                elif attribute_number == 6:
                    parts = line.strip().split(":")
                    game_result = parts[1].strip()
                    attribute_number += 1

                elif attribute_number == 7:
                    parts = line.strip().split(":")
                    game_white_elo = parts[1].strip()
                    attribute_number += 1

                elif attribute_number == 8:
                    parts = line.strip().split(":")
                    game_black_elo = parts[1].strip()
                    attribute_number += 1

                elif attribute_number == 9:
                    parts = line.strip().split(":")
                    game_number = parts[1].strip()
                    attribute_number += 1

                elif attribute_number == 10:
                    parts = line.strip().split(":")
                    event_key = parts[1].lower().replace(" ", "")
                    event_name = parts[1].strip()
                    attribute_number += 1

                elif attribute_number == 11:
                    parts = line.strip().split(":")
                    event_site = parts[1].strip()
                    attribute_number += 1

                elif attribute_number == 12:
                    parts = line.strip().split(":")
                    event_date = parts[1].strip()

                    if event_key not in events:
                        events[event_key] = (num_of_events, event_name, event_site, event_date)
                        num_of_events += 1
                    attribute_number += 1

                elif attribute_number == 13:
                    parts = line.strip().split(":")
                    game_round = parts[1].strip()
                    attribute_number += 1

                elif attribute_number == 14:
                    parts = line.strip().split(":")
                    game_eco = parts[1].strip()
                    attribute_number += 1

                elif attribute_number == 15:
                    parts = line.strip().split(":")
                    game_opening = parts[1].strip()
                    attribute_number += 1

                elif attribute_number == 16:
                    attribute_number += 1

                elif attribute_number == 17:
                    parts = line.split(",")
                    move_number = parts[0].split(':')[1].strip()
                    move_side = parts[1].split(':')[1].strip()
                    move_move = parts[2].split(':')[1].strip()
                    move_fen = parts[3].split(':')[1].strip()
                    moves[num_of_moves] = (num_of_moves, move_number, move_side, move_move, move_fen)

                    if first_move is None:
                        first_move = num_of_moves

                    num_of_moves += 1

    print(len(players))
    print(players)

    print(len(events))
    print(events)

    print(len(games))

    print(len(moves))

    print(games['1'])
    print(games['2'])
    print(games['3'])
