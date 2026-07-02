
a=int(input("Enter your age: "))
#if stamt 1
if(a%2==0):
   print("a is even")
#end of if stmt 1


#if stmt 2
if(a>=18):
    print("your are above the age of consent")
    print("good for you")
elif(a<0):
    print("you are entering an invalid age")
elif(a==0):
    print("you are entering zero it is an invalid")
     
else:
    print("your are below the age of consent")
#end of stmt2

print("end of the pgm")
    