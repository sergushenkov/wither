import random

monster_table = {
    "rat": [10, 1, 1, "r"],
    "wolf": [20, 2, 2, "w"],
    "skeleton": [30, 3, 1, "s"],
}


class Monster:
    def __init__(self, name):
        self.name = name
        self.health = monster_table[name][0]
        self.damage = monster_table[name][1]
        self.speed = monster_table[name][2]
        self.symbol = monster_table[name][3]

    def next_action(self):
        """определяет следующее действие монстра - куда и на какое расстояние переместится"""
        dy_dx = [
            (i, j)
            for i in range(-self.speed, self.speed + 1)
            for j in range(-self.speed, self.speed + 1)
        ]
        random.shuffle(dy_dx)
        return dy_dx

    def hurt(self, damage):
        """монстр получает урон"""
        if self.health > damage:
            self.health -= damage
            print(f"Монстр {self.name} получил урон {damage}")
            return "alive"
        self.health = 0
        print(f"Монстр {self.name} убит")
        return "dead"


class Player:
    move_to = {
        "2": (1, 0),
        "8": (-1, 0),
        "4": (0, -1),
        "6": (0, 1),
        "7": (-1, -1),
        "9": (-1, 1),
        "1": (1, -1),
        "3": (1, 1),
        "5": (0, 0),
    }

    def __init__(self):
        self.health = 100
        self.mana = 100
        self.damage = 3
        # self.bag = Bag()

    def next_action(self):
        """запрашивает действие пользователя и возвращает его"""
        print(f"Ваше здоровье: {self.health}")
        choose = input("Введите направление движения/атаки: ")
        return self.move_to.get(choose, (0, 0))

    def hurt(self, damage):
        self.health -= damage
        if self.health <= 0:
            return False
        return True


class Map:
    maps = {
        "default": """########################################
#......................................#
#......................................#
#......................................#
#......................................#
#......................................#
#......................................#
#......................................#
#......................................#
#......................................#
#......................................#
#......................................#
#......................................#
#......................................#
#......................................#
#......................................#
#......................................#
#...................####...............#
#......................................#
#..................####................#
#......................................#
#...............####...................#
#......................................#
#......................................#
########################################""",
        "test": """#######
#.....#
#..####
#.....#
#######""",
    }

    def __init__(self, map_name="default", monsters_num=10):
        current_map = self.maps[map_name]
        self.map = [list(line) for line in current_map.split("\n")]
        self.width = len(self.map[0])
        self.height = len(self.map)

        self.exit = (self.height - 1, self.width // 2)
        self.map[self.exit[0]][self.exit[1]] = "◙"

        self.player_yx = (self.height - 2, self.width // 2)

        self.monsters_num = monsters_num
        self.monsters = dict()
        x, y = 0, 0
        for _ in range(self.monsters_num):
            while (
                self.map[y][x] != "."  # HW
                or (y, x) in self.monsters
                or (y, x) == self.player_yx
            ):
                x = random.randint(1, self.width - 1)
                y = random.randint(1, self.height - 1)
            name = random.choice(list(monster_table.keys()))
            self.monsters[y, x] = Monster(name)

        self.player = Player()

    def __str__(self):
        map_for_print = [x.copy() for x in self.map]
        map_for_print[self.player_yx[0]][self.player_yx[1]] = "@"
        for y, x in self.monsters:
            map_for_print[y][x] = self.monsters[y, x].symbol
        return "\n".join("".join(line) for line in map_for_print)

    def turn(self):
        is_player_alive = True

        player_dy, player_dx = self.player.next_action()
        new_player_yx = (
            self.player_yx[0] + player_dy,
            self.player_yx[1] + player_dx,
        )
        is_player_attack = new_player_yx in self.monsters
        if not is_player_attack and self.map[new_player_yx[0]][new_player_yx[1]] == ".":
            self.player_yx = new_player_yx
        if is_player_attack:
            monster = self.monsters[
                self.player_yx[0] + player_dy, self.player_yx[1] + player_dx
            ]
            attack_result = monster.hurt(self.player.damage)
            if attack_result == "dead":
                del self.monsters[
                    self.player_yx[0] + player_dy, self.player_yx[1] + player_dx
                ]

        sum_damage = 0
        monsters_new = dict()
        for (y, x), monster in self.monsters.items():
            dy_dx = monster.next_action()
            for dy, dx in dy_dx:
                is_attack = (
                    y - monster.speed <= self.player_yx[0] <= y + monster.speed
                ) and (x - monster.speed <= self.player_yx[1] <= x + monster.speed)
                if is_attack:
                    monsters_new[y, x] = monster
                    sum_damage += monster.damage
                    break
                if (
                    (dy, dx) == (0, 0)
                    or 0 < y + dy < self.height - 1
                    and 0 < x + dx < self.width - 1
                    and self.map[y + dy][x + dx] == "."
                    and (y + dy, x + dx) not in self.monsters
                    and (y + dy, x + dx) not in monsters_new
                    and (y + dy, x + dx) != self.exit
                ):
                    monsters_new[y + dy, x + dx] = monster
                    break
        self.monsters = monsters_new

        is_player_alive = self.player.hurt(sum_damage)
        if not is_player_alive:
            print("Вы умерли")
            return True
        if self.player_yx == self.exit:
            print("Вы покинули подземелье живым")
            return True
        return False


if __name__ == "__main__":
    map = Map()
    is_game_over = False
    while not is_game_over:
        print(map)
        is_game_over = map.turn()
    print("Игра окончена")
