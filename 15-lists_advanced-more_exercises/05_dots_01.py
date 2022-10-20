size = int(input())

matrix = []
directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]

for row in range(size):
    new_row = input().split()
    matrix.append(new_row)

boundaries_row = range(0, len(matrix))
boundaries_col = range(0, len(matrix[0]))

max_dots_count = 0


def check_connections(row, col):
    counter = 0
    points_to_check = [[row, col]]
    while points_to_check:
        new_row, new_col = points_to_check.pop(0)
        found_connection = False
        for direction in directions:
            check_row = new_row + direction[0]
            check_col = new_col + direction[1]
            if check_row in boundaries_row and check_col in boundaries_col:
                if matrix[check_row][check_col] == ".":
                    found_connection = True
                    points_to_check.append([check_row, check_col])
                elif matrix[check_row][check_col] == "c":
                    found_connection = True
        if matrix[new_row][new_col] == "." and found_connection:
            counter += 1
            matrix[new_row][new_col] = "c"
    return counter


for row in range(len(matrix)):
    for col in range(len(matrix[0])):
        if matrix[row][col] == ".":
            count = check_connections(row, col)
            if count > max_dots_count:
                max_dots_count = count
print(max_dots_count)


