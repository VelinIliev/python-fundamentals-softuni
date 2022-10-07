number_of_rows = int(input())

matrix = []

for _ in range(number_of_rows):
    new_row = input().split()
    matrix.append(new_row)


def count_dots(x, y):
    counter = 0
    points_to_check = [[x, y]]
    while points_to_check:
        row, column = points_to_check.pop(0)
        if 0 < row < len(matrix) - 1 and 0 < column < len(matrix[0]) - 1:
            found_connection = False
            if matrix[row][column] == ".":
                counter += 1
            if matrix[row][column - 1] == ".":
                found_connection = True
                points_to_check.append([row, column - 1])
            if matrix[row][column + 1] == ".":
                found_connection = True
                points_to_check.append([row, column + 1])
            if matrix[row + 1][column] == ".":
                found_connection = True
                points_to_check.append([row + 1, column])
            if matrix[row - 1][column] == ".":
                found_connection = True
                points_to_check.append([row - 1, column])
            if found_connection:
                matrix[row][column] = "c"
            elif matrix[row - 1][column] == "c" or matrix[row + 1][column] == "c" \
                    or matrix[row][column - 1] == "c" or matrix[row][column + 1] == "c":
                matrix[row][column] = "c"
            else:
                matrix[row][column] = "-"
        elif row == 0 and 0 < column < len(matrix[0]) - 1:
            found_connection = False
            if matrix[row][column] == ".":
                counter += 1
            if matrix[row][column - 1] == ".":
                found_connection = True
                points_to_check.append([row, column - 1])
            if matrix[row][column + 1] == ".":
                found_connection = True
                points_to_check.append([row, column + 1])
            if matrix[row + 1][column] == ".":
                found_connection = True
                points_to_check.append([row + 1, column])
            if found_connection:
                matrix[row][column] = "c"
            elif matrix[row + 1][column] == "c" \
                    or matrix[row][column - 1] == "c" or matrix[row][column + 1] == "c":
                matrix[row][column] = "c"
            else:
                matrix[row][column] = "-"
        elif row == 0 and column == 0:
            found_connection = False
            if matrix[row][column] == ".":
                counter += 1
            if matrix[row][column + 1] == ".":
                found_connection = True
                points_to_check.append([row, column + 1])
            if matrix[row + 1][column] == ".":
                found_connection = True
                points_to_check.append([row + 1, column])
            if found_connection:
                matrix[row][column] = "c"
            elif matrix[row + 1][column] == "c" or matrix[row][column + 1] == "c":
                matrix[row][column] = "c"
            else:
                matrix[row][column] = "-"
        elif column == 0 and 0 < row < len(matrix) - 1:
            found_connection = False
            if matrix[row][column] == ".":
                counter += 1
            if matrix[row][column + 1] == ".":
                found_connection = True
                points_to_check.append([row, column + 1])
            if matrix[row + 1][column] == ".":
                found_connection = True
                points_to_check.append([row + 1, column])
            if matrix[row - 1][column] == ".":
                found_connection = True
                points_to_check.append([row - 1, column])
            if found_connection:
                matrix[row][column] = "c"
            elif matrix[row - 1][column] == "c" or matrix[row + 1][column] == "c" \
                    or matrix[row][column + 1] == "c":
                matrix[row][column] = "c"
            else:
                matrix[row][column] = "-"
        if 0 < row < len(matrix) - 1 and column > 0 and column == len(matrix[0]) - 1:
            found_connection = False
            if matrix[row][column] == ".":
                counter += 1
            if matrix[row][column - 1] == ".":
                found_connection = True
                points_to_check.append([row, column - 1])
            if matrix[row + 1][column] == ".":
                found_connection = True
                points_to_check.append([row + 1, column])
            if matrix[row - 1][column] == ".":
                found_connection = True
                points_to_check.append([row - 1, column])
            if found_connection:
                matrix[row][column] = "c"
            elif matrix[row - 1][column] == "c" or matrix[row + 1][column] == "c" \
                    or matrix[row][column - 1] == "c":
                matrix[row][column] = "c"
            else:
                matrix[row][column] = "-"
        elif row == 0 and column == len(matrix[0]) - 1:
            found_connection = False
            if matrix[row][column] == ".":
                counter += 1
            if matrix[row][column - 1] == ".":
                found_connection = True
                points_to_check.append([row, column - 1])
            if matrix[row + 1][column] == ".":
                found_connection = True
                points_to_check.append([row + 1, column])
            if found_connection:
                matrix[row][column] = "c"
            elif matrix[row + 1][column] == "c" \
                    or matrix[row][column - 1] == "c":
                matrix[row][column] = "c"
            else:
                matrix[row][column] = "-"
        elif row > 0 and column > 0 and row == len(matrix) - 1 and column < len(matrix[0]) - 1:
            found_connection = False
            if matrix[row][column] == ".":
                counter += 1
            if matrix[row][column - 1] == ".":
                found_connection = True
                points_to_check.append([row, column - 1])
            if matrix[row][column + 1] == ".":
                found_connection = True
                points_to_check.append([row, column + 1])
            if matrix[row - 1][column] == ".":
                found_connection = True
                points_to_check.append([row - 1, column])
            if found_connection:
                matrix[row][column] = "c"
            elif matrix[row - 1][column] == "c" \
                    or matrix[row][column - 1] == "c" or matrix[row][column + 1] == "c":
                matrix[row][column] = "c"
            else:
                matrix[row][column] = "-"
    return counter


max_count = 0

for x in range(len(matrix)):
    for y in range(len(matrix[0])):
        if matrix[x][y] == ".":
            current_counter = count_dots(x, y)
            if current_counter > max_count:
                max_count = current_counter
print(max_count)

# TODO: it works but needs to be simplified
