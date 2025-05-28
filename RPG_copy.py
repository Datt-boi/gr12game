import pygame
import random



clock = pygame.time.Clock()

title = True
timer = 0
time = 0

enemy_hp = 30
MOUSEUP = pygame.MOUSEBUTTONUP

enemy_hit = False


    
#class to create animations
class Player_animate(pygame.sprite.Sprite):
    def __init__(self, name, pos_x, pos_y, sx, sy):
        super().__init__()
        self.name = name
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.sx = sx
        self.sy = sy
        
        self.sprites = []
        self.is_animating = False
        
        #one image to output when not animating hero
        if self.name == "hero_static_animate":
            self.sprites.append(pygame.image.load("Sprites/hero/hero_attack/hero_attack0.png"))
            self.is_animating = True

        #one image to output when not animating enemy
        if self.name == "enemy_static_animate":
            self.sprites.append(pygame.image.load("Sprites/Enemy/Enemyattack/Enemy_attack0.png"))
            self.is_animating = True

        #hero attack animation
        elif self.name == "hero_attack_animate":
            self.sprites.append(pygame.image.load("Sprites/hero/hero_attack/hero_attack0.png"))
            self.sprites.append(pygame.image.load("Sprites/hero/hero_attack/hero_attack1.png"))
            self.sprites.append(pygame.image.load("Sprites/hero/hero_attack/hero_attack2.png"))
            self.sprites.append(pygame.image.load("Sprites/hero/hero_attack/hero_attack3.png"))
            self.sprites.append(pygame.image.load("Sprites/hero/hero_attack/hero_attack4.png"))
            
        #hero hurt animation
        elif self.name == "hero_hurt_animate":
            self.sprites.append(pygame.image.load("Sprites/hero/hero_hurt/hero_hurt0.png"))
            self.sprites.append(pygame.image.load("Sprites/hero/hero_hurt/hero_hurt1.png"))
            self.sprites.append(pygame.image.load("Sprites/hero/hero_hurt/hero_hurt2.png"))
            self.sprites.append(pygame.image.load("Sprites/hero/hero_hurt/hero_hurt3.png"))
            self.sprites.append(pygame.image.load("Sprites/hero/hero_hurt/hero_hurt4.png"))

        #enemy hurt animation
        elif self.name == "enemy_hurt_animate":
            self.sprites.append(pygame.image.load("Sprites/Enemy/Enemyhurt/Enemy_hurt0.png"))
            self.sprites.append(pygame.image.load("Sprites/Enemy/Enemyhurt/Enemy_hurt1.png"))
            self.sprites.append(pygame.image.load("Sprites/Enemy/Enemyhurt/Enemy_hurt2.png"))
            self.sprites.append(pygame.image.load("Sprites/Enemy/Enemyhurt/Enemy_hurt3.png"))
            self.sprites.append(pygame.image.load("Sprites/Enemy/Enemyhurt/Enemy_hurt4.png"))

        #enemy dead animation
        elif self.name == "enemy_dead_animate":
            self.sprites.append(pygame.image.load("Sprites/Enemy/Enemyhurt/Enemy_hurt0.png"))
            self.sprites.append(pygame.image.load("Sprites/Enemy/Enemyhurt/Enemy_hurt1.png"))
            self.sprites.append(pygame.image.load("Sprites/Enemy/Enemyhurt/Enemy_hurt2.png"))
            self.sprites.append(pygame.image.load("Sprites/Enemy/Enemyhurt/Enemy_hurt3.png"))
            self.sprites.append(pygame.image.load("Sprites/Enemy/Enemyhurt/Enemy_hurt4.png"))
            self.sprites.append(pygame.image.load("Sprites/Enemy/Enemyattack/Enemy_attack0.png"))
            self.sprites.append(pygame.image.load("Sprites/Enemy/Enemydead/Enemy_dead0.png"))
            self.sprites.append(pygame.image.load("Sprites/Enemy/Enemydead/Enemy_dead1.png"))
            self.sprites.append(pygame.image.load("Sprites/Enemy/Enemydead/Enemy_dead2.png"))
            self.sprites.append(pygame.image.load("Sprites/Enemy/Enemydead/Enemy_dead3.png"))
            self.sprites.append(pygame.image.load("Sprites/Enemy/Enemydead/Enemy_dead4.png"))
            

        #resizes the images
        for i in range(len(self.sprites)):
            self.sprites[i] = self.sprites[i] = pygame.transform.scale(self.sprites[i], (self.sx, self.sy))

        
        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]

        self.rect = self.image.get_rect()
        self.rect.topleft = [self.pos_x, self.pos_y]

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
        
    #goes through list and animates
    def update(self):
        if self.is_animating == True:
            self.current_sprite += 0.2

            if self.current_sprite >= len(self.sprites):
                self.current_sprite = 0
                self.is_animating = False
                
                
                
                if self.name == "hero_attack_animate":
                    hero_static_animate.animate()

                if self.name == "enemy_hurt_animate":
                    enemy_static_animate.animate()

                if self.name == "enemy_dead_animate":
                    timer = 0
                    pygame.time.delay(1400)
                    
                
            self.image = self.sprites[int(self.current_sprite)]
    
#A container class to hold and manage multiple Sprite objects
#create attack animation object
hero_attack_group = pygame.sprite.Group()
hero_attack_animate = Player_animate("hero_attack_animate", 600,200, 100, 100)
hero_attack_group.add(hero_attack_animate)

