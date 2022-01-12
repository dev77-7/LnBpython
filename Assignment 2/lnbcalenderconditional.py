a=int(input("Enter Year:- "))
b=int(input("Enter Month:- "))
c=int(input("Enter Day:- "))
L=[[12,1,2],[3,4,5],[6,7,8],[9,10,11]]
if(b in L[0]):
    season="Winter"
elif(b in L[1]):
    season="Spring"
elif(b in L[2]):
    season="Summer"
elif(b in L[3]):
    season="Automn"
else:
    print("Invalid Month\nPlease Enter value from 1 to 12 only")

print("Season on Given Date-" + str(season))

if(a%400==0 or a%4==0 and a%100!=0):
    print("366 Days")
else:
    while True:
         a+=1
         if(a%400==0 or a%4==0 and a%100!=0):
             print("Next Leap Year is " + str(a))
             break
   
    


