number_of_lines = int(input())

start_search = False

container = []

for _ in range(number_of_lines):
    line = input()
    if line == "(" and start_search is True:
        container.append("UNBALANCED")
    elif line == "(" and start_search is False:
        start_search = True
    if line == ")" and start_search is True:
        start_search = False
    elif line == ")" and start_search is False:
        container.append("UNBALANCED")

if "UNBALANCED" in container:
    print("UNBALANCED")
else:
    print("BALANCED")
