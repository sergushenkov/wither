class Monster:
    def __init__(self, name, health, damage, speed):
        self.name = name
        self.health = health
        # урон и скорость для монстров разного типа хранятся в отдельной таблице
        # self.damage = damage  
        # self.speed = speed

    def next_action(self):
        """определяет следующее действие монстра - куда и на какое расстояние переместится 
        до - монстр жив
        """

    def hurt(self, damage):
        """монстр получает урон
        до - монстр жив
        после - если здоровье меньше равно нулю - монстр исчезает"""
        self.health -= damage
        if self.health <= 0:
            self.die()


class Items:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def use(self):
        """использовать предмет"""
        pass


class Weapon(Items):
    def __init__(self, name, weight, damage, range):
        self.name = name
        self.weight = weight
        self.damage = damage
        self.range = range


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
        self.bag = Bag()

    def next_action(self):
        """запрашивает действие пользователя и возвращает его"""
        pass

    def use_item(self, item):
        """использует предмет
        до - предмет есть в мешке
        после - предмет оказал воздействие, исчез из мешка"""
        pass

    def attack(self, weapon, monster):
        """атакует монстра
        до - рядом есть монстр
        после - монстр получил урон"""
        pass

    def hurt(self, damage):
        """игрок получает урон
        до - игрок жив
        после - если здоровье меньше равно нулю - игра закончена исчезает"""
        self.health -= damage
        if self.health <= 0:
            self.die()

    def conjuire(self, sign, target):
        """активировать знак"""
        pass

    def drop(self, item):
        """бросить предмет
        до - предмет есть в мешке
        после - предмет исчез из мешка, оказался на карте в текущей позиции или рядом"""
        pass

class Bag():
    def __init__(self):
        self.items = []
        self.capacity = 100
        self.free_volume = 100
        self.current_armor = armor
        self.current_weapon = weapon
        
    def pick_up(self, item):
        """добавляет предмет в мешок"""
        pass

    def extract(self, item):
        """извлекает предмет из мешка"""
        pass

    def change_armor(self, armor):
        """смена доспеха
        до - в инвентаре есть доспех
        после - доспех стал current_armor, исчез из инвентаря, добавился в инвентарь старый доспех"""
        pass

    def change_weapon(self, weapon):
        """смена оружия
        до - в инвентаре есть оружие
        после - оружие стал current_weapon, исчез из инвентаря, добавился в инвентарь старое оружие"""
        pass