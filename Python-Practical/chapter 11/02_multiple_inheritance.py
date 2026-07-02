
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
        
a=Employee()
b=Programmer()

b.show()
b.printlanguages()
b.showlanguage()