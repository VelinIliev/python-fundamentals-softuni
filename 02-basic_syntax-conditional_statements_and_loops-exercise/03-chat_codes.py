number_of_messages = int(input())

for i in range(number_of_messages):
    message = int(input())
    if message == 88:
        print('Hello')
    elif message == 86:
        print('How are you?')
    elif message < 88 and message != 86:
        print('GREAT!')
    elif message > 88:
        print('Bye.')