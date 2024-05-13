import pygame, sys
from config import *
from button import Button

#things needed to add
#1 text box
#2 skip button
#3 func to add charac in screen (and can move)
#4 

pygame.init()

def button_font(size): 
    return pygame.font.Font("assets/ARCADECLASSIC.TTF", size)

def text_font(size):
    return pygame.font.Font('assets/introfont.otf', size)

def troll_font(size):
    return pygame.font.Font('assets/trollfont.ttf', size)

def intro():

    pygame.display.set_caption('YO1LO')

    bg1 = pygame.image.load('assets/prison.jpg')
    scaled_bg1 = pygame.transform.scale(bg1, (1280,720))
    bg1_rect = scaled_bg1.get_rect(x=0,y=0)

    hidden = pygame.image.load('assets/Play Rect.png')
    scaled_hidden = pygame.transform.scale(hidden, (500,200))

    while True:
        SCREEN.blit(scaled_bg1, bg1_rect)


        CONTINUE_BUTTON = Button(image=pygame.image.load("assets/transparent.png"), pos=(640, 600), 
                            text_input="Click here to continue", font=button_font(30), base_color="White", hovering_color="#ba2323")

        HIDDEN = Button(image=scaled_hidden, pos=(640, 360), 
                            text_input="ACT ONE", font=text_font(100), base_color="White", hovering_color="#ba2323")

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        for button in [CONTINUE_BUTTON, HIDDEN]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)

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
    #def button(self):


def troll():

    while True:
        SCREEN.fill((0,0,0))

        OPTIONS_TEXT = troll_font(30).render("What's with the intrusive thought to press the intro text?", True, "Red")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(640, 300))
        SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)

        BACK = Button(image=pygame.image.load("assets/transparent.png"), pos=(640, 600), 
                                text_input="BACK", font=button_font(100), base_color="White", hovering_color="Green")

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        for button in [BACK]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                    if BACK.checkForInput(MENU_MOUSE_POS):
                        intro()

        pygame.display.update()

def chap1():
    while True:
        bg1 = pygame.image.load('assets/prisoncell.jpg')
        scaled_bg1 = pygame.transform.scale(bg1, (1280,720))
        bg1_rect = scaled_bg1.get_rect(x=0,y=0)

        SCREEN.blit(scaled_bg1,bg1_rect)

        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
        
        pygame.display.update()


       
