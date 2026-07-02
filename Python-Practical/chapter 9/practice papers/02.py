# The game() fun in a program lets user play a game and returns the 
# score as an integer . you need to read a file "Hi-score.txt"
# which is either blank or contains the previous Hi-score. you
# need to write a pgm to update the Hi-score whenever the game()
# fun breaks the Hi-score.

import random 
def game():
    print("your playing game: ")
    score=random.randint(1,70)
    #fetch the Hi-score
    with open("hiscore.txt")as f:
        hiscore=f.read()
        if(hiscore!=""):
            hiscore=int(hiscore)
        else:
            hiscore=0
    print(f"your score: {score}")
    if(score>hiscore):
        #write this Hi-score to the file
        with open("hiscore.txt","w") as f:
            f.write(str(score))
            
    return score

game()