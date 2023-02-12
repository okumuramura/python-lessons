class Monster:
    def __init__(self, max_hp = 100):
        self.__hp = max_hp
        self.__max_hp = max_hp
        self.is_dead = False
    
    def hit(self, dmg):
        ...


dragon = Monster(1000)

dragon.hit(10)
dragon.hp = -200

print(dragon.hp)  # 0
print(dragon.is_dead)  # True

dragon.hp = 100000
print(dragon.hp)  # 1000
print(dragon.is_dead)  # False

goblin = Monster(10)
goblin.hit(15)

print(goblin.hp)  # 0
print(goblin.is_dead)  # True
