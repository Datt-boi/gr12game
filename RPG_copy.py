import pygame
import random



clock = pygame.time.Clock()

title = True
timer = 0

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
        
        #one image to output when not animating
        if self.name == "static_animate":
            self.sprites.append(pygame.image.load("Sprites/hero/hero_attack/hero_attack0.png"))
            self.is_animating = True

        #attack animation
        elif self.name == "attack_animate":
            self.sprites.append(pygame.image.load("Sprites/hero/hero_attack/hero_attack0.png"))
            self.sprites.append(pygame.image.load("Sprites/hero/hero_attack/hero_attack1.png"))
            self.sprites.append(pygame.image.load("Sprites/hero/hero_attack/hero_attack2.png"))
            self.sprites.append(pygame.image.load("Sprites/hero/hero_attack/hero_attack3.png"))
            self.sprites.append(pygame.image.load("Sprites/hero/hero_attack/hero_attack4.png"))
            
        #hurt animation
        elif self.name == "hurt_animate":
            self.sprites.append(pygame.image.load("Sprites/hero/hero_hurt/hero_hurt0.png"))
            self.sprites.append(pygame.image.load("Sprites/hero/hero_hurt/hero_hurt1.png"))
            self.sprites.append(pygame.image.load("Sprites/hero/hero_hurt/hero_hurt2.png"))
            self.sprites.append(pygame.image.load("Sprites/hero/hero_hurt/hero_hurt3.png"))
            self.sprites.append(pygame.image.load("Sprites/hero/hero_hurt/hero_hurt4.png"))

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
                static_animate.animate()
                
            self.image = self.sprites[int(self.current_sprite)]
    
#A container class to hold and manage multiple Sprite objects
#create attack animation object
moving_sprites_attack = pygame.sprite.Group()
attack_animate = Player_animate("attack_animate", 600,200, 100, 100)
moving_sprites_attack.add(attack_animate)

#create hurt animation object
moving_sprites_hurt = pygame.sprite.Group()
hurt_animate = Player_animate("hurt_animate", 600,200, 100, 100)
moving_sprites_hurt.add(hurt_animate)

#create static animation object
moving_sprites_static = pygame.sprite.Group()
static_animate = Player_animate("static_animate", 600,200, 100, 100)
moving_sprites_static.add(static_animate)
        
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
    def __init__(self, x, y, sx, sy, fbcolor, font, fcolor, text):
        self.x = x
        self.y = y
        self.sx = sx
        self.sy = sy
        self.fontsize = 35
        self.fbcolor = fbcolor
        self.fcolor = fcolor
        self.text = text
        self.CurrentState = False
        self.buttonf = pygame.font.SysFont(font, self.fontsize)

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

        
       

pygame.init()

 
# CREATING THE OBJECT OF THE
# CLASS Screen FOR MENU SCREEN
menuScreen = Screen("Menu Screen")

# CREATING THE OBJECT OF THE CLASS
# Screen FOR CONTROL SCREEN
gameScreen = Screen("Game Screen")
 
 
# CALLING OF THE FUNCTION TO
# MAKE THE SCREEN FOR THE WINDOW
win = menuScreen.makeCurrentScreen()
 
# Menu Buttons
play_BUTTON = Button(325, 200, 130, 70, (pygame.image.load("Sprites/Buttons/New_Piskel.png")))



#used for background of buttons
black_box = Box(0, 400, 800, 200, (0,0,0), "TimesNewRoman", (0,0,0), "")
left_gray_box = Box(10, 410, 290, 180, (128,128,128), "TimesNewRoman", (0,0,0), "")
right_gray_box = Box(310, 410, 480, 180, (128,128,128), "TimesNewRoman", (0,0,0), "")

