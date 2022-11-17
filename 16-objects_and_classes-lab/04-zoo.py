class Zoo:
    __animals = 0

    def __init__(self, name):
        name = name
        mammals = []
        fishes = []
        birds = []

    def add_animal(self, species, name):
        if species == "mammal":
            mammals.append(name)
        elif species == "fish":
            fishes.append(name)
        elif species == "bird":
            birds.append(name)

        Zoo.__animals += 1

    def get_info(self, species):
        result = ""
        if species == "mammal":
            result += f'Mammals in {name}: {", ".join(mammals)}\n'
        elif species == "fish":
            result += f'Fishes in {name}: {", ".join(fishes)}\n'
        elif species == "bird":
            result += f'Birds in {name}: {", ".join(birds)}\n'

        result += f'Total animals: {Zoo.__animals}'
        return result


zoo_name = input()
number_of_entries = int(input())
zoo = Zoo(zoo_name)

for x in range(number_of_entries):
    entry = input().split(" ")
    species = entry[0]
    name = entry[1]
    zoo.add_animal(species, name)

info = input()
print(zoo.get_info(info))
