# def fun1():
#     if(a>b and a>c):
#         print("a is large")
#     elif(b>a and b>c):
#         print("b is large")
#     elif(c>a and c>b):
#         print("c is large")
# a=int(input("enter the number: "))
# b=int(input("enter the number: "))
# c=int(input("enter the number: "))
# fun1()

# def convert():
#      return 5*(f-32)/9
    
# f=int(input("enter a degree"))
# print(convert())


# def sum(n):
#     if (n==1):
#      return 1
#     return sum(n-1)+n
# print(sum(9))


# def pattern(n):
#     if(n==0):
#         return 
#     print("*" * n)
#     pattern(n-1)
# n=int(input("Enter the number:c"))
# pattern(n)


# def i_to_c(inchs):
#     return inchs*2.54
# n=int(input("Enter the inch: "))
# print(i_to_c(n))



# def rem(l,word):
#     n=[]
#     for item in l:
#         if not(item==word):
#             n.append(item.strip(word))
#     return n
# l=["shaeya","hem","asha","nisha"]
# print(rem(l,"sh"))


def multiply(n):
    for i in range(1,11):
        print(f"{n*i}")
n=int(input("Enter the number: "))
print(multiply(n))