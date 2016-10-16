
class RandomGenerator:
    def __init__(self,seed):
	self.c =0
        self.a =10807
        self.m =2**31-1
        self.x = seed

    def genNext(self,deckLen):
	self.x = (self.a*self.x+self.c)%self.m
	return (self.x*deckLen)/self.m
