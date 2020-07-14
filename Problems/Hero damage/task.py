hero_damage = 100


def double_damage():
    global hero_damage
    hero_damage = hero_damage * 2


def disarmed():
    global hero_damage
    hero_damage = 10 / 100 * hero_damage


def power_potion():
    global hero_damage
    hero_damage = hero_damage + 100
