class Car:
    color="black"
    @staticmethod
    def start():
        print("car started")
        
    @staticmethod
    def stop():
        print("car stoped")
        
class ToyotaCar(Car):
        def __init__(self,brand):
            self.name=brand
            
class Fortune(ToyotaCar):
    def __init__(self,type):
        self.type=type
            
car1=Fortune("diesel")
car1.start()