
class Student:
    
   collage_name="klecet"
   name="autonomus" #class attr
   def __init__(self,fullname):
     self.name=fullname #obj attr
     print("hello")
        
        
s1=Student("shreya")
print(s1.name,s1.collage_name)  
                 
s2=Student("nish")
print(s2.name)

print(Student.collage_name)  #while o/p it gives the shreya and nisha only bcz obj attr>class attr
