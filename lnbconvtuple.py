a=tuple(input("Enter values for tuple:-").split())
print(a)
print(type(a))
b=input("Enter Sring:- ")
a=list(a)
for i in range(1,2*len(a),2):
    a.insert(i,b)
    
a=tuple(a)
print(a)
print(type(a))