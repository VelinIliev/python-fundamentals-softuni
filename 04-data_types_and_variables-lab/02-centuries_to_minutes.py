centuries = int(input())

# minutes = int(centuries * 100 * 365.2422) * 24 * 60

years = centuries * 100
days = int(years * 365.2422)
hours = days * 24
minutes = hours * 60


print(f'{centuries} centuries = {years} years = {days} days = {hours} hours = {minutes} minutes')
