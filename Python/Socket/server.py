import socket
import threading


class Server:
    def __init__(self):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.bind(('localhost', 22000))
        self.s.listen(2)
        self.connections = []

    def handler(self, c, a):
        while True:
            try:
                data = c.recv(1024)
            except:
                data = ''
            if not data:
                print(str(a[0]) + ':' + str(a[1]), 'is disconnected')
                self.connections.remove(c)
                c.close()
                break
            else:
                for connection in self.connections:
                    connection.send(data)

    def run(self):
        while True:
            c, a = self.s.accept()
            cThread = threading.Thread(target=self.handler, args=(c, a))
            cThread.daemon = True
            cThread.start()
            self.connections.append(c)
            print(str(a[0]) + ':' + str(a[1]), 'is connected')


server = Server()
server.run()