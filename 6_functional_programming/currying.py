# currying examples

"""many to single argument"""
def curry_many_to_single(a):
    def print_you(b):
        def print_shall(c):
            def print_not(d):
                def print_pass(e):
                    print(a, b, c, d, e)
                return print_pass
            return print_not
        return print_shall
    return print_you


def transform_something(you, shall, knot, passs):
    def say(x):
        return you(shall(knot(passs(x))))
    return say


def print_you():
    return 'you'


def print_shall():
    return 'shall'


def print_knot():
    return 'not'


def print_pass():
    return 'pass'

if __name__ == '__main__':
    curry_many_to_single('I say:')('you')('shall')('not')('pass')
    saying = transform_something(print_you, print_shall, print_knot, print_pass)
    print(saying)