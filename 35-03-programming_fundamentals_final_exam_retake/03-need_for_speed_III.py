number_of_cars = int(input())
cars = {}
for car in range(number_of_cars):
    entry = input().split("|")
    car_model = entry[0]
    mileage = int(entry[1])
    fuel_available = int(entry[2])
    # print(car_model, mileage,fuel_available)
    cars[car_model] = {"mileage": mileage, "fuel": fuel_available}

while True:
    command = input()
    if command == "Stop":
        break
    else:
        command = command.split(" : ")
        action = command[0]
    if action == "Drive":
        car = command[1]
        distance = int(command[2])
        fuel_needed = int(command[3])
        if car in cars:
            fuel_in_car = cars[car]['fuel']
            if fuel_in_car - fuel_needed >= 0:
                cars[car]["mileage"] += distance
                cars[car]["fuel"] -= fuel_needed
                print(f'{car} driven for {distance} kilometers. {fuel_needed} liters of fuel consumed.')
            else:
                print('Not enough fuel to make that ride')
            cars_to_delete = []
            for car, values in cars.items():
                if values['mileage'] >= 100000:
                    print(f"Time to sell the {car}!")
                    cars_to_delete.append(car)
            for car in cars_to_delete:
                del cars[car]
    elif action == "Refuel":
        car = command[1]
        fuel = int(command[2])
        if car in cars:
            if cars[car]['fuel'] + fuel > 75:
                fuel = 75 - cars[car]['fuel']
                cars[car]['fuel'] = 75
                print(f'{car} refueled with {fuel} liters')
            else:
                cars[car]['fuel'] += fuel
                print(f'{car} refueled with {fuel} liters')
    elif action == "Revert":
        car = command[1]
        amount_reverted = int(command[2])
        if car in cars:
            if cars[car]['mileage'] - amount_reverted < 10000:
                cars[car]['mileage'] = 10000
            else:
                cars[car]['mileage'] -= amount_reverted
                print(f'{car} mileage decreased by {amount_reverted} kilometers')
        # print(car,amount_reverted)

for car, values in cars.items():
    # print(car, values['mileage'])
    print(f'{car} -> Mileage: {values["mileage"]} kms, Fuel in the tank: {values["fuel"]} lt.')