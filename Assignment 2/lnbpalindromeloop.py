def triangle(n):
     
    
    k = n - 1
 
    i=0
    while(i<2*n):
     
        j=0
        while(j<k):
            print(end="  ")
            j+=1
     
        
        k = k - 1
     
        j=0
        while(j<i+1):
            if(j%2==0):
                print("1 ",end="")
            
            else:
                print("8 ",end="")
            j+=1
     
        i+=2
        print("\r")
 

n = int(input("Enter no. of lines to print:- "))
triangle(n)