import random

# Player's moves
# Sample moves - Name: [Damage, Hitting % Chance]
example_moves_class = {
    "Kick": [18, 50],
    "Stomp": [12, 75],
    "Shout": [5, 100],
}

# Bot's moves
# Sample moves - Name: [Damage, Hitting % Chance]
example_moves_bot = {
    "Kick": [18, 50],
    "Stomp": [12, 75],
    "Shout": [5, 100],
}

## Enemies System
current_enemies = []

class Enemy:
    def __init__(health, name, listname):
        self.hp = health
        self.name = name
        self.listname = listname

    # Deal damage to computer (bot) player
    def damage_computer(amount):

        self.hp -= amount 
        print("computer's hp: " + str(bot_hp))

        if self.hp <= 0:
            self.hp = 0
            return bot_hp, False # alive = false
        else:
            return bot_hp, True # alive = true

## Specific Enemies

class Zombie(Enemy):
    def __init__():
        self.hp = 25


# Spawn Enemies
def populate_enemies(amount, enemy_type):

    print("# enemies: ")
    
    for i in range(amount):
        current_enemies.append(enemy_type)
        
    return current_enemies
        

current_enemies = populate_enemies(1, Zombie)
print(current_enemies)

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


# When it is the player's turn to attack
def play_turn_player(bot_hp, plr_hp, enemy):
    
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

    player_turn = False

    # return computer and player health levels
    return bot_hp

# When it's the bot's turn to attack (WIP)
def play_turn_computer(bot_hp, plr_hp):
    
    print("players's hp: " + str(plr_hp))

    # Determine bot's move
    #print(random.choice(example_moves_bot))

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

    player_turn = False

    # return computer and player health levels
    return bot_hp


# Manages the entire round (determines who is playing and when someone wins)
def round_cycle(bot_hp, plr_hp):

    print(bot_hp, plr_hp)

    while currently_in_round == True:
        if player_turn == True:
            bot_hp, plr_hp = play_turn_player(bot_hp, plr_hp, current_enemies[0])

            if bot_hp <= 0:
                print("bot died")
            
        else:
            bot_hp, plr_hp = play_turn_computer(bot_hp, plr_hp, current_enemies[0])

            if plr_hp <= 0:
                print("player died")

    return bot_hp, plr_hp


computer_hp, player_hp = round_cycle(computer_hp, player_hp)
