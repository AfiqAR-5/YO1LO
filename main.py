import pygame, sys
from button import Button
from prologue import dialogue1

pygame.init()

#Screen
SCREEN = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Menu") #window name

#background picture
BG = pygame.image.load("assets/background.png")

#background music
introbgm = pygame.mixer.Sound("assets/Audio/introbgm.mp3")
bgmusic = pygame.mixer.Sound("assets/Audio/bgmone.mp3")
running = True
font = pygame.font.Font('assets/Font/ARCADECLASSIC.TTF', 32)

#default font
def get_font(size): 
    return pygame.font.Font("assets/Font/getfont.ttf", size)

#button font
def button_font(size): 
    return pygame.font.Font("assets/Font/buttonfont.ttf", size)

#title font
def title_font(size): 
    return pygame.font.Font("assets/Font/titlefont.ttf", size)

#char menu font
def charmenu_font(size):   
    return pygame.font.Font("assets/Font/ARCADECLASSIC.TTF", size)

#Credits button

def credits():

    title = charmenu_font(60).render("CREDITS", True, "White")
    title_rect = title.get_rect(x=530, y=65)
    SCREEN.blit(title, title_rect)

    while True:
        CREDITS_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.blit(BG, (0,0))
        SCREEN.blit(title,title_rect)


        CREDITS_WILLIE = ("Lecturer and Teacher              Mr Willie")
        CREDITS_AFIQ = ("Storyboarding                                Afiq")
        CREDITS_CANDU = ("Game Mechanics                       Wan Amier")
        CREDITS_AMIR = ("Data Sorter                         Amir Asyraf")

        CREDITS_TEXT1 = get_font(50).render(CREDITS_WILLIE, True, "White")
        CREDITS_TEXT2 = get_font(50).render(CREDITS_AFIQ, True, "White")
        CREDITS_TEXT3 = get_font(50).render(CREDITS_CANDU, True, "White")
        CREDITS_TEXT4 = get_font(50).render(CREDITS_AMIR, True, "White")

        CREDITS_RECT1 = CREDITS_TEXT1.get_rect(center=(640, 250))
        CREDITS_RECT2 = CREDITS_TEXT2.get_rect(center=(640, 350))
        CREDITS_RECT3 = CREDITS_TEXT3.get_rect(center=(640, 450))
        CREDITS_RECT4 = CREDITS_TEXT4.get_rect(center=(640, 550))

        SCREEN.blit(CREDITS_TEXT1, CREDITS_RECT1)
        SCREEN.blit(CREDITS_TEXT2, CREDITS_RECT2)
        SCREEN.blit(CREDITS_TEXT3, CREDITS_RECT3)
        SCREEN.blit(CREDITS_TEXT4, CREDITS_RECT4)


        #Credits back button
        CREDITS_BACK = Button(image=pygame.image.load("assets/backbutton.png"), pos=(130, 100), 
                            text_input="       ", font=charmenu_font(75), base_color="White", hovering_color="#ba2323")

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
                    dialogue()
                if CREDITS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    credits()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS): #if pressing the quit button
                    pygame.quit()
                    sys.exit()

        pygame.display.update()
        bgmusic.play(1)

def dialogue():
    font = pygame.font.Font('assets/Font/Cinzel.ttf', 24)
    screen = pygame.display.set_mode([1280, 720])
    timer = pygame.time.Clock()
    messages = ('In the cold, dim cell where time stretches like taffy...',
                'A young soul lingers on the bitter memories of a life stolen.',
                'A decade behind bars, yet the scene-',
                'Replays in his mind like yesterday\'s nightmare.',
                'The door creaking open...',
                'The sight of his mother\'s lifeless body...',
                'The shadowy figure fleeing into the night...',
                'Mistaken identity became his shackles...',
                'A cruel twist of fate that landed him here.',
                'With each passing day, the echoes of that-',
                'fateful evening grow louder...',
                'A relentless reminder of the injustice that binds him.',
                'This is a story that revolves around a certain figure...',
                'With a name bestowed upon him...',
                'IEMAN...',
                '...')
    snip = font.render('', True, 'white')
    counter = 0
    speed = 1
    active_message = 0
    message = messages[active_message]

    run = True
    while run:

        timer.tick(60)
        screen.fill('black')

        if counter < speed * len(message):
            counter += 1

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if counter >= speed * len(message) and active_message < len(messages) - 1:
                        active_message += 1
                        message = messages[active_message]
                        counter = 0
                    else:
                        counter = speed * len(message)
                if active_message == 15:
                    introbgm.stop()
                    dialogue1()

        snip = font.render(message[0:counter // speed], True, 'white')
        screen.blit(snip, (100, 360))

        pygame.display.flip()
        bgmusic.stop()
        introbgm.play(1)

main_menu()