search_for_wolf = input().split(", ")

if search_for_wolf[-1] == "wolf":
    print("Please go away and stop eating my sheep")
else:
    for n, is_wolf in enumerate(search_for_wolf):
        if is_wolf == "wolf":
            ship_to_be_eaten = (len(search_for_wolf) - n - 1)
            print(f'Oi! Sheep number {ship_to_be_eaten}! You are about to be eaten by a wolf!')
            break
