from multiprocessing import Process
import os

z = 0

def f(x, broj):
    global z
    y = x * broj
    print("rezultat = ", y)
    z += y

if __name__ == '__main__':
    x1 = 4
    x2 = 3.6
    x3 = 2.8
    broj1 = 4.24
    broj2 = 2.4
    broj3 = 1.345
    p = Process(target=f, args=(x1, broj1,))
    s = Process(target=f, args=(x2, broj2,))
    r = Process(target=f, args=(x3, broj3,))
    p.start()
    s.start()
    r.start()
    print('main done, waiting on spawns')
    p.join()
    print('spawn p done')
    s.join()
    print('spawn s done')
    r.join()
    print("konacno = ", z)
