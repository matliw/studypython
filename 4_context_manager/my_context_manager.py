import logging

logging.basicConfig(level=logging.INFO)


class my_context:

    def __init__(self, data_input):
        self.data_input = data_input

    def readit(self):
        my_list = [1, 2, 3, 4, 5, 67, 7, 8, 'asd']
        return my_list[self.data_input]

    def __enter__(self):
        logging.info(f'Entering: index position {self.data_input}')
        try:
            return self.readit()
        except IndexError:
            return f'IndexError: index {self.data_input} is out of range'

    def __exit__(self, exc_type, exc_val, exc_tb):
        logging.info(f'Exiting: index position {self.data_input}')


if __name__ == '__main__':
    with my_context(2) as list_value:
        b = list_value
        print(list_value)
