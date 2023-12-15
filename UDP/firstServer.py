import socket as sck

serverPort = 12000
# creating a socket (UDP socket)
serverSocket = sck.socket(sck.AF_INET, sck.SOCK_DGRAM)
# Binding port number 12000 to the server's socket
serverSocket.bind(('', serverPort))
print("Server is ready to recieve")
while True:
    # Reading message from socket and getting IP address of client
    message, clientAddress = serverSocket.recvfrom(2048)
    # modifying message to uppercase
    modifiedMessage = message.decode().upper()
    # Sending the modified message back to client.
    serverSocket.sendto(modifiedMessage.encode(), clientAddress)