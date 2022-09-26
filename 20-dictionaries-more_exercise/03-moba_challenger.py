command = input()

players = {}

while "Season end" not in command:
    if " -> " in command:
        entry = command.split(" -> ")
        player = entry[0]
        position = entry[1]
        skill = int(entry[2])
        if 0 <= skill <= 1000:
            if player not in players:
                players[player] = {"skills": {position:skill},
                                   'total': 0}
            else:
                if position in players[player]['skills'] and players[player]['skills'] [position] < skill:
                    players[player]['skills'][position] = skill
                else:
                    players[player]['skills'][position] = skill
    elif " vs " in command:
        battle = command.split(" vs ")
        first_player = battle[0]
        second_player = battle[1]
        if first_player in players and second_player in players:
            for key, value in players[first_player]['skills'].items():
                if key in players[second_player]['skills']:
                    first_player_total = 0
                    second_player_total = 0
                    for points in players[first_player]['skills'].values():
                        first_player_total += points
                    for points in players[second_player]['skills'].values():
                        second_player_total += points
                    if first_player_total > second_player_total:
                        players.pop(second_player)
                    elif first_player_total < second_player_total:
                        players.pop(first_player)

    command = input()

for key, value in players.items():
    total = 0
    for points in value['skills'].values():
        total += points
    players[key]['total'] = total

sorted_players = sorted(players.items(), key=lambda item: -item[1]["total"])
# print(sorted_players[1])
for x in sorted_players:
    name = x[0]
    total = x[1]["total"]
    print(f'{name}: {total} skill')
    sorted_skills = sorted(players[name]["skills"].items(), key=lambda kv: (-kv[1], kv[0]))
    for y in sorted_skills:
        print(f'- {y[0]} <::> {y[1]}')

# TODO not redy, and 2 more cases in this chapter
