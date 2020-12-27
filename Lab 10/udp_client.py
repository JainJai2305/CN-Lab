from socket import *
serverName = "127.0.0.1"
serverPort = 65198

# Create a UDP socket at client side
clientSocket = socket(AF_INET, SOCK_DGRAM)

sentence = input("Enter file name: ")

#send to server using created UDP socket
clientSocket.sendto(bytes(sentence, "utf-8"), (serverName, serverPort))

filecontents, serverAddress = clientSocket.recvfrom(2048)

print('File contents from Server:', filecontents)

clientSocket.close()
