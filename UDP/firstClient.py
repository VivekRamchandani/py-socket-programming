import socket as sck

# serverName stores IP address or the hostname (hostmachine name) of server
serverName = sck.gethostname()
serverPort = 12000
# clientSocket is client's socket
clientSocket = sck.socket(sck.AF_INET, sck.SOCK_DGRAM)
# First parameter of socket() is Address Family (AF_INET = IPv4)
# Second parameter of socket() Socket Kind (SOCK_DGRAM = UDP)
message = input('Input lowercase sentence: ')
# sendto() method to send message to a address
clientSocket.sendto(message.encode(), (serverName, serverPort))
# using recvfrom() method to read the message from the socket
modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
# recvfrom() method takes the buffer size as 
# the recvfrom() method return the message message and IP address of server
print(modifiedMessage.decode())
clientSocket.close()