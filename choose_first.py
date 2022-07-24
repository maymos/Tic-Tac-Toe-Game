import random

mylist = [1,2]

def choose_first():
    random.shuffle(mylist)
    player1,player2=mylist[0],mylist[1]
    if player1==1:
        print("Player 1 plays First")
        return player1,player2
    else:
        print("Player 2 plays First")
        return player1,player2 