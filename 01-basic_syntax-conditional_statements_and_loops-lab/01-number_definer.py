number = float(input())

printing_phrase = ""

if number == 0:
    printing_phrase = "zero"
elif abs(number) < 1:
    printing_phrase = "small "
elif abs(number) > 1000000:
    printing_phrase = "large "

if number > 0:
    printing_phrase += "positive"
elif number < 0:
    printing_phrase += "negative"

print(printing_phrase)