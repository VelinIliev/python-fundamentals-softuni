# 90/100
# see 10-winning_ticket-03.py

tickets = input().split(", ")

winning_symbols = ["@", "#", "$", "^"]


def find_max_uninterrupted_symbols(current_ticket):
    symbols = []
    start_count = False
    max_score = 0
    current_score = 0
    winning_symbol = ""
    for n, char in enumerate(current_ticket, 1):
        if char in winning_symbols:
            if not start_count:
                start_count = True
            current_score += 1
            symbols.append(char)
        elif char not in winning_symbols and start_count:
            start_count = False
            if current_score > max_score:
                max_score = current_score
            current_score = 0

        if n == 10 and start_count and char in winning_symbols:
            if current_score > max_score:
                max_score = current_score

    if len(symbols) > 0:
        winning_symbol = (max(set(symbols), key=symbols.count))

    return max_score, winning_symbol


for ticket in tickets:
    ticket = ticket.replace(" ", "")
    if len(ticket) == 20:
        first_half = ticket[:10]
        second_half = ticket[10:]
        first_max = find_max_uninterrupted_symbols(first_half)[0]
        winning_symbol_left = find_max_uninterrupted_symbols(first_half)[1]
        second_max = find_max_uninterrupted_symbols(second_half)[0]
        winning_symbol_right = find_max_uninterrupted_symbols(second_half)[1]

        if first_max >= 6 and second_max >= 6:
            if first_max == 10 and second_max == 10:
                print(f'ticket "{ticket}" - {first_max}{winning_symbol_left} Jackpot!')
            elif first_max <= second_max:
                print(f'ticket "{ticket}" - {first_max}{winning_symbol_left}')
            elif first_max > second_max:
                print(f'ticket "{ticket}" - {second_max}{winning_symbol_right}')
        else:
            print(f'ticket "{ticket}" - no match')
    else:
        print(f'invalid ticket')

