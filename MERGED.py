import pygame
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

#Enemy information table
# Name and animations for enemy
enemies_list = {
    "Demon": "Sprites/Enemy/Demon/",
    "Skeleton": "Sprites/Enemy/Enemyhurt/Enemy_hurt",
    "Warrior": "Sprites/Enemy/Enemyhurt/Enemy_hurt",
    "Goober": "Sprites/Enemy/Enemyhurt/Enemy_hurt",
}

players_list = {
    "Hero": "Sprites/hero/Hero_"
}


#class for spawning an enemy sprite
class spawn_sprite:
    def __init__(self, file, name, pos_x, pos_y, sx, sy):
        self.file = file
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.sx = sx
        self.sy = sy
        self.name = name
  
        self.hurt_sprites = []
        self.dead_sprites = []
        self.attack_sprites = []
        self.idle_sprite = []
        
        self.hurt_is_animating = False
        self.attack_is_animating = False
        self.dead_is_animating = False
        self.idle_is_animating = True

        for i in range(4):
            self.attack_sprites.append(pygame.image.load(self.file + "attack" + str(i) + ".png"))

        self.dead_sprites.append(pygame.image.load(self.file + "dead0.png"))
        self.dead_sprites.append(pygame.image.load(self.file + "dead1.png"))
        self.dead_sprites.append(pygame.image.load(self.file + "dead2.png"))
        self.dead_sprites.append(pygame.image.load(self.file + "dead3.png"))
        self.dead_sprites.append(pygame.image.load(self.file + "dead4.png"))
        self.dead_sprites.append(pygame.image.load(self.file + "dead4.png"))
        self.dead_sprites.append(pygame.image.load(self.file + "dead4.png"))
        self.dead_sprites.append(pygame.image.load(self.file + "dead4.png"))
        self.dead_sprites.append(pygame.image.load(self.file + "dead4.png"))
        self.dead_sprites.append(pygame.image.load(self.file + "dead4.png"))
        self.dead_sprites.append(pygame.image.load(self.file + "dead4.png"))
        

        for i in range(4):
            self.hurt_sprites.append(pygame.image.load(self.file + "hurt" + str(i) + ".png"))
            

        self.idle_sprite.append(pygame.image.load(self.file + "attack0.png"))


        for i in range(len(self.attack_sprites)):
            self.attack_sprites[i] = self.attack_sprites[i] = pygame.transform.scale(self.attack_sprites[i], (self.sx, self.sy))

        for i in range(len(self.hurt_sprites)):
            self.hurt_sprites[i] = self.hurt_sprites[i] = pygame.transform.scale(self.hurt_sprites[i], (self.sx, self.sy))
            
        for i in range(len(self.dead_sprites)):
            self.dead_sprites[i] = self.dead_sprites[i] = pygame.transform.scale(self.dead_sprites[i], (self.sx, self.sy))
            

        self.idle_sprite[0] = self.idle_sprite[0] = pygame.transform.scale(self.idle_sprite[0], (self.sx, self.sy))

        self.current_sprite = 0
    


    #used mainly to stop static image   
    def idle_not_animate(self):
        self.idle_is_animating = False

    #starts animation
    def idle_animate(self):
        self.idle_is_animating  = True

    #used to check if currently animating
    def return_hurt_animate(self):
        if self.hurt_is_animating == True:
            return True

    def return_dead_animate(self):
        if self.dead_is_animating == True:
            return True

    def return_attack_animate(self):
        if self.attack_is_animating == True:
            return True

    def return_idle_animate(self):
        if self.idle_is_animating == True:
            return True
    def return_name(self):
        return self.name
       
    def showIdle(self, display):
        display.blit(self.idle_sprite[0], (self.pos_x,self.pos_y))

    def hurt_animate(self):
        self.hurt_is_animating  = True

    def attack_animate(self):
        self.attack_is_animating  = True

    def dead_animate(self):
        self.dead_is_animating  = True

    def showAttack(self, display):
        if self.attack_is_animating == True:
            display.blit(self.attack_sprites[int(self.current_sprite)], (self.pos_x,self.pos_y))
            self.current_sprite += 0.2

            if self.current_sprite >= len(self.attack_sprites):
                self.current_sprite = 0
                self.attack_is_animating = False
                self.idle_animate()
                
    def showHurt(self, display):
        if self.hurt_is_animating == True:
            display.blit(self.hurt_sprites[int(self.current_sprite)], (self.pos_x,self.pos_y))
            self.current_sprite += 0.2

            if self.current_sprite >= len(self.hurt_sprites):
                self.current_sprite = 0
                self.hurt_is_animating = False
                self.idle_animate()

    def showDead(self, display):
        if self.dead_is_animating == True:
            display.blit(self.dead_sprites[int(self.current_sprite)], (self.pos_x,self.pos_y))
            self.current_sprite += 0.2

            if self.current_sprite >= len(self.dead_sprites):
                self.current_sprite = 0
                self.dead_is_animating = False
                
                    
                
            
            
    #used mainly to stop static image   
    def not_animate(self):
        self.is_animating = False

    #starts animation
    def animate(self):
        self.is_animating  = True

    #used to check if currently animating
    def return_animate(self):
        if self.is_animating == True:
            return True
        
    
        
    



