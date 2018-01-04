import random

"""Die.

创建一个 Die 类, 包含一个名为 sides 的属性, 默认值为 6.
编写一个 roll_die() 的方法, 打印位于1和骰子面数间的随机数.
创建一个6面的骰子, 掷10次.
创建一个10面和20面的, 投10次.
"""


class Die():
    """Die Class."""
    def __init__(self, sides=6):
        self.sides = sides
    def roll_die(self):
        print('\t- {}'.format(random.randint(1, self.sides)))

six_die = Die()
print('Six sides die: ')
for i in range(10):
    six_die.roll_die()

print('Ten sides die: ')
ten_die = Die(10)
for i in range(10):
    ten_die.roll_die()

print('Twenty sides die: ')
twenty_die = Die(20)
for i in range(10):
    twenty_die.roll_die()
