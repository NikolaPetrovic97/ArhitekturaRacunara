f = open('test.txt', 'w')

l = []

for i in range(30):
    l.append(i)

for item in l:
  f.write("%s\n" % item)