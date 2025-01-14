import os


print('process id:', os.getppid())
print('process id:', os.getpid())

response = input("Please enter your name: ")
    
print("Hello %s" % response)
    
print("exiting...")
