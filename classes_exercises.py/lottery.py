# Lottery 9.14

from random import choice

lotto = [1,2,3,4,5,6,7,8,9,10,'a','b','c','d','e']
winner = choice(lotto)

for entry in range(5):
    print(choice(lotto))