class Employee:
    language="python" #this is a class attribute
    salary=120000000
    
    def __init__(self,name,salary,language):
        self.name=name
        self.salary=salary
        self.language=language
        print("I am creating an object")
    
    def getInfo(self):
        print(f"the language is {self.language}. the salary is {self.salary}")
        
    @staticmethod
    def greet():
        print("happy morning")
        
shreya=Employee("shreya",1300000,"JavaScript")
print(shreya.name,shreya.salary,shreya.language)