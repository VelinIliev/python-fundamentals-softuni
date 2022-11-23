number_of_pieces = int(input())

pieces = {}

for _ in range(number_of_pieces):
    piece = input().split("|")
    name = piece[0]
    composer = piece[1]
    key = piece[2]
    if name not in pieces:
        pieces[name] = {"composer": composer, "key": key}

while True:
    command = input()
    if command == "Stop":
        break
    command = command.split("|")
    action = command[0]
    piece = command[1]
    if action == "Add":
        composer = command[2]
        key = command[3]
        if piece in pieces:
            print(f'{piece} is already in the collection!')
        else:
            pieces[piece] = {"composer": composer, "key": key}
            print(f"{piece} by {composer} in {key} added to the collection!")
    elif action == "Remove":
        if piece not in pieces:
            print(f'Invalid operation! {piece} does not exist in the collection.')
        else:
            del pieces[piece]
            print(f'Successfully removed {piece}!')
    elif action == "ChangeKey":
        new_key = command[2]
        if piece not in pieces:
            print(f'Invalid operation! {piece} does not exist in the collection.')
        else:
            pieces[piece]["key"] = new_key
            print(f'Changed the key of {piece} to {new_key}!')

for piece, values in pieces.items():
    print(f'{piece} -> Composer: {values["composer"]}, Key: {values["key"]}')