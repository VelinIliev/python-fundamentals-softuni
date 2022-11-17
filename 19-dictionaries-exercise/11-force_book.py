users = {}

while True:
    command = input()
    if command == "Lumpawaroo":
        break
    elif " | " in command:
        command = command.split(" | ")
        force_side = command[0]
        force_user = command[1]

        existing_user = False
        for value in users.values():
            if force_user in value:
                existing_user = True

        if force_side not in users and not existing_user:
            users[force_side] = [force_user]
        elif force_side in users and not existing_user:
            users[force_side].append(force_user)
    elif "->" in command:
        command = command.split(" -> ")
        force_user = command[0]
        force_side = command[1]

        existing_user = False
        for value in users.values():
            if force_user in value:
                existing_user = True

        if not existing_user and force_side not in users:
            users[force_side] = [force_user]
        elif not existing_user and force_side in users:
            users[force_side].append(force_user)
        elif existing_user:
            for key, value in users.items():
                if force_user in value:
                    value.remove(force_user)
            if force_side in users:
                users[force_side].append(force_user)
            else:
                users[force_side] = [force_user]
        print(f'{force_user} joins the {force_side} side!')

for key, value in users.items():
    if len(value) > 0:
        print(f'Side: {key}, Members: {len(value)}')
        for user in value:
            print(f'! {user}')
