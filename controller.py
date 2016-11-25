from model import Model
from view import View


class Controller:
    __INPUT_KNIGHTS_NUM = 'Please input the number of knights that you want to test.\n'
    __INPUT_DESC_SIZE = 'Please input the size of desc.\n'

    def __init__(self, _model, _view):
        self.model = _model
        self.view = _view
        self.actions = {1: self.example,
                        2: self.simple,
                        3: self.fill,
                        4: self.fill_with_sides}

    def example(self):
        self.model.desc_size = self.view.input(self.__INPUT_DESC_SIZE)
        self.view.output(self.model.example())

    def simple(self):
        self.knights_and_size()
        self.view.output(self.model.simple())

    def fill(self):
        self.knights_and_size()
        self.view.output(self.model.fill())

    def fill_with_sides(self):
        self.knights_and_size()
        self.view.output(self.model.fill_with_sides())

    def knights_and_size(self):
        self.model.knights_num = self.view.input(self.__INPUT_KNIGHTS_NUM)
        self.model.desc_size = self.view.input(self.__INPUT_DESC_SIZE)

    def do_actions(self, command):
        try:
            self.actions[command]()
        except Exception as e:
            return self.view.output(e)

    def run(self):
        while True:
            command = self.view.input('What do you want to do?\n1 - Knight moves\n'
                                      '2 - Simple check\n3 - Fill desc\n4 - Fill desc with sides\n')
            self.do_actions(command)


if __name__ == '__main__':
    controller = Controller(Model(), View())
    controller.run()
