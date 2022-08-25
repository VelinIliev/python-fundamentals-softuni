words = input()
words = words.split(" ")

even_length_words = [word for word in words if len(word) % 2 == 0]

for word in even_length_words:
    print(word)