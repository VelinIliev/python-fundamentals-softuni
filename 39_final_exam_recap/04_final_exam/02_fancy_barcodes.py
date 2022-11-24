import re

number_of_lines = int(input())
pattern = r'@#+([A-Z][a-zA-Z0-9]{4,}[A-Z])@#+'

for line in range(number_of_lines):
    barcode = input()
    match = re.findall(pattern, barcode)
    if match:
        number = [x for x in match[0] if x.isdigit()]
        if number:
            print(f'Product group: {"".join(number)}')
        else:
            print('Product group: 00')
    else:
        print('Invalid barcode')
