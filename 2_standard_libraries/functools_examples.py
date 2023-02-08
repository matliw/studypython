from functools import partial, reduce, lru_cache


def do_partial():
    # Shortens the code, returns partial object which behaves like func with
    # positional/keyword arguments
    def divide(a, b):
        return a / b

    divideby2 = partial(divide, b=2)
    divideby3 = partial(divide, b=3)
    result = divideby2(4)
    result2 = divideby3(1)
    return result, result2


def do_reduce(iterable_data):
    # Reduce the iterable to single value from LEFT to RIGHT - why is it
    # useful?

    result = reduce(lambda x, y: x+y, iterable_data)
    return result


def do_lru_cache(number):
    '''Caching is used to store results of expensive operations like computation, speeds up retrieving of the results from memory'''


    # e.g. calculating factorial
    @lru_cache()
    def factorial_calc(number):
        if number < 2:
            return 1
        else:
            return number * factorial_calc(number-1)

    return factorial_calc(number)


if __name__ == '__main__':
    do_partial()
    do_reduce([1, 2, 3, 4, 5, 6])
    print(do_lru_cache(150))
