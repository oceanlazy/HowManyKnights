from random import randint
import threading


class Model:
    POSITIONS = [(-2, -1), (-1, -2), (-2, 1), (-1, 2), (2, 1), (1, 2), (2, -1), (1, -2)]

    desc = []
    knights_cur = 0
    knights_num = 0
    desc_size = 0

    def example(self):
        self.create_desc()
        cur_row = randint(0, self.desc_size - 1)
        cur_column = randint(0, self.desc_size - 1)
        self.desc[cur_row][cur_column] = chr(9816)
        positions = self.get_available_positions(cur_row, cur_column)
        for row, column in positions:
            self.desc[row][column] = chr(8226)
        return self.desc

    def simple(self):
        """Knights can only go to the cell of a different color, respectively,
        if knights will be located in the cells of the same color, none of them can beat the other"""
        maximum_knights = (self.desc_size * self.desc_size) / 2
        if maximum_knights >= self.knights_num:
            return 'Simple: Yes you can put {} knights on the desc.'.format(self.knights_num)
        else:
            return 'Simple: No you can not put {} knights on the desc.'.format(self.knights_num)

    def fill(self):
        self.create_desc()
        knights = 0
        for row_num, row in enumerate(self.desc):
            for column_num, column in enumerate(row):
                positions = self.get_available_positions(row_num, column_num)
                if column == 'o' and not self.enemies_is_near(positions) \
                        and self.knights_num > knights:
                    self.desc[row_num][column_num] = chr(9822)
                    knights += 1
        return self.desc, knights

    def fill_with_sides(self):
        self.create_desc()
        self.knights_cur = 0
        self.event = threading.Event()
        t = threading.Thread(target=self.placing_black)
        t2 = threading.Thread(target=self.placing_white)
        t.start()
        t2.start()
        t.join()
        t2.join()
        return self.desc, self.knights_cur

    def placing_black(self):
        for row_num, row in enumerate(self.desc):
            for column_num, column in enumerate(row):
                if column == 'x':
                    positions = self.get_available_positions(row_num, column_num)
                    if not self.enemies_is_near(positions) and self.knights_num > self.knights_cur:
                        self.event.set()
                        self.desc[row_num][column_num] = chr(9816)
                        self.knights_cur += 1
                        self.event.clear()
                        self.event.wait(timeout=.1)

    def placing_white(self):
        for index in reversed(range(len(self.desc))):
            for column_num, column in enumerate(self.desc[index]):
                if column == 'o':
                    positions = self.get_available_positions(index, column_num)
                    if not self.enemies_is_near(positions) and self.knights_num > self.knights_cur:
                        self.event.set()
                        self.desc[index][column_num] = chr(9822)
                        self.knights_cur += 1
                        self.event.clear()
                        self.event.wait(timeout=.1)

    def create_desc(self):
        self.desc = []  # null
        for column in range(self.desc_size):
            row = ['x' if (cell + column % 2) % 2 else 'o' for cell in range(self.desc_size)]
            self.desc.append(row)

    def get_available_positions(self, cur_row, cur_column):
        available_positions = []
        for move in self.POSITIONS:
            # some figures can were out of the desc
            if 0 < cur_row - move[0] < self.desc_size and 0 < cur_column - move[1] < self.desc_size:
                available_positions.append((cur_row - move[0], cur_column - move[1]))
        return available_positions

    def enemies_is_near(self, available_positions):
        for row, column in available_positions:
            if self.desc[row][column] != 'x' and self.desc[row][column] != 'o':
                return True
