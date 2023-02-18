def only_positional_arguments(weapon_type, damage_type, damage, /):
    '''Order of the arguments is strict before the "/" character. Anything else can be added afterwards'''
    print(
        f'Your weapon is {weapon_type} type and causes {damage_type} damage of {damage} points!')


def only_keyword_named_arguments(*, weapon_type, damage_type, damage):
    '''Here order of argumentes is not importan since we declare parameter names, we require keywords'''
    print(
        f'Your weapon is {weapon_type} type and causes {damage_type} damage of {damage} points!')


def only_default_arguments(weapon_type, damage_type='PHYSICAL', damage=1):
    print(
        f'Your weapon is {weapon_type} type and causes {damage_type} damage of {damage} points!')


def take_args(standard_arg, standard_arg_2, *args, **kwargs):
    """1. *args take any number of positional arguments, **kwargs takes any number of keyword arguments
       2. * unpacks all iterables / ** unpacks dictionary
       3. * unpacks contents - so unpacked list is no longer a list
       4. unpacking to a method that requires 3 arguments must match the number of required args
       5. ordered as inputted"""

    my_args = args  # returns a tuple
    my_kwargs = kwargs  # keyword arguments return a dictionary
    a = []
    for arg_item in args:
        a.append(arg_item)
    k = [kwarg_item for kwarg_item in
         kwargs.values()]  # needs .values() to return data values from dict
    return standard_arg, standard_arg_2, a, k


def merge_lists(list_a, list_b):
    """Can also merge dictionaries"""
    print('Merged lists: ' + str([*list_a, *list_b]))


if __name__ == '__main__':
    only_keyword_named_arguments(damage_type='fire', weapon_type='bow',
                                 damage=5)
    only_positional_arguments('toothpick', 'ice', 7)
    #  only_positional_arguments(7, 'toothpick', damage='ice')  #Fails because 3 POSITIONAL arguments are required
    only_default_arguments(
        'screwdriver')  # positional but if one of the arguments is missing it will be filled in by default values from function
    take_args(1, 2, 3, 4, a='A', b='B', c='D')
    take_args(1, 2, a=3)  # no args were passed
    list_1 = [12, 13, 14]
    list_2 = [15, 16, 17]
    merge_lists(list_1, list_2)
