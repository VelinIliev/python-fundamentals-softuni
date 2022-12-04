import re
number_of_lines = int(input())

for i in range(number_of_lines):
    password = input()
    pattern = r'([\S]+)>([0-9]{3}\|[a-z]{3}\|[A-Z]{3}\|[\W\w^<>]{3})<([\S]+)'
    matches = re.findall(pattern, password)
    if matches and matches[0][0] == matches[0][2]:
        encrypted_password = "".join(matches[0][1].split("|"))
        print(f'Password: {encrypted_password}')
    else:
        print(f'Try another password!')