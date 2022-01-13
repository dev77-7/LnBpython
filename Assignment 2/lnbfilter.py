final2=[]
final=[]
def even_filter(a):
    for i in a:
        if(i%2!=0):
            final.append(i)
    print(final)
def odd_filter(a):
    for i in a:
        if(i%2==0):
            final2.append(i)
    print(final)
l=[int(l) for l in input("Enter list of numbers:- ").split()]
even_filter(l)
odd_filter(l)