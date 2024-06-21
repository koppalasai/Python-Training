l=list(map(int,input("enter list").split("_")))
l2=sum(l)
print("sum=",l2)
l2=min(l)
print("min=",l2)
l2=max(l)
print("max=",l2)
print(all(l))
print(any(l))
print("length of list",len(l))
l1=list(map(int,input("enter list").split("_")))
l3=l+l1
print("after cancat",l3)
l3=l*l1
print("after repitation",l3)
l3=20 in l1
print(l3)

