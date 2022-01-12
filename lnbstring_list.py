para=input("Enter a sentence or paragraph:- ")
sli=para.split()
L=[word for word in sli if len(word) >=4]
print(L)