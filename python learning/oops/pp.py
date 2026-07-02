#create student class that takes name & marks of 3 sub as arguments in constructor.then create a method to print the average.
class Student:
    def  __init__(self,name,marks):
        self.name=name
        self.marks=marks
        

    def average(self):
        sum=0
        for val in self.marks:
            sum+=val
        print("hi",self.name,"your average is",sum/3)
    
    
s1=Student("shreya",[67,56,78])        
s1.average()

s1.name="nish"
s1.average()