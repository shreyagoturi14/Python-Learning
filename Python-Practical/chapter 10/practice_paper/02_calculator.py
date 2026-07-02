# write a class "calculator" capable of finding square, cube,
#and square root of a number.
class Calculator:
    def __init__(self,n):
        self.n=n
    
    def square(self):
        print(f"the square is {self.n*self.n}")
        
    def cube(self):
        print(f"cube is {self.n*self.n*self.n}")
        
    def square_root(self):
        print(f"square root is {self.n**1/2}")
        
a=Calculator(4)
a.square()
a.cube()
a.square_root()