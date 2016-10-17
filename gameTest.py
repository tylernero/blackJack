import game as g
import cards as c
import randomGen as rg

import random

def dealerPlayTest(num):
    RandomGen = rg.RandomGenerator(num)
    shoe = c.Shoe(8,RandomGen)
    card1 = shoe.getCard()
    card2 = shoe.getCard()
    print(card1,card2)
    print(g.dealerPlay(card1,card2,shoe))



dealerPlayTest(int(round(random.random()*1000)))
