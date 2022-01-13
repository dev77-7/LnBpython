
def dv():
    a=input("Are you interested in a poll about dream vacation (Yes or No):- ")
    a=a.lower()
    if(a=="yes") :
        places=[]
        for i in range(1,50):
            b=input("Enter Your Dream Vacation Places ((type done when you are finished with the list)):- ")
            b=b.lower
            if(b=="done"):
                dv()
            elif(b=="quit"):
                print(places)
            else:
                places.append(b)
            
    else:
        dv()

dv()