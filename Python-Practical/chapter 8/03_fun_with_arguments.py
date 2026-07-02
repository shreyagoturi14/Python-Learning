#1
def goodDay(name):
    print("good day," + name)
    
goodDay("shreya")

#2
def happymorning(name,ending):
    print("Happy  Morning," +  name)
    print(ending)
    
happymorning("shreya","thank you")
happymorning("nishh","thanks")
happymorning("ashu","tq")


#3
def greet(name):
    gr="hello"+ name
    return gr
a=greet("goturi")
print(a)


#4 pgm using return
def happymorning(name,ending):
    print("Happy  Morning," +  name)
    print(ending)
    return "have a nice day"
    
a=happymorning("shrey","thank you")
print(a)