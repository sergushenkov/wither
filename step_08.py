class Monster:
    def __init__(self, name, health, damage, speed):
        self.name = name
        self.health = health
        self.damage = damage
        self.speed = speed
        self.state = (
            "roaming"  # attacking, fleeing, sleeping, trapped, controlled, roaming
        )

    def next_action(self):
        """определяет следующее действие монстра"""


class Items:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def use(self):
        """использовать предмет"""
        pass


class Weapon(Items):
    def __init__(self, name, weight, damage, range, damage_type):
        self.name = name
        self.weight = weight
        self.damage = damage
        self.range = range
        self.damage_type = damage_type  # cutting, piercing, blunt


class Armor(Items):
    def __init__(self, name, weight, damage_reduction, durability):
        self.name = name
        self.weight = weight
        self.damage_reduction = damage_reduction
        self.durability = durability


class Potion(Items):
    def __init__(self, name, weight, health_restore):
        self.name = name
        self.weight = weight
        self.health_restore = health_restore


class Player:
    def __init__(self, armor, weapon):
        self.health = 100
        self.mana = 100
        self.current_armor = armor
        self.current_weapon = weapon
        self.bag = Bag()  # TODO: bag should be a list of items

    def next_action(self):
        """запрашивает действие пользователя и возвращает его"""
        pass

    def pick_up(self, item):
        """добавляет предмет в мешок"""
        pass

    def use_item(self, item):
        """использует предмет"""
        pass

    def attack(self, weapon, monster):
        """атакует монстра"""
        pass

    def change_armor(self, armor):
        """смена доспеха"""
        pass

    def change_weapon(self, weapon):
        """смена оружия"""
        pass

    def conjuire(self, sign):
        """активировать знак"""
        pass

class Bag():
    def __init__(self):
        self.items = []
