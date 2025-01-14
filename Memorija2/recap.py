class clstst:
    def __init__(self, name):
        self.name = name
        print("clstst ", self.name, " init")
    def __del__(self):
        print("clstst ", self.name, " delete")


def my_function():
        t = clstst("i")
        u = clstst("i")
        v = clstst("i")
        w = clstst("i")
        x = clstst("i")
        y = clstst("i")

my_function()

