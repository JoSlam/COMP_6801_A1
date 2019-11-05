##Course: COMP 6801
##Name: Joshua Lambert
##ID: 815007658
##Assignment_1

import random
from A1_Q3 import findPrimitiveRoot
from A1_Q6_DES import encryptDES
from A1_Q6_DES import decryptDES


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

    privKey = encryptDES(str(d))

    with open("privatekey.dat", "wb") as privKeyFile:
        privKeyFile.write(privKey)

    with open("privatekey.dat", "rb") as readKeyFile:
        val = readKeyFile.read()
        decrVal = decryptDES(val)
        print(decrVal.decode("utf8"))