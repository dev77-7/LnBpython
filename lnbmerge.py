kl=[int(kl) for kl in input("Enter keys for Dictionary:- ").split()]
vl=str(input("Enter Values for Dictionary:- "))
vl=vl.split()
print(len(vl))
final={kl[i]:vl[i] for i in range(len(kl))}
print(str(final))
