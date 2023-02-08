from itertools import groupby, takewhile, dropwhile


def do_group_by():
    #  groupby returns consecutive keys and groups / lot's of possible uses here but too advanced now
    my_list = [('crank', 'shimano'), ('frame', 'bmc'), ('frame', 'giant'),
               ('crank', 'sram')]
    for brands, components in groupby(my_list, lambda x: x[
        0]):  # lambda tells groupby to use first item as grouping key
        for item in components:
            print(f'We have a {brands} by {item[1]}')


def do_takewhile():  # ???? I don't understand this, it's not iterating and just stops at the first odd number

    def is_even(x):
        return x % 2 == 0

    my_list = [2,3,4]
    result = list(takewhile(is_even, my_list))
    print(result)

def do_dropwhile():  # display after first time the condition is false, what for???
    def is_even(x):
        return x % 2 == 0

    my_list = [4, 6, 2, 3, 4, 5, 6]
    result = list(dropwhile(is_even, my_list))
    print(result)


if __name__ == '__main__':
    do_group_by()
    do_takewhile()
    do_dropwhile()

