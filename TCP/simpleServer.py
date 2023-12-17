import socket as sck

serverPort = 12000
serverSocket = sck.socket(sck.AF_INET, sck.SOCK_STREAM)
serverSocket.bind(('', serverPort))
# listen() method to listen for TCP connection requests from client
serverSocket.listen(1)
print("Server is ready.")
while True:
    # accept() to accept the connection request
    # and create a new socket dedicated to the particular client
    # This creates TCP connection between clientSocket and connectionSocket
    connectionSocket, addr = serverSocket.accept()
    message = connectionSocket.recv(2048).decode()
    modifiedMessage = message.upper()
    connectionSocket.send(modifiedMessage.encode())
    # Closing the connectionSocket.
    connectionSocket.close()
