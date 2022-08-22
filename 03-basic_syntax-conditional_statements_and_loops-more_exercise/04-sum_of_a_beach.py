string = input()

new_string = string.lower()
counter = 0

if "water" in new_string:
    counter += new_string.count('water')
if "fish" in new_string:
    counter += new_string.count('fish')
if "sand" in new_string:
    counter += new_string.count('sand')
if "sun" in new_string:
    counter += new_string.count('sun')

print(counter)