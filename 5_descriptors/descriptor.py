"""implement your own descriptor that logs when attrs of a class is modified"""
import logging

logging.basicConfig(level=logging.INFO)


class AttributeLogger:

    def __set_name__(self, owner,
                     name):  # records field names. So, we can access more than one field.
        self.public_name = name
        self.private_name = '_' + name  # not sure why we need the protected private name

    def __get__(self, obj,
                objtype=None):  # self is attribute; obj is instance of a class; objtype is CLASS
        value = getattr(obj, self.private_name)
        logging.info(
            'Accessing CLASS %r and attribute value %r. CLASS name is %r + self is %r',
            self.public_name, value, objtype.__name__, self.__dict__)
        return value  # what happens if I don't return it?

    def __set__(self, obj, value):
        if isinstance(value, str):  # check if string type, raise error if not. Can be used to create validators
            self.public_name = value
        else:
            raise TypeError(
                f'{value} is {type(value)} and it should be string value.')
        logging.info('Update CLASS %r and attribute value %r',
                     self.public_name, value)
        setattr(obj, self.private_name, value)

    def __delete__(self, obj):
        logging.info('Deleted %r attribute',
                     self.public_name)
        del self.public_name


class Developers:
    dev_name = AttributeLogger()
    programming_language = AttributeLogger()

    def __init__(self, dev_name, programming_language):
        self.dev_name = dev_name
        self.programming_language = programming_language


if __name__ == '__main__':
    Mateusz = Developers('Mateusz', 'Python')
    Mats_language = Mateusz.programming_language
    del Mateusz.programming_language
    Ivan = Developers(1, 2)
