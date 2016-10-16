import randomGen as r
import cards as c

gen = r.RandomGenerator(6)

shoe = c.Shoe(8,gen)

for i in range(0,416):
    x = shoe.getCard()
    print(x)
