contests = {}
students = {}

while True:
    command = input()
    if command == "no more time":
        break
    else:
        command = command.split(" -> ")
        username = command[0]
        contest = command[1]
        points = int(command[2])
        if 1000 < points < 0:
            pass
        else:
            if contest not in contests:
                contests[contest] = {}
            if username not in students:
                students[username] = 0

            if username not in contests[contest]:
                contests[contest][username] = points
                students[username] += points
            elif username in contests[contest] and contests[contest][username] < points:
                students[username] = students[username] - contests[contest][username] + points
                contests[contest][username] = points

for contest_name, users in contests.items():
    print(f'{contest_name}: {len(users)} participants')
    sorted_users = sorted(users.items(), key=lambda item: (-item[1], item[0]))
    for n, user in enumerate(sorted_users, 1):
        print(f'{n}. {user[0]} <::> {user[1]}')

print("Individual standings:")
sorted_students = sorted(students.items(), key=lambda item: (-item[1], item[0]))
for n, user in enumerate(sorted_students, 1):
    print(f'{n}. {user[0]} -> {user[1]}')
