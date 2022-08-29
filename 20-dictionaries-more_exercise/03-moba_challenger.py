command = input()

players = {}

while " -> " in command:
    entry = command.split(" -> ")
    player = entry[0]
    position = entry[1]
    skill = int(entry[2])
    if player not in players:
        players[player] = {position: skill}
    else:
        if position in players[player] and players[player][position] < skill:
            players[player][position] = skill
        else:
            players[player][position] = skill


    command = input()

print(players)