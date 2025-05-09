import pygame
import random



clock = pygame.time.Clock()

title = True
timer = 0

       
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
play_BUTTON = Button(325, 200, 130, 70, (pygame.image.load("New_Piskel.png")))


# Game Screen Buttons
black_box = Box(0, 400, 800, 200, (0,0,0), "TimesNewRoman", (0,0,0), "")
left_gray_box = Box(10, 410, 290, 180, (128,128,128), "TimesNewRoman", (0,0,0), "")
right_gray_box = Box(310, 410, 480, 180, (128,128,128), "TimesNewRoman", (0,0,0), "")

attack_button = Box(30, 470, 110, 50, (255,255,255), "TimesNewRoman", (0,0,0), "Attack")
defend_button = Box(170, 470, 110, 50, (255,255,255), "TimesNewRoman", (0,0,0), "Defend")
item_button = Box(30, 530, 110, 50, (255,255,255), "TimesNewRoman", (0,0,0), "Item")
skip_button = Box(170, 530, 110, 50, (255,255,255), "TimesNewRoman", (0,0,0), "Skip")

attack1_button = Box(350, 430, 130, 60, (255,255,255), "TimesNewRoman", (0,0,0), "Attack 1")
attack2_button = Box(620, 430, 130, 60, (255,255,255), "TimesNewRoman", (0,0,0), "Attack 2")
attack3_button = Box(350, 510, 130, 60, (255,255,255), "TimesNewRoman", (0,0,0), "Attack 3")
attack4_button = Box(620, 510, 130, 60, (255,255,255), "TimesNewRoman", (0,0,0), "Attack 4")

item1_button = Box(350, 430, 130, 60, (255,255,255), "TimesNewRoman", (0,0,0), "Item 1")
item2_button = Box(620, 430, 130, 60, (255,255,255), "TimesNewRoman", (0,0,0), "Item 2")
item3_button = Box(350, 510, 130, 60, (255,255,255), "TimesNewRoman", (0,0,0), "Item 3")
item4_button = Box(620, 510, 130, 60, (255,255,255), "TimesNewRoman", (0,0,0), "Item 4")

current_player = Box(325, 175, 150, 50, (255,255,255), "TimesNewRoman", (0,0,0), "Player 1")



 
done = False
 
toggle = False

attack_var = 0
item_var = 0

while not done:
    clock.tick(60)
    timer += 1
   
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

        current_player.showButton(gameScreen.returnTitle())
       
        attack_barbutton = attack_button.focusCheck(mouse_pos, mouse_click)
        item_barbutton = item_button.focusCheck(mouse_pos, mouse_click)


        if (mouse_pos[0] >= attack_button.x and mouse_pos[0] <= attack_button.x + attack_button.sx and mouse_pos [1] >= attack_button.y and mouse_pos[1] <= attack_button.y + attack_button.sy):
            attack_button = Box(30, 470, 110, 50, (150,30,30), "TimesNewRoman", (0,0,0), "Attack")

        else: 
            attack_button = Box(30, 470, 110, 50, (255,255,255), "TimesNewRoman", (0,0,0), "Attack")
            
        if attack_barbutton and timer > num or attack_var == 1:
            attack_var = 1
            item_var = 0
            
            attack1_button.showButton(gameScreen.returnTitle())
            attack2_button.showButton(gameScreen.returnTitle())
            attack3_button.showButton(gameScreen.returnTitle())
            attack4_button.showButton(gameScreen.returnTitle())

        if item_barbutton and timer > num or item_var == 1:
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

        
