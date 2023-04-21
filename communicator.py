import socket

class Communicator:
    def __init__(self, port. type):
        self.port = port
        self.type = type + ": "

    def printMessage(self, message):
        print (this.type + message)

    def createSocket(self):
        this.socket = createSocket()
    
    def connect(self, host):
        this.socket.connect(host, this.port)

    def listen(self):
        this.socket.listen()

    def bind(self, host):
        this.socket.bind(host, this.port)
    
    def receive(self):
        this. recvBuffer = this.socket.recv(1024)
    
    def closeSocket(self):
        this.socket.close()  