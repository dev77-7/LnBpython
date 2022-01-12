from itertools import islice
L=[int(L) for L in input("Enter Numbers to list:- ").split()]
print(L)
L2=[]
for i in range(100,501):
    if(i%11==0):
        if(i%2!=0 and i%3!=0):
            L2.append(i)

print(L2)

mts=[2,4,6]
L2=iter(L2)
final=[tuple(islice(L2,i)) for i in mts]
print(tuple(final))
