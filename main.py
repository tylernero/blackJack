import logicGeneration as lg
import strategy as st
import game as g
import randomGen as rg
import time

restart = False

HardLogic = lg.HardLogic(restart)
SoftLogic = lg.SoftLogic(restart)
SplittingLogic = lg.SplittingLogic(restart)
SurrenderLogic = lg.SurrenderLogic(restart)



RandomGen = rg.RandomGenerator(28)
Strategy = st.Strategy(SplittingLogic.splittingTest
,SoftLogic.softTest
,HardLogic.hardTest
,SurrenderLogic.surrenderTest)

starttime = time.time()
payOff = []
for i in range(1,100000):
    payOff.append(g.game(50,8,Strategy,RandomGen))

incumbent = sum(payOff)/len(payOff)

for i in range(6,20):
    for j in list(cardVals.key()):
        
print(time.time()-starttime)
