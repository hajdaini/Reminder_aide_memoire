# SERVEUR : 

```py
import socket

#SOCK_STREAM : protocole TCP.
server = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
server.bind(('localhost', 42000))
server.listen(1)
client, info = server.accept()
message = ''
while message != 'fin':
    client.send('5/5'.encode())
    message = client.recv(1024).decode()
    print('Client > ', message)

client.close()
server.close()
```

# CLIENT :

```py
import socket

client = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
client.connect(('localhost', 42000))

message = ''
while message != 'fin':
    message = input('Client > ')
    client.send(message.encode())
    print('Serveur > ', client.recv(1024).decode())
client.close()
```
