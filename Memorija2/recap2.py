class clstst:
    def __init__(self, name):
        self.name = name
        print("clstst ", self.name, " init")
    def __del__(self):
        print("clstst ", self.name, " delete")

test1 = 20

def my_function():
        print(test1)
#        test1 += 1

my_function()



for i in range(5):
	clstst(i)
	test2 = i

print(test2)