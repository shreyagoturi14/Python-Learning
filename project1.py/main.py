
#  SNAKE , WATER ,GUN GAME    
  
# Rules of Water–Snake–Gun:
    # Snake drinks Water → Snake wins
    # Gun shoots Snake → Gun wins
    # Gun sinks in Water → Water wins

      
import random   # Import random module to let computer make random choices
'''
1 for snake
-1 for water
0 for gun
'''
computer=random.choice([-1,0,1])
youstr=input("Enter your choice: ")
youDict={"s":1,"w":-1,"g":0}
reverseDict={1:"Snake",-1:"Water",0:"Gun"}
you=youDict[youstr]
print(f"You choose {reverseDict[you]}\nComputer choose {reverseDict [computer]}")
if(computer == you):    #if both choose same than it's tie.
    print("Its a draw")
else:
    if(computer == -1 and you==1):
        print("you won the  game")
    elif(computer==-1 and you==0):
        print("you lost the game")
       
    elif(computer==1 and you==-1):
        print("you lost the game")
       
    elif(computer==1 and you==0):
        print("you won the game")
       
    elif(computer==0 and you==-1):
        print("you won the game")
       
    elif(computer==0 and you==1):
        print("you lost the game")
        
    else:
        print("Something went wrong")
       