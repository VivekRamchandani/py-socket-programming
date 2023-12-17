import socket as sck

serverName = '127.0.0.1'
serverPort = 12000
# SOCK_STREAM = TDP
clientSocket = sck.socket(sck.AF_INET, sck.SOCK_STREAM)
clientSocket.connect((serverName, serverPort))
message = input("Enter message in lowercase: ")
clientSocket.send(message.encode())
modifiedMessage = clientSocket.recv(2048)
print('From Server: ', modifiedMessage.decode())
clientSocket.close()