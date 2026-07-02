# class Student():
#     name="shreya"
#     def __init__(self):
#         print(self)
#         print("hello")
        
        
# s1=Student()  #hello



class Student:
    
    #default constucture
   def __init__(self):
      pass
  
  #parameterized constucture
   def __init__(self,fullname):
     self.name=fullname
     print("hello")
        
        
s1=Student("shreya")
print(s1.name)  # hello
                 #shreya
s2=Student("nish")
print(s2.name)#hello #nish