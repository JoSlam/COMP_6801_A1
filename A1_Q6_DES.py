import Crypto
from Crypto.Cipher import DES

class DESEncryption:
    def __init__(self, key):
        self.key = key
        self.desLib = DES.new(self.key, DES.MODE_ECB)

    ##--Padding--##
    def pad(self, item):
        if(len(item) % 8 != 0):
            item += ' ' * (8 - (len(item) % 8))
        return item

    def removePadding(self, item):
        return item.rstrip(" ")

    def encryptDES(self, plaintext):
        paddedItem = self.pad(plaintext)
        return self.desLib.encrypt((paddedItem.encode("utf8")))

    def decryptDES(self, cipherText):
        decrVal = self.desLib.decrypt(cipherText).decode("utf8")
        return self.removePadding(decrVal)