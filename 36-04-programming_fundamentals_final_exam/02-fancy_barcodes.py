import re
number_of_lines = int(input())

pattern = r'[@][#]+([A-Z][a-zA-Z0-9]{4,}[A-Z])[@][#]+'

for line in range(number_of_lines):
    barcode = input()
    matches = re.findall(pattern, barcode)
    if len(matches) == 0:
        print("Invalid barcode")
    else:
        product_group = ''
        for char in matches[0]:
            if char.isdigit():
                product_group += char

        if len(product_group) == 0:
            print('Product group: 00')
        else:
            print(f'Product group: {product_group}')