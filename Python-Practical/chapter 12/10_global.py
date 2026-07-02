a=89 #global variable

def fun():
    # global a #it changes the global value.
    a=3
    print(a)
    
fun()
print(a)