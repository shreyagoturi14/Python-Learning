#if elif else 
a=int(input("Enter your age: "))
if(a>18):
    print("your are above the age of consent")
    print("good for you")
elif(a<0):
    print("you are entering an invalid age")
elif(a==0):
    print("you are entering zero it is an invalid")
     
else:
    print("your are below the age of consent")
print("end of the pgm")
    