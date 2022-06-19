nested_list = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f', ['h', ['i']], False],
    [1, 2, None],
]


class FlatIterator:
    def __init__(self, some_list):
        self.some_list = some_list
        self.iterators_queue = []
        self.current_iterator = iter(self.some_list)

    def __iter__(self):
        return self

    def __next__(self):
        while True:
            try:
                self.current_element = next(self.current_iterator)
            except StopIteration:
                if not self.iterators_queue:
                    raise StopIteration
                else:
                    self.current_iterator = self.iterators_queue.pop()
                    continue
            if isinstance(self.current_element, list):
                self.iterators_queue.append(self.current_iterator)
                self.current_iterator = iter(self.current_element)
            else:
                return self.current_element


def flat_generator(some_list):
    for element in some_list:
        if isinstance(element, list):
            for value in flat_generator(element):
                yield value
        else:
            yield element


if __name__ == '__main__':
    print('\nИтератор')
    for item in FlatIterator(nested_list):
        print(item)
    flat_list = [item for item in FlatIterator(nested_list)]
    print(flat_list)
    print('\nГенератор')
    for item in flat_generator(nested_list):
        print(item)
    print(*(flat_generator(nested_list)))
