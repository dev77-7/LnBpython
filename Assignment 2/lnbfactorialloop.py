b=[]
print("Enter 5 posiitve integers")
for i in range(0,5):
    a=int(input("Enter positive integers:- "))
    if(a>0):
        b.append(a)
    else:
        break

print(sum(b))
z=[]
for i in b:
    def fact(n):
        if n==0:
            return 1

        return n*fact(n-1)
    a=fact(i)
    z.append(a)

print(z)
    

