O = [[4, 14, 15, 5]]
I = [[4, 14, 24, 34], [3, 4, 5, 6]]
S = [[5, 4, 14, 13], [4, 14, 15, 25]]
Z = [[4, 5, 15, 16], [5, 15, 14, 24]]
L = [[4, 14, 24, 25], [5, 15, 14, 13], [4, 5, 15, 25], [6, 5, 4, 14]]
J = [[5, 15, 25, 24], [15, 5, 4, 3], [5, 4, 14, 24], [4, 14, 15, 16]]
T = [[4, 14, 24, 15], [4, 13, 14, 15], [5, 15, 25, 14], [4, 5, 6, 15]]

symbol_arr = ['O', 'I', 'S', 'Z', 'L', 'J', 'T']


def rotate(current_grid_state):
    update_shape_cords = []
    count = 0
    row_count = 0
    for i in current_grid_state:
        col_count = 0
        for j in i:
            if j == "0 ":
                current_grid_state[row_count][col_count] = "- "
                update_shape_cords.append(count)
            count += 1
            col_count += 1
        row_count += 1

    result = []
    print(update_shape_cords)
    if input_symbol == 'I':
        if update_shape_cords[0] + 3 == update_shape_cords[3]:
            result.append(update_shape_cords[1])
            result.append(update_shape_cords[1] + 10)
            result.append(update_shape_cords[1] + 20)
            result.append(update_shape_cords[1] + 30)
        else:
            result.append(update_shape_cords[0])
            result.append(update_shape_cords[0] - 1)
            result.append(update_shape_cords[0] + 1)
            result.append(update_shape_cords[0] + 2)
    elif input_symbol == 'S':
        if update_shape_cords[1] - update_shape_cords[0] == 1 and update_shape_cords[3] - update_shape_cords[2] == 1:
            result.append(update_shape_cords[0])
            result.append(update_shape_cords[0] + 10)
            result.append(update_shape_cords[0] + 10 + 1)
            result.append(update_shape_cords[0] + 10 + 1 + 10)
        else:
            result.append(update_shape_cords[0])
            result.append(update_shape_cords[0] + 1)
            result.append(update_shape_cords[2] - 1)
            result.append(update_shape_cords[2] - 2)
    elif input_symbol == 'Z':
        if update_shape_cords[1] - update_shape_cords[0] == 1 and update_shape_cords[3] - update_shape_cords[2] == 1:
            result.append(update_shape_cords[1])
            result.append(update_shape_cords[1] + 10)
            result.append(update_shape_cords[1] + 10 - 1)
            result.append(update_shape_cords[1] + 10 - 1 + 10)
        else:
            result.append(update_shape_cords[0])
            result.append(update_shape_cords[0] - 1)
            result.append(update_shape_cords[1] + 1)
            result.append(update_shape_cords[1] + 2)
    elif input_symbol == 'L':
        if update_shape_cords[1] - update_shape_cords[0] == 10 and update_shape_cords[2] - update_shape_cords[1] == 10:
            result.append(update_shape_cords[0] + 1)
            result.append(update_shape_cords[0] + 1 + 10)
            result.append(update_shape_cords[0] + 1 + 10 - 1)
            result.append(update_shape_cords[0] + 1 + 10 - 2)
        elif update_shape_cords[2] - update_shape_cords[1] == 1 and update_shape_cords[3] - update_shape_cords[2] == 1:
            result.append(update_shape_cords[0])
            result.append(update_shape_cords[0] + 10)
            result.append(update_shape_cords[0] + 20)
            result.append(update_shape_cords[0] - 1)
        elif update_shape_cords[2] - update_shape_cords[1] == 10 and update_shape_cords[3] - update_shape_cords[
            2] == 10:
            result.append(update_shape_cords[1] + 1)
            result.append(update_shape_cords[1])
            result.append(update_shape_cords[1] - 1)
            result.append(update_shape_cords[1] - 1 + 10)
        elif update_shape_cords[1] - update_shape_cords[0] == 1 and update_shape_cords[2] - update_shape_cords[1] == 1:
            result.append(update_shape_cords[0])
            result.append(update_shape_cords[0] + 10)
            result.append(update_shape_cords[0] + 20)
            result.append(update_shape_cords[0] + 20 + 1)
    if input_symbol == 'J':
        if update_shape_cords[1] - update_shape_cords[0] == 10 and update_shape_cords[3] - update_shape_cords[1] == 10:
            result.append(update_shape_cords[1])
            result.append(update_shape_cords[1] - 10)
            result.append(update_shape_cords[1] - 10 - 1)
            result.append(update_shape_cords[1] - 10 - 2)
        elif update_shape_cords[1] - update_shape_cords[0] == 1 and update_shape_cords[2] - update_shape_cords[1] == 1:
            result.append(update_shape_cords[2])
            result.append(update_shape_cords[2] - 1)
            result.append(update_shape_cords[2] - 1 + 10)
            result.append(update_shape_cords[2] - 1 + 20)
        elif update_shape_cords[2] - update_shape_cords[0] == 10 and update_shape_cords[3] - update_shape_cords[2] == 10:
            result.append(update_shape_cords[0])
            result.append(update_shape_cords[0] + 10)
            result.append(update_shape_cords[0] + 10 + 1)
            result.append(update_shape_cords[0] + 10 + 2)
        elif update_shape_cords[2] - update_shape_cords[1] == 1 and update_shape_cords[3] - update_shape_cords[2] == 1:
            result.append(update_shape_cords[0] + 1)
            result.append(update_shape_cords[0] + 1 + 10)
            result.append(update_shape_cords[0] + 1 + 20)
            result.append(update_shape_cords[0] + 20)
    if input_symbol != 'T':

    print(result)
    temp_count = 0
    row_count = 0
    for k in current_grid_state:
        col_count = 0
        for m in k:
            if result.__contains__(temp_count):
                current_grid_state[row_count][col_count] = '0 '
            temp_count += 1
            col_count += 1
        row_count += 1
    return current_grid_state