# Game Screen Buttons
attack_button = Button(30, 470, 110, 50, (pygame.image.load("Sprites/Buttons/Button_fight.png")))
guard_button = Button(170, 470, 110, 50, (pygame.image.load("Sprites/Buttons/Button_guard.png")))
item_button = Button(30, 530, 110, 50, (pygame.image.load("Sprites/Buttons/Button_item.png")))
skip_button = Button(170, 530, 110, 50, (pygame.image.load("Sprites/Buttons/Button_skip.png")))


item1_button = Box(350, 430, 130, 60, (255,255,255), "TimesNewRoman", (0,0,0), "Item 1")
item2_button = Box(620, 430, 130, 60, (255,255,255), "TimesNewRoman", (0,0,0), "Item 2")
item3_button = Box(350, 510, 130, 60, (255,255,255), "TimesNewRoman", (0,0,0), "Item 3")
item4_button = Box(620, 510, 130, 60, (255,255,255), "TimesNewRoman", (0,0,0), "Item 4")





 
done = False
 
#used so buttons aren't created over eachother
attack_var = 0
item_var = 0




while not done:
    clock.tick(60)
    timer += 1

    #test to see if attack options will change based on what this variable is
    #options are 'brawler' and 'wizard'
    current_player = brawler
   
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
            pygame.event.wait()
            menuScreen.endCurrentScreen()
            win = gameScreen.makeCurrentScreen()
            num = timer
            
    # CHECKING GAME SCREEN FOR ITS UPDATE
    elif gameScreen.checkUpdate((0, 50, 125)):

        #displays boxes and buttons
        black_box.showButton(gameScreen.returnTitle())
        left_gray_box.showButton(gameScreen.returnTitle())
        right_gray_box.showButton(gameScreen.returnTitle())
        
        attack_button.showButton(gameScreen.returnTitle())
        guard_button.showButton(gameScreen.returnTitle())
        item_button.showButton(gameScreen.returnTitle())
        skip_button.showButton(gameScreen.returnTitle())

        
        #variables to check if buttons have been pressed
        attack_barbutton = attack_button.focusCheck(mouse_pos, mouse_click)
        item_barbutton = item_button.focusCheck(mouse_pos, mouse_click)

        #to display static image
        if static_animate.return_animate() == True:  
            moving_sprites_static.draw(gameScreen.returnTitle())
            
        #to display attack animation
        elif attack_animate.return_animate() == True:  
            moving_sprites_attack.draw(gameScreen.returnTitle())
            moving_sprites_attack.update()

        #to display hurt animation
        elif hurt_animate.return_animate() == True:  
            moving_sprites_hurt.draw(gameScreen.returnTitle())
            moving_sprites_hurt.update()
        
        
        #if attack button is pressed, shows different attacks   
        if (attack_barbutton and timer > num) or attack_var == 1:
            attack_var = 1
            item_var = 0

            #creates and displays the four attacks
            attack1_button = Box(350, 430, 130, 60, (255,255,255), "TimesNewRoman", (0,0,0), Players.return_move_name1(current_player))
            attack2_button = Box(620, 430, 130, 60, (255,255,255), "TimesNewRoman", (0,0,0), Players.return_move_name2(current_player))
            attack3_button = Box(350, 510, 130, 60, (255,255,255), "TimesNewRoman", (0,0,0), Players.return_move_name3(current_player))
            attack4_button = Box(620, 510, 130, 60, (255,255,255), "TimesNewRoman", (0,0,0), "Attack 4")
            
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
            if (attack1_barbutton or attack2_barbutton or attack3_barbutton or attack4_barbutton) and current_player == brawler :
                static_animate.not_animate()
                attack_animate.animate()
                
            #if button has been pressed, stop static image and start hurt animation
            elif (attack1_barbutton or attack2_barbutton or attack3_barbutton or attack4_barbutton) and current_player == wizard :
                static_animate.not_animate()
                hurt_animate.animate()

            
        #if item button has been pressed, shows item options
        if (item_barbutton and timer > num) or item_var == 1:
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

        
