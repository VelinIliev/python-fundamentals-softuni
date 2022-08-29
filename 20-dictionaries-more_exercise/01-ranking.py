contests = {}
while True:
    command = input()
    if command == "end of contests":
        break
    else:
        entry = command.split(":")
        if ':' in entry[0] or "=" in entry[0] or ">" in entry[0]:
            continue
        elif ':' in entry[1] or "=" in entry[1] or ">" in entry[1]:
            continue
        else:
            contest = entry[0]
            password = entry[1]
            contests[contest] = password

candidates = {}
while True:
    command = input()
    if command == "end of submissions":
        break
    else:
        entry = command.split("=>")
        if ':' in entry[0] or "=" in entry[0] or ">" in entry[0]:
            continue
        elif ':' in entry[1] or "=" in entry[1] or ">" in entry[1]:
            continue
        elif ':' in entry[2] or "=" in entry[2] or ">" in entry[2]:
            continue
        elif 10000 < int(entry[3]) < 0:
            continue
        else:
            contest = entry[0]
            password = entry[1]
            username = entry[2]
            points = int(entry[3])
            if contest in contests:
                if password == contests[contest]:
                    if username in candidates:
                        if contest in candidates[username]:
                            if candidates[username][contest] < points:
                                candidates[username][contest] = points
                        else:
                            candidates[username][contest] = points
                    else:
                        candidates[username] = {contest: points}
ranking = {}

for key, value in candidates.items():
    name = key
    total_points = 0
    for key1, value1 in value.items():
        total_points += value1
    ranking[name] = total_points

sorted_ranking = sorted(ranking.items(), key=lambda kv: kv[1])

winner_name = max(sorted_ranking)[0]
winner_points = max(sorted_ranking)[1]
print(f'Best candidate is {winner_name} with total {winner_points} points.')
print("Ranking:")

sorted_names = sorted(candidates)

for name in sorted_names:
    print(name)
    sorted_courses = sorted(candidates[name].items(), key=lambda kv: kv[1], reverse=True)
    for course in sorted_courses:
        print(f'#  {course[0]} -> {course[1]}')

# TODO: not ready
