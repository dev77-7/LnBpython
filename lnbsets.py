from os import name


try:
    from googlesearch import search
except ImportError:
    print("No module named 'google' found")
 

query =input("Enter query to search:- ")
final={}
final=set(final)
for j in search(query, tld="co.in", num=10, stop=10, pause=2):
    final.add(j)
print(list(final))
nameset=[]
b=list(final)
a=b[3]
nameset.append(a)

nameset=set(nameset)
print(nameset)
