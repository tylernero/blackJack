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
decks = 2
games = 100000
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

if spot['block'] < 1:
    if spot['val']==0:
        i = 6
    else:
        i = spot['val']
    while i < 20:
        for j in list(cardVals.keys()):
            HardLogic.tempSwitch(i,j)
            RandomGen = rg.RandomGenerator(randomNumberSeed)
            payOff = []
            for q in range(1,games):
                payOff.append(g.game(hands,decks,Strategy,RandomGen))
            new = sum(payOff)/len(payOff)
            if incumbent > new:
                HardLogic.reverseTempChange()
            else:
                incumbent = new
                HardLogic.setTempChange()
            print("HardLogic Value="+str(i)+" dealerCard="+str(j)+" at time="+str(time.time()-starttime)+" value="+str(incumbent))
        i = i+1
        spot['val']=i
        pickle.dump(spot,open("spot.p","wb"))
    spot['block']=1
    spot['val']=0
    pickle.dump(spot,open("spot.p","wb"))

if spot['block']<2:
    if spot['val']==0:
        i = 2
    else:
        i = spot['val']
    while i < 10:
        for j in list(cardVals.keys()):
            SoftLogic.tempSwitch(i,j)
            RandomGen = rg.RandomGenerator(randomNumberSeed)
            payOff = []
            for q in range(1,games):
                payOff.append(g.game(hands,decks,Strategy,RandomGen))
            new = sum(payOff)/len(payOff)
            if incumbent > new:
                SoftLogic.reverseTempChange()
            else:
                incumbent = new
                SoftLogic.setTempChange()
            print("SoftLogic Value="+str(i)+" dealerCard="+str(j)+" at time="+str(time.time()-starttime)+" value="+str(incumbent))
        i = i +1
        spot['val']=1
        pickle.dump(spot,open("spot.p","wb"))
    spot['block']=2
    spot['val']=0
    pickle.dump(spot,open("spot.p","wb"))

if spot['block']<3:
    for i in list(cardVals.keys()):
        for j in list(cardVals.keys()):
            SplittingLogic.tempSwitch(i,j)
            RandomGen = rg.RandomGenerator(randomNumberSeed)
            payOff = []
            for q in range(1,games):
                payOff.append(g.game(hands,decks,Strategy,RandomGen))
            new = sum(payOff)/len(payOff)
            if incumbent > new:
                SplittingLogic.reverseTempChange()
            else:
                incumbent = new
                SplittingLogic.setTempChange()
            print("SplittingLogic Value="+str(i)+" dealerCard="+str(j)+" at time="+str(time.time()-starttime)+" value="+str(incumbent))
    spot['block']=3
    spot['val']=0
    pickle.dump(spot,open("spot.p","wb"))

if spot['block']<4:
    if spot['val']==0:
        i=12
    else:
        i=spot['val']
    while i < 20:
        for j in list(cardVals.keys()):
            FirstCardLogic.tempSwitch(i,j,1)
            RandomGen = rg.RandomGenerator(randomNumberSeed)
            payOff=[]
            for q in range(1,games):
                payOff.append(g.game(hands,decks,Strategy,RandomGen))
            new = sum(payOff)/len(payOff)
            if incumbent > new:
                changeCode = FirstCardLogic.reverseTempChange()
            else:
                incumbent = new
                changeCode = FirstCardLogic.setTempChange()
            FirstCardLogic.tempSwitch(i,j,changeCode)
            RandomGen = rg.RandomGenerator(randomNumberSeed)
            payOff=[]
            for q in range(1,games):
                payOff.append(g.game(hands,decks,Strategy,RandomGen))
            new = sum(payOff)/len(payOff)
            if incumbent > new:
                FirstCardLogic.reverseTempChange()
            else:
                incumbent = new
                FirstCardLogic.setTempChange()
            print("FirstCardLogic Value="+str(i)+" dealerCard="+str(j)+" at time="+str(time.time()-starttime)+" value="+str(incumbent))
        i=i+1
        spot['val']=i
        pickle.dump(spot,open("spot.p","wb"))
    spot['block']=4
    pickle.dump(spot,open("spot.p","wb"))

print("completed at "+str(time.time()-starttime))
