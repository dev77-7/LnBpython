a=input("Enter Binary numbers:- ").split()
print(a)
v=[]
for i in a:
   if(len(i)>3 and len(i)<5):
        a=int(i)
        if(a%5==0):
            v.append(i)
            
        else:
            a+=1
            v.append(bin(a))

print(v)