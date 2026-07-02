a=int(input("Enter a number: "))
b=int(input("Enter the secend nummber: "))

if(b==0):
    raise ZeroDivisionError("hi our program is not meant to divide numbers by zero")
else:
    print(f"The dividion a/b is{a/b}")