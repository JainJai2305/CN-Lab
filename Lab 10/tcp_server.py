from socket import *

serverName = '127.0.0.1'
serverPort = 25109

#create
serverSocket = socket(AF_INET, SOCK_STREAM)

#bind
serverSocket.bind((serverName, serverPort))

#listen
serverSocket.listen(1)

print("The server is ready to receive: TCP")
while 1:
    connectionSocket, addr = serverSocket.accept()
    print("Client has been connected from : ",addr)
    sentence = connectionSocket.recv(1024).decode()

    file = open(sentence, "r")
    l = file.read(1024)

    connectionSocket.send(l.encode())
    file.close()
    connectionSocket.close()
