from socket import *

serverName = '127.0.0.1'
serverPort = 25109

#create socket
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))

sentence = input("Enter file name: \n")

clientSocket.send(sentence.encode())
filecontents = clientSocket.recv(1024).decode()
print('File contents from Server:\n', filecontents)
clientSocket.close()
