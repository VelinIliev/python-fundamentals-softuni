number_of_pieces = int(input())

pieces = {}

for piece in range(number_of_pieces):
    entry = input().split("|")
    piece_name = entry[0]
    composer = entry[1]
    key = entry[2]
    # print(composer, piece, key)
    pieces[piece_name] = {'composer':composer, "key": key}

while True:
    command = input()
    if command == "Stop":
        break
    else:
        command = command.split("|")

    if command[0] == "Add":
        piece = command[1]
        composer = command[2]
        key = command[3]
        if piece not in pieces:
            print(f'{piece} by {composer} in {key} added to the collection!')
            pieces[piece] = {'composer':composer, "key": key}
        else:
            print(f'{piece} is already in the collection!')
    elif command[0] == "Remove":
        piece_to_remove = command[1]
        if piece_to_remove in pieces:
            del pieces[piece_to_remove]
            print(f'Successfully removed {piece_to_remove}!')
        else:
            print(f'Invalid operation! {piece_to_remove} does not exist in the collection.')
    elif command[0] == "ChangeKey":
        piece = command[1]
        new_key = command[2]
        if piece in pieces:
            pieces[piece]['key'] = new_key
            print(f'Changed the key of {piece} to {new_key}!')
        else:
            print(f'Invalid operation! {piece} does not exist in the collection.')

for k,v in pieces.items():
    piece = k
    composer = v["composer"]
    key = v["key"]
    print(f'{piece} -> Composer: {composer}, Key: {key}')