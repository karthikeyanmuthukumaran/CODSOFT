import random
def play():
    player=str(input("s stands for Scissor , s stands for Rock and p stands for Paper :")).lower()
    choose=["s","r","p"]
    computer=random.choice(choose)

    print(f"your choice {player} <=> opponent {computer}")

    if(player == computer):
        print("GAME IS IN TIE")
    elif(player == 'r' and computer == 's' or player == 'p' and computer == 'r' or player == 's' and computer == 'p'):
        print("PLAYER WON THE GAME")
    else:
        print("well tried !!, BETTER LUCK NEXT TIME")
 

play()