class Employee:
    language="python" #this is a class attribute
    salary=120000000
    
    def getInfo(self):
        print(f"the language is {self.language}. the salary is {self.salary}")
        
        
    def greet(self):
        print("happy morning")
        
shreya=Employee()
shreya.language="java"
# shreya.getInfo()  # you can write this or below line it gives output
Employee.getInfo(shreya)
shreya.greet()