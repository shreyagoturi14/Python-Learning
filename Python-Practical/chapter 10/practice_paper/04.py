# Add a static method in problem2, to greet the user with hello.

class Calculator:
    def __init__(self,n):
        self.n=n
    
    def square(self):
        print(f"the square is {self.n*self.n}")
        
    def cube(self):
        print(f"cube is {self.n*self.n*self.n}")
        
    def square_root(self):
        print(f"square root is {self.n**1/2}")
        
    @staticmethod
    def greet():
        print("happy morning")   
  
  
a=Calculator(4)
a.greet()
a.square()
a.cube()
a.square_root()
# a.greet()