def create_grid(grid_wh):
    grid = []
    temp_wh_arr = grid_wh.split(' ')
    grid_width = temp_wh_arr[0]
    grid_high = temp_wh_arr[1]
    for x in range(0, int(grid_high)):
        grid_row = ["- " for k in range(int(grid_width))]
        grid.append(grid_row)
    return grid


def print_grid(arr):
    for r in arr:
        print(''.join(r))
    print('')


def fill_the_grid_with_starting_pos(two_dm_arr, input_shape):
    if symbol_arr.__contains__(input_shape):
        symbol_all_coordinates = globals()[input_symbol]
        counter = 0
        index = 0
        while counter < 1:
            shape_cords_to_be_printed = symbol_all_coordinates[index]

            if index + 1 < len(symbol_all_coordinates):
                index += 1
            else:
                index = 0
            row_count = 0
            count = 0
            for row in two_dm_arr:
                col_count = 0
                for col in row:
                    if count in shape_cords_to_be_printed:
                        two_dm_arr[row_count][col_count] = '0 '
                    else:
                        two_dm_arr[row_count][col_count] = '- '
                    col_count += 1
                    count += 1
                row_count += 1
            print_grid(two_dm_arr)
            counter += 1
    return two_dm_arr


def move_down(current_grid_state):
    update_shape_cords = []
    count = 0
    row_count = 0
    for i in current_grid_state:
        col_count = 0
        for j in i:
            if j == "0 ":
                current_grid_state[row_count][col_count] = "- "
                update_shape_cords.append(str(int(row_count + 1)) + " " + str(col_count))
            count += 1
            col_count += 1
        row_count += 1
    for k in update_shape_cords:
        new_coordinates = k.split(" ")
        current_grid_state[int(new_coordinates[0])][int(new_coordinates[1])] = '0 '
    return current_grid_state


def move_right(current_grid_state):
    update_shape_cords = []
    count = 0
    row_count = 0
    for i in current_grid_state:
        col_count = 0
        for j in i:
            if j == "0 ":
                current_grid_state[row_count][col_count] = "- "
                update_shape_cords.append(str(row_count) + " " + str(int(col_count + 1)))
            count += 1
            col_count += 1
        row_count += 1
    for k in update_shape_cords:
        new_coordinates = k.split(" ")
        current_grid_state[int(new_coordinates[0])][int(new_coordinates[1])] = '0 '
    return current_grid_state


def move_left(current_grid_state):
    update_shape_cords = []
    count = 0
    row_count = 0
    for i in current_grid_state:
        col_count = 0
        for j in i:
            if j == "0 ":
                current_grid_state[row_count][col_count] = "- "
                update_shape_cords.append(str(row_count) + " " + str(int(col_count - 1)))
            count += 1
            col_count += 1
        row_count += 1
    for k in update_shape_cords:
        new_coordinates = k.split(" ")
        current_grid_state[int(new_coordinates[0])][int(new_coordinates[1])] = '0 '
    return current_grid_state


def move_shape(user_command, current_grid_state):
    # move_down(current_grid_state)
    if user_command == 'down':
        move_down(current_grid_state)
    elif user_command == 'right':
        move_right(current_grid_state)
    elif user_command == 'left':
        move_left(current_grid_state)
    elif user_command == 'rotate':
        rotate(current_grid_state)
    return current_grid_state


input_symbol = str(input())
input_grid_dimensions = str(input())

grid = create_grid(input_grid_dimensions)

print_grid(grid)

fill_the_grid_with_starting_pos(grid, input_symbol)

while True:
    usr_cmd = str(input())
    if usr_cmd == 'exit':
        break
    else:
        move_shape(usr_cmd, grid)
        print_grid(grid)
