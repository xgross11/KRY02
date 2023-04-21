import sys
import hashlib
import math
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

_random_source = open("/dev/random", "rb")

from client import *
from kry import *

def readFromFile(filepath):
    file = open(filepath, "r")
    return file.read()

def writeInFile(content, filepath):
    file = open(filepath, "w")
    file.write(content)
    file.close()

def generateKeys():
    keyPair = RSA.generate(2048)
 
    pubKey = keyPair.publickey().exportKey()
    writeInFile(pubKey.decode('ascii'), "cert/klient_key.pub")
    privKey = keyPair.exportKey()
    writeInFile(privKey.decode('ascii'), "cert/klient_key")

    keyPair = RSA.generate(2048)
    pubKey = keyPair.publickey().exportKey()
    writeInFile(pubKey.decode('ascii'), "cert/server_key.pub")
    privKey = keyPair.exportKey()
    writeInFile(privKey.decode('ascii'), "cert/server_key")

def createMD5hash(message):
    return hashlib.md5(message).hexdigest()

def getRandomNumber(bytes):
    return _random_source.read(bytes)

def encoder(message):
    encoded = []
    # Calling the encrypting function in encoding function
    for letter in message:
        encoded.append(encrypt(ord(letter)))
    return encoded
 
 
def decoder(encoded):
    s = ''
    # Calling the decrypting function decoding function
    for num in encoded:
        s += chr(decrypt(num))
    return s

def RSAencrypt(message, keyPath):
    readKey = readFromFile(keyPath)
    key = RSA.importKey(readKey) #key = Private RSA key at ....
    print(key)
    #encryptor = PKCS1_OAEP.new(key)
    #return encryptor.encrypt(msg)

def RSAdecrypt():
    return



if __name__ == '__main__':
    port = sys.argv[1]
    type = sys.argv[2]

    # uncomment for generating new pair of keys every run
    #generateKeys()

    # """ CLIENT """

    if type == 'c':   # run as client
        runClient(port)

    # """ SERVER """

    else:             # run as server
        runServer(port)

