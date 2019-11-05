import Crypto
from Crypto.Cipher import DES

password = b'secrpass' 

##--Padding--##
def pad(item):
    if(len(item) % 8 != 0):
        item += '0' * (8 - (len(item) % 8))
    return item

def encryptDES(plaintext):
    desLib = DES.new(password, DES.MODE_ECB)
    paddedItem = pad(plaintext)
    return desLib.encrypt((paddedItem.encode("utf8")))