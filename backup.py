import pygame, sys
from button import Button

pygame.init()

#Screen
SCREEN = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Menu") #window name

#background picture
BG = pygame.image.load("assets/background.png")

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
    bg = pygame.image.load('assets/Background.png')
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


#default font
def get_font(size): 
    return pygame.font.Font("assets/getfont.ttf", size)

#button font
def button_font(size): 
    return pygame.font.Font("assets/buttonfont.ttf", size)

#title font
def title_font(size): 
    return pygame.font.Font("assets/titlefont.ttf", size)


#Play button


def play():
    while True:
        char_menu()
        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        #from this point, story selection loop

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
        #test


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
                    play()
                if CREDITS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    credits()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS): #if pressing the quit button
                    pygame.quit()
                    sys.exit()

        pygame.display.update()
        bgmusic.play() #to play the music while main menu is running

main_menu()