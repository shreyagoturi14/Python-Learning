#7 override the __len__() method on vector of problem 5 to displaay the dimention of the vector
#5 write a class vector representing vector of n dimenstions. overload the +and * operator which calculates the sum and dot(.) product of them
class Vector:
    def __init__(self,l):
       self.l=l
     
   
    
    def __len__(self):
        return len(self.l)
    
#test the implemention
v1=Vector([1,2,3])
print(len(v1))