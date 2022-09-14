contests = {}
users = {}
while True:
    command = input()
    if command == "end of contests":
        break
    else:
        command = command.split(":")
        contest = command[0]
        password = command[1]
        if ":" in contest or "=" in contest or ">" in contest:
            pass
        elif ":" in password or "=" in password or ">" in password:
            pass
        else:
            contests[contest] = password

while True:
    command = input()
    if command == "end of submissions":
        break
    else:
        command = command.split("=>")
        if ":" in command or "=" in command or ">" in command:
            pass
        else:
            contest = command[0]
            password = command[1]
            username = command[2]
            points = int(command[3])
            if 0 > points > 10000:
                pass
            else:
                if contest in contests and password == contests.get(contest):
                    if username not in users:
                        users[username] = {}
                    if contest in users[username]:
                        if users[username][contest] < points:
                            users[username][contest] = points
                    elif contest not in users[username]:
                        users[username][contest] = points

max_points = 0
max_user = ""
for name, courses in users.items():
    total_points = 0
    for points in courses.values():
        points = points
        total_points += points
    if total_points > max_points:
        max_points = total_points
        max_user = name



print(f'Best candidate is {max_user} with total {max_points} points.')
print("Ranking:")
for key, value in sorted(users.items()):
    print(key)
    sorted_values = sorted(value.items(), key=lambda kv: kv[1], reverse=True)
    for x in sorted_values:
        print(f'#  {x[0]} -> {x[1]}')

