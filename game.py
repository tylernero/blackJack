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
        if action == 'capitulate':
            wallet = wallet - minbet/2
        elif action == 'blackjack':
            wallet = wallet + 3*minbet/2
        elif action == 'split':
            splitPlay(cards[0],cards[1],dealerUpCard,dealerDownCard)
        else:
            if action == 'double':
                cards.append(shoe.getCard())
                val += cardVals[cards[-1]][0]
            else:
                val = c.cardVals[cards[0]]+c.cardVals[cards[1]]
                while action == 'hit':
                    cards.append(shoe.getCard())
                    val += c.cardVals[cards[-1]]
                    if val > 21:
                        wallet = wallet-minbet
                        break
                    else:
                        action = strategy.laterCards(cards,dealerUpCard)
                dealerVal = dealerPlay(dealerUpCard,dealerDownCard,shoe)
                playerVal = getPlayerVal(val,cards)
                if dealerVal > playerVal:
                    wallet = wallet - minbet
                elif playerVal > dealerVal:
                    wallet = wallet + minbet
    return wallet

def dealerPlay(dealerUpCard,dealerDownCard,shoe):
    dealerVal = c.cardVals[dealerUpCard][0]+c.cardVals[dealerDownCard][0]
    dealerAces =0
    if dealerUpCard == 'ace' or dealerDownCard == 'ace':
        dealerAces=1
    if (dealerVal > 16 and dealerVal < 22):
        return dealerVal
    elif(dealerAces>0 and dealerVal+10>16 and dealerVal+10<22):
        return dealerVal + 10
    while 1==1:
        newCard = shoe.getCard()
        dealerVal+= c.cardVals[newCard][0]
        if newCard =='ace':
            dealerAces += 1
        if (dealerVal > 16 and dealerVal < 22):
            return dealerVal
        elif(dealerAces>0 and dealerVal+10>16 and dealerVal+10<22):
            return dealerVal + 1
        elif dealerVal > 21:
            return 'dealer bust'

def getPlayerVal(val,cards):
    if any([x=='ace' for x in cards]):
        playerAce = 1
    else:
        playerAce = 0
    if playerAce == 1 and val <= 11:
        return val + 10
    else:
        return val

def splitPlay(card1,card2,dealerupcard,dealerDownCard):
    pass