#create hurt animation object
hero_hurt_group = pygame.sprite.Group()
hero_hurt_animate = Player_animate("hero_hurt_animate", 600,200, 100, 100)
hero_hurt_group.add(hero_hurt_animate)

#create static animation object
hero_static_group = pygame.sprite.Group()
hero_static_animate = Player_animate("hero_static_animate", 600,200, 100, 100)
hero_static_group.add(hero_static_animate)

#create static animation object
enemy_static_group = pygame.sprite.Group()
enemy_static_animate = Player_animate("enemy_static_animate", 100, 200, 100, 100)
enemy_static_group.add(enemy_static_animate)

#create enemy hurt animation object
enemy_hurt_group = pygame.sprite.Group()
enemy_hurt_animate = Player_animate("enemy_hurt_animate", 100, 200, 100, 100)
enemy_hurt_group.add(enemy_hurt_animate)

#create enemy hurt animation object
enemy_dead_group = pygame.sprite.Group()
enemy_dead_animate = Player_animate("enemy_dead_animate", 100, 200, 100, 100)
enemy_dead_group.add(enemy_dead_animate)
        
# Player's moves
# Sample moves - Name: [Damage, Hitting % Chance]
class Players():
    def __init__(self, name, health, move1, move2, move3):
        self.name = name
        self.health = health
        
        self.move1 = move1
        
        self.move2 = move2

        self.move3 = move3
        
    
    def return_move_name1(self):
        return self.move1[0]
    
    def return_move_name2(self):
        return self.move2[0]
    
    def return_move_name3(self):
        return self.move3[0]
    
    def return_name(self):
        return self.name

    def return_hp(self):
        return self.health

#create list with temporary moves and create brawler player
brawler_move1 = ["Kick", 18, 50]
brawler_move2 = ["Stomp", 12, 75]
brawler_move3 = ["Shout", 5, 100]
brawler = Players("Adrian", 50, brawler_move1, brawler_move2, brawler_move3)

#create list with temporary moves and create wizard player
wizard_move1 = ["Flame", 18, 50]
wizard_move2 = ["Ice", 12, 75]
wizard_move3 = ["Explosion", 5, 100]
wizard = Players("Isaac", 50, wizard_move1, wizard_move2, wizard_move3)
    

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

    #test to see if attack options will change based on what this variable is
    #options are 'brawler' and 'wizard'
    current_player = brawler
    name_text = Box(10, 420, 290, 20, (128,128,128), "TimesNewRoman", 23, (0,0,0), Players.return_name(current_player))
    hp_text = Box(10, 442, 60, 20, (128,128,128), "TimesNewRoman", 23, (0,0,0), str(Players.return_hp(current_player)))
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
            

            if timer >= (time + 360) and enemy_dead_animate.return_animate() != True:
                enemy_died.showButton(gameScreen.returnTitle())
                enemy_static_animate.not_animate()
            
            
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
        if hero_static_animate.return_animate() == True:  
            hero_static_group.draw(gameScreen.returnTitle())
            
        #to display attack animation
        elif hero_attack_animate.return_animate() == True:  
            hero_attack_group.draw(gameScreen.returnTitle())
            hero_attack_group.update()

        #to display hurt animation
        elif hero_hurt_animate.return_animate() == True:  
            hero_hurt_group.draw(gameScreen.returnTitle())
            hero_hurt_group.update()

        if enemy_hp_red_box.return_health_deplete() == True:
            enemy_hp_red_box.health_depleting()


        #to display static image
        if enemy_static_animate.return_animate() == True:  
            enemy_static_group.draw(gameScreen.returnTitle())
            
        #to display attack animation
        if enemy_hurt_animate.return_animate() == True:  
            enemy_hurt_group.draw(gameScreen.returnTitle())
            enemy_hurt_group.update()
            enemy_damage_taken_box = Box(175, 200, 0, 0, (0,50,125), "TimesNewRoman",  35, (155,0,0), "-" + enemy_damage_taken)

            if enemy_hp > 0:
                enemy_damage_taken_box.showButton(gameScreen.returnTitle())

        if enemy_dead_animate.return_animate() == True:  
            enemy_dead_group.draw(gameScreen.returnTitle())
            enemy_dead_group.update()
            
            
            

        
        
        
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
            if (attack1_barbutton or attack2_barbutton or attack3_barbutton or attack4_barbutton) and current_player == brawler and enemy_hp > 0:
                ev = pygame.event.wait()
                if ev.type == MOUSEUP:
                    
                    hero_static_animate.not_animate()
                    hero_attack_animate.animate()

                    
                    enemy_damage_taken = str(random.randint(5,15))
                    int_enemy_damage_taken = int(enemy_damage_taken)
                    enemy_hp -= int(enemy_damage_taken)

                    enemy_hp_red_box.health_deplete(enemy_hp, int_enemy_damage_taken)
                    
                    
                    if enemy_hp <= 0:
                        enemy_hp = 0

                        enemy_static_animate.not_animate()
                        enemy_dead_animate.animate()

                    else:
                        enemy_static_animate.not_animate()
                        enemy_hurt_animate.animate()
                    
                
            #if button has been pressed, stop static image and start hurt animation
            elif (attack1_barbutton or attack2_barbutton or attack3_barbutton or attack4_barbutton) and current_player == wizard :
                hero_static_animate.not_animate()
                hero_hurt_animate.animate()

            
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