sprite = spawn_sprite(enemies_list['Demon'], "Demon", 100, 200, 100, 100)
hero = spawn_sprite(players_list['Hero'], "Antonio", 600, 200, 100, 100)


clock = pygame.time.Clock()

title = True
timer = 0
time = 0

enemy_hp = 30
MOUSEUP = pygame.MOUSEBUTTONUP

enemy_hit = False

    

#to create screens 
class Screen():
   
    def __init__(self, title, width = 800, height = 600, fill=(0,0,255)):
        self.height = height
        self.title = title
        self.width = width
        self.fill = fill
        self.CurrentState = False

    def makeCurrentScreen(self):
        pygame.display.set_caption(self.title)
        self.CurrentState = True
        self.screen = pygame.display.set_mode((self.width, self.height))

    def endCurrentScreen(self):
        self.CurrentState = False

    def checkUpdate(self, fill):
        self.fill = fill
        return self.CurrentState

    def screenUpdate(self):
        if (self.CurrentState):
            self.screen.fill(self.fill)

    def returnTitle(self):
        return self.screen
   


#to create buttons with images
class Button():
    def __init__(self, x, y, sx, sy, picture):
        self.x = x
        self.y = y
        self.picture = pygame.transform.scale(picture, (sx, sy))
        self.sx = sx
        self.sy = sy
       
        self.CurrentState = False
       
    
    def showButton(self, display):
        display.blit(self.picture, (self.x,self.y))
           
       
    #checks if mouse is clicked on button
    def focusCheck(self, mousepos, mouseclick):
        if (mousepos[0] >= self.x and mousepos[0] <= self.x + self.sx and mousepos [1] >= self.y and mousepos[1] <= self.y + self.sy):
            self.CurrentState = True
            return mouseclick[0]
        else:
            self.CurrentState = False
            return False

