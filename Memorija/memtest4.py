class clstst:
    def __init__(self, name):
        self.name = name
        print("clstst ", self.name, " init")
    def __del__(self):
        print("clstst ", self.name, " delete")

def my_function():
    for i in range(30):
        t = clstst(i)

my_function()
