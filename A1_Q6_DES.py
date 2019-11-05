import Crypto
from Crypto.Cipher import DES

password = b'secrpass'
desLib = DES.new(password, DES.MODE_ECB)

##--Padding--##
def pad(item):
    if(len(item) % 8 != 0):
        item += '0' * (8 - (len(item) % 8))
    return item

def encryptDES(plaintext):
    paddedItem = pad(plaintext)
    return desLib.encrypt((paddedItem.encode("utf8")))


def decryptDES(cipherText):
    return desLib.decrypt(cipherText)