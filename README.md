# Entropy-and-Encryption
Final project attempting to affect (and measure) the unicity distance of ciphers by creating an expanded alphabet. This project is poorly organized, poorly implemented, and poorly documented. I will attempt to clean it up.

affineCipher.py uses a simple cipher to encrypt or decrypt text via a key.

The asciiEntropy files seem to calculate the entropy of a language sample given the size of the alphabet. NewAsciiEntropy seems to do this with a larger alphabet, probably used in junction with the xorEncryptor, while the original asciiEntropy is probably used with affineCipher.

xorEncryptory.py is a more practical cipher which uses bit xor to encode data

The entropyMeasurement file has two files for measuring entropy of text files, entropy.py and test.py
The charSpread.py file spreads false characters throughout text. This is to be used before encoding to affect the language entropy and resulting unicity distance.

PROBLEMS:
There seems to be a lot of redundancy. I obviously did not have a central plan when implementing this project. All the measurement programs have doubles. Similarly, there are multiple ciphers at play here.
There are limitations on the actual language, since I require some files to be strictly alphabet characters and so on. This could have been handled better.
Nothing is clearly documented. Even these vague explanations don't make this into a cohesive project. The original aim was to measure the entropy of ciphertext produced by a simple cipher when one enters a standard message as plaintext vs a message with additional false characters. This could have been done much more feasibly. I should return to this some day.
