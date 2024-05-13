import pygame, sys
from button import Button
from Chap1 import *

pygame.init()

#Screen
SCREEN = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Menu") #window name

#background picture
BG = pygame.image.load("assets/background.png")

#background music
bgmusic = pygame.mixer.Sound("assets/bgmone.mp3")
running = True
font = pygame.font.Font('assets/ARCADECLASSIC.TTF', 32)

#default font
def get_font(size): 
    return pygame.font.Font("assets/getfont.ttf", size)

#button font
def button_font(size): 
    return pygame.font.Font("assets/buttonfont.ttf", size)

#title font
def title_font(size): 
    return pygame.font.Font("assets/titlefont.ttf", size)

#char menu font
def charmenu_font(size):   
    return pygame.font.Font("assets/ARCADECLASSIC.TTF", size)


#character menu screen


def char_menu():

    pygame.display.set_caption('Character Menu')

    display = SCREEN
    bg = pygame.image.load('assets/Background.png')
    scaled_bg = pygame.transform.scale(bg, (1280,720))

    bg_rect = scaled_bg.get_rect(x=0,y=0)
    title = charmenu_font(60).render("Choose your character", True, "White")
    title_rect = title.get_rect(x=320, y=100)
    SCREEN.blit(title, title_rect)

    while running:
        display.blit(scaled_bg, bg_rect)

        CHAR_MOUSE_POS = pygame.mouse.get_pos()

        BACK_BUTTON = Button(image=pygame.image.load("assets/transparent.png"), pos=(650, 630), 
                    text_input="BACK", font=get_font(70), base_color="White", hovering_color="#ba2323")
        
        MC = Button(image=pygame.image.load("assets/mc.png"), pos=(640, 360), 
                    text_input=None, font=get_font(55), base_color="White", hovering_color="#ba2323")
        
        LOVER = Button(image=pygame.image.load("assets/lover.png"), pos=(320, 390), 
                    text_input=None, font=get_font(55), base_color="White", hovering_color="#ba2323")
        
        VILLAIN = Button(image=pygame.image.load("assets/villain.png"), pos=(960, 330), 
                    text_input=None, font=get_font(55), base_color="White", hovering_color="#ba2323")
            
        SCREEN.blit(title, title_rect)
        
        for button in [BACK_BUTTON, MC, LOVER, VILLAIN]:
            button.changeColor(CHAR_MOUSE_POS)
            button.update(display)

        for event in pygame.event.get():

            if event.type == pygame.QUIT: #if pressing x button on window screen
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if BACK_BUTTON.checkForInput(CHAR_MOUSE_POS):
                    main_menu()
                
                if MC.checkForInput(CHAR_MOUSE_POS):
                    print("working!")
                    fade1(1280,720)
                
                if LOVER.checkForInput(CHAR_MOUSE_POS):
                    print("working!")
                
                if VILLAIN.checkForInput(CHAR_MOUSE_POS):
                    print("working!")
            
            pygame.display.update()
            bgmusic.play()


#function to add fade in effect


def fade1(width, height): 
    
    screenfade = True

    while screenfade == True:    
        fade = pygame.Surface((width, height))
        fade.fill((0,0,0))
        for alpha in range(0, 300):
            fade.set_alpha(alpha)
            SCREEN.blit(fade, (0,0))
            bgmusic.stop()
            pygame.display.update()
            pygame.time.delay(5)
            screenfade == False
            intro()


#function to add loading bar


def loading_bar():
    loading = True
    
    while loading == True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        




#Credits button

def credits():
    while True:
        CREDITS_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.blit(BG, (0,0))

        #Credits message.. (I dont know how to do this so i made one by one ;-;)

        CREDITS_WILLIE = ("Lecturer and Teacher              Mr Willie")
        CREDITS_AFIQ = ("Storyboarding                                Afiq")
        CREDITS_CANDU = ("Game Mechanics                       Wan Amier")
        CREDITS_AMIR = ("Data Sorter                         Amir Asyraf")

        CREDITS_TEXT1 = get_font(50).render(CREDITS_WILLIE, True, "White")
        CREDITS_TEXT2 = get_font(50).render(CREDITS_AFIQ, True, "White")
        CREDITS_TEXT3 = get_font(50).render(CREDITS_CANDU, True, "White")
        CREDITS_TEXT4 = get_font(50).render(CREDITS_AMIR, True, "White")

        CREDITS_RECT1 = CREDITS_TEXT1.get_rect(center=(640, 200))
        CREDITS_RECT2 = CREDITS_TEXT2.get_rect(center=(640, 300))
        CREDITS_RECT3 = CREDITS_TEXT3.get_rect(center=(640, 400))
        CREDITS_RECT4 = CREDITS_TEXT4.get_rect(center=(640, 500))

        SCREEN.blit(CREDITS_TEXT1, CREDITS_RECT1)
        SCREEN.blit(CREDITS_TEXT2, CREDITS_RECT2)
        SCREEN.blit(CREDITS_TEXT3, CREDITS_RECT3)
        SCREEN.blit(CREDITS_TEXT4, CREDITS_RECT4)


        #Credits back button
        CREDITS_BACK = Button(image=None, pos=(640, 660), 
                            text_input="BACK", font=title_font(75), base_color="White", hovering_color="#ba2323")

        CREDITS_BACK.changeColor(CREDITS_MOUSE_POS)
        CREDITS_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if CREDITS_BACK.checkForInput(CREDITS_MOUSE_POS):
                    main_menu()

        pygame.display.update()


#Main menu (all buttons located, comes after defining buttons)


def main_menu():
    while True:
        SCREEN.blit(BG, (0, 0))  #background

        MENU_MOUSE_POS = pygame.mouse.get_pos()  #detecting mouse position

        #Title Screen
        MENU_TEXT = title_font(225).render("YOLO", True, "White")
        MENU_RECT = MENU_TEXT.get_rect(center=(340, 175))


        #Button Appearance
        PLAY_BUTTON = Button(image=pygame.image.load("assets/transparent.png"), pos=(340, 350), 
                            text_input="PLAY", font=button_font(100), base_color="White", hovering_color="#ba2323") #find better colour
        
        CREDITS_BUTTON = Button(image=pygame.image.load("assets/transparent.png"), pos=(340, 450), 
                            text_input="CREDITS", font=button_font(100), base_color="White", hovering_color="#ba2323")
        
        QUIT_BUTTON = Button(image=pygame.image.load("assets/transparent.png"), pos=(340, 550), 
                            text_input="QUIT", font=button_font(100), base_color="White", hovering_color="#ba2323")

        SCREEN.blit(MENU_TEXT, MENU_RECT)

        #Button change colour function

        for button in [PLAY_BUTTON, CREDITS_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)
        
        #detecting mouse click, and what action to do

        for event in pygame.event.get():

            if event.type == pygame.QUIT: #if pressing x button on window screen
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    char_menu()
                if CREDITS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    credits()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS): #if pressing the quit button
                    pygame.quit()
                    sys.exit()

        pygame.display.update()
        bgmusic.play() #to play the music while main menu is running

main_menu()