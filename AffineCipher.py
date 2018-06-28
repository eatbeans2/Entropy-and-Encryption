# -*- coding: utf-8 -*-
quit = 0
#program loop
while quit==0:
    #each menu option takes place in an "if command" based on input
    userMenuInput = input("Affine Cypher with Dummy Characters\nEnter 1 to Encrypt \nEnter 2 to Decrypt \nEnter 3 to quit\n")
    if userMenuInput==1:
        #this is the encryption process. Starts with key input
        userKeyInput = raw_input("Enter a Valid Key, in the form \"a,b,x,y,z\"\nThe first character is the Affine cipher, the second the added constant, and x, y, z are the dummy characters\n(NOTE: x<y<z, 0=<a,b,x,y,z<29), and a!=0):\n")
        #processes key input to find each particular character
        comma1 = userKeyInput.find(",")
        comma2 = userKeyInput[comma1+1:].find(",")+comma1+1
        comma3 = userKeyInput[comma2+1:].find(",")+comma2+1
        comma4 = userKeyInput[comma3+1:].find(",")+comma3+1
        #this variable is where we keep key components
        keyList = [int(userKeyInput[0:comma1])%29, int(userKeyInput[comma1+1:comma2])%29, int(userKeyInput[comma2+1:comma3])%29, int(userKeyInput[comma3+1:comma4])%29, int(userKeyInput[comma4+1:])%29]
        #here we check key formatting and, if all is well, start shuffling the dummy characters into the plaintext alphabet
        if keyList[2]!=keyList[3] and keyList[2]!=keyList[4] and keyList[3]!=keyList[4] and keyList[2]<keyList[3]<keyList[4] and keyList[0]!=0:
            alphabet=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","<",">","/"]
            newAlphabet=alphabet[:]
            newAlphabet[keyList[2]]=alphabet[26]
            for i in xrange(keyList[2]+1, 29):
                newAlphabet[i]=alphabet[(i-1)%29]
            newAlphabet[keyList[3]]=alphabet[27]
            for i in xrange(keyList[3]+1, 29):
                newAlphabet[i]=alphabet[(i-2)%29]
            newAlphabet[keyList[4]]=alphabet[28]
            for i in xrange(keyList[4]+1, 29):
                newAlphabet[i]=alphabet[(i-3)%29]
            #set both alphabets equal so that each letter can be encrypted
            alphabet=newAlphabet[:]
            #encrypts the newAlphabet using standard affine cipher procedure
            for i in xrange(0, 29):
                newAlphabet[i]=alphabet[(keyList[0]*i+keyList[1])%29]
            print alphabet[:]
            print newAlphabet[:]
            #takes the input to encrypt
            plainText = raw_input("Enter the message to be encrypted ('<', '>', and '/' are dud characters):\n")
            #cipherText is to be the encrypted output
            cipherText = plainText
            #replaces each character at a time with its respective encrypted counterpart
            wasChanged=[0]*len(plainText)
            for i in xrange(0,len(plainText)):
                notRep = 1
                plainTextCopy = plainText
                j = 0;
                while notRep == 1 and j < 29:
                    plainText = plainText[:i] + plainText[i].replace(alphabet[j], newAlphabet[j]) + plainText[i+1:]
                    if not plainTextCopy == plainText:
                        notRep = 0
                    j = j+1
            cipherText = plainText
            print cipherText
	else:
		print "It appears two dummy characters are equal, x<y<z does not hold, or a=1. Please fix the error."

    #This is the decryption option. Identical to encryption except we calculate the modular inverses for the key
    if userMenuInput==2:
        #Retrieving the key
        userKeyInput = raw_input("Enter the encryption key in the form \"a,b,x,y,z\"\nThe first character is the Affine cipher, the second the added constant, and x, y, z are the dummy characters\n(NOTE: x<y<z, 0=<a,b,x,y,z<29), and a!=0):\n")
        #processes key input to find each particular character
        comma1 = userKeyInput.find(",")
        comma2 = userKeyInput[comma1+1:].find(",")+comma1+1
        comma3 = userKeyInput[comma2+1:].find(",")+comma2+1
        comma4 = userKeyInput[comma3+1:].find(",")+comma3+1
        #this variable is where we keep key components
        keyList = [int(userKeyInput[0:comma1])%29, int(userKeyInput[comma1+1:comma2])%29, int(userKeyInput[comma2+1:comma3])%29, int(userKeyInput[comma3+1:comma4])%29, int(userKeyInput[comma4+1:])%29]
        if keyList[2]!=keyList[3] and keyList[2]!=keyList[4] and keyList[3]!=keyList[4] and keyList[2]<keyList[3]<keyList[4] and keyList[0]!=0:
            alphabet=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","<",">","/"]
            newAlphabet=alphabet[:]
            newAlphabet[keyList[2]]=alphabet[26]
            for i in xrange(keyList[2]+1, 29):
                newAlphabet[i]=alphabet[(i-1)%29]
            newAlphabet[keyList[3]]=alphabet[27]
            for i in xrange(keyList[3]+1, 29):
                newAlphabet[i]=alphabet[(i-2)%29]
            newAlphabet[keyList[4]]=alphabet[28]
            for i in xrange(keyList[4]+1, 29):
                newAlphabet[i]=alphabet[(i-3)%29]
            #set both alphabets equal so that each letter can be encrypted
            alphabet=newAlphabet[:]
            #encrypts the newAlphabet using standard affine cipher procedure
            for i in xrange(0, 29):
                newAlphabet[i]=alphabet[(keyList[0]*i+keyList[1])%29]
            print alphabet[:]
            print newAlphabet[:]
            #takes the input to encrypt
            plainText = raw_input("Enter the message to be decrypted ('<', '>', and '/' are dud characters):\n")
            #cipherText is to be the encrypted output
            cipherText = plainText
            #replaces each character at a time with its respective encrypted counterpart
            wasChanged=[0]*len(plainText)
            for i in xrange(0,len(plainText)):
                notRep = 1
                plainTextCopy = plainText
                j = 0;
                while notRep == 1 and j < 29:
                    plainText = plainText[:i] + plainText[i].replace(newAlphabet[j], alphabet[j]) + plainText[i+1:]
                    if not plainTextCopy == plainText:
                        notRep = 0
                    j = j+1
            cipherText = plainText
            print cipherText
        else:
            print "It appears two dummy characters are equal, x<y<z does not hold, or a=1. Please fix the error."
    if userMenuInput==3:
        print "Goodbye!"
        quit=1
