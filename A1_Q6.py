##Course: COMP 6801
##Name: Joshua Lambert
##ID: 815007658
##Assignment_1

import random
from A1_Q3 import findPrimitiveRoot

p = 5711
g = findPrimitiveRoot(p)

#generate private key
def generatePrivate(p):
    return random.randrange(1, p)

#generate public key
def generatePublic(g, d, p):
    return pow(g, d, p)



if __name__ == "__main__":
    d = generatePrivate(p)
    e = generatePublic(g, d, p)
    print("{0} - {1}", e, d)