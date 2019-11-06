##Course: COMP 6801
##Name: Joshua Lambert
##ID: 815007658
##Assignment_1

import random
from A1_Q3 import findPrimitiveRoot
from A1_Q6_DES import DESEncryption


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

    secrKey = b'secrpass'
    desEncr = DESEncryption(secrKey)

    pubKey = "{0},{1},{2}".format(p,g,e)
    privKey = desEncr.encryptDES(str(d))

    #write keys to files
    with open("privatekey.dat", "wb") as privKeyFile:
        privKeyFile.write(privKey)

    with open("publickey.dat", "w") as pubKeyFile:
        pubKeyFile.write(pubKey)



    #load message
    trumpMsgData = ""
    with open("Trump.dat", "r") as trumpFile:
        trumpMsgData = trumpFile.read()

    # with open("privatekey.dat", "rb") as readKeyFile:
    #     val = readKeyFile.read()
    #     decrVal = desEncr.decryptDES(val)
    #     print(decrVal)