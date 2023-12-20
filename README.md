# Socket Programming in Python
Creating clients and servers using TCP and UDP sockets.

## fakeWebServer
The [fakeWebServer.py](./TCP/fakeWebServer.py) responds to HTTP messages arriving at port $1234$, with HTTP/1.1 ($200$) message:

```http
HTTP/1.1 200 OK
Connection: keep-alive
Server: Apache/2.2.3 (Linux)
Last-Modified: Fri, 20 Oct 2023 22:02:03 IST
Content-Length: _data_length
Content-Type: text/html

(data)
```

<br>

**Browser Output:** <br>
Hello, {*your_ip_addr*}