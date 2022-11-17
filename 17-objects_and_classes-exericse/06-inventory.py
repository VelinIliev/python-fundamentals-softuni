class Inventory:

    def __init__(self, capacity: int):
        _capacity = capacity
        items = []

    def add_item(self, item: str):
        if len(items) < _capacity:
            items.append(item)
        else:
            return "not enough room in the inventory"

    def get_capacity(self):
        return _capacity

    def __repr__(self):
        items = ', '.join(items)
        capacity_left = _capacity - len(items)
        return f"Items: {items}.\nCapacity left: {capacity_left}"


inventory = Inventory(2)
inventory.add_item("potion")
inventory.add_item("sword")
inventory.add_item("bottle")
print(inventory.get_capacity())
print(inventory)
