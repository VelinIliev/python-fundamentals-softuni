class Catalogue:
    def __init__(self, name: str):
        self.name = name
        self.products = []

    def add_product(self, product_name: str):
        self.products.append(product_name)

    def get_by_letter(self, first_letter: str):
        return [item for item in self.products if item[0] == first_letter]

    def __repr__(self):
        report = ""
        report += f'Items in the {self.name} catalogue:\n'
        self.products.sort()
        for item in self.products:
            report += f'{item}\n'
        return report

# TODO: not ready

catalogue = Catalogue("Furniture")
catalogue.add_product("Sofa")
catalogue.add_product("Mirror")
catalogue.add_product("Desk")
catalogue.add_product("Chair")
catalogue.add_product("Carpet")
print(catalogue.get_by_letter("C"))
print(catalogue)
