# Create a class "programmer" for storing information of few
#programmers working microsoft.

class Programmer:
    company="Microsoft"
    def __init__(self,name,salary,pin):
        self.name=name
        self.salary=salary
        self.pin=pin
        
p=Programmer("Shreya",120000000,291225)
print(p.name,p.salary,p.pin,p.company)

      
r=Programmer("ranjani",1200,291225)
print(r.name,r.salary,r.pin,r.company)
        