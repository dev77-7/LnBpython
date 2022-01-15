def lnbsum():
    try:
        a=int(input("Enter First integer for sum:- "))
        b=int(input("Enter Second integer for sum:- "))
        print("Sum:-",a+b)
    except ZeroDivisionError:
        print("Division by zero is not allowed\nPlease try again with a divisor greater than zero")
    except NameError:
        print("The variable you enetered is not defined in the code\nPlease try again with some integer value")
    except TypeError:
        print("The operand you entered are not supported\nPlease try agin with integers input")
    except ValueError:
        print("You cant operate a interger with a string\nPlease try with two integers")

def lnbdiv():
    try:
        c=int(input("Enter First integer for Division:- "))
        d=int(input("Enter Second integer for Divison:- "))
        print(a/b)
    except ZeroDivisionError:
        print("Division by zero is not allowed\nPlease try again with a divisor greater than zero")
    except NameError:
        print("The variable you enetered is not defined in the code\nPlease try again with some integer value")
    except TypeError:
        print("The operand you entered are not supported\nPlease try agin with integers input")
    except ValueError:
        print("You cant operate a interger with a string\nPlease try with two integers")


lnbsum()
lnbdiv()