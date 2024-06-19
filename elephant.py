n=int(input("enter number of friends house"))
if(n<=5):
    print(1)
elif(n%5==0):
    print(n/5)
else:
    print("number of steps",(n//5)+1)
