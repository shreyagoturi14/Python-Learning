#2 create a class 'pets' from a class 'animals' and further create a class 'dog' from 'pets'. add method 'bark' to class 'dog'.
class Animals:
    pass

class Pets(Animals):
    pass

class Dog(Pets):
    @staticmethod
    def bark():
        print("Bow Bow!")
        
        
d=Dog()
d.bark()
    