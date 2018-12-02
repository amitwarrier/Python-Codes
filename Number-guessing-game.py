# -*- coding: utf-8 -*-
"""
Created on Fri Apr  7 22:06:52 2017

@author: Amit Warrier
"""
n1=0
n2=5000
res="y"
print("\nThink of a number between 1 and 10000.")

print("\nType y for yes and n for no.")
count=0

while (res=="y"):
    count=count+1
    if (n1+1)!=n2:
        res=input("\nIs the number between "+str(n1+1)+" and "+ str(int(n2))+"?:")
    else:
        res=input("\nIs the number "+str(n1+1)+"?:")
        
    if (n1>10000 or ((res!="y") & (res!="n"))):
        print("\nPlease check your responses.")
        break
    if ((res=="y")&((n1+1)==n2)):
        break
    elif res=="y":
        n3=int(((n2-n1)+1)/2)
        n2=n1+n3
    elif ((res=="n")&((n1+1)==n2)):
        n2=n2+1
        break
    elif res=="n":
        while (res=="n"):
            count=count+1
            n3=int(((n2-n1)+1)/2)
            n1=n2
            n2=n2+n3
            if (n1>10000 or ((res!="y") & (res!="n"))):
                print("\nPlease check your responses.")
                break
            if (n1+1)!=n2:
                res=input("\nIs the number between "+str(n1+1)+" and "+ str(int(n2))+"?:")
            else:
                res=input("\nIs the number "+str(n1+1)+"?:")
            if (n1>10000 or ((res!="y") & (res!="n"))):
                print("\nPlease check your responses.")
                break
            if ((res=="n")&((n1+1)==n2)):
                n2=n2+1
                break
        if ((res=="y")&((n1+1)==n2)):
            break
        elif res=="y":
            n3=int(((n2-n1)+1)/2)
            n2=n1+n3
if ((n2<10001) & (res=="y" or res=="n")) :       
    print("\nNumber is "+str(n2)) 
    print("\nNo of Attempts:"+str(count))      
input("\n\nPress enter key to exit.")          
            
        
       
