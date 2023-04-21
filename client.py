import socket
from server import *

def runClient(port): 
    clientSocket = socket.socket()
    clientSocket.connect(('127.0.0.1', int(port)))
    print ('c: Successfully connected server')
    print ('c: RSA_public_key_sender=' + readFromFile("cert/klient_key.pub"))
    print ('c: RSA_private_key_sender=' + readFromFile("cert/klient_key"))
    print ('c: RSA_public_key_receiver=' + readFromFile("cert/server_key.pub"))
    while True:
        message = input('Enter input: ')
        key = getRandomNumber(16)
        print ('c: AES_key=' + key.hex())
        padding = getRandomNumber(255 - (key.__sizeof__()))
        paddedKey = key + padding
        print ('c: AES_key_padding=' + paddedKey.hex())
        messageHash = createMD5hash(message.encode())
        print ('c: MD5=' + messageHash)
        padding = getRandomNumber(255 - (messageHash.__sizeof__()))
        paddedHash = messageHash + padding.hex()
        print ('c: MD5_padding=' + paddedHash)
        RSAencrypt(messageHash, "cert/klient_key")
        #rsaEncryptedHash = RSAencrypt(paddedHash, "cert/klient_key")
        #print ('c: RSA_MD5_hash=' + rsaEncryptedHash)


        #ENCODING 
        #clientSocket.send(messageHash.encode())
        #data = clientSocket.recv(4096).decode()
        #print('Received from server: ' + data)
    clientSockets.close()