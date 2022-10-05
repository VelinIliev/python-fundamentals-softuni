number_of_rows = int(input())

maze = []

for x in range(number_of_rows):
    row = input()
    maze.append(row)

# print(maze)
# for row in maze:
#     print(row)

current_row = 0
current_index = 0

for n, row in enumerate(maze):
    if row.find("k") > 0:
        current_row = n
        current_index = row.find("k")


counter = 0
# directions = ["top", "left", "bottom", "right"]
direction = "top"
counter_clockwise_moves = 0
# counterclockwise
while counter <= 100:
    kate_position = [current_row, current_index]
    # print(kate_position)

    # go top
    if direction == "top" and current_row - 1 >= 0 and maze[current_row - 1][current_index] != "#":
        current_row = current_row - 1
        counter_clockwise_moves += 1
    elif direction == "top" and current_row - 1 >= 0 and maze[current_row - 1][current_index] == "#":
        direction = "left"
    elif direction == "top" and current_row - 1 < 0:
        counter_clockwise_moves += 1
        break
    # go left
    if direction == "left" and current_index - 1 >= 0 and maze[current_row][current_index - 1] != "#":
        current_index = current_index - 1
        counter_clockwise_moves += 1
    elif direction == "left" and current_index - 1 >= 0 and maze[current_row][current_index - 1] == "#":
        direction = "bottom"
    elif direction == "left" and current_index - 1 < 0:
        counter_clockwise_moves += 1
        break
    # go bottom
    if direction == "bottom" and current_row + 1 <= len(maze) - 1 and maze[current_row + 1][current_index] != "#":
        current_row = current_row + 1
        counter_clockwise_moves += 1
    elif direction == "bottom" and current_row + 1 <= len(maze) - 1 and maze[current_row + 1][current_index] == "#":
        direction = "right"
    elif direction == "bottom" and current_row + 1 > len(maze) - 1:
        counter_clockwise_moves += 1
        break
    # go right
    if direction == "right" and current_index + 1 <= number_of_rows and maze[current_row][current_index + 1] != "#":
        current_index = current_index + 1
        counter_clockwise_moves += 1
    elif direction == "right" and current_index + 1 <= number_of_rows and maze[current_row][current_index + 1] == "#":
        direction = "top"
    elif direction == "right" and current_index + 1 > number_of_rows:
        counter_clockwise_moves += 1
        break

    counter += 1

counter = 0
direction = "bottom"
clockwise_moves = 0
# clockwise
while counter <= 100:
    kate_position = [current_row, current_index]
    # go bottom
    if direction == "bottom" and current_row + 1 <= len(maze) - 1 and maze[current_row + 1][current_index] != "#":
        current_row = current_row + 1
        clockwise_moves += 1
    elif direction == "bottom" and current_row + 1 <= len(maze) - 1 and maze[current_row + 1][current_index] == "#":
        direction = "left"
    elif direction == "bottom" and current_row + 1 > len(maze) - 1:
        clockwise_moves += 1
        break
    # go left
    if direction == "left" and current_index - 1 >= 0 and maze[current_row][current_index - 1] != "#":
        current_index = current_index - 1
        clockwise_moves += 1
    elif direction == "left" and current_index - 1 >= 0 and maze[current_row][current_index - 1] == "#":
        direction = "top"
    elif direction == "left" and current_index - 1 < 0:
        clockwise_moves += 1
        break
    # go top
    if direction == "top" and current_row - 1 >= 0 and maze[current_row - 1][current_index] != "#":
        current_row = current_row - 1
        clockwise_moves += 1
    elif direction == "top" and current_row - 1 >= 0 and maze[current_row - 1][current_index] == "#":
        direction = "rigt"
    elif direction == "top" and current_row - 1 < 0:
        clockwise_moves += 1
        break
    # go right
    if direction == "right" and current_index + 1 <= number_of_rows and maze[current_row][current_index + 1] != "#":
        current_index = current_index + 1
        clockwise_moves += 1
    elif direction == "right" and current_index + 1 <= number_of_rows and maze[current_row][current_index + 1] == "#":
        direction = "top"
    elif direction == "right" and current_index + 1 > number_of_rows:
        clockwise_moves += 1
        break
    counter += 1

if counter ==101:
    print("Kate cannot get out")
else:
    if clockwise_moves == counter_clockwise_moves:
        print(f'Kate got out in {counter_clockwise_moves} moves')
    elif clockwise_moves > counter_clockwise_moves:
        print(f'Kate got out in {clockwise_moves} moves')
    elif counter_clockwise_moves > clockwise_moves:
        print(f'Kate got out in {counter_clockwise_moves} moves')


# TODO: not ready
