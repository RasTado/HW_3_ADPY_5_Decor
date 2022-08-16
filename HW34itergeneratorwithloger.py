from loger_deco import loger, path_loger

nested_list = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f', 'h', False],
    [1, 2, None],
]


@path_loger(path_l='log_directory')
class FlatIterator:

    def __init__(self, list_t):
        self.list_t = list_t
        self.end = len(list_t)
        self.pos_1 = 0
        self.pos_2 = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.pos_2 += 1
        if self.pos_2 >= len(self.list_t[self.pos_1]):
            self.pos_2 = 0
            self.pos_1 += 1
        if self.pos_1 >= len(self.list_t):
            raise StopIteration
        return self.list_t[self.pos_1][self.pos_2]


@path_loger(path_l='log_directory')
def flat_generator(list_t):
    for pos_1 in list_t:
        for pos_2 in pos_1:
            yield pos_2


advance_nested_list = [
    ['a', ['b', 'c']],
    ['d', 'e', ['f', 'h'], False],
    [1, 2, None],
    '2',
    [True],
]


@path_loger(path_l='log_directory')
class AdvanceFlatIterator:

    def __init__(self, list_t):
        self.list_t = self.open_list(list_t)
        self.end = len(list_t)
        self.pos_1 = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.pos_1 += 1
        if self.pos_1 >= len(self.list_t):
            raise StopIteration
        return self.list_t[self.pos_1]

    def open_list(self, lst, res=[]):
        for el in lst:
            if isinstance(el, list):
                self.open_list(el)
            else:
                res.append(el)
        return res


@path_loger(path_l='log_directory')
def advance_flat_generator(list_t):
    for pos_1 in list_t:
        if isinstance(pos_1, list):
            for pos_2 in advance_flat_generator(pos_1):
                yield pos_2
        else:
            yield pos_1


def run_function():
    while True:
        comm = input('_______________\n'
                     '1 - FlatIterator\n'
                     '2 - FlatGenerator\n'
                     '3 - AdvanceFlatIterator\n'
                     '4 - AdvanceFlatGenerator (recursive function)\n'
                     'Choice function (any key to exit): ')
        if comm == '1':
            FlatIterator(nested_list)
        elif comm == '2':
            flat_generator(nested_list)
        elif comm == '3':
            AdvanceFlatIterator(advance_nested_list)
        elif comm == '4':
            advance_flat_generator(advance_nested_list)
        else:
            break


if __name__ == '__main__':
    run_function()
