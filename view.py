class View:
    ERROR_FORMAT = "Error: {}"

    def output(self, res):
        if isinstance(res, tuple):
            desc, knights = res
            for row in desc:
                print(*row)
            print('\n{} knights on the desc.\n'.format(knights))
        elif isinstance(res, list):
            for row in res:
                print(*row)
            print()
        elif isinstance(res, str):
            print(res)
        elif isinstance(res, Exception):
            print(self.ERROR_FORMAT.format(res))
            raise res

    @staticmethod
    def input(msg):
        inp = input(msg)
        return int(inp)
