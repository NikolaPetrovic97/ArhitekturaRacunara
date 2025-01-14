from multiprocessing import Process
import os

def info(title):
    print(title)
    print('module name:', __name__)
    print('parent process:', os.getppid())
    print('process id:', os.getpid())

def f(name):
    info('function f')
    print('hello', name)
    print('exiting', name)

if __name__ == '__main__':
    info('main line')
    p = Process(target=f, args=('bob',))
    s = Process(target=f, args=('sam',))
    p.start()
    s.start()
    print('main done, waiting on spawns')
    p.join()
    print('spawn p done')
    s.join()
    print('spawn s done')