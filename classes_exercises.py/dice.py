# Dice 9.13

from random import randint

class Die:
    """A representation of dice"""
    def __init__(self, sides, value=6):
        self.sides = sides
        self.value = value
    
    def roll_die(self, sides, value):
        val = randint(self.sides, self.value)
        print(val)
    

regular_die = Die(6, 6)
regular_die.roll_die


