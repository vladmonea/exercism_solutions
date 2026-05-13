import random


class Character:
    def __init__(self):
        self.strength = self.ability()
        self.dexterity = self.ability()
        self.constitution = self.ability()
        self.intelligence = self.ability()
        self.wisdom = self.ability()
        self.charisma = self.ability()

    def ability(self):
        dice = [random.choice(range(1, 7)) for i in range(4)]
        return sum(sorted(dice)[3:])

    @property
    def hitpoints(self):
        return 10 + modifier(self.constitution)


def modifier(value):
    return round((value - 10) // 2)
