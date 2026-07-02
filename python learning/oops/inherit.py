class Car:
    color="black"
    @staticmethod
    def start():
        print("car started")
        
    @staticmethod
    def stop():
        print("car stoped")
        
class ToyotaCar(Car):
        def __init__(self,name):
            self.name=name
            
car1=ToyotaCar("fortune")
car2=ToyotaCar("prius")

print(car1.start())
print(car1.color)