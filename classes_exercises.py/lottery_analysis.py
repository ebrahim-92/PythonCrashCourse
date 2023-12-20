# Lottery analysis 9.15

from random import choice

lotto = [1,2,3,4,5,6,7,8,9,10,'a','b','c','d','e']

while lotto:
    my_ticket = ['e']
    winner = choice(lotto)
    if my_ticket == winner:
        print("I win!!!")
        break
    else:
        print("You lose!!!")