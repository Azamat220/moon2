import random

from random import choice, randint

from enum import Enum


class SuperAbility(Enum):
    CRITICAL_DAMAGE = 1
    HEAL = 2
    BOOST = 3
    SAVE_DAMAGE_AND_REVERT = 4
    DAMAGE_RETURN = 5
    STUN = 6
    RANDOM_BOOST = 7


class GameEntity:
    def __init__(self, name, health, damage):
        self.__name = name
        self.__health = health
        self.__damage = damage

    @property
    def name(self):
        return self.__name

    @property
    def health(self):
        return self.__health

    @health.setter
    def health(self, value):
        if value < 0:
            self.__health = 0
        else:
            self.__health = value

    @property
    def damage(self):
        return self.__damage

    @damage.setter
    def damage(self, value):
        self.__damage = value

    def __str__(self):
        return f'{self.__name} health: {self.__health} damage: {self.__damage}'


class Boss(GameEntity):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage)
        self.__defence = None

    @property
    def defence(self):
        return self.__defence

    def choose_defence(self, heroes):
        hero = random.choice(heroes)
        self.__defence = hero.super_ability

    def hit(self, heroes):
        for hero in heroes:
            if hero.health > 0:
                hero.health -= self.damage

    def __str__(self):
        return f'BOSS ' + super().__str__() + f' defence: {self.__defence}'


class Hero(GameEntity):
    def __init__(self, name, health, damage, super_ability):
        super().__init__(name, health, damage)
        self.__super_ability = super_ability

    @property
    def super_ability(self):
        return self.__super_ability

    def hit(self, boss):
        if self.health > 0 and boss.health > 0:
            boss.health -= self.damage

    def apply_super_power(self, boss, heroes):
        pass


class Warrior(Hero):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage, SuperAbility.CRITICAL_DAMAGE)

    def apply_super_power(self, boss, heroes):
        coeff = random.randint(2, 5)
        boss.health -= self.damage * coeff
        print(f'Warrior hits critically {self.damage * coeff}')


class Magic(Hero):
    def __init__(self, name, health, damage, boost):
        super().__init__(name, health, damage, SuperAbility.BOOST)
        self.__boost = boost

    def apply_super_power(self, boss, heroes):
        for hero in heroes:
            if hero.health > 0 and hero != self:
                hero.damage += self.__boost


class Medic(Hero):
    def __init__(self, name, health, damage, heal_points):
        super().__init__(name, health, damage, SuperAbility.HEAL)
        self.__heal_points = heal_points

    def apply_super_power(self, boss, heroes):
        for hero in heroes:
            if hero.health > 0 and hero != self:
                hero.health += self.__heal_points


class Berserk(Hero):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage, SuperAbility.SAVE_DAMAGE_AND_REVERT)
        self.__saved_damage = 0

    @property
    def saved_damage(self):
        return self.__saved_damage

    @saved_damage.setter
    def saved_damage(self, value):
        self.__saved_damage = value

    def apply_super_ability(self, boss, heroes):
        if boss.health > 0:
            reverted_damage = self.saved_damage // randint(3, 5)
            boss.health = max(0, boss.health - reverted_damage)
            print(f'Berserk {self.name} hitted boss by {reverted_damage}')
            self.saved_damage = 0


class Spectra(Hero):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage, SuperAbility.DAMAGE_RETURN)


    def apply_super_power(self, boss, heroes):
         boss.health -= boss.damage * 0.5
         return boss.health


class Thor(Hero):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage, SuperAbility.STUN)
        self.__stun = 0

    def apply_super_power(self, boss, heroes):
        chance = randint(1, 6)
        if chance == 1:
            boss.damage = 0
            print(f'{self.name} Оглушает {Boss.name}')
        else:
            boss.damage = 50


class Imba(Hero):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage, SuperAbility.RANDOM_BOOST)

    def apply_super_power(self, boss, heroes):
        chance = random.randint(1, 6)
        if self.health > 0:
            if chance == 1:
                coef = random.randint(2,3)
                boss.health -= self.damage * coef
                print(f'Imba hits critically {self.damage * coef}')
            elif chance == 2:
                self.damage += 5
                print(f'Imba boost his damage!')
            elif chance == 3:
                self.health += 5
                print(f'Imba heal himself!')


def print_statistics(boss, heroes):
    print('ROUND ' + str(round_number) + ' ----------------')
    print(boss)
    for hero in heroes:
        print(hero)


def is_game_finished(boss, heroes):
    if boss.health <= 0:
        print('Heroes won!!!')
        return True
    all_heroes_dead = True
    for hero in heroes:
        if hero.health > 0:
            all_heroes_dead = False
            break
    if all_heroes_dead:
        print('Boss won!!!')
    return all_heroes_dead

round_number = 0
def play_round(boss, heroes):
    global round_number
    round_number += 1
    boss.choose_defence(heroes)
    boss.hit(heroes)
    for hero in heroes:
        if boss.defence != hero.super_ability and hero.health > 0:
            if hero.super_ability != SuperAbility.CRITICAL_DAMAGE:
                hero.hit(boss)
            hero.apply_super_power(boss, heroes)
    print_statistics(boss, heroes)


def start_game():
    boss = Boss('Pudge', 2000, 50)
    warrior = Warrior('Ahiles', 280, 10)
    doc = Medic('Invoker', 250, 5, 15)
    magic = Magic('Lolita', 290, 15, 5)
    berserk = Berserk('Boom', 270, 10)
    assistant = Medic('Rafael', 300, 5, 5)
    spectra = Spectra('Fantom', 360, 10)
    thor = Thor('Son of Azgard', 320, 10)
    imba = Imba('Master', 280, 5)
    heroes_list = [warrior, doc, magic, berserk, assistant, spectra, thor, imba]

    print_statistics(boss, heroes_list)
    while not is_game_finished(boss, heroes_list):
        play_round(boss, heroes_list)


start_game()
