class Storage:
    def __init__(self, capacity):
        capacity = capacity
        storage = []

    def add_product(self, product: str):
        if len(storage) < capacity:
            storage.append(product)

    def get_products(self):
        return storage

