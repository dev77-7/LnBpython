a=10
b=20
c=12
final=0
if(a>b and a>c):
    greater=a
elif(a>b and a<c):
    greater=c
elif(b>a and b>c):
    greater=b
elif(b>a and b<c):
    greater=c
while(True):
    if(greater%a==0 and greater%b==0 and greater%c==0):
        final=greater
        break
    greater+=1
print(final)
    