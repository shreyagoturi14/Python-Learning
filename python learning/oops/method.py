class Student:
    c_n="klecet"
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
        
    def wellcome(self):  #method
        print("Welcome student,")
        
    def get_marks(self): #method
        return self.marks
            
s1=Student("shreya",100)
print(s1.name)
s1.wellcome()
print(s1.get_marks())