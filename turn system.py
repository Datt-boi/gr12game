import random

# Player's moves
# Sample moves - Name: [Damage, Hitting % Chance]
example_moves_class = {
    "Kick": [12, 50],
    "Stomp": [8, 75],
    "Shout": [5, 100],
}

# Bot's moves
# Sample moves - Name: [Damage, Hitting % Chance]
example_moves_bot = {
    "Kick": [18, 100],
    "Stomp": [12, 75],
    "Shout": [5, 100],
}

## Enemies System
current_enemies = []

class Enemy:
    def __init__(self, health, name, moves):
        self.hp = health
        self.name = name
        self.moves = moves

        print(self.moves)

    # Deal damage to computer (bot) player
    def damage_computer(self, amount):

        self.hp -= amount 
        print("computer's hp: " + str(current_enemies[0].hp))

        if self.hp <= 0:
            self.hp = 0
            return current_enemies[0].hp, False # alive = false
        else:
            return current_enemies[0].hp, True # alive = true

## Specific Enemies

class Zombie(Enemy):
    def __init__(self):
        self.hp = 25
        self.moves = example_moves_class # Set the character's moves


# Spawn Enemies
def populate_enemies(amount, enemy_type, moves):
    
    for i in range(amount):
        current_enemies.append(enemy_type())
        
    return current_enemies
        
# Populates list with enemies
current_enemies = populate_enemies(1, Zombie, example_moves_bot)

## Turn System
player_hp = 30
computer_hp = 30
currently_in_round = True

# Player's class, will be decided at beginning of game
player_class = example_moves_class

# More variables for turn system
player_turn = True # True = Player's Turn | False = Computer's Turn
player_move = "" # Name of player's move
computer_move = "" # Name of Computer's move

move_lands = 0 # Used for calculating if a move hits or misses

def damage_player(amount):
    plr_hp = player_hp
    plr_hp -= amount
    return plr_hp


# When it is the player's turn to attack
def play_turn_player(bot_hp, plr_hp, enemy):
    
    print("computer's hp: " + str(bot_hp))
        
       #input placeholder (will become a gui button)
    player_move = input("It's your turn. What's your move: ")

     # If 100% chance it ihts
    if player_class[player_move][1] == 100:

        
        bot_hp = current_enemies[0].damage_computer(player_class[player_move][0])

        # Determine if it's a hit or a miss
    else:
        move_lands = random.randint(1, 100)

        # If the move lands
        if move_lands <= player_class[player_move][1]:

            
            bot_hp, alive = current_enemies[0].damage_computer(player_class[player_move][0])

        # If it's a miss
        else:
            print("Missed your move")


    # return computer and player health levels
    return bot_hp

# Bot's attack system
def play_turn_computer(bot_hp, plr_hp, enemy):

    enemymoves = enemy.moves
    
    print("players's hp: " + str(plr_hp))

    # Determine bot's move
    move = random.choice(list(enemymoves.items()))
    print("Move: " + str(move))

     # If 100% chance it ihts
    if move[1][1] == 100: # enemy's move 
        plr_hp = damage_player(move[1][0]) # Damage Player

        # Determine if it's a hit or a miss
    else:
        move_lands = random.randint(1, 100)

        # If the move lands

        if move_lands <= int(move[1][1]):
            plr_hp = damage_player(move[1][0]) # Damage Player
            
        # If it's a miss
        else:
            print("Missed your move")


    # return computer and player health levels
    return plr_hp


# Manages the entire round (determines who is playing and when someone wins)
def round_cycle(bot_hp, plr_hp, player_turn):

    while currently_in_round == True:

        # Player's turn
        if player_turn == True:

            print(current_enemies[0])
            bot_hp = play_turn_player(bot_hp, plr_hp, current_enemies[0]) # player attacks
            print("bot HP: " + str(bot_hp))

            # When bot dies
            if bot_hp[0] <= 0:
                print("bot died")
                current_enemies.pop(0) # remove enemy from list
                if len(current_enemies) == 0:
                    currently_in_round == False
                    print("Round Ended")

            # Switches to bot's turn
            player_turn = False

        # Bot's turn
        else:
            print("BOTS TURN")
            plr_hp = play_turn_computer(bot_hp, plr_hp, current_enemies[0]) # bot attacks

            # When player dies
            if plr_hp <= 0:
                print("player died")
                currently_in_round == False 

            # Switches to players's turn
            player_turn = True

    return bot_hp, plr_hp, player_turn


computer_hp, player_hp, player_turn = round_cycle(computer_hp, player_hp, player_turn)
