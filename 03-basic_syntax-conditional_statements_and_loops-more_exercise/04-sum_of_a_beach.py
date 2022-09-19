string = input().lower()

counter = 0
words = ["water", "fish", "sand", "sun"]

for word in words:
    counter += string.count(word)

print(counter)