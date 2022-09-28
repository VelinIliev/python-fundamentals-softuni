players = {}

while True:
    command = input()
    if command == "Season end":
        break
    elif len(command.split(" -> ")) > 1:
        command = command.split(" -> ")
        player = command[0]
        position = command[1]
        skill = int(command[2])
        if player not in players:
            players[player] = {'total': skill, position: skill }
        elif player in players and position not in players[player]:
            players[player]['total'] += skill
            players[player][position] = skill
        elif player in players and position in players[player]:
            if players[player][position] < skill: #
                players[player]['total'] += skill - players[player][position]
                players[player][position] = skill
    elif len(command.split(" vs ")) > 1:
        command = command.split(" vs ")
        player1 = command[0]
        player2 = command[1]
        if player1 in players and player2 in players:
            for key in players[player1].keys():
                if key in players[player2] and key != "total":
                    if players[player1]['total'] > players[player2]['total']:
                        del players[player2]
                    elif players[player2]['total'] > players[player1]['total']:
                        del players[player1]
                    break #

sorted_players = sorted(players.items(), key=lambda item: (-item[1]["total"], item[0]))

for item in sorted_players:
    player = item[0]
    values = item[1]
    sorted_values = sorted(values.items(), key=lambda kv: (-kv[1], kv[0]))
    print(f'{player}: {players[player]["total"]} skill')
    for value in sorted_values:
        position = value[0]
        skill = value[1]
        if position != "total":
            print(f'- {position} <::> {skill}')