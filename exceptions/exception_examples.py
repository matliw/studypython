"""Handling exceptions
   - catch multiples exceptions
   - catch exceptions with arguments
   - re-raising exception to get stack"""


def catch_my_exceptions():
    try:
        pass
    except (ZeroDivisionError, TypeError, RuntimeError):
        print('Exception found.')


def catch_exceptions_with_arguments():
    try:
        raise Exception('first argument', 'second argument')
    except Exception as exc_instance:
        print(type(exc_instance))  # class type
        print(exc_instance.args)
        first, second = exc_instance.args  # accessible arguments
        print('First: ' + first)


def reraise():
    import sys

    try:
        f = open('myfile.txt')
        s = f.readline()
        i = int(s.strip())
    # except OSError as err:
    #     print("OS error:", err)
    # except ValueError:
    #     print("Could not convert data to an integer.")
    except Exception as err:  # catch any exception and print exception class name
        print(f"Unexpected {err=}, {type(err)=}")
        raise  # re-raise the exception for caller, it will show stack trace


"""Raising exceptions -  forcing exception to raise"""


def raise_specified_exception():
    try:
        raise TimeoutError('Timeout!')
    except TimeoutError:
        print('Timeout exception!')
        raise


"""Chaining exceptions
   + cleanup with finally"""


def chain_one_exception_to_another():
    try:
        return 1/0
    except ZeroDivisionError:  # catch zero division error
        raise RuntimeError('cannot run it under such conditions')  #raise runtime error
    finally:  # clean-up: print and raise another error
        print('Cleanup action')
        raise KeyboardInterrupt


"""User-defined exceptions, inheritance"""


class ExpensiveCarError(Exception):
    "You can\'t afford this car! It\'s too expensive!"
    pass


class NotEnoughMoneyError(Exception):

    def __init__(self, amount):
        self.amount = amount

    def __str__(self):
        return f'Error, {self.amount} is not enough money!'


def check_amount(money):
    if money < 250000:
        raise NotEnoughMoneyError(money)


def buy_new_car():
    car = 'Porsche'
    try:
        input_car = input('What car do you want to buy? Write: Citroen, Porsche or Kia ')
        if car == 'Porsche':
            raise ExpensiveCarError
        else:
            print("You can have it right away!")
    except ExpensiveCarError:
        print('Bad luck! Your wallet is empty.')


def main():
    # reraise()
    # raise_specified_exception()
    # chain_one_exception_to_another()
    # buy_new_car()
    check_amount(12)


if __name__ == '__main__':
    main()
