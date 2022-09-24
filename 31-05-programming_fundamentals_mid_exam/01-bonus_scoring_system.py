from math import ceil

number_of_students = int(input())
number_of_lectures = int(input())
additional_bonus = int(input())

max_bonus = 0
attendances_max = 0

for student in range(number_of_students):
    attendances = int(input())
    total_bonus = attendances / number_of_lectures * (5 + additional_bonus)
    if attendances >= attendances_max:
        max_bonus = ceil(total_bonus)
        attendances_max = attendances

print(f'Max Bonus: {max_bonus}.')
print(f'The student has attended {attendances_max} lectures.')