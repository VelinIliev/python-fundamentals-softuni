import re
destinations = input()

pattern = r'(=|\/)([A-Z]{1}[a-zA-Z]{2,})(=|\/)'

matches = re.findall(pattern, destinations)

valid_destinations = []
for match in matches:
    if len(set(match)) == 2:
        valid_destinations.append(match[1])

points = 0
for destination in valid_destinations:
    points += len(destination)

print(f'Destinations: {", ".join(valid_destinations)}')
print(f'Travel Points: {points}')