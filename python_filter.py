l1=[]
for i in range(0,11):
    i=i**2/2
    l1.append(i)
print(f"the list before filtering:{l1}")
# def filters(n):
#     if n>18:
#         return n
# filtering=filter(filters,l1)
filtering=filter(lambda a:(a**2/2)>18,l1)
print(list(filtering))