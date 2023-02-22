""" object:
    The base class of the class hierarchy.

    When called, it accepts no arguments and returns a new featureless
    instance that has no instance attributes and cannot be given any.
    """


class SingletonClass(object):
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(SingletonClass, cls).__new__(cls)
        return cls.instance


if __name__ == '__main__':
    c = SingletonClass()
    d = SingletonClass()
    c.variable = 10
    d.variable == 10  # c and d point to the same only instance
    print(c is d)
    d.variable = 0
    print(c == 0)
