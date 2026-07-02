#factorial(n)=n*factorial(n-1)

# def factorial(n):
if(n==1 or n==0):
     return 1
 return n*factorial(n-1)
n=int(input("Eneter a number: "))
print(f"The factiorial of number is: {factorial(n)}")