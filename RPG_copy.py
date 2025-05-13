import pygame
import random



clock = pygame.time.Clock()

title = True
timer = 0

class Player_animate(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y, sx, sy):
        super().__init__()
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.sx = sx
        self.sy = sy
        
        self.sprites = []
        self.is_animating = False
        
        self.sprites.append(pygame.image.load("Sprites/hero/hero_attack/hero_attack0.png"))
        self.sprites.append(pygame.image.load("Sprites/hero/hero_attack/hero_attack1.png"))
        self.sprites.append(pygame.image.load("Sprites/hero/hero_attack/hero_attack2.png"))
        self.sprites.append(pygame.image.load("Sprites/hero/hero_attack/hero_attack3.png"))
        self.sprites.append(pygame.image.load("Sprites/hero/hero_attack/hero_attack4.png"))
        
        for i in range(5):
            self.sprites[i] = self.sprites[i] = pygame.transform.scale(self.sprites[i], (self.sx, self.sy))

        
        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]

        self.rect = self.image.get_rect()
        self.rect.topleft = [self.pos_x, self.pos_y]
            
    def animate(self):
        self.is_animating  = True
        
    def update(self):
        if self.is_animating == True:
            self.current_sprite += 0.2

            if self.current_sprite >= len(self.sprites):
                self.current_sprite = 0
                self.is_animating = False
                
            self.image = self.sprites[int(self.current_sprite)]

moving_sprites = pygame.sprite.Group()
slash_animate = Player_animate(600,200, 100, 100)
moving_sprites.add(slash_animate)
        
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

brawler_move1 = ["Kick", 18, 50]
brawler_move2 = ["Stomp", 12, 75]
brawler_move3 = ["Shout", 5, 100]
brawler = Players("Adrian", 50, brawler_move1, brawler_move2, brawler_move3)

wizard_move1 = ["Flame", 18, 50]
wizard_move2 = ["Ice", 12, 75]
wizard_move3 = ["Explosion", 5, 100]
wizard = Players("Isaac", 50, wizard_move1, wizard_move2, wizard_move3)
    
player1_moves = {
    "Kick": [18, 50],
    "Stomp": [12, 75],
    "Shout": [5, 100],
}

player2_moves = {
    "Punch": [18, 50],
    "Stab": [12, 75],
    "Arrow": [5, 100],
}

# Bot's moves
# Sample moves - Name: [Damage, Hitting % Chance]
example_moves_bot = {
    "Kick": [18, 50],
    "Stomp": [12, 75],
    "Shout": [5, 100],
}

      
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
           
       

    def focusCheck(self, mousepos, mouseclick):
        if (mousepos[0] >= self.x and mousepos[0] <= self.x + self.sx and mousepos [1] >= self.y and mousepos[1] <= self.y + self.sy):
            self.CurrentState = True
            return mouseclick[0]
        else:
            self.CurrentState = False
            return False

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



# Game Screen Buttons
black_box = Box(0, 400, 800, 200, (0,0,0), "TimesNewRoman", (0,0,0), "")
left_gray_box = Box(10, 410, 290, 180, (128,128,128), "TimesNewRoman", (0,0,0), "")
right_gray_box = Box(310, 410, 480, 180, (128,128,128), "TimesNewRoman", (0,0,0), "")

attack_button = Button(30, 470, 110, 50, (pygame.image.load("Sprites/Buttons/Button_fight.png")))
defend_button = Button(170, 470, 110, 50, (pygame.image.load("Sprites/Buttons/Button_guard.png")))
item_button = Button(30, 530, 110, 50, (pygame.image.load("Sprites/Buttons/Button_item.png")))
skip_button = Button(170, 530, 110, 50, (pygame.image.load("Sprites/Buttons/Button_skip.png")))


item1_button = Box(350, 430, 130, 60, (255,255,255), "TimesNewRoman", (0,0,0), "Item 1")
item2_button = Box(620, 430, 130, 60, (255,255,255), "TimesNewRoman", (0,0,0), "Item 2")
item3_button = Box(350, 510, 130, 60, (255,255,255), "TimesNewRoman", (0,0,0), "Item 3")
item4_button = Box(620, 510, 130, 60, (255,255,255), "TimesNewRoman", (0,0,0), "Item 4")





 
done = False
 
toggle = False

attack_var = 0
item_var = 0




while not done:
    clock.tick(60)
    timer += 1

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

    

   

# MENU BAR CODE TO ACCESS
    # CHECKING MENU SCREEN FOR ITS UPDATE
    if menuScreen.checkUpdate((0, 125, 125)):
        play_BUTTON.showButton(menuScreen.returnTitle())
        play_barbutton = play_BUTTON.focusCheck(mouse_pos, mouse_click)
 
        if play_barbutton:
            pygame.event.wait()
            menuScreen.endCurrentScreen()
            win = gameScreen.makeCurrentScreen()
            num = timer
            

    elif gameScreen.checkUpdate((0, 50, 125)):

        black_box.showButton(gameScreen.returnTitle())
        left_gray_box.showButton(gameScreen.returnTitle())
        right_gray_box.showButton(gameScreen.returnTitle())
        
        attack_button.showButton(gameScreen.returnTitle())
        defend_button.showButton(gameScreen.returnTitle())
        item_button.showButton(gameScreen.returnTitle())
        skip_button.showButton(gameScreen.returnTitle())

        
       
        attack_barbutton = attack_button.focusCheck(mouse_pos, mouse_click)
        item_barbutton = item_button.focusCheck(mouse_pos, mouse_click)

        moving_sprites.draw(gameScreen.returnTitle())
        moving_sprites.update()
        

            
        if (attack_barbutton and timer > num) or attack_var == 1:
            attack_var = 1
            item_var = 0
            
            attack1_button = Box(350, 430, 130, 60, (255,255,255), "TimesNewRoman", (0,0,0), Players.return_move_name1(current_player))
            attack2_button = Box(620, 430, 130, 60, (255,255,255), "TimesNewRoman", (0,0,0), Players.return_move_name2(current_player))
            attack3_button = Box(350, 510, 130, 60, (255,255,255), "TimesNewRoman", (0,0,0), Players.return_move_name3(current_player))
            attack4_button = Box(620, 510, 130, 60, (255,255,255), "TimesNewRoman", (0,0,0), "Attack 4")
            
            attack1_button.showButton(gameScreen.returnTitle())
            attack2_button.showButton(gameScreen.returnTitle())
            attack3_button.showButton(gameScreen.returnTitle())
            attack4_button.showButton(gameScreen.returnTitle())

            attack1_barbutton = attack1_button.focusCheck(mouse_pos, mouse_click)
            attack2_barbutton = attack2_button.focusCheck(mouse_pos, mouse_click)
            attack3_barbutton = attack3_button.focusCheck(mouse_pos, mouse_click)
            attack4_barbutton = attack4_button.focusCheck(mouse_pos, mouse_click)
            
            if attack1_barbutton or attack2_barbutton or attack3_barbutton or attack4_barbutton :
                slash_animate.animate()

            

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

        
