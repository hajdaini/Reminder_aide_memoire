import socket
import threading

class Client:

    def __init__(self):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.connect(('localhost', 22000))

    def send_msg(self):
        while True:
            msg = input()
            self.s.send(msg.encode())

    def run(self):
        iThread = threading.Thread(target=self.send_msg)
        iThread.daemon = True
        iThread.start()

        while True:
            data = self.s.recv(1024)
            if not data:
                break
            else:
                print('Server >', data.decode())

    def dead(self):
        self.s.close()

client = Client()
client.run()
client.dead()




