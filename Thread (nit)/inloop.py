import threading
import os

lock = threading.Lock()
cnt = 0

def worker(num):
    global lock
    global cnt
    """thread worker function"""
    for i in range(3000):
        lock.acquire()
        tmp = cnt + 1
        for j in range(1000):
            u = j
        cnt = tmp
        lock.release()
    print('process id:', os.getpid())
    print ('Worker: %s' % num)
    return

threads = []
for i in range(15):
    t = threading.Thread(target=worker, args=(i, ))
    threads.append(t)
    t.start()
    
for t in threads:
    t.join()
    
print('final count = ', cnt)