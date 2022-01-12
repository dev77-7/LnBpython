a=input("Enter String to Search:- ")
sample=open("sample.txt","r")
current=0
stop=0
for line in sample:
    current+=1
    if a in line:
        stop=1
        break

if(stop==1):
    print("String",a,"found in line no.",current )
else:
    print("String not found")