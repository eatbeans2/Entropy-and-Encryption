import math
import random
f = open("Entropyf.txt", "r")
text = f.read()
f.close()
maxN = int(raw_input("Enter maximum n-gram size:\n"))
maxEnt = math.log(8836, 2)
print "Maximum possible entropy: " + str(maxEnt)
for i in xrange(1, maxN+1):
    alphSize=94*i
    strTracker = [['', 0]]
    for j in xrange(0, len(text)-i):
        isNew = 1
        for k in xrange(0, len(strTracker)):
            if text[j:j+i] == strTracker[k][0]:
                strTracker[k][1] = strTracker[k][1]+1
                isNew = 0
        if(isNew):
            strTracker.append([text[j:j+i], 1])
    for q in xrange(0, (8836-94)*i):
        strTracker.append(['', 30])
    total = 0
    prob = []
    entropyEst = 0.0
    for j in xrange(0, len(strTracker)):
        total = total + strTracker[j][1]
    for j in xrange(1, len(strTracker)):
        prob.append(float(float(strTracker[j][1])/float(total)))
        entropyEst = entropyEst + prob[j-1]*math.log(prob[j-1], 2.0)
    entropyEst = entropyEst
    print "Entropy for " + str(i) + "-grams:"
    print -1*entropyEst/float(i)
