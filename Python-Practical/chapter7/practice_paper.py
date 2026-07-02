#1 write pgm to print multiplication table of a given number number using for loop
n=int(input("enter the number: "))
for i in range(1,11):
    print(f"{n} X {i} = {n*i}")
    
    
#2 write a pgm to greet all the person names stored in a list
#'l' and which starts with s
#l=["shreya","nisha","pooja","spoorti"]
l=["shreya","nisha","pooja","spoorti"]
for name in l:
    if(name.startswith("s")):
        print(f"hello{name}")
        

#3 attemt pgm1 using while loop
n=int(input("enter the number: "))
i=1
while(i<11):
    print(f"{n} X {i} = {n*i}")
    i+=1
    
    
#4 write a pgm to find whether a given number is prime or not
n=int(input("enter the number: "))
for i in range(2,n):
    if(n%i)==0:
        print("number is not prime")
        break
else:
        print("number is prime")
        
        
#5 write a pgm to find the sum of first n natural number using while loop
n=int(input("Enter the number"))
i=1
sum=0
while(i<=n):
    sum+=i
    i+=1
print(sum)


#6 write pgm to calculate the factorial of a given number using for loop
n=int(input("Enetr the number: "))
product=1
for i in range(1,n+1):
    product=product*i
print(f"The factorial of {n} is {product}")
    
    
#7 write pgm to print following
    #   *
    #  ***
    # ***** for n=3
# print("  *  ")
# print(" *** ")
# print("*****")
n=int(input("Enter the number: "))
for i in range(1,n+1):
    print(" "* (n-i),end="")
    print("*"*(2*i-1),end="")  #end="" it by default new line it dont give if we use this
    print("")
    
    
#8write pgm to print following
    # *
    # **
    # *** for n=3

n=int(input("Enter the number: "))
for i in range(1,n+1):
    print("*"*i,end="")  #end="" it by default new line it dont give if we use this
    print("")

#9 write pgm to print following
    # ***
    # * *
    # *** for n=3
    # 
n=int(input("Enter the number: "))
for i in range(1,n+1):
    if(i==1 or i==n):
        print("*"* n,end="")
    else:
        print("*",end="")
        print(" "* (n-2),end="")
        print("*",end="")
    print("")
    
    
#10 write pgm to print multiplication table of n using for loops in reversed order
n=int(input("Enter the number: "))
for i in range(1,11):
    print(f"{n}X{11-i}={n*(11-i)}")
    