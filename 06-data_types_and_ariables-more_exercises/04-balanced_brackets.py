number_of_lines = int(input())

start_search = False

is_unbalanced = False

for _ in range(number_of_lines):
    line = input()
    if line == "(" and start_search is True:
        is_unbalanced = True
    elif line == "(" and start_search is False:
        start_search = True
    if line == ")" and start_search is True:
        start_search = False
    elif line == ")" and start_search is False:
        is_unbalanced = True

if is_unbalanced:
    print("UNBALANCED")
else:
    print("BALANCED")
