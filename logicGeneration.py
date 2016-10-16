from cards import cardVals
try:
    import cPickle as pickle
except:
    import pickle as pickle

class HardLogic:
    def __init__(self,restart=None):
        if restart==False or restart==None:
            self.logicDic = getHardLogic()
        else:
            self.logicDic = pickle.load(open("hardLogic.p","rb"))
        pickle.dump(self.logicDic,open("hardLogic.p","wb"))
    def hardTest(self,value,dealerCard):
        if value < 6:
            return 'hit'
        elif value > 19:
            return 'stay'
        else:
            return self.logicDic[value][dealerCard]

class SoftLogic:
    def __init__(self,restart=None):
        if restart==False or restart==None:
            self.logicDic = getSoftLogic()
        else:
            self.logicDic = pickle.load(open("softLogic.p","rb"))
        pickle.dump(self.logicDic,open("softLogic.p","wb"))
    def softTest(self,value,dealerCard):
        if value == 1:
            return 'hit'
        elif value > 9:
            return 'stay'
        else:
            return self.logicDic[value][dealerCard]

class SplittingLogic:
    def __init__(self,restart=None):
        if restart==False or restart==None:
            self.logicDic = getSplitLogic()
        else:
            self.logicDic = pickle.load(open("splitLogic.p","rb"))
        pickle.dump(self.logicDic,open("splitLogic.p","wb"))
    def splittingTest(self,card,dealerCard):
        return self.logicDic[card][dealerCard]

class SurrenderLogic:
    def __init__(self,restart=None):
        if restart==False or restart==None:
            self.logicDic = getLateSurrenderLogic()
        else:
            self.logicDic = pickle.load(open("surrenderLogic.p","rb"))
        pickle.dump(self.logicDic,open("surrenderLogic.p","wb"))
    def surrenderTest(self,value,dealerCard):
        if value < 12 or value > 19:
            return 'fight'
        else:
            return self.logicDic[value][dealerCard]


def getHardLogic():
    logicDic = {}
    for i in range(6,20):
        logicDic[i] = {}
        for j in list(cardVals.keys()):
            logicDic[i][j] = 'hit' if i < 16 else 'stay'
    return logicDic

def getSoftLogic():
    logicDic = {}
    for i in range(2,10):
        logicDic[i]={}
        for j in list(cardVals.keys()):
            logicDic[i][j] = 'hit' if i < 4 else 'stay'
    return logicDic

def getSplitLogic():
    logicDic = {}
    for i in list(cardVals.keys()):
        logicDic[i]= {}
        for j in list(cardVals.keys()):
            logicDic[i][j] = 'split'
    return logicDic

def getLateSurrenderLogic():
    logicDic = {}
    for i in range(12,20):
        logicDic[i]={}
        for j in list(cardVals.keys()):
            logicDic[i][j] = 'fight'
    return logicDic
