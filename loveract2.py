import pygame, sys, time
from button import Button

pygame.init()

#things needed to add
#1 text box /
#2 skip button 
#3 func to add charac in screen (and can move) /

# screen display
WIDTH = 1280
HEIGHT = 720
SCREEN = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption("ACT 1")

surface = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
fps = 60
timer = pygame.time.Clock()


# text fonts
def intro_font(size): 
    return pygame.font.Font("assets/getfont.ttf", size)


# act1 begins
def act1():
    while True:
        for event in pygame.event.get():

            #if pressing x button on window screen

            if event.type == pygame.QUIT: 
                pygame.quit()
                sys.exit()
                
        pygame.display.update()


# intro before act1 begins

introtext = pygame.transform.scale(pygame.image.load("assets/introact1.png"), (1128, 634))
introtext_rect = introtext.get_rect(center = (WIDTH // 2 , HEIGHT // 2))

transparency = 120
change = 0

def surfaceintro():
    pygame.draw.rect(surface, (255, 0, 0 ,transparency), [100, 100, 200, 100])

def intro():
    while True:
        
        timer.tick(fps)
                
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    change = 1 
                if event.key == pygame.K_DOWN:
                    change = -1 
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    change = 0
                if event.key == pygame.K_DOWN:
                    change = 0
        
        transparency += change

        if transparency > 255:
            transparency = 0
        if transparency < 0:
            transparency = 255

        SCREEN.fill("black")
        SCREEN.blit(surface, (0,0))
        surfaceintro()
        

        pygame.display.flip()
    
intro()