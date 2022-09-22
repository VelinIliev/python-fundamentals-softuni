import re

pattern_name = r'%([A-Z][a-z]+)%'
pattern_product = r'<([\S]+)>'
pattern_quantity = r'\|([0-9]+)\|'
pattern_price = r'([0-9]+\.?[0-9]+)\$'
# pattern = r'([\S]+)?%([A-Z][a-z]+)%<([\S]+)>([\S]+)?\|([0-9]+)\|([\S]+)?([0-9]+\.?[0-9]+)\$'
grand_total = 0

command = input()
while command != "end of shift":
    text = command
    matches = []

    matches_name = re.findall(pattern_name, text)
    matches_product = re.findall(pattern_product, text)
    matches_quantity = re.findall(pattern_quantity, text)
    matches_price = re.findall(pattern_price, text)

    if len(matches_name) > 0:
        matches.append(matches_name[0])
    if len(matches_product) > 0:
        matches.append(matches_product[0])
    if len(matches_quantity) > 0:
        matches.append(matches_quantity[0])
    if len(matches_price) > 0:
        matches.append(matches_price[0])

    if len(matches) == 4:
        name = matches[0]
        product = matches[1]
        quantity = int(matches[2])
        price = float(matches[3])
        total = quantity * price
        print(f'{name}: {product} - {total:.2f}')
        grand_total += total

    command = input()

print(f'Total income: {grand_total:.2f}')

# TODO 90/100
