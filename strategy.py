from cards import cardVals

class Strategy:
    def __init__(self,splitLogic,softLogic,hardLogic,firstCardOptions):
        self.splitLogic = splitLogic
        self.softLogic = softLogic
        self.hardLogic = hardLogic
        self.firstCardOptions = firstCardOptions

    def firstCard(self,card1,card2,dealerCard,dealerDownCard):
        if card1=='ace' and cardVals[card2][0]==10:
            return 'blackjack'
        elif card2=='ace' and cardVals[card1][0]==10:
            return 'blackjack'
        val = cardVals[card1][0]+cardVals[card2][0]
        #splitting logic
        if card1 == card2:
            if self.splitLogic(card1,dealerCard) == 'split':
                return 'split'
        extraLogic = self.firstCardOptions(val,dealerCard)
        if extraLogic == 'capitulate':
            return 'capitulate'
        elif extraLogic == 'double':
            return 'double'
        #late surrender logic
        if dealerCard=='ace' and cardVals[dealerDownCard]==10:
            return 'stay'
        elif dealerDownCard=='ace' and cardVals[dealerCard]==10:
            return 'stay'
        #other logic
        if card1 == 'ace' or card2 == 'ace':
            if card1 =='ace':
                return self.softLogic(cardVals[card2][0],dealerCard)
            else:
                return self.softLogic(cardVals[card1][0],dealerCard)
        else:
            return self.hardLogic(val,dealerCard)

    def laterCards(self,cards,dealerCard):
        total = 0
        for i in cards:
            total += cardVals[i][0]
        try:
            ace = cards.index('ace')
            return self.softLogic(total-1,dealerCard)
        except ValueError:
            return self.hardLogic(total,dealerCard)

    def lateSurr(cards,dealerCard):
        return lateSurrender(cards,dealerCard)
