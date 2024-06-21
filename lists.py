l=input("enter list").split("#")
print(l)
l=list(map(int,input("enter list").split("#")))
print(l)
#indexing#
l[2]=50
print("after changing of index number to another",l)
#list methods#
l.append([1,2,3])
print("after append",l)
l.extend([1,2,3])
print("after extend",l)
l.insert(1,"car")
print("after inster",l)
l.remove(10)
print("after remove",l)
l.pop(-1)
print("after pop",l)
l.index(20)
print("position",l)
l.count(20)
print(l)
l2=l.copy()
print("after copy",l2)
l.sort()
print("after sorting",l)
l.reverse()
print("after reverse",l)
l.clear()
print("after clear",l)




