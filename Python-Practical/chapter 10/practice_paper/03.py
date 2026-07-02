# create a class with a class attribute a; create an object from 
#it and set 'a' directly using object.a=0. Does this change
#the class attribute?


# Answer is NO

class Demo:
    a=4
    
o=Demo()
print(o.a) #prints the classs attribute bcz instant atttribute is not present
o.a=0  #instance attribute is set
print(o.a) #prints the instance attribute bcz instance attribute is present
print(Demo.a) #prints the class attributes.
