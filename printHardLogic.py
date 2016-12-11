from .. import cards
import pickle as p

hard = p.load(open("hardLogic.p","rb"))

header = []
for i,j in cards.cardVals.iteritems():
    header.append(i)

body = []
for i in range(6,19):
    body.append([])
    body[-1].append(i)
    for j in header:
        body[-1].append(hard[i][j])

print(header)
for i in body:
    print(i)
