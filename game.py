import cards as c

def game(hands,shoeSize,strategy,randomGen):
    shoe = c.Shoe(8,randomGen)
    wallet = Wallet(10000)
    global minbet
    minbet = 10
    for i in range(0,hands):
        shoe.shuffleTest(20)
        if wallet.cashOut() < minbet:
            return wallet.cashOut()
        cards = [shoe.getCard()]
        dealerDownCard = shoe.getCard()
        cards.append(shoe.getCard())
        dealerUpCard = shoe.getCard()
        bet = minbet
        action = strategy.firstCard(cards[0],cards[1],dealerUpCard,dealerDownCard)
        if action == 'capitulate':
            wallet.updateDollars(-minbet/2.0)
            playerVal = []
        elif action == 'blackjack':
            wallet.updateDollars((3.0*minbet)/2.0)
            playerVal = []
        elif action == 'split':
            playerVal = splitPlay(cards,dealerUpCard,dealerDownCard,shoe,wallet,strategy,1)
        elif action == 'double':
            bet = bet*2
            cards.append(shoe.getCard())
            val = getVals(cards)
            val += c.cardVals[cards[-1]][0]
            playerVal = [getPlayerVal(val,cards)]
        elif action == 'stay':
            playerVal = [getVals(cards)]
        else:
            playerVal = [playerPlay(cards,shoe,strategy,dealerUpCard)]
        dealerVal = dealerPlay(dealerUpCard,dealerDownCard,shoe)
        for pays in playerVal:
            payout(pays,dealerVal,wallet,bet)
    return wallet.cashOut()



def payout(playerVal,dealerVal,wallet,minbet):
    if (dealerVal > playerVal and dealerVal != 'bust') or playerVal == 'bust':
        wallet.updateDollars(-minbet)
    elif playerVal > dealerVal or dealerVal == 'bust':
        wallet.updateDollars(minbet)
    else:
        pass


def playerPlay(cards,shoe,strategy,dealerUpCard):
    action = 'hit'
    val = c.cardVals[cards[0]][0]+c.cardVals[cards[1]][0]
    while action == 'hit':
        cards.append(shoe.getCard())
        val += c.cardVals[cards[-1]][0]
        if val > 21:
            'bust'
            break
        else:
            action = strategy.laterCards(cards,dealerUpCard)
    return getPlayerVal(val,cards)

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
            return dealerVal + 10
        elif dealerVal > 21:
            return 'bust'

def getVals(cards):
    if any([x=='ace' for x in cards]):
        aces = 1
    else:
        aces = 0
    val = c.cardVals[cards[0]][0]+c.cardVals[cards[1]][0]
    if aces == 1 and val <= 11:
        return val + 10
    else:
        return val

def getPlayerVal(val,cards):
    if any([x=='ace' for x in cards]):
        playerAce = 1
    else:
        playerAce = 0
    if val > 21:
        return 'bust'
    elif playerAce == 1 and val <= 11:
        return val + 10
    else:
        return val

def splitPlay(cards,dealerUpCard,dealerDownCard,shoe,wallet,strategy,depth):
    playerVals = []
    for i in cards:
        hand = [i, shoe.getCard()]
        action = strategy.firstCard(hand[0],hand[1],dealerUpCard,dealerDownCard)
        if action == 'capitulate':
            wallet.updateDollars(-minbet/2.0)
        elif action == 'blackjack':
            wallet.updateDollars((3.0*minbet)/2.0)
        elif action == 'split' and depth < 3:
            playerVals = playerVals + splitPlay(hand,dealerUpCard,dealerDownCard,shoe,wallet,strategy,depth+1)
        elif action == 'double':
            hand.append(shoe.getCard())
            val = c.cardVals[hand[0]][0]+c.cardVals[hand[1]][0]
            val += c.cardVals[hand[-1]][0]
            playerVals.append(getPlayerVal(val,hand))
        elif action == 'stay':
            playerVals.append(getVals(hand))
        else:
            playerVals.append(playerPlay(hand,shoe,strategy,dealerUpCard))
    return playerVals

class Wallet:
    def __init__(self,dollars):
        self.dollars = dollars

    def updateDollars(self,change):
        self.dollars = self.dollars + change

    def cashOut(self):
        return self.dollars
