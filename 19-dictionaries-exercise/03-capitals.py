country_names = input().split(", ")
capital_cities = input().split(", ")

capitals = {}

for i in range(len(country_names)):
    capitals[country_names[i]] = capital_cities[i]

for key, value in capitals.items():
    print(f'{key} -> {value}')