# On the 1st line, you will receive the days of the plunder –
# an integer number in the range [0…100000]
days_of_plunder = int(input())
# •	On the 2nd line, you will receive the daily plunder –
# an integer number in the range [0…50]
daily_plunder = int(input())
# •	On the 3rd line, you will receive the expected plunder –
# a real number in the range [0.0…10000.0]
expected_plunder = float(input())

# Create a program that checks if target plunder is reached.
# First, you will receive how many days the pirating lasts.
# Then you will receive how much the pirates plunder for a day.
# Last you will receive the expected plunder at the end.
# Calculate how much plunder the pirates manage to gather.
total_plunder = 0
for day in range(1, days_of_plunder + 1):
    # Each day they gather the plunder.
    total_plunder += daily_plunder
    # Keep in mind that they attack more ships every
    # third day and add additional plunder to their total gain,
    # which is 50% of the daily plunder.
    if day % 3 == 0:
        total_plunder += daily_plunder / 2
    # Every fifth day the pirates encounter a warship, and after the battle,
    # they lose 30% of their total plunder.
    if day % 5 == 0:
        total_plunder = total_plunder * .7

# If the gained plunder is more or equal to the target, print the following:
# "Ahoy! {totalPlunder} plunder gained."
if total_plunder >= expected_plunder:
    print(f'Ahoy! {total_plunder:.2f} plunder gained.')
# If the gained plunder is less than the target.
# Calculate the percentage left and print the following:
# "Collected only {percentage}% of the plunder."
else:
    percentage = total_plunder / expected_plunder * 100
    print(f'Collected only {percentage:.2f}% of the plunder.')