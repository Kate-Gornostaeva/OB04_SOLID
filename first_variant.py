import random
from abc import ABC, abstractmethod


class Fighter:
    def __init__(self, name, health):
        self.name = name
        self.health = health
        self.weapon = None

    def change_weapon(self, weapon, monster):
        self.weapon = weapon
        print(f"{self.name} сменил оружие на {type(weapon).__name__}")
        self.weapon.attack(monster)

class Monster():
    def __init__(self, name, health, damage):
        self.name = name
        self.health = health
        self.damage = damage

    def make_damage(self):
        self.damage = random.randint(10, 50)
        print(f"Здоровье {fighter.name} уменьшилось на {self.damage} единиц")


class Weapon(ABC):
    @abstractmethod
    def attack(self, damage):
        pass

class Sword(Weapon):
    def __init__(self, damage):
        self.damage = damage

    def attack(self, monster):
        monster.health -= self.damage
        print(f"{fighter.name} наносит мечом урон {monster.name}")
        if monster.health > 0:
            print (f"У монстра осталось {monster.health} единиц здоровья")
        else:
            print(f"Монстр {monster.name} побежден")


class Bow(Weapon):
    def __init__(self, damage):
        self.damage = damage

    def attack(self, monster):
        monster.health -= self.damage
        print(f"{fighter.name} наносит луком урон {monster.name}")

        if monster.health > 0:
            print(f"У монстра осталось {monster.health} единиц здоровья")
        else:
            print(f"Монстр {monster.name} побежден")



fighter = Fighter("Sam", 100)
monster = Monster("Goblin", 80, 20)

sword = Sword(30)
bow = Bow(20)

fighter.change_weapon(sword, monster)

fighter.change_weapon(bow, monster)

monster.make_damage()

fighter.change_weapon(sword, monster)



