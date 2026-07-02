# write a pgm using function to find greatest of three numbers
def fun1():
    if(a>b and a>c):
        print("a is a gretest number")
    elif(b>a and b>c):
        print("b is the gretest number")
    elif(c>a and c>b):
        print("c is the gretest number")

a=int(input("Enter the number:"))
b=int(input("Enter the number:"))
c=int(input("Enter the number:"))
fun1()

#harry solve
def greatest(a,b,c):
    if(a>b and a>c):
        return a
    elif(b>a and b>c):
        return b
    elif(c>a and c>b):
        return c
# a=int(input("Enter the number:"))
# b=int(input("Enter the number:"))
# c=int(input("Enter the number:"))
a=1
b=4
c=99
print(greatest (a,b,c))