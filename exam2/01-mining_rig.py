from math import ceil

video_card_price = int(input())
transition_price = int(input())
electricity_by_card_per_day = float(input())
earning_by_card_per_day = float(input())

total_video_cars = video_card_price * 13
total_transitions = transition_price * 13
others = 1000

total = total_video_cars + total_transitions + others

profit_per_day = earning_by_card_per_day - electricity_by_card_per_day

days_to_return_investment = ceil(total / (profit_per_day * 13))

print(total)
print(days_to_return_investment)