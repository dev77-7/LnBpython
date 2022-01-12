print("Main Menu\n1.Add\n2.Sub\n3/Multiply\n4.Divide\n5.Exit")
a=int(input("Enter Your Choice:- "))
answer=0
if(a!=5):
    if(a>0 and a<6):
        x=int(input("Enter A:- "))
        y=int(input("Enter B:- "))

        if(a==1):
            print(x+y)
        elif(a==2):
            print(x-y)
        elif(a==3):
            print(x*y)
        elif(a==4):
            print(x/y)
    else:
        print("Invalid Input....Try Again")
else:
    print("Exited")