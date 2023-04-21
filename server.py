import socket
from kry import *

def runServer(port): 
    serverSocket = socket.socket()
    serverSocket.bind(("127.0.0.1", int(port)))
    serverSocket.listen(5)
    conn, addr = serverSocket.accept()
    print ('s: Client has joined')
    print ('s: RSA_public_key_receiver=' + readFromFile("cert/server_key.pub"))
    print ('s: RSA_private_key_receiver=' + readFromFile("cert/server_key"))
    print ('s: RSA_public_key_sender=' + readFromFile("cert/klient_key.pub"))
    while True:
        data = conn.recv(4096).decode()
        if not data: 
            break
        print("ciphertext=" + str(data))
        #conn.send("I am SERVER\n".encode())
    conn.close()