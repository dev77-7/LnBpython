a=input("Enter String:- ")
b=len(a)
if(b>7):
    print(a[1:b:2])
else:
    print(a[0:b:2])