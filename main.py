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
running = True
font = pygame.font.Font('ARCADECLASSIC.TTF', 32)

def get_font(size): 
    return pygame.font.Font("assets/font.ttf", size)

def char_menu():

    pygame.display.set_caption('Character Menu')

    display = SCREEN
    mc_pic = pygame.image.load('mc.png')
    bg = pygame.image.load('Background.png')
    size1 = pygame.transform.scale(bg, (1280,720))

    mc_pic = pygame.image.load('mc.png')
    mc_rect = mc_pic.get_rect(x=400,y=95)

    lover_pic = pygame.image.load('lover.png')
    lover_rect = mc_pic.get_rect(x=200,y=200)

    villain_pic = pygame.image.load('villain.png')
    villain_rect = mc_pic.get_rect(x=600,y=100)

    bg_rect = size1.get_rect(x=0,y=0)
    title = font.render("Choose your character", True, "White")
    title_rect = title.get_rect(x=320, y=100)
    SCREEN.blit(title, title_rect)

    while running:
        display.blit(size1, bg_rect)
        display.blit(mc_pic, mc_rect)
        display.blit(lover_pic, lover_rect)
        display.blit(villain_pic, villain_rect)

        CHAR_MOUSE_POS = pygame.mouse.get_pos()

        BACK_BUTTON = Button(image=pygame.image.load("assets/transparent.png"), pos=(340, 550), 
                    text_input="BACK", font=get_font(55), base_color="#d7fcd4", hovering_color="White")
            
        SCREEN.blit(title, title_rect)
        
        for button in [BACK_BUTTON]:
            button.changeColor(CHAR_MOUSE_POS)
            button.update(display)

        for event in pygame.event.get():

            if event.type == pygame.QUIT: #if pressing x button on window screen
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if BACK_BUTTON.checkForInput(CHAR_MOUSE_POS):
                    main_menu()
            pygame.display.update()
            bgmusic.play()


#button font
def get_font(size): 
    return pygame.font.Font("assets/font.ttf", size)

#Play button

def play():
    while True:
        char_menu()
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