Data = ["PPPPP", "PPAPP", "AAAPP", "PAPAP", "AAAAA", "PAAAP", "PPPPP"]
for i in range(len(Data)):
    if(Data[i].count('A')==0):
        print(i+1)

