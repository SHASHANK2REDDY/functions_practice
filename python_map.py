# # l1=[]
# # for i in range(1,10):
# #     l1.append(i)
# # print("before maping: ")
# # print(l1)
# # def square(n):
# #     return n*2
# # maping=map(square,l1)
# # print(list(maping))

# buy using ananonymous function
l1=[]
for i in range (0,11):
    l1.append(i)
print(f"before updateing l1:{l1}")
# def square(n):
#     return n**2
maping=map(lambda n:n**n,l1)
print(list(maping))