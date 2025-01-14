import threading
import os

z = 0

def f(x, broj):
    global z
    y = x * broj
    print("rezultat = ", y)
    z += y

x1 = 4
x2 = 3.6
x3 = 2.8
broj1 = 4.24
broj2 = 2.4
broj3 = 1.345
t1 = threading.Thread(target=f, args=(x1, broj1,))
t1.start()
t2 = threading.Thread(target=f, args=(x2, broj2,))
t2.start()
t3 = threading.Thread(target=f, args=(x3, broj3,))
t3.start()
    
t1.join()
t2.join()
t3.join()
    
print("konacno = ", z)
