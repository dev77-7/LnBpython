def div(a,b):
    print(a/b)

def div2(func):
    def inner(a,b):
        if(a>b):
            return func(a,b)
        if(b>a):
            a,b=b,a
            return func(a,b)
    return inner

fin=div2(div)
fin(4,2)
