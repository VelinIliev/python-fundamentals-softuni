string =input()
vowels = ["a", "o", "u", "e", "i"]

new_string = [chr for chr in string if chr.lower() not in vowels]
new_string = "".join(new_string)

print(new_string)