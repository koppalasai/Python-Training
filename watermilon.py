w=int(input("enter weight of watermilon"))
if(w%2!=0 or w==2):
      print("odd")
else:
    x=w/2
    if(x%2==0):
        print("yes,brother 1 gets",x,"brother 2 gets",x)
    else:
         print("yes,brother 1 gets",x-1,"brother 2 gets",x+1)
        
