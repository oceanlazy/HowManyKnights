from random import randint

size = 3
positions = [(-2, -1), (-1, -2), (-2, 1), (-1, 2), (2, 1), (1, 2), (2, -1), (1, -2)]


def simple(knights, desc_size_inp):
    """horse can only go to the cell of a different color, respectively,
    if the horses dotting the cells of the same color, none of them can beat the other"""
    maximum_knights = (desc_size_inp * desc_size_inp) / 2
    if maximum_knights >= knights:
        return 'Simple: Yes you can put {} knights on the desc.'.format(knights)
    else:
        return 'Simple: No you can not put {} knights on the desc.'.format(knights)


def create_desc():
    desc = []
    for column in range(size):
        row = ['x' if (cell + column % 2) % 2 else 'o' for cell in range(size)]
        desc.append(row)
    return desc


def knight_example_moves(cur_row=randint(0, size-1), cur_column=randint(0, size-1)):
    desc = create_desc()

    desc[cur_row][cur_column] = chr(9822)
    for move in positions:
        try:
            # here some figures were out of the desc and appears from other and like [-1]
            if cur_row - move[0] >= 0 and cur_column - move[1] >= 0:
                desc[cur_row - move[0]][cur_column - move[1]] = chr(8226)
        except IndexError:
            # here some figures were out of the desc, like row or column > size
            pass
    return desc


def get_available_positions(cur_row, cur_column):
    available_positions = []
    for move in positions:
        try:
            # here some figures were out of the desc and appears from other and like [-1]
            if 0 < cur_row - move[0] < size and 0 < cur_column - move[1] < size:
                available_positions.append((cur_row - move[0], cur_column - move[1]))
        except IndexError:
            # here some figures were out of the desc, like row or column > size
            pass

    return available_positions


def enemies_is_near(desc, positions):
    for row, column in positions:
        if desc[row][column] != 'x' and desc[row][column] != 'o':
            return True


def fill_desc_two_sides():
    desc = create_desc()
    knights = 0
    row_num = 0
    for row in desc:
        column_num = 0
        for column in row:
            if column == 'x' and row_num < round(size / 2):
                if not enemies_is_near(desc, get_available_positions(row_num, column_num)) and knights_num > knights:
                    desc[row_num][column_num] = chr(9816)
                    knights += 1
            if column == 'o' and row_num > round(size / 2):
                if not enemies_is_near(desc, get_available_positions(row_num, column_num)) and knights_num > knights:
                    desc[row_num][column_num] = chr(9822)
                    knights += 1
            column_num += 1
        row_num += 1
    return desc, knights


def fill_desc():
    desc = create_desc()
    knights = 0
    row_num = 0
    for row in desc:
        column_num = 0
        for column in row:
            if column == 'o' and not enemies_is_near(desc, get_available_positions(row_num, column_num)) \
                    and knights_num > knights:
                desc[row_num][column_num] = chr(9822)
                knights += 1
            column_num += 1
        row_num += 1
    return desc, knights


def controller():
    while True:
        global knights_num, size
        try:
            knights_num = int(input('Please input the number of knights that you want to test.\n'))
            size = int(input('Please input the size of desc.\n'))
            action = int(input('What action do you want to do?\n1 - Show knight moves\n2 - Simple check\n3 - Fill desc\n'
                               '4 - Fill desc with sides\n'))
        except ValueError:
            print('Value must be an integer.')
            continue

        if action == 1:
            res = knight_example_moves()
            for row in res:
                print(*row)
            print('\n')

        if action == 2:
            res = simple(knights_num, size)
            print(res)

        if action == 3:
            res, knights_num = fill_desc()
            for row in res:
                print(*row)
            print('\nResult: {} knights on the desc of {} size.\n'.format(knights_num, size))

        if action == 4:
            res, knights_num = fill_desc_two_sides()
            for row in res:
                print(*row)
            print('\nResult: {} knights on the desc of {} size.\n'.format(knights_num, size))

if __name__ == '__main__':
    controller()