#to create buttons with text, not images
class Box():
    def __init__(self, x, y, sx, sy, fbcolor, font, fontsize, fcolor, text):
        self.x = x
        self.y = y
        self.sx = sx
        self.sy = sy
        self.fontsize = fontsize
        self.fbcolor = fbcolor
        self.fcolor = fcolor
        self.text = text
        self.CurrentState = False
        self.buttonf = pygame.font.SysFont(font, self.fontsize)
        self.is_depleting = False

        self.damage = 0
        self.hp = 0
        self.hit = False
        self.pixels_delete = 0

    def showButton(self, display):
        if(self.CurrentState):
            pygame.draw.rect(display, self.fbcolor, (self.x, self.y, self.sx, self.sy))

        else:
            pygame.draw.rect(display, self.fbcolor, (self.x, self.y, self.sx, self.sy))
           
       
        textsurface = self.buttonf.render(self.text, False, self.fcolor)
        display.blit(textsurface, ((self.x + (self.sx/2)-(self.fontsize/2)*(len(self.text)/2)+2, (self.y +(self.sy/2)-(self.fontsize/2)-4))))
        
    #checks if mouse is clicked on button
    def focusCheck(self, mousepos, mouseclick):
        if (mousepos[0] >= self.x and mousepos[0] <= self.x + self.sx and mousepos [1] >= self.y and mousepos[1] <= self.y + self.sy):
            self.CurrentState = True
            return mouseclick[0]
        else:
            self.CurrentState = False
            return False

    def health_deplete(self, hp, damage):
        self.is_depleting = True
        self.hp = hp
        self.damage = damage
        self.hit = True
        
        
        

    def return_health_deplete(self):
        if self.is_depleting == True:
            return True
        

    def health_depleting(self):
        


        if self.is_depleting:
            
            
            if self.hit:
           
                self.pixels_delete = (self.damage/(self.hp+self.damage)) * self.sx
            
                self.hit = False
                
                
           
            enemy_hp_red_box = Box(75, 160, self.sx -(self.pixels_delete/30), 10, (125,0,0), "TimesNewRoman", 35, (0,0,0), "")
           

            self.sx = self.sx -(self.pixels_delete/30)
           
            if self.sx <= (self.hp/30) * 200:
                self.is_depleting = False
                
 

pygame.init()

 
# CREATING THE OBJECT OF THE
# CLASS Screen FOR MENU SCREEN
menuScreen = Screen("Menu Screen")

# CREATING THE OBJECT OF THE CLASS
# Screen FOR CONTROL SCREEN
gameScreen = Screen("Game Screen")

gameScreen_background = Button(0, 0, 800, 600, (pygame.image.load("Sprites/RPG Background-1.png.png")))
 
 
# CALLING OF THE FUNCTION TO
# MAKE THE SCREEN FOR THE WINDOW
win = menuScreen.makeCurrentScreen()
 
# Menu Buttons
play_BUTTON = Button(310, 200, 180, 72, (pygame.image.load("Sprites/Buttons/Button_PLAY.png")))



#used for background of buttons
black_box = Box(0, 400, 800, 200, (0,0,0), "TimesNewRoman", 35, (0,0,0), "")
left_gray_box = Box(10, 410, 290, 180, (128,128,128), "TimesNewRoman", 35, (0,0,0), "")
right_gray_box = Box(310, 410, 480, 180, (128,128,128), "TimesNewRoman", 35, (0,0,0), "")

hp_black_box = Box(70, 440, 210, 20, (0,0,0), "TimesNewRoman", 35, (0,0,0), "")
hp_red_box = Box(75, 445, 200, 10, (125,0,0), "TimesNewRoman", 35, (0,0,0), "")

enemy_hp_black_box = Box(70, 155, 210, 20, (0,0,0), "TimesNewRoman", 35, (0,0,0), "")
enemy_hp_red_box = Box(75, 160, 200, 10, (125,0,0), "TimesNewRoman", 35, (0,0,0), "")


enemy_died = Box(250, 115, 0, 0, (0,50,125), "TimesNewRoman", 35, (0,0,0), "You defeated the enemy")


# Game Screen Buttons
attack_button = Button(30, 470, 110, 50, (pygame.image.load("Sprites/Buttons/Button_fight.png")))
guard_button = Button(170, 470, 110, 50, (pygame.image.load("Sprites/Buttons/Button_guard.png")))
item_button = Button(30, 530, 110, 50, (pygame.image.load("Sprites/Buttons/Button_item.png")))
skip_button = Button(170, 530, 110, 50, (pygame.image.load("Sprites/Buttons/Button_skip.png")))


