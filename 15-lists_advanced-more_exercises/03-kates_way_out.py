number_of_rows = int(input())

maze = []

for x in range(number_of_rows):
    row = input()
    maze.append(row)

# print(maze)
for row in maze:
    print(row)

current_row = 0
current_index = 0

for n, row in enumerate(maze):
    if row.find("k") > 0:
        current_row = n
        current_index = row.find("k")

kate_position = [current_row, current_index]

# print(kate_position)


def move_up(row, index):
    if row - 1 < 0:
        return [row, index]
    elif maze[row - 1][index] == "#":
        return [row, index]
    else:
        # kate_position = [row, index]
        return [row - 1, index]


def move_down(row, index):
    if row + 1 > number_of_rows - 1:
        return [row, index]
    elif maze[row + 1][index] == "#":
        return [row, index]
    else:
        return [row + 1, index]


print(kate_position)
kate_position = move_up(kate_position[0], kate_position[1])
kate_position = move_down(kate_position[0], kate_position[1])
print(kate_position)
# current_row, current_index = move_down(current_row, current_index)
# current_row, current_index = move_down(current_row, current_index)
# current_row, current_index = move_down(current_row, current_index)
# print(move)


