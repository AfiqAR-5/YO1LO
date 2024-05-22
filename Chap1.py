import pygame, sys
from config import *
from button import Button
from Save_data import SaveLoadManager

#things needed to add
#1 text box
#2 skip button
#3 func to add charac in screen (and can move)
#4 

pygame.init()

screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("YO1LO")
font = pygame.font.Font("assets/ARCADE.TTF", 100)


bg = pygame.image.load('assets/prisoncell.png')
scaled_bg = pygame.transform.scale(bg, (1280,720))
bg_rect = scaled_bg.get_rect(x=0,y=0)


class Button1():
	def __init__(self, image, x_pos, y_pos, text_input):
		self.image = image
		self.x_pos = x_pos
		self.y_pos = y_pos
		self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
		self.text_input = text_input
		self.text = font.render(self.text_input, True, "white")
		self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))

	def update(self, screen):
		if self.image is not None:
			screen.blit(self.image, self.rect)
		screen.blit(self.text, self.text_rect)

	def checkForInput(self, position):
		if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
			return True
		return False

	def changeColor(self, position):
		if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
			self.text = font.render(self.text_input, True, "#ba2323")
		else:
			self.text = font.render(self.text_input, True, "white")



def text(text):
     
    run = True

    

    while run:

        button_surface = pygame.image.load("assets/textbox.png")
        button_surface = pygame.transform.scale(button_surface, (850, 200))

        textbox = Button(image=button_surface, pos=(640, 600), 
                            text_input=None, font=button_font(30), base_color="White", hovering_color="#ba2323")
        CHAR_MOUSE_POS = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
               if textbox.checkForInput(pygame.mouse.get_pos()):
                    pass

        texthere = button_font(20).render(text, True, "White")
        text_rect = texthere.get_rect(x=500, y=615)

        return screen.blit(texthere, text_rect)

    textbox.update(screen)
    textbox.changeColor(CHAR_MOUSE_POS)
    pygame.display.update()    

def button_font(size): 
    return pygame.font.Font("assets/ARCADECLASSIC.TTF", size)

def text_font(size):
    return pygame.font.Font('assets/introfont.otf', size)

def troll_font(size):
    return pygame.font.Font('assets/trollfont.ttf', size)

def charmenu_font(size):   
    return pygame.font.Font("assets/ARCADECLASSIC.TTF", size)

def mc():
     mc = pygame.image.load('assets/mc.png')
     mc_rect = mc.get_rect(x=300,y=300)

     return screen.blit(mc,mc_rect)

def intro():

    pygame.display.set_caption('YO1LO')

    bg1 = pygame.image.load('assets/prison.jpg')
    scaled_bg1 = pygame.transform.scale(bg1, (1280,720))
    bg1_rect = scaled_bg1.get_rect(x=0,y=0)

    hidden = pygame.image.load('assets/Play Rect.png')
    scaled_hidden = pygame.transform.scale(hidden, (500,200))

    while True:
        screen.blit(scaled_bg1, bg1_rect)


        CONTINUE_BUTTON = Button(image=pygame.image.load("assets/transparent.png"), pos=(640, 600), 
                            text_input="Click here to continue", font=button_font(30), base_color="White", hovering_color="#ba2323")

        HIDDEN = Button(image=scaled_hidden, pos=(640, 360), 
                            text_input="ACT ONE", font=text_font(100), base_color="White", hovering_color="#ba2323")

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        for buttons in [CONTINUE_BUTTON, HIDDEN]:
            buttons.changeColor(MENU_MOUSE_POS)
            buttons.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if HIDDEN.checkForInput(MENU_MOUSE_POS):
                    troll()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if CONTINUE_BUTTON.checkForInput(MENU_MOUSE_POS):
                     chap1()
                

        pygame.display.flip()


def troll():

    while True:
        screen.fill((0,0,0))

        OPTIONS_TEXT = troll_font(30).render("What's with the intrusive thought to press the intro text?", True, "Red")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(640, 300))
        screen.blit(OPTIONS_TEXT, OPTIONS_RECT)

        BACK = Button(image=pygame.image.load("assets/transparent.png"), pos=(640, 600), 
                                text_input="BACK", font=button_font(100), base_color="White", hovering_color="Green")

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        for button in [BACK]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                    if BACK.checkForInput(MENU_MOUSE_POS):
                        intro()

        pygame.display.update()

def chap1():

    run = True

    while run:

        screen.blit(scaled_bg,bg_rect)
        button_surface = pygame.image.load("assets/textbox.png")
        button_surface = pygame.transform.scale(button_surface, (850, 200))

        textbox = Button(image=button_surface, pos=(640, 600),
                            text_input=None, font=button_font(100), base_color="White", hovering_color="#ba2323")
        CHAR_MOUSE_POS = pygame.mouse.get_pos()
        PAUSE_BUTTON = Button(image=pygame.image.load("assets/PauseButton.png"), pos=(100, 60),
                            text_input=None, font=button_font(100), base_color="White", hovering_color="#ba2323")

        
        
        mc()
        PAUSE_BUTTON.changeColor(CHAR_MOUSE_POS)
        PAUSE_BUTTON.update(screen)
        textbox.changeColor(CHAR_MOUSE_POS)
        textbox.update(screen)
        text("testing")

        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if PAUSE_BUTTON.checkForInput(CHAR_MOUSE_POS):
                    Pause_button()
                if textbox.checkForInput(CHAR_MOUSE_POS):
                    text("testing2")
                    
        pygame.display.update()

def Pause_button():

    pygame.display.set_caption('Resume Menu')

    display = SCREEN
    bg = pygame.image.load('assets/Background.png')
    scaled_bg = pygame.transform.scale(bg, (1280,720))

    bg_rect = scaled_bg.get_rect(x=0,y=0)
    title = charmenu_font(120).render("MENUS", True, "Gold")
    title_rect = title.get_rect(x=480, y=90)
    SCREEN.blit(title, title_rect)
        
    while True :
        display.blit(scaled_bg, bg_rect)
        
        CHAR_MOUSE_POS = pygame.mouse.get_pos()

        RESUME_BUTTON = Button(image=pygame.image.load("assets/transparent.png"), pos=(650, 280),
                       text_input="RESUME", font=button_font(100), base_color="White", hovering_color="#ba2323")
        
        SAVE_BUTTON = Button(image=pygame.image.load("assets/transparent.png"), pos=(650, 430),
                       text_input="SAVE", font=button_font(100), base_color="White", hovering_color="#ba2323")
        
        EXIT_BUTTON = Button(image=pygame.image.load("assets/transparent.png"), pos=(650, 580),
                       text_input="QUIT", font=button_font(100), base_color="White", hovering_color="#ba2323")
        
        SCREEN.blit(title, title_rect)
        
        for button in [RESUME_BUTTON, SAVE_BUTTON, EXIT_BUTTON]:
            button.changeColor(CHAR_MOUSE_POS)
            button.update(screen)
    
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                    if RESUME_BUTTON.checkForInput(CHAR_MOUSE_POS):
                        chap1()
                    if SAVE_BUTTON.checkForInput(CHAR_MOUSE_POS):
                        SaveLoadManager()
                    if EXIT_BUTTON.checkForInput(CHAR_MOUSE_POS):
                        pygame.quit()
                        sys.exit()
                    
        pygame.display.update()

                    