# Write your code here

O = [[5, 6, 9, 10]]
I = [[1, 5, 9, 13], [4, 5, 6, 7]]
S = [[6, 5, 9, 8], [5, 9, 10, 14]]
Z = [[4, 5, 9, 10], [2, 5, 6, 9]]
L = [[1, 5, 9, 10], [2, 4, 5, 6], [1, 2, 6, 10], [4, 5, 6, 8]]
J = [[2, 6, 9, 10], [4, 5, 6, 10], [1, 2, 5, 9], [0, 4, 5, 6]]
T = [[1, 4, 5, 6], [1, 4, 5, 9], [4, 5, 6, 9], [1, 5, 6, 9]]

symbol_arr = ['O', 'I', 'S', 'Z', 'L', 'J', 'T']

grid = []

for x in range(0, 4):
    grid.append(['- ', '- ', '- ', '- '])

input_symbol = str(input())


def printGrid(arr):
    for row in arr:
        print(''.join(row))
    # print('\n')


printGrid(grid)

if symbol_arr.__contains__(input_symbol):
    symbol_all_coordinates = globals()[input_symbol]

    counter = 0
    while counter < len(symbol_all_coordinates) + 1:
        shape_cords_to_be_printed = ''
        if counter == len(symbol_all_coordinates):
            shape_cords_to_be_printed = symbol_all_coordinates[0]
        else: shape_cords_to_be_printed = symbol_all_coordinates[counter]
        row_count = 0
        count = 0
        for row in grid:
            col_count = 0
            for col in row:
                if count in shape_cords_to_be_printed:
                    grid[row_count][col_count] = '0 '
                else:
                    grid[row_count][col_count] = '- '
                col_count += 1
                count += 1
            row_count += 1
        printGrid(grid)
        counter += 1
