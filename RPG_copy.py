import pygame 
import random



clock = pygame.time.Clock()

title = True

class Screen():
    
    def __init__(self, title, width = 440, height = 445, fill=(0,0,255)):
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
    def __init__(self, x, y, sx, sy, bcolor, fbcolor, font, fcolor, text):
        self.x = x
        self.y = y
        self.sx = sx
        self.sy = sy
        self.fontsize = 25
        self.bcolor = bcolor
        self.fbcolor = fcolor
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
        display.blit(textsurface, ((self.x + (self.sx/2)-(self.fontsize/2)*(len(self.text)/2)-5, (self.y +(self.sy/2)-(self.fontsize/2)-4))))

    def focusCheck(self, mousepos, mouseclick):
        if (mousepos[0] >= self.x and mousepos[0] <= self.x + self.sx and mousepos [1] >= self.y and mousepos[1] <= self.y + self.sy):
            self.CurrentState = True
            return mouseclick[0]
        else:
            self.CurrentState = False
            return False

pygame.init()
# INITIALIZATION OF SYSTEM FONTS
pygame.font.init()
 
# CREATING THE OBJECT OF THE
# CLASS Screen FOR MENU SCREEN
menuScreen = Screen("Menu Screen")
 
# CREATING THE OBJECT OF THE CLASS
# Screen FOR CONTROL SCREEN
control_bar = Screen("Control Screen")

sound = Screen("Sound")
 
# CALLING OF THE FUNCTION TO
# MAKE THE SCREEN FOR THE WINDOW
win = menuScreen.makeCurrentScreen()
 
# MENU BUTTON
MENU_BUTTON = Button(150, 150, 150, 50, (255, 250, 250), (255, 0, 0), "TimesNewRoman", (255, 255, 255), "Main Menu")
 
# CONTROL BUTTON
CONTROL_BUTTON = Button(150, 150, 150, 50, (0, 0, 0), (0, 0, 255), "TimesNewRoman", (255, 255, 255), "Back")

SOUND_BUTTON = Button(150, 150, 150, 50, (0, 0, 0), (0, 0, 255), "TimesNewRoman", (255, 255, 255), "Sound")
 
done = False
 
toggle = False

while not done:
    clock.tick(60)
# CALLING OF screenUpdate
    # function FOR MENU SCREEN
    menuScreen.screenUpdate()
    # CALLING THE FUNCTION OF CONTROL BAR
    control_bar.screenUpdate()

    sound.screenUpdate()
    # STORING THE MOUSE EVENT
    # TO CHECK THE POSITION OF THE MOUSE
    mouse_pos = pygame.mouse.get_pos()
    # CHECKING THE MOUSE CLICK EVENT
    mouse_click = pygame.mouse.get_pressed()
    # KEY PRESSED OR NOT
    keys = pygame.key.get_pressed()
 
# MENU BAR CODE TO ACCESS
    # CHECKING MENU SCREEN FOR ITS UPDATE
    if menuScreen.checkUpdate((255, 0, 0)):
        control_barbutton = MENU_BUTTON.focusCheck(mouse_pos, mouse_click)
        MENU_BUTTON.showButton(menuScreen.returnTitle())
 
        if control_barbutton:
            pygame.event.wait()
            win = control_bar.makeCurrentScreen()
            menuScreen.endCurrentScreen()
 
# CONTROL BAR CODE TO ACCESS
        # CHECKING CONTROL SCREEN FOR ITS UPDATE
    elif control_bar.checkUpdate((0, 255, 0)):
        return_back = CONTROL_BUTTON.focusCheck(mouse_pos, mouse_click)
        CONTROL_BUTTON.showButton(control_bar.returnTitle())
 
        if return_back:
            pygame.event.wait()
            win = sound.makeCurrentScreen()
            control_bar.endCurrentScreen()
    
 
# SOUND BAR CODE TO ACCESS
        # CHECKING CONTROL SCREEN FOR ITS UPDATE
    elif sound.checkUpdate((0, 0, 255)):
        return_menu = SOUND_BUTTON.focusCheck(mouse_pos, mouse_click)
        SOUND_BUTTON.showButton(sound.returnTitle())
 
        if return_menu:
            pygame.event.wait()
            win = menuScreen.makeCurrentScreen()
            sound.endCurrentScreen()
            
    #  CHECKING IF THE EXIT BUTTON HAS BEEN CLICKED OR NOT
    for event in pygame.event.get():
        # IF CLICKED THEN CLOSE THE WINDOW
        if(event.type == pygame.QUIT):
            done = True
 
    pygame.display.update()
# CLOSE THE PROGRAM
pygame.quit()
