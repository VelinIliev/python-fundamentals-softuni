class Catalogue:
    def __init__(self, name: str):
        name = name
        products = []

    def add_product(self, product_name: str):
        products.append(product_name)

    def get_by_letter(self, first_letter: str):
        items = [item for item in products if item[0].lower() == first_letter.lower()]
        return items

    def __repr__(self):
        report = ""
        report += f'Items in the {name} catalogue:'
        products.sort()
        for item in products:
            report += f'\n{item}'
        return report

catalogue = Catalogue("Furniture")
catalogue.add_product("Sofa")
catalogue.add_product("Mirror")
catalogue.add_product("Desk")
catalogue.add_product("Chair")
catalogue.add_product("Carpet")
print(catalogue.get_by_letter("c"))
print(catalogue)
