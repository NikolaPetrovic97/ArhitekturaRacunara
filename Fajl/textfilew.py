f = open('test.txt', 'w')

#probati izlaz sa jednom i sa drugom petljom
for i in range(500):
	f.write(str(i))

# for i in range(500):
# 	f.write(str(i) + '\n')

f.close()