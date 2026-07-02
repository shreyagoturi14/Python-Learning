# Can you change the self-parameter inside a class to something else(say "shreya")
#Try changing self to "slf" or "shreya" and see the effects.

# class Flowers:
#     name="rose"
#     color="white"
# def fun(slf):
#     print(f"the color of the {slf.name} is {slf.color}")   
# a=Flowers(slf.name,slf.color)

from random import randint
class Train:
    def __init__(slf,trainNo):
        slf.trainNo=trainNo
    
    def book(self,fro,to):
        print(f"Ticket is booked in train no: {self.trainNo},from {fro} to {to}") 
    
    def getStatus(self):
        print(f" train no: {self.trainNo} is running on time")
        
    def getFare(self,fro,to):
        print(f"Ticket fare in train no;{self.trainNo},from {fro} to {to} is {randint(222,55555)}")
    
t=Train(12399)
t.book("akkiwat","chikodi")
t.getStatus()
t.getFare("akkiwat","chikodi")
           