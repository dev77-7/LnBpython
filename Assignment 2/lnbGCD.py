a=[int(a) for a in input("Enter integers:- ").split()]
def gcd(x,y):
    if(x==0):
        return y
    if(y==0):
        return x
    if(x==y):
        return x
    if(x>y):
        return gcd(x-y,y)
    return gcd(x,y-x)
final=[]
for i in range(0,len(a)-1):
    f=a[i]
    s=a[i+1]
    
    final.append(gcd(f,s))
print(a)
print(final)
