import math

#function to convert characters in a string to corresponding numbers
def toNum(str, charNum):
    numArray=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','<','>','/']
    newNum = -1
    for i in xrange(0,29):
        if str[charNum]==numArray[i]:
            newNum = i
            break
    return newNum;
print "NOTE: text file must be strictly alphabet characters"
#find alphabet size for entropy calculations
alphSize = float(raw_input("What is the alphabet size: "))
#calculate absolute rate
absRate = math.log(alphSize, 2)
#open the text file
readFile = open("text.txt", "r")
#create a string from the file (inefficient?)
text = readFile.read()
text = text.lower()
#prints absolute rate
print "The absolute rate is "+str(absRate)
readFile.close()
textLenNoSpace = 0
for i in xrange(0, len(text)):
    if text[i]!=" ":
        textLenNoSpace+=1
#generates lists to track ngrams
monogramList = [float(0)]*int(alphSize)
digramList = [[float(0)]*int(alphSize) for x in range(int(alphSize))]
trigramList = [[[float(0)]*int(alphSize) for x in range(int(alphSize))]for x in range(int(alphSize+1))]

#monogram counter
for i in xrange(0, len(text)-1):
    if text[i]!=" ":
        firstChar=toNum(text[i], 0)
        monogramList[firstChar]+=1
#digram counter
for i in xrange(0, len(text)-len(text)%2-2):
    if text[i]!=" " and text[i+1]!=" ":
        firstChar=toNum(text[i], 0)
        secondChar=toNum(text[i+1], 0)
        digramList[firstChar][secondChar]+=1
#trigram counter
for i in xrange(0, len(text)-len(text)%3-3):
    if text[i]!=" " and text[i+1]!=" " and text[i+2]!=" ":
        firstChar=toNum(text[i], 0)
        secondChar=toNum(text[i+1], 0)
        thirdChar=toNum(text[i+2], 0)
        trigramList[firstChar][secondChar][thirdChar]+=1

#calculating the entropy for digrams
monogramEntropy = 0
monogramCount = 0
#counts monograms
for i in xrange(0,int(alphSize)):
    monogramCount+=monogramList[i]
#creates entropy list
monogramEntropy=monogramList[:]
print monogramList[:]
totalMonogramEntropy= float(0)
for i in xrange(0, int(alphSize)):
    monogramEntropy[i]=monogramList[i]/(textLenNoSpace)
    print monogramEntropy[i]
    if monogramEntropy[i]!=0:
        monogramEntropy[i]=-1*(monogramEntropy[i]*math.log(monogramEntropy[i], 2))
        totalMonogramEntropy+=monogramEntropy[i]

digramEntropy = 0
digramCount = 0
#counts digrams
for i in xrange(0,int(alphSize)):
    for j in xrange(0,int(alphSize)):
        digramCount+=digramList[i][j]
#creates entropy list
digramEntropy = digramList[:]
totalDigramEntropy = float(0)
for i in xrange(0,int(alphSize)):
    for j in xrange(0,int(alphSize)):
        digramEntropy[i][j] = digramList[i][j]/(textLenNoSpace-1)
        if digramEntropy[i][j]!=0:
            digramEntropy[i][j] = -1*(digramEntropy[i][j]*math.log(digramEntropy[i][j] ,2))
            totalDigramEntropy+=digramEntropy[i][j]/2

#calculating the entropy for trigrams
trigramEntropy = 0
trigramCount = 0
#counts trigrams
for i in xrange(0,int(alphSize)):
    for j in xrange(0,int(alphSize)):
        for k in xrange(0, int(alphSize)):
            trigramCount+=trigramList[i][j][k]
#creates entropy list
trigramEntropy = trigramList[:]
totalTrigramEntropy = float(0)
for i in xrange(0,int(alphSize)):
    for j in xrange(0,int(alphSize)):
        for k in xrange(0, int(alphSize)):
            trigramEntropy[i][j][k] = trigramList[i][j][k]/(textLenNoSpace-2)
            if trigramEntropy[i][j][k]!=0:
                trigramEntropy[i][j][k] = -1*(trigramEntropy[i][j][k]*math.log(trigramEntropy[i][j][k] ,2))
                totalTrigramEntropy+=trigramEntropy[i][j][k]/3

print "Absolute rate: " + str(absRate)
print "Monogram Entropy Approximation: " + str(totalMonogramEntropy)
print "Digram Entropy Approximation: " + str(totalDigramEntropy)
print "Trigram Entropy Approximation: " + str(totalTrigramEntropy)
