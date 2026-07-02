#write a python fun to print first n lines of the following pattern
#***
#**
#* for n=3

def pattern(n):
    if(n==0):
        return
    print("*" * n)
    pattern(n-1)
p=int(input("enter the number: "))
pattern(p)