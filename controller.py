from model import Model
from view import View


class Controller:
    __INPUT_KNIGHTS_NUM = 'Please enter the amount of knights, that will be placed to the board.\n'
    __INPUT_DESC_SIZE = 'Please input the size of desc.\n'

    def __init__(self, _model, _view):
        self.model = _model
        self.view = _view
        self.actions = {1: self.example,
                        2: self.simple,
                        3: self.fill,
                        4: self.fill_with_sides,
                        5: self.settings,
                        6: exit}

    def create_html(self):
        self.view.output(self.model.create_desc_html())

    def example(self):
        self.view.output(self.model.example())

    def simple(self):
        self.view.output(self.model.simple())

    def fill(self):
        self.view.output(self.model.fill())

    def fill_with_sides(self):
        self.view.output(self.model.fill_with_sides())

    def settings(self):
        knights_num = self.view.input(self.__INPUT_KNIGHTS_NUM)
        desc_size = self.view.input(self.__INPUT_DESC_SIZE)
        self.view.output(self.model.settings(knights_num, desc_size))

    def do_actions(self, command):
        try:
            self.actions[int(command)]()
        except Exception as e:
            return self.view.output(e)

    def run(self):
        while not (self.model.desc_size or self.model.knights_num):
            self.settings()
        while True:
            command = self.view.input('What do you want to do?\n1 - Knight moves\n2 - Simple check\n3 - Fill desc\n'
                                      '4 - Fill desc with sides\n5 - Settings\n6 - Exit\n')
            self.do_actions(command)


if __name__ == '__main__':
    controller = Controller(Model(), View())
    controller.run()
