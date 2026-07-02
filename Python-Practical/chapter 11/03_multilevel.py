
class Employee:
    company="ITC"
    name="shreya"
    def show(self):
        print(f"The name of the Employee is {self.name} and the company is{self.company}")
        
class Coder:
    language="python"
    def printlanguages(self):
        print(f"out of all the language here is your language:{self.language}")
        
class Programmer(Employee,Coder):
    company="ITC Infotech"
    def showlanguage(self):
        print(f"The name is {self.company}and he is good with {self.language} language")
      
class Manager(Programmer):
    list="somepeople"
    def printlanguage(self):
        print(f"the  list is {self.list} and he is good with {self.language}")
        
a=Employee()
b=Programmer()
c=Manager()

c.show()
c.printlanguages()
c.showlanguage()
c.printlanguage()


class Employee:
    a=1
class Programmer(Employee):
    b=2
class Manager(Programmer):
    c=3
    
o=Employee()
print(o.a) #prints the a attribute
#print(o.b) #shows error as there is no b attribute in employee class

o=Programmer()
print(o.a,o.b)

o=Manager()
print(o.a,o.b,o.c)