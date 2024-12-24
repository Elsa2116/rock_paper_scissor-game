import random
choices=["rock","paper","scissor"]
def determine_winner(player,computer):
    if player == computer:
        return "it is a tie"
    elif(player =="rock" and computer =="scissor") or\
    (player =="paper" and computer =="rock") or\
    (player =="scissor" and computer =="paper" ):
        return "player win"
    else:
        return "player loss"
def play_game():
        print("welcome to rock,paper,scissor game")
       
        while(True):
            choice = ["rock","paper","scissor"]
            player_choice = input("please enter your choice:")
            if player_choice not in choice:
                print("invalid input.please try again")
                continue
            computer_choice = random.choice(choices)
            print("computers choice:{computer_choice}")
            result = determine_winner(player_choice,computer_choice)
            print(result)

            play_again = input("do you want to play again(yes or no)")
            if play_again !="yes":
                print("thanks for playing the game:goodbye!")
                break
play_game()