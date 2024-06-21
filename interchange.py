l=list(map(int,input("enter list").split(" ")))
print(l)
l[0],l[-1]=l[-1],l[0]
print(l)
