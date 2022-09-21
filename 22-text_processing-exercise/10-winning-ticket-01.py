import re
tickets = input()
tickets = ''.join(tickets.split())
tickets = tickets.split(",")

if len(tickets) <= 100:
    winning_symbols = ["@", "#", "$", "^"]
    for ticket in tickets:
        if len(ticket) == 20:
            left_side = ticket[:10]
            right_side = ticket[10::]
            left_winning_symbol = ""
            right_winning_symbol = " "
            for winning_symbol in winning_symbols:
                if winning_symbol in left_side:
                    left_winning_symbol = winning_symbol
                if winning_symbol in right_side:
                    right_winning_symbol = winning_symbol
            if left_winning_symbol == right_winning_symbol:
                pattern = '[@|#|$|^]{6,}'
                left_matches = re.findall(pattern, left_side)
                right_matches = re.findall(pattern, right_side)
                if len(left_matches[0]) == 10 and len(right_matches[0]) == 10:
                    print(f'ticket "{ticket}" - {len(left_matches[0])}{left_winning_symbol} Jackpot!')
                elif len(left_matches) >= len(right_matches):
                    print(f'ticket "{ticket}" - {len(right_matches[0])}{left_winning_symbol}')
                elif len(left_matches) < len(right_matches):
                    print(f'ticket "{ticket}" - {len(left_matches[0])}{left_winning_symbol}')
            else:
                print(f'ticket "{ticket}" - no match')
        else:
            print("invalid ticket")