schedule_of_lessons = input()
schedule_of_lessons = schedule_of_lessons.split(", ")

while True:
    command = input()
    if command == "course start":
        break
    else:
        command = command.split(":")

    if command[0] == "Add":
        lesson_title = command[1]
        if lesson_title not in schedule_of_lessons:
            schedule_of_lessons.append(lesson_title)

    elif command[0] == "Insert":
        lesson_title = command[1]
        index = int(command[2])
        if len(schedule_of_lessons) - 1 >= index >= 0:
            if lesson_title not in schedule_of_lessons:
                schedule_of_lessons.insert(index, lesson_title)

    elif command[0] == "Remove":
        lesson_title = command[1]
        if lesson_title in schedule_of_lessons:
            schedule_of_lessons.remove(lesson_title)

    elif command[0] == "Swap":
        lesson_title1 = command[1]
        lesson_title2 = command[2]

        if lesson_title1 in schedule_of_lessons and lesson_title2 in schedule_of_lessons:

            index1 = schedule_of_lessons.index(lesson_title1)
            index2 = schedule_of_lessons.index(lesson_title2)

            schedule_of_lessons[index1] = lesson_title2
            schedule_of_lessons[index2] = lesson_title1

            lesson_exercise1 = f'{lesson_title1}-Exercise'
            lesson_exercise2 = f'{lesson_title2}-Exercise'

            if lesson_exercise1 in schedule_of_lessons:
                schedule_of_lessons.insert(index2 + 1, schedule_of_lessons.pop(index1 + 1))
            if lesson_exercise2 in schedule_of_lessons:
                schedule_of_lessons.insert(index1 + 1, schedule_of_lessons.pop(index2 + 1))

    elif command[0] == "Exercise":
        lesson_title = command[1]
        lesson_exercise = f'{lesson_title}-Exercise'

        if lesson_title in schedule_of_lessons and lesson_exercise not in schedule_of_lessons:
            index = schedule_of_lessons.index(lesson_title) + 1
            schedule_of_lessons.insert(index, lesson_exercise)
        elif lesson_title not in schedule_of_lessons:
            schedule_of_lessons.append(lesson_title)
            schedule_of_lessons.append(lesson_exercise)

for n, lesson in enumerate(schedule_of_lessons, start=1):
    print(f'{n}.{lesson}')
