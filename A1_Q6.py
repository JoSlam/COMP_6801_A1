##Course: COMP 6801
##Name: Joshua Lambert
##ID: 815007658
##Assignment_1

import random
from A1_Q3 import findPrimitiveRoot
from A1_Q6_DES import DESEncryption


#generate private key
def getRandomNum(p):
    return random.randrange(1, p)

#generate public key
def generatePublic(g, d, p):
    return pow(g, d, p)

def encryptElGamal(msg, p, e, g):
    msg_arr = []

    k = getRandomNum(p)
    enKey = pow(e, k, p)

    c_first = pow(g, k, p)
    
    for i in range(0, len(msg)):
        msg_arr.append(msg[i])

    for i in range(0, len(msg_arr)):
        msg_arr[i] = ord(msg_arr[i]) * enKey

    return msg_arr, c_first


def decryptElGamal(msg, c_first, key, p):
    decr_msg = []
    divisor = pow(c_first, key, p)

    for i in range(0, len(msg)): 
        decr_msg.append(chr(int(ord(msg[i])/divisor))) 
          
    return "".join(decr_msg) 


def encrypt():
    #load message
    msgData = ""
    with open("NoWar.dat", "r") as warFile:
        msgData = warFile.read()

    ciph, c_first = encryptElGamal(msgData, p, e, g)
    encodedMsg = list(map(lambda x: chr(x), ciph))
    
    pubKey = "{0},{1},{2}".format(p,g,c_first)
    with open("publickey.dat", "w") as pubKeyFile:
        pubKeyFile.write(pubKey)

    #save encrypted message
    with open("Trump.dat", "w", encoding="utf-16") as tFile:
        tFile.write("".join(encodedMsg))



def decrypt():
    privKey = ""
    publicKey = ""
    secrKey = ""
    encryptedMsg = ""

    #load priv key
    with open("privatekey.dat", "rb") as privKeyFile:
        privKeyEncrypted = privKeyFile.read()
    
    #load des secr key
    with open("secretkey.dat", "r") as secrKeyFile:
        secrKey = secrKeyFile.read()

    #decrypt priv key
    desEncr = DESEncryption(bytes(secrKey, "utf8"))
    privKey = desEncr.decryptDES(privKeyEncrypted)

    #load encrypted msg
    with open("Trump.dat", "r", encoding="utf-16") as encrFile:
        encryptedMsg = encrFile.read()

    #load public key
    with open("publickey.dat", "r") as pubKeyFile:
        p, g, c_first = pubKeyFile.read().split(",")

    #decrypt msg
    decryptElGamal(encryptedMsg, c_first, privKey, p)


if __name__ == "__main__":
    p = 5711                    #large prime
    g = findPrimitiveRoot(p)    #primitive root

    key = getRandomNum(p)
    e = generatePublic(g, key, p)

    secrKey = b'secrpass'
    desEncr = DESEncryption(secrKey)
    privKey = desEncr.encryptDES(str(key))

    #write keys to files
    with open("privatekey.dat", "wb") as privKeyFile:
        privKeyFile.write(privKey)

    encrypt()
    decrypt()