import threading
from queue import Queue
import time

lock = threading.Lock()
q = Queue()
workers_nbr = 20
threads_nbr = 10

# 20 travailleurs
for worker in range(workers_nbr):
    q.put(worker) # mettre un travailleur au travail :p


def exampleJob(worker):
    time.sleep(0.5)
    with lock:
        print(threading.current_thread().name, worker)


def threader():
    while not q.empty():
        worker = q.get() # 2 travailleurs pour chaque thread
        exampleJob(worker)
        q.task_done() #Vider la queue


for x in range(threads_nbr):
    t = threading.Thread(target= threader)
    t.daemon = True # Quand le main Thread est terminé alors ce thread la se termine aussi
    t.start()

start_time = time.time()
q.join()  # bloquer jusqu'à ce que toutes les tâches soient terminées
print('Entire job took : {}'.format((time.time() - start_time)))
