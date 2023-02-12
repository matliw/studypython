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


if __name__ == '__main__':
    only_keyword_named_arguments(damage_type='fire', weapon_type='bow', damage=5)
    only_positional_arguments('toothpick', 'ice', 7)
    #  only_positional_arguments(7, 'toothpick', damage='ice')  #Fails because 3 POSITIONAL arguments are required
    only_default_arguments('screwdriver')  # positional but if one of the arguments is missing it will be filled in by default values from function