import threading
import socket
from queue import Queue

lock = threading.Lock()
target = "server_address"
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
list_ports_open = []
def scanner(port):
    try:
        client = s.connect((target, port))
        with lock:
            print(port, 'is open')
            list_ports_open.append(port)
    except:
        pass


def threader():
    while True:
        worker = q.get()
        scanner(worker)
        q.task_done()

q = Queue()

for x in range(30):
    t = threading.Thread(target= threader)
    t.daemon = True
    t.start()

for worker in range(1, 1025):
    q.put(worker)

q.join()

if len(list_ports_open) == 0:
    print('All port are closed')

print("\nScan complete")
