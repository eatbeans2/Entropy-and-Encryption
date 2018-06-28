# Entropy-and-Encryption
Final project attempting to affect (and measure) the unicity distance of ciphers by creating an expanded alphabet. This project is poorly organized, poorly implemented, and poorly documented. I will attempt to clean it up.

affineCipher.py uses a simple cipher to encrypt or decrypt text via a key.

The asciiEntropy files seem to calculate the entropy of a language sample given the size of the alphabet. NewAsciiEntropy seems to do this with a larger alphabet, probably used in junction with the xorcipher, while the original asciiEntropy is probably used with affineCipher.
