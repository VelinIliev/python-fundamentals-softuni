contests = {
    'courses': {},
    'students': {}
}

while True:
    command = input()
    if command == "no more time":
        break
    else:
        entry = command.split(' -> ')
        name = entry[0]
        contest = entry[1]
        points = int(entry[2])
        # print(name, contest, points)
        if name in contests['students'] and contest in contests['students'][name] and contests['students'][name][contest] < points:
            contests['students'][name][contest] = points
        if name not in contests['students']:
            contests['students'][name] = {}
        contests['students'][name][contest] = points
        if contest not in contests['courses']:
            contests['courses'][contest] = {name: points}
        elif contest in contests['courses'] and name in contests['courses'][contest] and contests['courses'][contest][name] < points:
            contests['courses'][contest][name] = points
        else:
            contests['courses'][contest][name] = points

for key, value in contests['courses'].items():
    participants = (len(contests['courses'][key]))
    course_name = key
    print(f'{course_name}: {participants} participants')
    course = contests['courses'][course_name]
    sorted_by_name = {}
    sorted_score = sorted(course.items(), key=lambda kv: kv[0])
    for item in sorted_score:
        name = item[0]
        score = item[1]
        sorted_by_name[name] = score
    sorted_by_score = sorted(sorted_by_name.items(), key=lambda kv: kv[1], reverse=True)
    # print(sorted_by_score)
    for num, entry in enumerate(sorted_by_score, 1):
        name = entry[0]
        points = entry[1]
        print(f'{num}. {name} <::> {points}')

individual = {}
for name, courses in contests['students'].items():
    score = 0
    for course, points in courses.items():
        score += points
    individual[name] = score
sorted_individuals = sorted(individual.items(), key=lambda kv: (kv[1], kv[0][::-1]), reverse=True)
# sorted(dic.items(),key= lambda  x: (x[1],x[0]))

print("Individual standings:")
for num, student in enumerate(sorted_individuals, 1):
    name = student[0]
    points = student[1]
    print(f'{num}. {name} -> {points}')

# TODO: not ready