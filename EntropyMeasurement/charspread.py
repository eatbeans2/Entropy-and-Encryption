import random

#this program aims to add false characters according to inputted probabilities
charCount = 0
prob1 = 0.
prob2 = 0.
prob3 = 0.

print "This program inserts 1-3 dummy characters into the file 'rewrite.txt' according to the inputted probabilities (inputted as decimals '.0xx' with two sig figs."
print "The edited document is outputted as another file, 'rewriteDone.txt'"
charCount = int(raw_input("Input 1-3 for character count: "))
if charCount > 0:
    prob1 = float(raw_input("Input the probability for character 1: "))*1000
    if charCount > 1:
        prob2 = float(raw_input("Input the probability for character 2: "))*1000
        if charCount > 2:
            prob3 = float(raw_input("Input the probability for character 3: "))*1000
readFile = open("rewrite.txt", "r")
editFile =readFile.read()
readFile.close()
skipIt = 0
for i in xrange(0, len(editFile)):
    if random.randint(1,1001) < prob1:
        editFile = editFile[:i+skipIt] + '<' + editFile[i+skipIt:]
        skipIt += 1
    if random.randint(1,1001) < prob2:
        editFile = editFile[:i+skipIt] + '>' + editFile[i+skipIt:]
        skipIt += 1
    if random.randint(1,1001) < prob3:
        editFile = editFile[:i+skipIt] + '/' + editFile[i+skipIt:]
writeFile = open("rewriteDone.txt", "w+")
writeFile.write(editFile[:])
writeFile.close()
