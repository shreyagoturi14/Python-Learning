#write a python fun to print multiplication table of given number
n=int(input("enter the number: "))   
def multiply(n):
    for i in range(1,11):
        print(f"{n}X{i}={n*i}")
        
multiply(n)
  
