class Vehicle:
    def __init__(self, type, model, price):
        type = type
        model = model
        price = price
        owner = None

    def buy(self, money: int, owner: str):
        if owner is not None:
            return "Car already sold"
        elif money >= price and owner is None:
            change = money - price
            owner = owner
            return f'Successfully bought a {type}. Change: {change:.2f}'
        elif money < price:
            return f'Sorry, not enough money'

    def sell(self):
        if owner:
            owner = None
        else:
            return "Vehicle has no owner"

    def __repr__(self):
        if owner is not None:
            return f"{model} {type} is owned by: {owner}"
        else:
            return f"{model} {type} is on sale: {price}"

vehicle_type = "car"
model = "BMW"
price = 30000
vehicle = Vehicle(vehicle_type, model, price)
print(vehicle.buy(15000, "Peter"))
print(vehicle.buy(35000, "George"))
print(vehicle)
vehicle.sell()
print(vehicle)
