from multiprocessing import Lock
from multiprocessing import Process



def f(l, i):
    print('inside process ', i)
    l.acquire()
    try:
        print('hello world', i)
    finally:
        l.release()
        

if __name__ == '__main__':
    lock = Lock()

    for num in range(10):
        print('creating process ', num)
        Process(target=f, args=(lock, num)).start()
