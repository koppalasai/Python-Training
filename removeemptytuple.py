T=T=list(input("enter list ").split())
print(T)
for i in T:
    if(len(i)>1):
        temp=list(i)
        temp.remove("(")
        temp.remove(")")
        if(len(temp)==0):
            continue
        print(i,end=' ' )   
    else:
        print(i,end=' ')     