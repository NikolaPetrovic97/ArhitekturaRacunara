from multiprocessing import Pool
import os

def f(x):
    print('process id:', os.getppid())
    print('process id:', os.getpid())
    res = x * x
    print('res = ', res)
    return res

if __name__ == '__main__':
    print('process id:', os.getpid())
    with Pool(5) as p:
        print(p.map(f, [1, 2, 3]))