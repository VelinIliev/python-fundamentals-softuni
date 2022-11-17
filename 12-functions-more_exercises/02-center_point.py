from math import sqrt
from math import floor

x1 = floor(float(input()))
y1 = floor(float(input()))
x2 = floor(float(input()))
y2 = floor(float(input()))


def find_closest_point(x1, y1, x2, y2):
    first_distance = floor(abs(sqrt(x1 ** 2 + y1 ** 2)))
    second_distance = floor(abs(sqrt(x2 ** 2 + y2 ** 2)))
    if first_distance < second_distance:
        return f'({int(x1)}, {int(y1)})'
    else:
        return f'({int(x2)}, {int(y2)})'


print(find_closest_point(x1, y1, x2, y2))

