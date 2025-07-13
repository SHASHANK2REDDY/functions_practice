def double(*n):
    l1=[]
    for i in n:
        for j in range(0,11):
            print("{} * {} = {}".format(i,j,i*j),end=" ")
        print()
n=[12,2,3,54,5,15,9,10]
double(*n)
