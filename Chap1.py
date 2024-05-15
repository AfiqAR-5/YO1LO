import pygame, sys, time, button
from config import *

#things needed to add
#1 text box
#2 skip button
#3 func to add charac in screen (and can move)
#4 

pygame.init()

def text_font():
    return pygame.font.Font('assets/Ticketing.ttf', 30)

def screenbg():

    pygame.display.set_caption('YO1LO')

    bg = pygame.image.load('assets/prisoncell.png')
    scaled_bg = pygame.transform.scale(bg, (1280,720))
    bg_rect = scaled_bg.get_rect(x=0,y=0)
    
    text = text_font().render("testing", True, "White")
    text_rect = text.get_rect(x=320, y=100)

    while True:
        SCREEN.blit(bg, bg_rect)
        SCREEN.blit(text, text_rect)
        pygame.time.delay(1)


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
    
        pygame.display.update()
        time.sleep(2)
    #def button(self):
       
