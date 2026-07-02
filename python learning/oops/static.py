class Student:
    def  __init__(self,name,marks):
        self.name=name
        self.marks=marks
        
        
    @staticmethod
    def hello():
        print("hiheloo")
        
    def average(self):
        sum=0
        for val in self.marks:
            sum+=val
        print("hi",self.name,"your average is",sum/3)
    
    
s1=Student("shreya",[67,56,78])        
s1.average()

s1.hello()