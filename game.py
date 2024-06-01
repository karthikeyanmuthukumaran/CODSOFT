import random
#importing required library

def play():
    player=str(input("s stands for Scissor , s stands for Rock and p stands for Paper :")).lower()
    #player turn
    
    choose=["s","r","p"]
    computer=random.choice(choose) #computer turn 

    print(f"your choice {player} <=> opponent {computer}")

    #if the game is in tie , no one win 
    if(player == computer):
        print("GAME IS IN TIE")

    #possibilities of player gets win
    elif(player == 'r' and computer == 's' or player == 'p' and computer == 'r' or player == 's' and computer == 'p'):
        print("PLAYER WON THE GAME")
    
    #or else the computer will be won
    else:
        print("well tried !!, BETTER LUCK NEXT TIME")
 

play()
