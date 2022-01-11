a=[int(a) for a in input("Enter intergers (Minimum 10 & Maximum 20):- ").split()]
b=[]
for i in a:
    c=bin(i)
    b.append(c)

c=b[-1]
d=b[-2]
e=(c and d) and (c or d)
print(int(e,2))