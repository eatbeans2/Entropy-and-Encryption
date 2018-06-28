import binascii
from random import randint


print "This program doubles the ASCII alphabet, shuffles characters, encrypts a message using a generated vignere cipher of length x,  and returns a key and encoded message in hexidecimal format"
menuOption = int(raw_input("Enter 1 to encrypt a message or 2 to decrypt:\n"))
if menuOption == 1:
    rawMessage = raw_input("Enter the message to be encrypted/decrypted:\n").decode("utf-8").encode("latin-1")
    keyLen = int(raw_input("Enter the length of the key to be generated:\n"))
#encryption process
    rawKey = []
#firstly we shuffle the standard alphabet into a two-byte alphabet
    shufAlph = [['', '']]*94
    for i in xrange(0, 94):
        repeat = 1
        while repeat == 1:
            shufAlph[i] = [chr(randint(32, 126)), chr(randint(32,126))]
            repeat = 0
            for j in xrange(0, i):
                if shufAlph[i][0] == shufAlph[j][0] and shufAlph[i][1] == shufAlph[j][1]:
                    repeat = 1
                    break
#now we must encode the new message according to the new alphabet
    newMessage = ''
    for i in rawMessage:
        newMessage = newMessage + shufAlph[ord(i)-32][0]+shufAlph[ord(i)-32][1]
#generates the key two bytes at a time, storing the two bytes as individual characters
    for i in xrange(0, keyLen):
        rawKey.append(randint(32,126))
        rawKey.append(randint(32,126))
    encodeMessage = ''
    counter = 0
    for ch in newMessage:
        encodeMessage = encodeMessage + str(ord(ch)^rawKey[counter]) + ' '
        if counter == len(rawKey)-1:
            counter = 0
        else:
            counter += 1
    encodeMessage = encodeMessage[:-1]
    print "The following is your message:"
    print encodeMessage.encode("base64").replace("\n", "")
    print "The following is your key:"
    keyString = ''
    for i in xrange(0, len(rawKey)):
        keyString = keyString + str(rawKey[i]) + " "
    print keyString[:-1].encode("base64").replace("\n", "")
    print "And the following is your alphabet index:"
    print shufAlph
    alphString = ''
    for i in xrange(0, 94):
        alphString = alphString + shufAlph[i][0] + shufAlph[i][1]
    alphString = alphString.encode("base64")
    print alphString.replace("\n", "")

#this is the decode process
if menuOption == 2:
#collecting inputs
    cipherText = raw_input("Enter the ciphertext:\n").decode("base64")
    inputKey = raw_input("Enter the key (not the alphabet):\n").decode("base64")
    alphScram = raw_input("Enter the alphabet index:\n").decode("base64")
    shufAlph = [['', '']]*94
#lots of formatting. Strings must be made back into lists
    for i in xrange(0, len(alphScram)/2):
        shufAlph[i] = [alphScram[2*i],  alphScram[2*i+1]]
    rawKey = []
    inputKey = ' ' + inputKey[:]
    cipherText = ' ' + cipherText[:]
    print cipherText
#formatting the key into a list using spaces as dividers
    for i in xrange(0, len(inputKey)):
        if inputKey[i] == ' ':
            nextKey = ''
            for j in inputKey[i+1:]:
                if j == ' ':
                    break
                else:
                    nextKey = nextKey + j
            rawKey.append(nextKey)
#un'XOR'ing each member of the ciphertext
    counter = 0
    plainText = ''
    for i in xrange(0, len(cipherText)):
        nextChar = ''
        if cipherText[i] == ' ':
            for j in cipherText[i+1:]:
                if j == ' ':
                    break
                else:
                    nextChar = nextChar + j
        if nextChar != '':
            plainText = plainText + chr(int(nextChar)^int(rawKey[counter]))
            if counter == len(rawKey)-1:
                counter = 0
            else:
                counter += 1
#finally we unshuffle the output members
    decoded = ''
    for i in xrange(0, len(plainText)/2):
        for j in xrange(0, 94):
            if plainText[i*2] == shufAlph[j][0] and plainText[i*2+1] == shufAlph[j][1]:
                decoded = decoded + chr(j+32)
    print decoded
