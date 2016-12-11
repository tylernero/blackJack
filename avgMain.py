import logicGeneration as lg
import strategy as st
import game as g
import randomGen as rg
import time
from cards import cardVals

try:
    import cPickle as pickle
except:
    import pickle as pickle

restart = True
decks = 8
games = 1000000
hands = 50
randomNumberSeed = 123

if restart == True:
    spot = pickle.load(open("spot.p","rb"))
elif restart == False:
    spot = {'block':0,
        'val':0}
else:
    restart = True
    spot = {'block':0,
        'val':0}
pickle.dump(spot,open("spot.py","wb"))

HardLogic = lg.HardLogic(restart)
SoftLogic = lg.SoftLogic(restart)
SplittingLogic = lg.SplittingLogic(restart)
FirstCardLogic = lg.FirstCardLogic(restart)



RandomGen = rg.RandomGenerator(randomNumberSeed)
Strategy = st.Strategy(SplittingLogic.splittingTest
,SoftLogic.softTest
,HardLogic.hardTest
,FirstCardLogic.firstTest)

starttime = time.time()
payOff = []
for q in range(1,games):
    payOff.append(g.game(hands,decks,Strategy,RandomGen))

incumbent = sum(payOff)/len(payOff)
print("intial incumbent established "+str(time.time()-starttime)+ " value=",str(incumbent))
