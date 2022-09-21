tickets = input().split(", ")

winning_symbols = ["@", "#", "$", "^"]

for ticket in tickets:
    ticket = ticket.replace(" ", "")
    winning_ticket = False
    jackpot_found = False
    winning_symbol = ""
    max_count = 6

    if len(ticket) == 20:
        first_half = ticket[:10]
        second_half = ticket[10:]
        for symbol in winning_symbols:
            if symbol * 10 in first_half and symbol * 10 in second_half:
                jackpot_found = True
                winning_symbol = symbol
            elif symbol * 6 in first_half and symbol * 6 in second_half:
                winning_ticket = True
                winning_symbol = symbol
                for i in range(7, 10):
                    if symbol * i in first_half and symbol * i in second_half:
                        max_count = i

        if winning_ticket:
            print(f'ticket "{ticket}" - {max_count}{winning_symbol}')
        elif jackpot_found:
            print(f'ticket "{ticket}" - 10{winning_symbol} Jackpot!')
        else:
            print(f'ticket "{ticket}" - no match')
    else:
        print("invalid ticket")