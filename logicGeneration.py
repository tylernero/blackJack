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
    def tempSwitch(self,value,dealerCard):
        self.switchValue=value
        self.switchDealerCard=dealerCard
        self.incumbdentValue=self.logicDic[value][dealerCard]
        if self.logicDic[value][dealerCard] == 'hit':
            self.logicDic[value][dealerCard] = 'stay'
        elif self.logicDic[value][dealerCard] == 'stay':
            self.logicDic[value][dealerCard] = 'hit'
        else:
            raise Exception
    def setTempChange(self):
        pickle.dump(self.logicDic,open("hardLogic.p","wb"))
    def reverseTempChange(self):
        self.logicDic[self.switchValue][self.switchDealerCard]=self.incumbdentValue
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
    def tempSwitch(self,value,dealerCard):
        self.switchValue=value
        self.switchDealerCard=dealerCard
        self.incumbdentValue=self.logicDic[value][dealerCard]
        if self.logicDic[value][dealerCard] == 'hit':
            self.logicDic[value][dealerCard] ='stay'
        elif self.logicDic[value][dealerCard] == 'stay':
            self.logicDic[value][dealerCard] ='hit'
        else:
            raise Exception
    def setTempChange(self):
        pickle.dump(self.logicDic,open("softLogic.p","wb"))
    def reverseTempChange(self):
        self.logicDic[self.switchValue][self.switchDealerCard]=self.incumbdentValue

class SplittingLogic:
    def __init__(self,restart=None):
        if restart==False or restart==None:
            self.logicDic = getSplitLogic()
        else:
            self.logicDic = pickle.load(open("splitLogic.p","rb"))
        pickle.dump(self.logicDic,open("splitLogic.p","wb"))
    def splittingTest(self,card,dealerCard):
        return self.logicDic[card][dealerCard]
    def tempSwitch(self,value,dealerCard):
        self.switchValue=value
        self.switchDealerCard=dealerCard
        self.incumbdentValue=self.logicDic[value][dealerCard]
        if self.logicDic[value][dealerCard] == 'split':
            self.logicDic[value][dealerCard] = 'dont'
        elif self.logicDic[value][dealerCard] == 'dont':
            self.logicDic[value][dealerCard] = 'split'
        else:
            raise Exception
    def setTempChange(self):
        pickle.dump(self.logicDic,open("splitLogic.p","wb"))
    def reverseTempChange(self):
        self.logicDic[self.switchValue][self.switchDealerCard]=self.incumbdentValue

class FirstCardLogic:
    def __init__(self,restart=None):
        if restart==False or restart==None:
            self.logicDic = getFirstCardLogic()
        else:
            self.logicDic = pickle.load(open("FirstCardLogic.p","rb"))
        pickle.dump(self.logicDic,open("FirstCardLogic.p","wb"))
    def firstTest(self,value,dealerCard):
        if value < 12 or value > 19:
            return 'fight'
        else:
            return self.logicDic[value][dealerCard]
    def tempSwitch(self,value,dealerCard,test):
        self.switchValue=value
        self.switchDealerCard=dealerCard
        self.incumbdentValue=self.logicDic[value][dealerCard]
        #2:cap->none;3:cap->none;4:db->none;5:db->db;6:none->cap;7:none->none
        if test == 1:
            if self.logicDic[value][dealerCard]=='fight':
                self.logicDic[value][dealerCard]='capitulate'
            elif self.logicDic[value][dealerCard]=='capitulate':
                self.logicDic[value][dealerCard]='fight'
            elif self.logicDic[value][dealerCard]=='double':
                self.logicDic[value][dealerCard]='fight'
            else:
                raise Exception
        elif test == 2:
            self.logicDic[value][dealerCard]='double'
        elif test == 3:
            self.logicDic[value][dealerCard]='double'
        elif test == 4:
            self.logicDic[value][dealerCard]='capitulate'
        elif test == 5:
            self.logicDic[value][dealerCard]='capitulate'
        elif test == 6:
            self.logicDic[value][dealerCard]='double'
        elif test == 7:
            self.logicDic[value][dealerCard]='double'
        else:
            raise Exception
    def setTempChange(self):
        pickle.dump(self.logicDic,open("FirstCardLogic.p","wb"))
        if self.incumbdentValue =='capitulate':
            return 2
        elif self.incumbdentValue == 'double':
            return 4
        else:
            return 6
    def reverseTempChange(self):
        self.logicDic[self.switchValue][self.switchDealerCard]=self.incumbdentValue
        if self.incumbdentValue =='capitulate':
            return 3
        elif self.incumbdentValue =='double':
            return 5
        else:
            return 7
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

def getFirstCardLogic():
    logicDic = {}
    for i in range(12,20):
        logicDic[i]={}
        for j in list(cardVals.keys()):
            logicDic[i][j] = 'fight'
    return logicDic
