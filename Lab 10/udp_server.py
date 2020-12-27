from socket import *
serverPort = 65198

# Create a datagram socket
serverSocket = socket(AF_INET, SOCK_DGRAM)

# Bind to address and ip
serverSocket.bind(("127.0.0.1", serverPort))

print("The server is ready to receive: UDP")

# Listen for incoming datagrams
while 1:
    sentence, clientAddress = serverSocket.recvfrom(2048)

    file = open(sentence, "r")
    l = file.read(2048)

    # Sending a reply to client
    serverSocket.sendto(bytes(l, "utf-8"), clientAddress)
    print("Sent back to client", l)
file.close()
