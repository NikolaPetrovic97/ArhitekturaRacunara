
f = open('test.txt', 'r')

niz = []

for i in range(10):
    niz.append(float(f.readline()))

print(niz)

f.close()
