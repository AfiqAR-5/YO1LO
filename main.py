import pygame, sys
from button import Button

pygame.init()

#Screen
SCREEN = pygame.display.set_mode((1280, 720), pygame.RESIZABLE)
pygame.display.set_caption("Menu") #window name

#background picture
BG = pygame.image.load("assets/Background.png")

#background music
bgmusic = pygame.mixer.Sound("assets/bgmone.mp3")

#button font
def get_font(size): 
    return pygame.font.Font("assets/font.ttf", size)

#title font
#def get_font(size): 
    #return pygame.font.Font("assets/font.ttf", size)



#Play button

def play():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("black")

        PLAY_TEXT = get_font(45).render("This is the PLAY screen.", True, "White")
        PLAY_RECT = PLAY_TEXT.get_rect(center=(640, 260))
        SCREEN.blit(PLAY_TEXT, PLAY_RECT)

        PLAY_BACK = Button(image=None, pos=(640, 460), 
                            text_input="BACK", font=get_font(75), base_color="White", hovering_color="Green")

        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    main_menu()

        pygame.display.update()



#Credits button

def credits():
    while True:
        CREDITS_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("white")

        CREDITS_TEXT = get_font(45).render("This is the CREDITS screen.", True, "Black")
        CREDITS_RECT = CREDITS_TEXT.get_rect(center=(640, 260))
        SCREEN.blit(CREDITS_TEXT, CREDITS_RECT)

        CREDITS_BACK = Button(image=None, pos=(640, 460), 
                            text_input="BACK", font=get_font(75), base_color="Black", hovering_color="Green")

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



#Main menu (all buttons located, come after defining buttons)

def main_menu():
    while True:
        SCREEN.blit(BG, (0, 0)) #background

        MENU_MOUSE_POS = pygame.mouse.get_pos() #detecting mouse position

        MENU_TEXT = get_font(100).render("YO1LO", True, "white")
        MENU_RECT = MENU_TEXT.get_rect(center=(340, 200))


        #Button Appearance
        PLAY_BUTTON = Button(image=pygame.image.load("assets/transparent.png"), pos=(340, 350), 
                            text_input="PLAY", font=get_font(55), base_color="#d7fcd4", hovering_color="White")
        CREDITS_BUTTON = Button(image=pygame.image.load("assets/transparent.png"), pos=(340, 450), 
                            text_input="CREDITS", font=get_font(55), base_color="#d7fcd4", hovering_color="White")
        QUIT_BUTTON = Button(image=pygame.image.load("assets/transparent.png"), pos=(340, 550), 
                            text_input="QUIT", font=get_font(55), base_color="#d7fcd4", hovering_color="White")

        SCREEN.blit(MENU_TEXT, MENU_RECT)

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
                    play()
                if CREDITS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    credits()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS): #if pressing the quit button
                    pygame.quit()
                    sys.exit()

            #if event.type == pygame.VIDEORESIZE: #to adjust the screen to full size
                #pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)

        pygame.display.update()
        bgmusic.play() #to play the music while main menu is running

main_menu()