try:
    from googlesearch import search
except ImportError:
    print("No module named 'google' found")
 

query = "Most Popular 5 Modules in Deep Learning"
final={}
final=set(final)
for j in search(query, tld="co.in", num=5, stop=6, pause=2):
    final.add(j)
print(final)