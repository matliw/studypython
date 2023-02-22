class Hero:
    def __init__(self, hit_points, mana, strength, mind, weapon, race):
        self.__hp = hit_points  # private, more secure than protected: accessible only in its class
        self.__mana = mana
        self._strength = strength  # protected; accessible only in their class and sub-classes (pass in inheritance)
        self._mind = mind
        self.weapon = weapon
        self.race = race  # instance attributes

    def display_visible_hero_info(self):  # public
        print(f'Hero is {self.race} and has a {self.weapon}.')

    def _display_base_stats(self):  # private
        print(f'Strength: {self._strength}')
        print(f'Mind: {self._mind}')

    def __display_hp_mana_bars_values(self):  # protected
        return {'HP': self.__hp, 'Mana': self.__mana}

    def access_hp_mana(self):
        return self.__display_hp_mana_bars_values()


class Warrior(Hero):
    _attack_type = 'Poison'  # class attribute

    def __init__(self, hit_points, mind, mana, strength, weapon, race):
        super().__init__(hit_points, mind, mana, strength,
                         weapon, race)

    def slash(self):
        if self.access_hp_mana()['HP'] > 10:
            print(f'{self.__class__.__name__} uses Slash!')
        else:
            print('You\'re too tired to slash.')

    @staticmethod  # doesn't take self or cls,
    def offend_your_enemy():
        print('You old cabbage!')


class Mage(Hero):
    _immunity = 'Fire'

    def __init__(self, hit_points, mind, mana, strength, weapon, race):
        super().__init__(hit_points, mind, mana, strength,
                         weapon, race)

    def fireball(self):
        if self.access_hp_mana()['Mana'] < 61:
            print(f'{self.__class__.__name__} uses Fireball!')
        else:
            print('You don\'t have mana to cast this spell.')


class Spellsword(Mage, Warrior):
    _special_dance = 'Macarena'

    def __init__(self, hit_points, mind, mana, strength, weapon, race):
        super().__init__(hit_points, mind, mana, strength,
                         weapon, race)

    @classmethod  # has access only to class state, not to self
    def dance(cls):
        print(f'Doing a special dance: {cls._special_dance}')

    @classmethod
    def change_dance(cls):
        cls._special_dance = 'Labamba'


class MagicBonus:
    _magic_bonus_list = ['Earth', 'Pikachu', 'Fire']

    def __init__(self, bonus=None):
        self.bonus = bonus

    @property  # getter
    def bonus(self):
        print('Getting bonus: ')
        return self._bonus  # why does it have to be private? / this doesn't have to be declared anywhere

    @bonus.setter
    def bonus(self, new_bonus):
        print('I am changing my bonus...')
        if new_bonus in self._magic_bonus_list:
            print(f'My bonus is {new_bonus}')

        self._bonus = new_bonus

    @bonus.deleter
    def bonus(self):
        del self._bonus


if __name__ == '__main__':
    hero = Warrior(13, 12, 45, 13, 'Sword', 'Argonian')
    hero.slash()
    hero.display_visible_hero_info()
    hero_mage = Mage(13, 12, 45, 13, 'Wand', 'Breton')
    hero_mage.display_visible_hero_info()
    hero_mage.fireball()
    a, b = hero_mage.weapon, hero_mage.race
    hero3 = Spellsword(13, 12, 45, 13, 'Firesword', 'Khajiit')
    hero3.fireball()
    hero3.slash()
    print(Spellsword.__mro__)
    hero3.dance()
    hero3.change_dance()
    hero3.dance()
    hero3.offend_your_enemy()
    addd_magic_bonus = MagicBonus('Earth')
    addd_magic_bonus.bonus = 'Ice'
    addd_magic_bonus.bonus = 'Fire'
