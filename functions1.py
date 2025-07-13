def mul(n):
    for i in range(1,n):
        for j in range(1,11):
            print("{}*{}={}".format(i,j,i*j),end="")
        print()
n=int(input("enter the number:"))
mul(n)