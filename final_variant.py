import random
from abc import ABC, abstractmethod


class Fighter:
    def __init__(self, name, health):
        self.name = name
        self.health = health
        self.weapon = None

    def change_weapon(self, weapon, monster):
        self.weapon = weapon
        print(f"{self.name} сменил оружие на {type(weapon).__name__}\n")
        self.weapon.attack(monster)
        self.check_health()

    def check_health(self):
        if self.health <= 0:
            print(f"{self.name} побежден!")


class Monster:
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def make_damage(self, fighter):
        damage = random.randint(10, 50)
        fighter.health -= damage
        print(f"{monster.name} наносит удар")
        print(f"Здоровье {fighter.name} уменьшилось на {damage} единиц. Осталось {fighter.health} единиц здоровья\n")



class Weapon(ABC):
    def __init__(self, damage):
        self.damage = damage

    @abstractmethod
    def attack(self, monster):
        pass


class Sword(Weapon):
    def attack(self, monster):
        monster.health -= self.damage
        print(f"{fighter.name} наносит мечом урон {monster.name}")
        if monster.health > 0:
            print(f"У монстра осталось {monster.health} единиц здоровья\n")
        else:
            print(f"Монстр {monster.name} побежден")


class Bow(Weapon):
    def attack(self, monster):
        monster.health -= self.damage
        print(f"{fighter.name} наносит луком урон {monster.name}")
        if monster.health > 0:
            print(f"У монстра осталось {monster.health} единиц здоровья\n")
        else:
            print(f"Монстр {monster.name} побежден")


# Пример использования классов
fighter = Fighter("Sam", 100)
monster = Monster("Goblin", 80)

sword = Sword(random.randint (20,30))
bow = Bow(random.randint(15,20))

print(f"Начинается бой между {fighter.name}({fighter.health}) и {monster.name}({monster.health})\n")
while True:
    fighter.change_weapon(sword, monster)
    if monster.health <= 0:  # Проверка на победу монстра
        break

    monster.make_damage(fighter)
    if fighter.check_health():  # Проверка на победу бойца
        break

    fighter.change_weapon(bow, monster)
    if monster.health <= 0:  # Проверка на победу монстра
        break

    monster.make_damage(fighter)
    if fighter.check_health():  # Проверка на победу бойца
        break

print("Бой закончился!")