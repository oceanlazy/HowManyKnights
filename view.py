class View:
    ERROR_FORMAT = "Error: {}"

    def output(self, res):
        if isinstance(res, tuple):
            desc, knights = res
            print('\n'.join([' '.join(row) for row in desc]))
            print('\n{} knights on the desc.\n'.format(knights))
        elif isinstance(res, list):
            print('\n'.join([' '.join(row) for row in res]))
            print()
        elif isinstance(res, str):
            print(res)
        elif isinstance(res, Exception):
            print(self.ERROR_FORMAT.format(res))

    @staticmethod
    def input(msg):
        inp = input(msg)
        return inp
