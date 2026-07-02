# project 1:snake , water , gun game
import random
'''
1 for snake
-1 for water 0 for gun
'''

computer=random.choice([-1,0,1])
youstr=input("Enter your choice: ")
youDict={"s":1,"w":-1,"g":0}
reverseDict={1:"Snake",-1:"Water",0:"Gun"}
you=youDict[youstr]
print(f"You choose {reverseDict[you]}\nComputer choose {reverseDict [computer]}")
if(computer == you):
    print("Its a draw")
else:
    if((computer - you )== -1 or (computer - you ) == 2):
        print("you lose")
    else:
        print("you win")