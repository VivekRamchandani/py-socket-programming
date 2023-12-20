import socket as sck

serverPort = 1234
serverSocket = sck.socket(sck.AF_INET, sck.SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
print("Server is ready.")
while True:
    connectionSocket, addr = serverSocket.accept()
    htmlMsg = f"<html><head><title>Got you!</title></head><body>Hello, {addr[0]}</body></html>"
    httpMsg = f"""HTTP/1.1 200 OK\r\n\
    Connection: keep-alive\r\n\
    Server: Apache/2.2.3 (Linux Mint)\r\n\
    Last-Modified: Fri, 20 Oct 2023 22:02:03 IST\r\n\
    Content-Length: {len(htmlMsg)}\r\n\
    Content-type: text/html\r\n\r\n""" + htmlMsg
    request = connectionSocket.recv(2048).decode()
    print(request)
    connectionSocket.send(httpMsg.encode())
    connectionSocket.close()
