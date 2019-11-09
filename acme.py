import random
from random import randint
class:
    product


def __init__(self, name, price=10, weight=20, flammability=0.5)
self.name = name
self.price = price
self.weight = weight
self.flammability = flammability
# identifier - 1000000 to 9999999
self.identifier = random.randint(1000000, 9999999)


def stealability(self):
    s = self.price/self.weight
    if s < 0.5:
        return "Not so stealable..."
    elif s >= 0.5 and s < 1.0:
        return "Kinda stealable."
    else:
        return "Very stealable!"


def explode(self):
    e = self.flammability * self.weight
    if e < 10:
        return print('...fizzle.')
    elif 50 > e >= 10:
        return print('...boom!')
    else:
        return print('...BABOOM!!')


class boxingglove(product)


def __init__(self, name, price=10, weight=20, flammability=0.5)
self.name = name
self.price = price
self.weight = weight
self.flammability = flammability
# identifier - 1000000 to 9999999
self.identifier = random.randint(1000000, 9999999)


def explode(self):
    return ("...it's a glove")


def punch(self):
    if self.weight < 5:
        return "That tickles."
    elif self.weight >= 5 and self.weight < 15:
        return "Hey that hurt!"
    else:
        return "Ouch!"
