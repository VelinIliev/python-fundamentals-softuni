
phonebook = {}
query = 0

while True:
    command = input().split("-")

    if len(command) > 1:
        name = command[0]
        phone = command[1]
        phonebook[name] = phone
    else:
        query = int(command[0])
        break

for i in range(query):
    query_name = input()
    if query_name in phonebook:
        print(f'{query_name} -> {phonebook[query_name]}')
    else:
        print(f'Contact {query_name} does not exist.')