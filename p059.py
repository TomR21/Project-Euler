# PROBLEM 59
import numpy as np
import itertools

numlist = np.loadtxt("p059_cipher.txt", delimiter=",", unpack=False)
ascstring = ''.join(chr(int(i)) for i in numlist)

# General XOR decryption function
def xor(message, key):
    return "".join(chr(ord(x) ^ ord(y)) for x, y in zip(message, itertools.cycle(key)))

keylist = []
permlist = list(itertools.permutations("abcdefghijklmnopqrstuvwxyz", 3))
for item in permlist:
    key = "".join(item)
    decrypt = xor(ascstring, key)
    if decrypt.count("e") > len(decrypt) * 0.1:         # Check if atleast 10% of characters is "e", as it is most common in English language
        keylist.append(key)

for key in keylist:                              # Print out all keys with atleast 10% of characters being e, and check which one is readable
    decrypt = xor(ascstring, key)
    print("Key: "+ key + "   " + decrypt)

input_key = input("Which key")                      # Input the right key and get the sum of character values back
sum = 0
for char in xor(ascstring, input_key):
    sum += ord(char)

print(sum)
