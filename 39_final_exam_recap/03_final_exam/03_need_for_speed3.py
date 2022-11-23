number_of_cars = int(input())

cars = {}

for car in range(number_of_cars):
    new_car, mileage, fuel = input().split("|")
    cars[new_car] = {"mileage": int(mileage), "fuel": int(fuel)}

while True:
    command = input()
    if command == "Stop":
        break
    command = command.split(" : ")
    action = command[0]
    car = command[1]
    if action == "Drive":
        if car in cars:
            distance = int(command[2])
            fuel = int(command[3])
            if cars[car]['fuel'] >= fuel:
                cars[car]['mileage'] += distance
                cars[car]['fuel'] -= fuel
                print(f'{car} driven for {distance} kilometers. {fuel} liters of fuel consumed.')
            else:
                print(f'Not enough fuel to make that ride')
            if cars[car]['mileage'] >= 100000:
                del cars[car]
                print(f'Time to sell the {car}!')
    elif action == 'Refuel':
        fuel = int(command[2])
        if car in cars:
            if cars[car]["fuel"] + fuel > 75:
                fuel = 75 - cars[car]["fuel"]
            cars[car]["fuel"] += fuel
            print(f'{car} refueled with {fuel} liters')
    elif action == "Revert":
        kilometers = int(command[2])
        if car in cars:
            if cars[car]['mileage'] - kilometers < 10000:
                cars[car]['mileage'] = 10000
            else:
                cars[car]['mileage'] -= kilometers
                print(f'{car} mileage decreased by {kilometers} kilometers')

for car, values in cars.items():
    print(f'{car} -> Mileage: {values["mileage"]} kms, Fuel in the tank: {values["fuel"]} lt.')