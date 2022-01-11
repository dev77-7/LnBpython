from itertools import islice
L=[int (L) for L in range(1,21)]
print(L)
L2=[]
L3=[]
lenl=len(L)
for i in range(0,5):
    L2.append(L[i])
for i in range(len(L)-5,len(L)):
    L2.append(L[i])
print(L2)
for i in L2:
    a=i*i
    L3.append(a)
print(L3)
L4=iter(L3)
lts=[2,3,5]
final=[list(islice(L4,i))for i in lts]
print(final)

