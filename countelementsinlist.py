T=list(input("enter list ").split())
print(T)
count=0
for i in T:
    if "(" in i:
        break
    count+=1
print(count)        