import randomGen as rg
cardVals = {
'ace':[1],
'two':[2],
'three':[3],
'four':[4],
'five':[5],
'six':[6],
'seven':[7],
'eight':[8],
'nine':[9],
'ten':[10],
'jack':[10],
'queen':[10],
'king':[10]
}

cardList = list(cardVals.keys())

class Shoe:
    def __init__(self,decks, randomGenerator):
        self.decks = decks
        self.randomGenerator = randomGenerator
        self.shuffle()
    def getCard(self):
        card = self.shoe[0]
        del self.shoe[0]
        if len(self.shoe)==0:
            self.shuffle()
        return card

    def shuffleTest(self,cards):
        if len(self.shoe)<=cards:
            self.shuffle()

    def shuffle(self):
        self.shoeLength = self.decks*len(cardVals)*4
        self.shoe = [None]*self.shoeLength
        for i in range(0,self.shoeLength):
            x = self.randomGenerator.genNext(self.shoeLength)
            if self.shoe[x] is None and self.shoe[i] is None:
                self.shoe[x] = cardList[i%len(cardList)]
                self.shoe[i] = cardList[x%len(cardList)]
            elif self.shoe[x] is None:
                self.shoe[x] = self.shoe[i]
                self.shoe[i]= cardList[x%len(cardList)]
            elif self.shoe[i] is None:
                self.shoe[i] = self.shoe[x]
                self.shoe[x] =cardList[i%len(cardList)]
            else:
                self.shoe[i],self.shoe[x] = self.shoe[x],self.shoe[i]
