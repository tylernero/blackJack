import logicGeneration as lg
import strategy as st
import game as g
import randomGen as rg

restart = False

HardLogic = lg.HardLogic(restart)
SoftLogic = lg.SoftLogic(restart)
SplittingLogic = lg.SplittingLogic(restart)
SurrenderLogic = lg.SurrenderLogic(restart)

RandomGen = rg.RandomGenerator(27)
Strategy = st.Strategy(SplittingLogic.splittingTest,SoftLogic.softTest,HardLogic.hardTest,SurrenderLogic.surrenderTest)

for i in range(1,10000):
    payoff = g.game(1000,8,Strategy,RandomGen)
    print(payoff)