item1_button = Box(350, 430, 130, 60, (255,255,255), "TimesNewRoman", 35, (0,0,0), "Item 1")
item2_button = Box(620, 430, 130, 60, (255,255,255), "TimesNewRoman", 35, (0,0,0), "Item 2")
item3_button = Box(350, 510, 130, 60, (255,255,255), "TimesNewRoman", 35, (0,0,0), "Item 3")
item4_button = Box(620, 510, 130, 60, (255,255,255), "TimesNewRoman", 35, (0,0,0), "Item 4")





 
done = False
 
#used so buttons aren't created over eachother
attack_var = 0
item_var = 0



enemy_damage_taken = ""


while not done:
    clock.tick(60)
    timer += 1

    
    name_text = Box(10, 420, 290, 20, (128,128,128), "TimesNewRoman", 23, (0,0,0), spawn_sprite.return_name(hero))
    hp_text = Box(10, 442, 60, 20, (128,128,128), "TimesNewRoman", 23, (0,0,0), str(50))
    enemy_hp_text = Box(40, 167, 0, 0, (0,50,125), "TimesNewRoman", 23, (0,0,0), str(enemy_hp))
    
# CALLING OF screenUpdate
    # function FOR MENU SCREEN
    menuScreen.screenUpdate()
    # CALLING THE FUNCTION OF CONTROL BAR
    gameScreen.screenUpdate()
    # STORING THE MOUSE EVENT
    # TO CHECK THE POSITION OF THE MOUSE
    mouse_pos = pygame.mouse.get_pos()
    # CHECKING THE MOUSE CLICK EVENT
    mouse_click = pygame.mouse.get_pressed()
    # KEY PRESSED OR NOT
    keys = pygame.key.get_pressed()




    # CHECKING MENU SCREEN FOR ITS UPDATE
    if menuScreen.checkUpdate((0, 125, 125)):
        play_BUTTON.showButton(menuScreen.returnTitle())
        play_barbutton = play_BUTTON.focusCheck(mouse_pos, mouse_click)
 
        if play_barbutton:
            ev = pygame.event.wait()
            if ev.type == MOUSEUP:
                menuScreen.endCurrentScreen()
                win = gameScreen.makeCurrentScreen()
                num = timer
            
    # CHECKING GAME SCREEN FOR ITS UPDATE
    elif gameScreen.checkUpdate((0, 50, 125)):
       
        

        gameScreen_background.showButton(gameScreen.returnTitle())
        

        name_text.showButton(gameScreen.returnTitle())

        
        if enemy_hp <= 0:
            enemy_hp = 0
            

            if timer >= (time + 360) and sprite.return_dead_animate() != True:
                enemy_died.showButton(gameScreen.returnTitle())
                sprite.idle_not_animate()
            
            
        #displays boxes and buttons
        black_box.showButton(gameScreen.returnTitle())
        left_gray_box.showButton(gameScreen.returnTitle())
        right_gray_box.showButton(gameScreen.returnTitle())

        
        hp_black_box.showButton(gameScreen.returnTitle())
        hp_red_box.showButton(gameScreen.returnTitle())
        hp_text.showButton(gameScreen.returnTitle())
        
        enemy_hp_text.showButton(gameScreen.returnTitle())
        enemy_hp_black_box.showButton(gameScreen.returnTitle())
        enemy_hp_red_box.showButton(gameScreen.returnTitle())
        
        name_text.showButton(gameScreen.returnTitle())
        
        
        
        attack_button.showButton(gameScreen.returnTitle())
        guard_button.showButton(gameScreen.returnTitle())
        item_button.showButton(gameScreen.returnTitle())
        skip_button.showButton(gameScreen.returnTitle())

        
        #variables to check if buttons have been pressed
        attack_barbutton = attack_button.focusCheck(mouse_pos, mouse_click)
        item_barbutton = item_button.focusCheck(mouse_pos, mouse_click)

        #to display static image
        if hero.return_idle_animate() == True:  
            hero.showIdle(gameScreen.returnTitle())
            
        #to display attack animation
        elif hero.return_attack_animate() == True:  
            hero.showAttack(gameScreen.returnTitle())

        #to display hurt animation
        elif hero.return_hurt_animate() == True:  
            hero.showHurt(gameScreen.returnTitle())

        if enemy_hp_red_box.return_health_deplete() == True:
            enemy_hp_red_box.health_depleting()


        #to display static image
        if sprite.return_idle_animate() == True:  
            sprite.showIdle(gameScreen.returnTitle())
            
        #to display attack animation
        if sprite.return_hurt_animate() == True:  
            sprite.showHurt(gameScreen.returnTitle())
            enemy_damage_taken_box = Box(175, 200, 0, 0, (0,50,125), "TimesNewRoman",  35, (155,0,0), "-" + enemy_damage_taken)

            if enemy_hp > 0:
                enemy_damage_taken_box.showButton(gameScreen.returnTitle())

        if sprite.return_dead_animate() == True:
            sprite.showDead(gameScreen.returnTitle())
            
            
            

        
        
        
        #if attack button is pressed, shows different attacks   
        if ((attack_barbutton and timer > num) or attack_var == 1):
            
            if enemy_hp > 0:  
                attack_var = 1
                item_var = 0
            
            #creates and displays the four attacks
            attack1_button = Button(370, 430, 130, 60, (pygame.image.load("Sprites/Buttons/Button_chop.png")))
            attack2_button = Button(600, 430, 130, 60, (pygame.image.load("Sprites/Buttons/Button_slice.png")))
            attack3_button = Button(370, 510, 130, 60, (pygame.image.load("Sprites/Buttons/Button_stab.png")))
            attack4_button = Button(600, 510, 130, 60, (pygame.image.load("Sprites/Buttons/Button_kick.png")))

               
            attack1_button.showButton(gameScreen.returnTitle())
            attack2_button.showButton(gameScreen.returnTitle())
            attack3_button.showButton(gameScreen.returnTitle())
            attack4_button.showButton(gameScreen.returnTitle())

            
            #variables to check if buttons have been pressed
            attack1_barbutton = attack1_button.focusCheck(mouse_pos, mouse_click)
            attack2_barbutton = attack2_button.focusCheck(mouse_pos, mouse_click)
            attack3_barbutton = attack3_button.focusCheck(mouse_pos, mouse_click)
            attack4_barbutton = attack4_button.focusCheck(mouse_pos, mouse_click)

            #if button has been pressed, stop static image and start attack animation
            if (attack1_barbutton or attack2_barbutton or attack3_barbutton or attack4_barbutton) and enemy_hp > 0:
                ev = pygame.event.wait()
                if ev.type == MOUSEUP:
                    
                    hero.idle_not_animate()
                    hero.attack_animate()

                    
                    enemy_damage_taken = str(random.randint(5,15))
                    int_enemy_damage_taken = int(enemy_damage_taken)
                    enemy_hp -= int(enemy_damage_taken)

                    enemy_hp_red_box.health_deplete(enemy_hp, int_enemy_damage_taken)
                    
                    
                    if enemy_hp <= 0:
                        enemy_hp = 0

                        sprite.idle_not_animate()
                        sprite.dead_animate()

                    else:
                        sprite.idle_not_animate()
                        sprite.hurt_animate()
                    
                

            
        #if item button has been pressed, shows item options
        
        if ((item_barbutton and timer > num) or item_var == 1):
            if enemy_hp > 0:  
                item_var = 1
                attack_var = 0
            
            
                item1_button.showButton(gameScreen.returnTitle())
                item2_button.showButton(gameScreen.returnTitle())
                item3_button.showButton(gameScreen.returnTitle())
                item4_button.showButton(gameScreen.returnTitle())


           
    #  CHECKING IF THE EXIT BUTTON HAS BEEN CLICKED OR NOT
    for event in pygame.event.get():
        # IF CLICKED THEN CLOSE THE WINDOW
        if(event.type == pygame.QUIT):
            done = True
 
    pygame.display.update()
# CLOSE THE PROGRAM
pygame.quit()
