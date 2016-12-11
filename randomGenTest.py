import randomGen as r
import matplotlib.pyplot as plt

a = r.RandomGenerator(4509)

testArray = [0]*450
postion = []
for i in range(0,450):
    postion.append(i)

for i in range(0,10000000):
    testArray[a.genNext(416)]+=1

for i,idata in enumerate(testArray):
	print( idata)
	print(postion[i])

plt.plot(postion,testArray)
plt.show()
