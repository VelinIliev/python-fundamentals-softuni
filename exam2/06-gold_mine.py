number_of_locations = int(input())

for location in range(number_of_locations):
    expected_yield = float(input())
    number_of_days = int(input())
    total_mined_gold = 0
    for day in range(number_of_days):
        mined_gold_per_day = float(input())
        total_mined_gold += mined_gold_per_day

    average_mined_gold = total_mined_gold / number_of_days

    if average_mined_gold >= expected_yield:
        print(f'Good job! Average gold per day: {average_mined_gold:.2f}.')
    else:
        difference = expected_yield - average_mined_gold
        print(f'You need {difference:.2f} gold.')