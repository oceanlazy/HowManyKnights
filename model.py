from random import randint


class Model:
    POSITIONS = [(-2, -1), (-1, -2), (-2, 1), (-1, 2), (2, 1), (1, 2), (2, -1), (1, -2)]

    knights_num = 0
    desc_size = 0

    def example(self):
        desc = self.create_desc()
        cur_row = randint(0, self.desc_size - 1)
        cur_column = randint(0, self.desc_size - 1)
        desc[cur_row][cur_column] = chr(9822)
        positions = self.get_available_positions(cur_row, cur_column)
        for row, column in positions:
            desc[row][column] = chr(8226)
        return desc

    def simple(self):
        """Knights can only go to the cell of a different color, respectively,
        if knights will be located in the cells of the same color, none of them can beat the other"""
        maximum_knights = (self.desc_size * self.desc_size) / 2
        if maximum_knights >= self.knights_num:
            return 'Simple: Yes you can put {} knights on the desc.'.format(self.knights_num)
        else:
            return 'Simple: No you can not put {} knights on the desc.'.format(self.knights_num)

    def fill(self):
        desc = self.create_desc()
        knights = 0
        row_num = 0
        for row in desc:
            column_num = 0
            for column in row:
                positions = self.get_available_positions(row_num, column_num)
                if column == 'o' and not self.enemies_is_near(desc, positions) \
                        and self.knights_num > knights:
                    desc[row_num][column_num] = chr(9822)
                    knights += 1
                column_num += 1
            row_num += 1
        return desc, knights

    def fill_with_sides(self):
        desc = self.create_desc()
        knights = 0
        row_num = 0
        for row in desc:
            column_num = 0
            for column in row:
                if column == 'x' and row_num < round(self.desc_size / 2):
                    positions = self.get_available_positions(row_num, column_num)
                    if not self.enemies_is_near(desc, positions) and self.knights_num > knights:
                        desc[row_num][column_num] = chr(9816)
                        knights += 1
                if column == 'o' and row_num > round(self.desc_size / 2):
                    positions = self.get_available_positions(row_num, column_num)
                    if not self.enemies_is_near(desc, positions) and self.knights_num > knights:
                        desc[row_num][column_num] = chr(9822)
                        knights += 1
                column_num += 1
            row_num += 1
        return desc, knights

    def create_desc(self):
        desc = []
        for column in range(self.desc_size):
            row = ['x' if (cell + column % 2) % 2 else 'o' for cell in range(self.desc_size)]
            desc.append(row)
        return desc

    def get_available_positions(self, cur_row, cur_column):
        available_positions = []
        for move in self.POSITIONS:
            # here some figures were out of the desc and appears from other side and looks like [-1]
            # here some figures were out of the desc, like row or column > size
            if 0 < cur_row - move[0] < self.desc_size and 0 < cur_column - move[1] < self.desc_size:
                available_positions.append((cur_row - move[0], cur_column - move[1]))
        return available_positions

    def enemies_is_near(self, desc, available_positions):
        for row, column in available_positions:
            if desc[row][column] != 'x' and desc[row][column] != 'o':
                return True
