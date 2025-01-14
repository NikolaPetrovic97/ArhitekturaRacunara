f = open('test.txt', 'r')

#probati citanje na vise nacina
#print(f.read())

# print(f.readline())
# print(f.readline())
# print(f.readline())
# print(f.readline())

# f.seek(300) #uociti problem sa funkcijom seek kod tekstualnih fajlova
# with f as ins:
#     array = []
#     for line in ins:
#         array.append(int(line))
# print(array)

f.close()