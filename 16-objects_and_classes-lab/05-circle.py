class Circle:
    __pi = 3.14

    def __init__(self,diameter):
        diameter = diameter
        radius = diameter / 2

    def calculate_circumference(self):
        circumference = diameter * Circle.__pi
        return circumference

    def calculate_area(self):
        area = Circle.__pi * radius ** 2
        return area

    def calculate_area_of_sector(self, angle):
        area_of_sector = (angle / 360) * Circle.__pi * radius ** 2
        return area_of_sector
