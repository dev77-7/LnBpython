def cal():
    x=input("Calculator Opened enter 'n' to continue and 'quit' to exit:- ")
    x=x.lower()
    if(x=="n"):
        a=[input("Enter 1 Interger then 1 operator and then 1 integer separated by spaces:- ").split()]
        if(len(a[0])==3):
            if(a[0][1]=="+"):
                print(int(a[0][0])+int(a[0][2]))
                cal()
            elif(a[0][1]=="-"):
                print(int(a[0][0])-int(a[0][2]))
                cal()
            else:
                print("Formula Error\nPleases Try again with '+' or '-'")
                cal()   
        else:
            print("Formula Error\nPlease try to enter 2 integers and 1 operator in the given order")
            cal()

    elif(x=="quit"):
        return

cal()