a=[int(a) for a in input("Enter 5 integers:- ").split()]
if len(a)>5:
    print("You have to enter 5 numeric values\nRe-run the code")
else:
    a.sort(reverse=True)
    print("Values in decresing order:-",a)
    print("Sum of values:-",sum(a))