from multiprocessing import Process, Manager

def f(d, l):
    d[1] = '1'
    d['2'] = 2
    d[0.25] = None
    l.reverse()

if __name__ == '__main__':
    lst = []
    for i in range(20):
        lst.append(i + 3)

    with Manager() as manager:
        d = manager.dict()



        l = manager.list(lst)
#        l = manager.list(range(10))

        p = Process(target=f, args=(d, l))
        p.start()
        p.join()

        print(d)
        print(l)