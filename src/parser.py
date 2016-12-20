import re
import csv

# A dictionary keeping all the unique players
players = {}

# An integer variable used for a unique id for the players
num_of_players = 1

# A dictionary keeping all the unique events
events = {}

# An integer variable used for a unique id for the events
num_of_events = 1

# A dictionary keeping all the unique games
games = {}

# A dictionary keeping all the unique moves
moves = {}

# An integer variable used for a unique id for the moves
num_of_moves = 1

# A list that will contain tuples of the format (playerId, gameId, playerColor) that keeps the information for each
# player that participates in a specific game.
players_to_games = []

# A list that will contain tuples of the format (moveId, nextMoveId) that keeps sequence of the moves
moves_to_moves = []


def save_players_to_csv():
    with open('../csv/players.csv', 'w+') as out_file:
        csv_writer = csv.writer(out_file, delimiter=',', lineterminator='\n')
        csv_writer.writerow(['id', 'name'])

        for item in players.values():
            csv_writer.writerow([item[1], item[0]])


def save_events_to_csv():
    with open('../csv/events.csv', 'w+') as out_file:
        csv_writer = csv.writer(out_file, delimiter=',', lineterminator='\n')
        csv_writer.writerow(['id', 'name', 'site', 'date'])

        for item in events.values():
            csv_writer.writerow([item[0], item[1], item[2], item[3]])


def save_moves_to_csv():
    with open('../csv/moves.csv', 'w+') as out_file:
        csv_writer = csv.writer(out_file, delimiter=',', lineterminator='\n')
        csv_writer.writerow(['id', 'number', 'side', 'move', 'fen'])

        for item in moves.values():
            csv_writer.writerow([item[0], item[1], item[2], item[3], item[4]])


def save_games_to_csv():
    with open('../csv/games.csv', 'w+') as out_file:
        csv_writer = csv.writer(out_file, delimiter=',', lineterminator='\n')
        csv_writer.writerow(['id', 'date', 'result', 'eco', 'opening', 'halfMoves', 'moves', 'whiteELO', 'blackELO',
                             'round', 'eventID', 'firstMoveID'])

        for item in games.values():
            csv_writer.writerow([item[0], item[1], item[2], item[3], item[4], item[5], item[6], item[7], item[8],
                                 item[9], item[10], item[11]])


def save_players_to_games_to_csv():
    with open('../csv/playersGames.csv', 'w+') as out_file:
        csv_writer = csv.writer(out_file, delimiter=',', lineterminator='\n')
        csv_writer.writerow(['playerID', 'gameID', 'color'])

        for item in players_to_games:
            csv_writer.writerow([item[0], item[1], item[2]])


def save_move_to_move_to_csv():
    with open('../csv/moveMove.csv', 'w+') as out_file:
        csv_writer = csv.writer(out_file, delimiter=',', lineterminator='\n')
        csv_writer.writerow(['moveId', 'nextMoveId'])

        for item in moves_to_moves:
            csv_writer.writerow([item[0], item[1]])


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
                    players_to_games.append((player1_id, game_number, player_color_1))
                    players_to_games.append((player2_id, game_number, player_color_2))
                else:
                    game_found = True
                    attribute_number = 0
                    first_move = None
                    prev_move = None

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
                        player1_id = num_of_players
                        num_of_players += 1
                    else:
                        player1_id = players[player_name_1][1]

                    attribute_number += 1

                elif attribute_number == 2:
                    parts = line.strip().split(":")
                    player_name_2 = parts[1].lower().replace(" ", "")
                    player_color_2 = parts[0].lower().strip()

                    if player_name_2 not in players:
                        players[player_name_2] = (parts[1].strip(), num_of_players)
                        player2_id = num_of_players
                        num_of_players += 1
                    else:
                        player2_id = players[player_name_2][1]

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
                    game_result = parts[1].strip().lower()
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

                    if prev_move is None:
                        prev_move = num_of_moves
                    else:
                        moves_to_moves.append((prev_move, num_of_moves))
                        prev_move = num_of_moves

                    num_of_moves += 1

    print(len(players))

    print(len(events))

    print(len(games))

    print(len(moves))

    print(len(players_to_games))

    print(len(moves_to_moves))

    save_players_to_csv()
    save_events_to_csv()
    save_moves_to_csv()
    save_games_to_csv()
    save_players_to_games_to_csv()
    save_move_to_move_to_csv()
