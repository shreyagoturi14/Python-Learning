class Employee:
    language="py"  #this is a class attribute
    salary=12000000
    
shreya=Employee()
shreya.name="Shreya" #this is an object attribute
print(shreya.name,shreya.salary,shreya.language)

bhagya=Employee()
bhagya.name="Bhagya" #this is an instance attribute
print(bhagya.name,bhagya.salary,bhagya.language)

#here name is instance attribute and salary and language and
#attributes as they directly belong to the class.