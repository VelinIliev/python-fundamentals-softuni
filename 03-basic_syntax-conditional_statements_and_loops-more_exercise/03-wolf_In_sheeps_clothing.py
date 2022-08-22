search_for_wolf = input()

search_for_wolf = search_for_wolf.split(", ")

# print(search_for_wolf)

if search_for_wolf[-1] == "wolf":
    print("Please go away and stop eating my sheep")
else:
    for n, wolf in enumerate(search_for_wolf):
        if wolf == "wolf":
            ship_n = (len(search_for_wolf) - n - 1)
    print(f'Oi! Sheep number {ship_n}! You are about to be eaten by a wolf!')
