import cards as c

def game(hands,shoeSize,strategy,randomGen):
    shoe = c.Shoe(8,randomGen)
    wallet = 10000
    minbet = 10
    for i in range(0,hands):
        shoe.shuffleTest(20)
        if wallet < minbet:
            return wallet
        cards = [shoe.getCard()]
        dealerDownCard = shoe.getCard()
        cards.append(shoe.getCard())
        dealerUpCard = shoe.getCard()
        action = strategy.firstCard(cards[0],cards[1],dealerUpCard,dealerDownCard)
        if action = 'capitulate':
            wallet = wallet - minbet/2
            break
        if action = 'blackjack':
            wallet = wallet + 3*minbet/2
            break
        if action = 'split':
            splitPlay(cards[0],cards[1],dealerUpCards,dealerDownCard)
        else:
            val = cardVals[card1][0]+cardVals[card2][0]
            while action != 'hit':
                cards.append(shoe.getCard())
                val += cardVals[cards[-1]][0]
                if val > 21:
                    wallet = wallet-minbet
                    break
                else:
                    action = laterCards(cards,dealerUpCard)
            




def splitPlay():
