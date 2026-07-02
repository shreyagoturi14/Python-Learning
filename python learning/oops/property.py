class Student():
    def __init__(self,phy,chem,math):
        self.phy=phy
        self.chem=chem
        self.math=math
        
        
        
    # def calpercentage(self):
    #     self.percentage=str((self.phy + self.chem + self.math)/3)+"%"
        #  "we can write it as below easly" 
        
    @property
    def percentage(self):
        return str((self.phy + self.chem + self.math)/3)+"%"
        
        
stu1=Student(98,99,100)
print(stu1.percentage)

stu1.phy=86
print(stu1.percentage)