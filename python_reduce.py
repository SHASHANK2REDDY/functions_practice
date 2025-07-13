from functools import reduce
# l1=[]
# for i in range (20,31):
#     i=i*2
#     l1.append(i)
# print(l1)
# def reduces(a,b):
#     return a+b
# reducing=reduce(reduces,l1)
# print(reducing)
l1=[]
for i in range(20,31):
    l1.append(i)
print(f"the list before converting:{l1}")
reducing=reduce(lambda a,b:a+b,l1)
print(reducing)