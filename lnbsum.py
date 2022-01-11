a = [int(a) for a in input("Enter 5 values: ").split()]
sum=0
for i in range(0,5):
    if(a[i]>=9):
        sum+=a[i]

print(sum)