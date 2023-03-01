""" object:
    The base class of the class hierarchy.

    When called, it accepts no arguments and returns a new featureless
    instance that has no instance attributes and cannot be given any.
    """


class SingletonClass(object):  # <-- old stuff
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(SingletonClass, cls).__new__(cls)
        return cls.instance


"""
more advanced task - I need a singleton class that returns the same instance only if init args match

a1 = Singleton('AAA')
a2 = Singleton('AAA')
a1 is a2 # must be true
b1 = Singleton('BBB')
a1 is b1 # must be false
"""


class SingletonMeta(type):

    _instances = {}

    def __call__(cls, *args, **kwargs):
        """
        Possible changes to the value of the `__init__` argument do not affect
        the returned instance.
        """

        key = (cls, args[0])
        a = cls._instances.items()
        if key not in cls._instances.keys():
            instance = super().__call__(*args, **kwargs)
            cls._instances[key] = instance
        return cls._instances[key]


class NewSingleton(metaclass=SingletonMeta):

    def __init__(self, val):
        self.val = val

    def return_stuff(self):
        return self.val


class NewSingleton2(metaclass=SingletonMeta):

    def __init__(self, val):
        self.val = val

    def return_stuff(self):
        return self.val


if __name__ == '__main__':
    # c = SingletonClass()
    # d = SingletonClass()
    # c.variable = 10
    # d.variable == 10  # c and d point to the same only instance
    # print(c is d)
    # d.variable = 0
    # print(c == 0)

    b2 = NewSingleton2('BBB')
    a1 = NewSingleton('AAA')
    a2 = NewSingleton('AAA')
    print(a1 is a2) # must be true
    b1 = NewSingleton('BBB')
    print(a1 is b1) # must be false
    print(b1 is not b2)