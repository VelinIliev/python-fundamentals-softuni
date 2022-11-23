import re

places = input()
pattern = r'(=|\/)([A-Z][A-Za-z]{2,})\1'
matches = re.findall(pattern, places)
travel_points = 0
destinations = []

for x in matches:
    place = x[1]
    travel_points += len(place)
    destinations.append(place)

print(f"Destinations: {', '.join(destinations)}")
print(f'Travel Points: {travel_points}')