import random

## Turn System
player_hp = 30
player_alive = True
computer_hp = 30
computer_alive = True

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

# Deal damage to computer (bot) player
def damage_computer(amount, bot_hp):

    alive = True

    bot_hp -= amount 
    print("computer's hp: " + str(bot_hp))

    if bot_hp <= 0:
        alive = False
        bot_hp = 0

    return bot_hp, alive

def play_turn(bot_hp, plr_hp):
    
    if player_turn == True:

        print("computer's hp: " + str(bot_hp))
        
        #input placeholder (will become a gui button)
        player_move = input("It's your turn. What's your move: ")

        # If 100% chance it ihts
        if player_class[player_move][1] == 100:
            print("100% chance")
            bot_hp = damage_computer(player_class[player_move][0], bot_hp)

        # Determine if it's a hit or a miss
        else:
            move_lands = random.randint(1, 100)

            # If the move lands
            if move_lands <= player_class[player_move][1]:
               bot_hp, alive = damage_computer(player_class[player_move][0], bot_hp)
               print(alive)

            # If it's a miss
            else:
                print("Missed your move")

        #player_turn = false

    # computer's turn
    else:

        #input placeholder (will become a gui button)
        player_move = input("It's the computer's turn")

    # return computer and player health levels
    return bot_hp, plr_hp

        

computer_hp, player_hp = play_turn(computer_hp, player_hp)
computer_hp, player_hp = play_turn(computer_hp, player_hp)
computer_hp, player_hp = play_turn(computer_hp, player_hp)
computer_hp, player_hp = play_turn(computer_hp, player_hp)
computer_hp, player_hp = play_turn(computer_hp, player_hp)
computer_hp, player_hp = play_turn(computer_hp, player_hp)
computer_hp, player_hp = play_turn(computer_hp, player_hp)
computer_hp, player_hp = play_turn(computer_hp, player_hp)
computer_hp, player_hp = play_turn(computer_hp, player_hp)
computer_hp, player_hp = play_turn(computer_hp, player_hp)

