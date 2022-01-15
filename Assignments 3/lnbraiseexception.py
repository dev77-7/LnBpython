
def sam():
    try:
        a=int(input("Enter integer from 0-100:- "))
        if(a>0 and a<100):  
            print(a)
        else:
            print("Interger Entered is not between 0 and 100\nPlease try with an interger between 0 and 100")

    except ValueError:
        print("You need to enter a integer value\nPlease try again")
    
sam()