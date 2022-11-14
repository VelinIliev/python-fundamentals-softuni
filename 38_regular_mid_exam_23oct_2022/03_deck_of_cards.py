deck_of_cards = input().split(", ")
number_of_lines = int(input())
# print(deck_of_cards)

for line in range(number_of_lines):
    new_line = input().split(", ")
    action = new_line[0]
    if action == "Add":
        card = new_line[1]
        if card in deck_of_cards:
            print(f'Card is already in the deck')
        else:
            deck_of_cards.append(card)
            print(f'Card successfully added')
    elif action == "Insert":
        index = int(new_line[1])
        card = new_line[2]
        if index < 0 or index > len(deck_of_cards):
            print(f'Index out of range')
        elif card in deck_of_cards:
            print(f'Card is already added')
        else:
            deck_of_cards.insert(index, card)
            print(f'Card successfully added')
    elif action == "Remove":
        card = new_line[1]
        if card in deck_of_cards:
            deck_of_cards.remove(card)
            print('Card successfully removed')
        else:
            print('Card not found')
    elif action == "Remove At":
        index = int(new_line[1])
        if index < 0 or index > len(deck_of_cards):
            print("Index out of range")
        else:
            deck_of_cards.pop(index)
            print(f'Card successfully removed')

print(", ".join(deck_of_cards))