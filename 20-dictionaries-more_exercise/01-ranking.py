contests = {}
while True:
    command = input()
    if command == "end of contests":
        break
    else:
        entry = command.split(":")
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
# print(contests)
ranking = {}
for key, value in candidates.items():
    name = key
    total_points = 0
    for key1, value1 in value.items():
        total_points += value1
    ranking[name] = total_points

sorted_ranking = sorted(ranking.items(), key=lambda kv: kv[1])
# print(ranking)
winner_name = max(sorted_ranking)[0]
winner_points = max(sorted_ranking)[1]
print(f'Best candidate is {winner_name} with total {winner_points} points.')
print("Ranking:")

sorted_names = sorted(candidates)


for name in sorted_names:
    print(name)
    # print(candidates[name])
    sorted_courses = sorted(candidates[name].items(), key=lambda kv: kv[1], reverse=True)
    # print(sorted_courses[0])
    for course in sorted_courses:
        print(f'#  {course[0]} -> {course[1]}')



# TODO: add Constraints
