a=int(input("Enter age:- "))
n=int(input("Enter no. of people:- "))
if(a<3):
    t=0
elif(a>3 and a<=12):
    t=100*n
elif(a>12):
    t=150*n
else:
    print("Invalid Input..Please Enter Integer")

print("Total cost for tickets:-" + str(t))