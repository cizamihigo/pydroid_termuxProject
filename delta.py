#git 
import math

print("welcome to my program")
a = int(input("*Enter a number* :  "))
b = int(input("*Enter a number* :  "))
c = int(input("*Enter a number* :  "))

delta = b* b -(4 *a * c)

if delta == 0 : 
    vardelta =0
    vardelta = (-b)/ 2*a
    #print(vardelta)
elif delta > 0 :
    vardelta1 = 0.1
    vardelta2 = 0.1
    
    vardelta1 =  (-b + (delta * 0.5)) / (2* a)
    
    vardelta2 =  (-b - (delta * 0.5)) / (2* a)
    
    print("X1 =   ", vardelta1)
    #print(vardelta2)
    
    
    print("X2 =   ", vardelta2)
    
