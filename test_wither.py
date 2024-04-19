from wither import Monster


def test_monster_init():
    monster = Monster("rat")
    assert monster.name == "rat"
    assert monster.health == 10
    assert monster.damage == 1
    assert monster.speed == 1


def test_monster_next_action():
    monster = Monster("rat")
    delta = [(i, j) for i in range(-1, 2) for j in range(-1, 2)]
    next_delta = monster.next_action()
    next_delta.sort()
    assert next_delta == delta
    next_delta = monster.next_action()
    next_delta.sort()
    assert next_delta == delta
    next_delta = monster.next_action()
    next_delta.sort()
    assert next_delta == delta


def test_monster_next_action_to_far():
    monster = Monster("wolf")
    delta = [(i, j) for i in range(-2, 3) for j in range(-2, 3)]
    next_delta = monster.next_action()
    next_delta.sort()
    assert next_delta == delta
    next_delta = monster.next_action()
    next_delta.sort()
    assert next_delta == delta
    next_delta = monster.next_action()
    next_delta.sort()
    assert next_delta == delta


def test_monster_hurt():
    monster = Monster("rat")
    is_alive = monster.hurt(0)
    assert is_alive == "alive"
    assert monster.health == 10
    is_alive = monster.hurt(1)
    assert is_alive == "alive"
    assert monster.health == 9
    is_alive = monster.hurt(5)
    assert is_alive == "alive"
    assert monster.health == 4
    is_alive = monster.hurt(5)
    assert is_alive == "dead"
    assert monster.health == 0
