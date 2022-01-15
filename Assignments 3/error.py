def lnbsum(a,b):
    try:
        print("Sum:-",a+b)
    except ZeroDivisionError:
        print("Division by zero is not allowed\nPlease try again with a divisor greater than zero")
    except NameError:
        print("The variable you enetered is not defined in the code\nPlease try again with some integer value")
    except TypeError:
        print("The operand you entered are not supported\nPlease try agin with integers input")

def lnbdiv(a,b):
    try:
        print(a/b)
    except ZeroDivisionError:
        print("Division by zero is not allowed\nPlease try again with a divisor greater than zero")
    except NameError:
        print("The variable you enetered is not defined in the code\nPlease try again with some integer value")
    except TypeError:
        print("The operand you entered are not supported\nPlease try agin with integers input")
a=int(input("Enter First integer for sum:- "))
b=int(input("Enter Second integer for sum:- "))
c=int(input("Enter First integer for Division:- "))
d=int(input("Enter Second integer for Divison:- "))
lnbsum(a,b)
lnbdiv(c,d)