#3 write a list comprehension to print a liist which contains the multiplication table of a user entered number
n=int(input("Enter a number: "))
n=5

table=[n*i for i in range(1,11) ]
print(table)