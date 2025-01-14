
f = open('test.txt', 'w')

niz = []

for i in range(10):
    niz.append(i + 0.00005)

for i in range(10):
    f.write(str(niz[i]) + '\n')

f.close()
