try:
    a=int(input("hii,Enter a number: "))
    print(a)
    
except ValueError as v:
    print("hello")
    print(v)
    
except Exception as e:
    print(e)
    
print("thank you")