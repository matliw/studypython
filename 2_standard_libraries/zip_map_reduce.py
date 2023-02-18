def do_zip():
    lst1 = ['bicycle', 'car', 'train']
    lst2 = ['Marin', 'Honda', 'Shinkansen']

    [print(item) for item in zip(lst1, lst2)]


def do_map():
    def multiply_by_2(x):
        return x * 2

    lst = [1, 2, 3, 4, 5, 6]
    result = map(multiply_by_2, lst)
    print(list(result))


def do_reduce():
    #  Is there a reduce that is built-in? I used it in functools.
    pass


if __name__ == '__main__':
    do_zip()
    do_map()
