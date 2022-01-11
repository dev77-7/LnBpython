L1 = [11, 21, 24, 12, 18]
L2 = [14, 44, 25, 37, 13]
L3=[]
l1len=len(L1)
l2len=len(L2)
for i in range(0,l1len,2):
    a=L1[i]
    L3.append(a)
for i in range(1,l2len,2):
    a=L2[i]
    L3.append(a)
print(L3)

