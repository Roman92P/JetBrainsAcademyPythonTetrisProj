# Write your code here
import collections

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

row_count = 0
col_count = 0

if symbol_arr.__contains__(input_symbol):
    symbol_all_coordinates = globals()[input_symbol]
    print(symbol_all_coordinates)
    for row in grid:
        for col in row:
            col_count += 1
    row_count += 1
