import random
import time


## Turn System
player_hp = 30
computer_hp = 30

# Sample moves - Name: [Damage, Hitting % Chance]
example_moves_class = {
    "Kick": [18, 50],
    "Stomp": [12, 75],
    "Shout": [5, 100],
}


# Player's class, will be decided at beginning of game
player_class = example_moves_class

# More variables for turn system
player_turn = True # True = Player's Turn | False = Computer's Turn
player_move = "" # Name of player's move
computer_move = "" # Name of Computer's move

move_lands = 0 # Used for calculating if a move hits or misses

def play_turn():
    if player_turn == True:

        #input placeholder (will become a gui button)
        player_move = input("It's your turn. What's your move: ")

        # Determine if move lands (hits or misses)
        if player_class[player_move][1] == 100:
            print("100% chance")
        else:
            move_lands = random.randint(1, 100)

            # If the move lands
            if move_lands <= player_class[player_move][1]:
                print(computer_hp)
                computer_hp -= player_class[player_move][0]
                print("computer's hp: " + str(computer_hp))

            # If it's a miss
            else:
                print("Missed your move")

        #player_turn = false

    # computer's turn
    else:

        #input placeholder (will become a gui button)
        player_move = input("It's the computer's turn")

        

play_turn()
play_turn()
play_turn()
play_turn()
play_turn()
