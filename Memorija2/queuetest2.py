from multiprocessing import Process, Queue

def f(q):
	lst = q.get()
	for i in range(len(lst)):
		x = lst[i]
		lst[i] = x * x
	q.put(lst)

if __name__ == '__main__':
	q = Queue()
	lst = [1, 2, 3, 4, 5]
	q.put(lst)
	p = Process(target=f, args=(q,))
	p.start()
	p.join()
	print(q.get())
