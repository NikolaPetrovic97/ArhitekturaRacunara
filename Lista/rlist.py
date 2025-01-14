with open('test.txt') as f:
    niz = f.read().splitlines()

print(niz)

lst = []

with open('test.txt') as fl:
	for line in fl:
		lst.append(int(line))

print(lst)