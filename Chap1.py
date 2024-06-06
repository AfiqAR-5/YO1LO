import pygame, sys
from config import *
from button import Button
pygame.init()

bgmusic = pygame.mixer.Sound("assets/bgmtwo.mp3")
sadbgm = pygame.mixer.Sound("assets/sadbgm.mp3")
introbgm = pygame.mixer.Sound("assets/introbgm.mp3")
speed = 0
strength = 0
sinful = 0
righteous = 0

def textbutton_font(size):   
    return pygame.font.Font("assets/ARCADE.TTF", size)

def prologuefont(size):
    return pygame.font.Font("assets/Cinzel.ttf", size)

def mc(xpos,ypos):
     mc = pygame.image.load('assets/mc.png')
     mc_rect = mc.get_rect(x=xpos,y=ypos)

     return SCREEN.blit(mc,mc_rect)

def walter(xpos,ypos):
     walter = pygame.image.load('assets/walter.png')
     walter_rect = walter.get_rect(x=xpos,y=ypos)

     return SCREEN.blit(walter, walter_rect)

def villain(xpos,ypos):
    villain = pygame.image.load('assets/villain.png')
    villain_rect = villain.get_rect(x=xpos,y=ypos)

    return SCREEN.blit(villain,villain_rect)

def guard(xpos,ypos):
    guard = pygame.image.load('assets/securityguard.png')
    guard_rect = guard.get_rect(x=xpos,y=ypos)

    return SCREEN.blit(guard,guard_rect)

def mcdark():
     mc = pygame.image.load('assets/mcdark.png')
     mc_rect = mc.get_rect(x=270,y=1)

     return SCREEN.blit(mc,mc_rect)

def walterdark():
     walter = pygame.image.load('assets/walterdark.png')
     walter_rect = walter.get_rect(x=670,y=130)

     return SCREEN.blit(walter, walter_rect)

def silhoutte(xpos,ypos):
     silhoutte = pygame.image.load('assets/silhoutte.png')
     silhoutte_rect = silhoutte.get_rect(x=xpos,y=ypos)

     return SCREEN.blit(silhoutte,silhoutte_rect)

def warden(xpos,ypos):
     warden = pygame.image.load('assets/warden.png')
     warden_rect = warden.get_rect(x=xpos,y=ypos)

     return SCREEN.blit(warden,warden_rect)

def pausemenu():

    run = True

    while run:
        MENU_MOUSE_POS = pygame.mouse.get_pos()

        bg = pygame.image.load('assets/background.png')
        scaled_bg = pygame.transform.scale(bg, (1280,720))
        bg_rect = scaled_bg.get_rect(x=0,y=0)
        
        pmenu = pygame.image.load('assets/Play Rect.png')
        scaled_pmenu = pygame.transform.scale(pmenu, (1280,720))
        pmenu_rect = scaled_pmenu.get_rect(x=0,y=0)

        SCREEN.blit(scaled_bg, bg_rect)
        SCREEN.blit(scaled_pmenu, pmenu_rect)

        RESUME = Button(image=pygame.image.load("assets/transparent.png"), pos=(640, 300), 
                            text_input="RESUME", font=textbutton_font(100), base_color="white", hovering_color="red") #find better colour
        
        QUIT = Button(image=pygame.image.load("assets/transparent.png"), pos=(640, 500), 
                            text_input="QUIT", font=textbutton_font(100), base_color="white", hovering_color="red")
        
        for button in [RESUME,QUIT]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)

        for event in pygame.event.get():

            if event.type == pygame.QUIT: #if pressing x button on window screen
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if RESUME.checkForInput(MENU_MOUSE_POS):
                    run = False
                if QUIT.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

            pygame.display.flip()

def choice2():
    while True:

        timer = pygame.time.Clock()

        bg = pygame.image.load('assets/deadlift.jpg')
        scaled_bg = pygame.transform.scale(bg, (1280,720))
        bg_rect = scaled_bg.get_rect(x=0,y=0)

        c1 = pygame.image.load('assets/cbutton.png')
        scaled_c1 = pygame.transform.scale(c1, (500,70))
        c1_rect = scaled_c1.get_rect(x=400,y=550)

        SCREEN.blit(scaled_bg, bg_rect)
        SCREEN.blit(scaled_c1, c1_rect)

        timer.tick(60)

        MENU_MOUSE_POS = pygame.mouse.get_pos()  #detecting mouse position

        CHOICE3 = Button(image=pygame.image.load("assets/next.png"), pos=(1150, 365), 
                            text_input=None, font=textbutton_font(21), base_color="black", hovering_color="#FF3131") #find better colour
        
        CHOICE2 = Button(image=pygame.image.load("assets/nextinverted.png"), pos=(130, 365), 
                            text_input=None, font=textbutton_font(21), base_color="black", hovering_color="#FF3131")

        CHOICE1 = Button(image=pygame.image.load("assets/transparent.png"), pos=(650, 590), 
                            text_input="Deadlift", font=textbutton_font(30), base_color="black", hovering_color="#FF3131")

        PAUSE = Button(image=pygame.image.load("assets/pause.png"), pos=(50, 50), 
                            text_input="           ", font=textbutton_font(21), base_color="black", hovering_color="#FF3131")

        for button in [PAUSE,CHOICE1,CHOICE2,CHOICE3]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)

        for event in pygame.event.get():

            if event.type == pygame.QUIT: #if pressing x button on window screen
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if CHOICE1.checkForInput(MENU_MOUSE_POS):
                    print('Deadlift pressed')
                    pygame.quit()
                    sys.exit()

                if CHOICE2.checkForInput(MENU_MOUSE_POS):
                    print('Next inverted pressed')
                    choice4()
                if CHOICE3.checkForInput(MENU_MOUSE_POS):
                    print('Next pressed')
                    choice3()
                if PAUSE.checkForInput(MENU_MOUSE_POS):
                    pausemenu()

            pygame.display.flip()

def choice3():
    global speed
    while True:

        timer = pygame.time.Clock()

        bg = pygame.image.load('assets/treadmill.jpg')
        scaled_bg = pygame.transform.scale(bg, (1280,720))
        bg_rect = scaled_bg.get_rect(x=0,y=0)

        c1 = pygame.image.load('assets/cbutton.png')
        scaled_c1 = pygame.transform.scale(c1, (500,70))
        c1_rect = scaled_c1.get_rect(x=400,y=550)

        SCREEN.blit(scaled_bg, bg_rect)
        SCREEN.blit(scaled_c1, c1_rect)

        timer.tick(60)

        MENU_MOUSE_POS = pygame.mouse.get_pos()  #detecting mouse position

        CHOICE3 = Button(image=pygame.image.load("assets/next.png"), pos=(1150, 365), 
                            text_input=None, font=textbutton_font(21), base_color="black", hovering_color="#FF3131") #find better colour
        
        CHOICE2 = Button(image=pygame.image.load("assets/nextinverted.png"), pos=(130, 365), 
                            text_input=None, font=textbutton_font(21), base_color="black", hovering_color="#FF3131")

        CHOICE1 = Button(image=pygame.image.load("assets/transparent.png"), pos=(650, 590), 
                            text_input="Treadmill", font=textbutton_font(30), base_color="black", hovering_color="#FF3131")

        PAUSE = Button(image=pygame.image.load("assets/pause.png"), pos=(50, 50), 
                            text_input="           ", font=textbutton_font(21), base_color="black", hovering_color="#FF3131")

        for button in [PAUSE,CHOICE1,CHOICE2,CHOICE3]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)

        for event in pygame.event.get():

            if event.type == pygame.QUIT: #if pressing x button on window screen
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if CHOICE1.checkForInput(MENU_MOUSE_POS):
                    speed =+ 1
                    dialogue15()
                if CHOICE2.checkForInput(MENU_MOUSE_POS):
                    print('Next inverted pressed')
                    choice2()
                if CHOICE3.checkForInput(MENU_MOUSE_POS):
                    print('Next pressed')
                    choice4()
                if PAUSE.checkForInput(MENU_MOUSE_POS):
                    pausemenu()

            pygame.display.flip()

def choice4():
    global strength
    while True:

        timer = pygame.time.Clock()

        bg = pygame.image.load('assets/pullup.jpg')
        scaled_bg = pygame.transform.scale(bg, (1280,720))
        bg_rect = scaled_bg.get_rect(x=0,y=0)

        c1 = pygame.image.load('assets/cbutton.png')
        scaled_c1 = pygame.transform.scale(c1, (500,70))
        c1_rect = scaled_c1.get_rect(x=400,y=550)

        SCREEN.blit(scaled_bg, bg_rect)
        SCREEN.blit(scaled_c1, c1_rect)

        timer.tick(60)

        MENU_MOUSE_POS = pygame.mouse.get_pos()  #detecting mouse position

        CHOICE3 = Button(image=pygame.image.load("assets/next.png"), pos=(1150, 365), 
                            text_input=None, font=textbutton_font(21), base_color="black", hovering_color="#FF3131") #find better colour
        
        CHOICE2 = Button(image=pygame.image.load("assets/nextinverted.png"), pos=(130, 365), 
                            text_input=None, font=textbutton_font(21), base_color="black", hovering_color="#FF3131")

        CHOICE1 = Button(image=pygame.image.load("assets/transparent.png"), pos=(650, 590), 
                            text_input="Pullup", font=textbutton_font(30), base_color="black", hovering_color="#FF3131")

        PAUSE = Button(image=pygame.image.load("assets/pause.png"), pos=(50, 50), 
                            text_input="           ", font=textbutton_font(21), base_color="black", hovering_color="#FF3131")

        for button in [PAUSE,CHOICE1,CHOICE2,CHOICE3]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)

        for event in pygame.event.get():

            if event.type == pygame.QUIT: #if pressing x button on window screen
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if CHOICE1.checkForInput(MENU_MOUSE_POS):
                    strength =+ 1
                    dialogue15v2()
                if CHOICE2.checkForInput(MENU_MOUSE_POS):
                    print('Next inverted pressed')
                    choice3()
                if CHOICE3.checkForInput(MENU_MOUSE_POS):
                    print('Next pressed')
                    choice2()
                if PAUSE.checkForInput(MENU_MOUSE_POS):
                    pausemenu()

            pygame.display.flip()

def choice5():
    global strength, sinful
    while True:

        timer = pygame.time.Clock()

        bg = pygame.image.load('assets/vents.png')
        scaled_bg = pygame.transform.scale(bg, (1280,720))
        bg_rect = scaled_bg.get_rect(x=0,y=0)

        c1 = pygame.image.load('assets/cbutton.png')
        scaled_c1 = pygame.transform.scale(c1, (500,70))
        c1_rect = scaled_c1.get_rect(x=400,y=295)

        c2 = pygame.image.load('assets/cbutton.png')
        scaled_c2 = pygame.transform.scale(c2, (500,70))
        c2_rect = scaled_c2.get_rect(x=400,y=395)

        SCREEN.blit(scaled_bg, bg_rect)
        SCREEN.blit(scaled_c1, c1_rect)
        SCREEN.blit(scaled_c2, c2_rect)

        timer.tick(60)

        MENU_MOUSE_POS = pygame.mouse.get_pos()  #detecting mouse position
        
        CHOICE1 = Button(image=pygame.image.load("assets/transparent.png"), pos=(650, 330), 
                            text_input="Pry open the vent", font=textbutton_font(21), base_color="black", hovering_color="#FF3131")

        CHOICE2 = Button(image=pygame.image.load("assets/transparent.png"), pos=(650, 430), 
                            text_input="Resort to violence", font=textbutton_font(21), base_color="black", hovering_color="#FF3131")

        PAUSE = Button(image=pygame.image.load("assets/pause.png"), pos=(50, 50), 
                            text_input="           ", font=textbutton_font(21), base_color="black", hovering_color="#FF3131")

        for button in [PAUSE,CHOICE1,CHOICE2]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)

        for event in pygame.event.get():

            if event.type == pygame.QUIT: #if pressing x button on window screen
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                    if CHOICE1.checkForInput(MENU_MOUSE_POS):
                        if strength == 1:
                            dialogue35()
                        else:
                            sinful =+ 1
                            dialogue35v2()
                    if CHOICE2.checkForInput(MENU_MOUSE_POS):
                        sinful =+ 1
                        dialogue36()
                    if PAUSE.checkForInput(MENU_MOUSE_POS):
                        pausemenu()

            pygame.display.flip()


def chap1_opening():
    timer = pygame.time.Clock()

    run = True
    while run:

        timer.tick(60)

        bg = pygame.image.load('assets/cafeteriabgblur.jpg')
        scaled_bg = pygame.transform.scale(bg, (1280,720))
        bg_rect = scaled_bg.get_rect(x=0,y=0)
        SCREEN.blit(scaled_bg, bg_rect)

        box = pygame.image.load('assets/Play Rect.png')
        scaled_box = pygame.transform.scale(box, (640,240))
        box_rect = scaled_box.get_rect(x=320,y=250)
        SCREEN.blit(scaled_box, box_rect)

        end = prologuefont(40).render("Chapter 1 - Act 1", True, "White")
        end_rect = end.get_rect(x=340, y=265)
        SCREEN.blit(end,end_rect)

        troll = prologuefont(22).render("Life outta prison is great, isn\'t it?", True, "White")
        troll_rect = troll.get_rect(x=343, y=320)
        SCREEN.blit(troll,troll_rect)

        info = textbutton_font(19).render("New Klang Private Penitentiary - Cafeteria - 11:37:14 PM", True, "White")
        info_rect = end.get_rect(x=343, y=450)
        SCREEN.blit(info,info_rect)
        pygame.draw.rect(SCREEN, 'white', (343, 360, 590, 75))

        text1 = prologuefont(13).render("In the earlier part of the story... The story revolves around MC, who was stuck in", True, "black")
        text1_rect = text1.get_rect(x=350, y=370)
        SCREEN.blit(text1,text1_rect)

        text2 = prologuefont(13).render("the prison, for crimes he didn\'t commit, but oh well, it is what it is... After nearly", True, "black")
        text2_rect = text2.get_rect(x=350, y=390)
        SCREEN.blit(text2,text2_rect)

        text2 = prologuefont(13).render("10 years in prison, his cellmate, NPC, invites him in devising a plan to escape.", True, "black")
        text2_rect = text2.get_rect(x=350, y=410)
        SCREEN.blit(text2,text2_rect)

        info = textbutton_font(24).render("(click Enter to continue...)", True, "White")
        info_rect = end.get_rect(x=500, y=600)
        SCREEN.blit(info,info_rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    chap1_steps()
                    
        pygame.display.flip()

def chap1_steps():
    font = pygame.font.Font('assets/ARCADE.TTF', 24)
    screen = pygame.display.set_mode ([1280, 720])
    timer = pygame.time.Clock()
    messages = ('*thud* *thud*',
                'Footsteps can be heard going into the cafeteria...',
                '...')
    snip = font.render('', True, 'black')
    counter = 0
    speed = 1
    active_message = 0
    message = messages[active_message]

    run = True
    while run:

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        PAUSE = Button(image=pygame.image.load("assets/pause.png"), pos=(50, 50), 
                            text_input="           ", font=textbutton_font(21), base_color="black", hovering_color="#FF3131")

        bg = pygame.image.load('assets/cafeteriabg.jpg')
        scaled_bg = pygame.transform.scale(bg, (1280,720))
        bg_rect = scaled_bg.get_rect(x=0,y=0)
        
        textbox = pygame.image.load('assets/textbox.png')
        scaled_texbox = pygame.transform.scale(textbox, (850,200))
        textbox_rect = scaled_texbox.get_rect(x=220,y=500)

        screen.blit(scaled_bg, bg_rect)
        PAUSE.update(SCREEN)
        PAUSE.changeColor(MENU_MOUSE_POS)
        mc(475,1)
        screen.blit(scaled_texbox, textbox_rect)

        timer.tick(60)

        if counter < speed * len(message):
            counter += 1

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PAUSE.checkForInput(MENU_MOUSE_POS):
                    pausemenu()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if counter >= speed * len(message) and active_message < len(messages) - 1:
                        active_message += 1
                        message = messages[active_message]
                        counter = 0
                    else:
                        counter = speed * len(message)
                if active_message == 2:
                    chap1()

        snip = font.render(message[0:counter//speed], True, 'white')
        screen.blit(snip, (280, 570))

        pygame.display.flip()

def chap1():
    font = pygame.font.Font('assets/ARCADE.TTF', 24)
    screen = pygame.display.set_mode ([1280, 720])
    timer = pygame.time.Clock()
    messages = ('MC : My belly really hurting right now...',
                'MC : If NPC didn\'t delay my meal, my mood wouldn\'t get that bad...',
                '...')
    snip = font.render('', True, 'black')
    counter = 0
    speed = 1
    active_message = 0
    message = messages[active_message]

    run = True
    while run:

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        PAUSE = Button(image=pygame.image.load("assets/pause.png"), pos=(50, 50), 
                            text_input="           ", font=textbutton_font(21), base_color="black", hovering_color="#FF3131")

        bg = pygame.image.load('assets/cafeteriabg.jpg')
        scaled_bg = pygame.transform.scale(bg, (1280,720))
        bg_rect = scaled_bg.get_rect(x=0,y=0)
        
        textbox = pygame.image.load('assets/textbox.png')
        scaled_texbox = pygame.transform.scale(textbox, (850,200))
        textbox_rect = scaled_texbox.get_rect(x=220,y=500)

        screen.blit(scaled_bg, bg_rect)
        PAUSE.update(SCREEN)
        PAUSE.changeColor(MENU_MOUSE_POS)
        mc(475,1)
        screen.blit(scaled_texbox, textbox_rect)

        timer.tick(60)

        if counter < speed * len(message):
            counter += 1

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PAUSE.checkForInput(MENU_MOUSE_POS):
                    pausemenu()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if counter >= speed * len(message) and active_message < len(messages) - 1:
                        active_message += 1
                        message = messages[active_message]
                        counter = 0
                    else:
                        counter = speed * len(message)
                if active_message == 2:
                    dialogue2()

        snip = font.render(message[0:counter//speed], True, 'white')
        screen.blit(snip, (280, 570))

        pygame.display.flip()
        bgmusic.play()

def dialogue2():
    font = pygame.font.Font('assets/ARCADE.TTF', 24)
    screen = pygame.display.set_mode ([1280, 720])
    timer = pygame.time.Clock()
    messages = ('MC : But, atleast I\'m in the cafeteria.',
                'MC : Time to get my meal!',
                '...')
    snip = font.render('', True, 'black')
    counter = 0
    speed = 1
    active_message = 0
    message = messages[active_message]

    run = True
    while run:

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        PAUSE = Button(image=pygame.image.load("assets/pause.png"), pos=(50, 50), 
                            text_input="           ", font=textbutton_font(21), base_color="black", hovering_color="#FF3131")

        bg = pygame.image.load('assets/cafeteria.jpg')
        scaled_bg = pygame.transform.scale(bg, (1280,720))
        bg_rect = scaled_bg.get_rect(x=0,y=0)
        
        textbox = pygame.image.load('assets/textbox.png')
        scaled_texbox = pygame.transform.scale(textbox, (850,200))
        textbox_rect = scaled_texbox.get_rect(x=220,y=500)

        screen.blit(scaled_bg, bg_rect)
        PAUSE.update(SCREEN)
        PAUSE.changeColor(MENU_MOUSE_POS)
        screen.blit(scaled_texbox, textbox_rect)


        timer.tick(60)

        if counter < speed * len(message):
            counter += 1

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PAUSE.checkForInput(MENU_MOUSE_POS):
                    pausemenu()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if counter >= speed * len(message) and active_message < len(messages) - 1:
                        active_message += 1
                        message = messages[active_message]
                        counter = 0
                    else:
                        counter = speed * len(message)
                if active_message == 2:
                    dialogue3()

        snip = font.render(message[0:counter//speed], True, 'white')
        screen.blit(snip, (280, 570))

        pygame.display.flip()

def dialogue3():
    font = pygame.font.Font('assets/ARCADE.TTF', 24)
    screen = pygame.display.set_mode ([1280, 720])
    timer = pygame.time.Clock()
    messages = ('MC takes a food tray and hands the plate to the server.',
                'The splatting sound coming from the soggy meal can be heard.',
                'MC : ...',
                'MC : Well, well, well... a new menu today huh?',
                '...')
    snip = font.render('', True, 'white')
    counter = 0
    speed = 1
    active_message = 0
    message = messages[active_message]

    run = True
    while run:

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        PAUSE = Button(image=pygame.image.load("assets/pause.png"), pos=(50, 50), 
                            text_input="           ", font=textbutton_font(21), base_color="black", hovering_color="#FF3131")

        bg = pygame.image.load('assets/prisonfood.jpg')
        scaled_bg = pygame.transform.scale(bg, (1280,720))
        bg_rect = scaled_bg.get_rect(x=0,y=0)
        
        textbox = pygame.image.load('assets/textbox.png')
        scaled_texbox = pygame.transform.scale(textbox, (850,200))
        textbox_rect = scaled_texbox.get_rect(x=220,y=500)

        screen.blit(scaled_bg, bg_rect)
        PAUSE.update(SCREEN)
        PAUSE.changeColor(MENU_MOUSE_POS)
        screen.blit(scaled_texbox, textbox_rect)

        timer.tick(60)

        if counter < speed * len(message):
            counter += 1

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PAUSE.checkForInput(MENU_MOUSE_POS):
                    pausemenu()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if counter >= speed * len(message) and active_message < len(messages) - 1:
                        active_message += 1
                        message = messages[active_message]
                        counter = 0
                    else:
                        counter = speed * len(message)
                if active_message == 4:
                    dialogue4()

        snip = font.render(message[0:counter//speed], True, 'white')
        screen.blit(snip, (280, 570))

        pygame.display.flip()

def dialogue4():
    font = pygame.font.Font('assets/ARCADE.TTF', 24)
    screen = pygame.display.set_mode ([1280, 720])
    timer = pygame.time.Clock()
    messages = ('MC : Even if it looks like somebody\'s shit...',
                'MC : ...I\'m just gonna ignore it.',
                'MC : Lowkey looks good though.',
                'MC : Yo, NPC! Come on here!',
                '...')
    snip = font.render('', True, 'white')
    counter = 0
    speed = 1
    active_message = 0
    message = messages[active_message]

    run = True
    while run:

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        PAUSE = Button(image=pygame.image.load("assets/pause.png"), pos=(50, 50), 
                            text_input="           ", font=textbutton_font(21), base_color="black", hovering_color="#FF3131")

        bg = pygame.image.load('assets/cafeteriabg.jpg')
        scaled_bg = pygame.transform.scale(bg, (1280,720))
        bg_rect = scaled_bg.get_rect(x=0,y=0)
        
        textbox = pygame.image.load('assets/textbox.png')
        scaled_texbox = pygame.transform.scale(textbox, (850,200))
        textbox_rect = scaled_texbox.get_rect(x=220,y=500)

        screen.blit(scaled_bg, bg_rect)
        PAUSE.update(SCREEN)
        PAUSE.changeColor(MENU_MOUSE_POS)
        mc(475,1)
        screen.blit(scaled_texbox, textbox_rect)

        timer.tick(60)
        if counter < speed * len(message):
            counter += 1

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PAUSE.checkForInput(MENU_MOUSE_POS):
                    pausemenu()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if counter >= speed * len(message) and active_message < len(messages) - 1:
                        active_message += 1
                        message = messages[active_message]
                        counter = 0
                    else:
                        counter = speed * len(message)
                if active_message == 4:
                    dialogue5()

        snip = font.render(message[0:counter//speed], True, 'white')
        screen.blit(snip, (280, 570))

        pygame.display.flip()
        sadbgm.stop()
        bgmusic.play()

def dialogue5():
    font = pygame.font.Font('assets/ARCADE.TTF', 24)
    screen = pygame.display.set_mode ([1280, 720])
    timer = pygame.time.Clock()
    messages = ('NPC : This is why I\'d rather sleep than eat...',
                'NPC : What\'s with this gooey monstrosity...?',
                'NPC pokes the smelly mac \'n cheese...' ,
                'Bubbles of gas fizzing out from the food.',
                'NPC and MC : ...',
                'NPC : I\'m not sure if I should eat this...',
                'MC : If you\'re not eating it, then lemme.',
                'MC pulls NPC\'s tray and immediately gobbles them up.',
                'NPC looks with disbelief.',
                'MC : You sure you don\'t want?',
                'NPC : Nah man...',
                'MC : Come on! Give it some taste!',
                'NPC : Get that shit from me bro!',
                'MC : Just a lil\' bit!' ,
                'NPC : NO!',
                '...')
    snip = font.render('', True, 'white')
    counter = 0
    speed = 1
    active_message = 0
    message = messages[active_message]

    run = True
    while run:

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        PAUSE = Button(image=pygame.image.load("assets/pause.png"), pos=(50, 50), 
                            text_input="           ", font=textbutton_font(21), base_color="black", hovering_color="#FF3131")

        bg = pygame.image.load('assets/cafeteriabg.jpg')
        scaled_bg = pygame.transform.scale(bg, (1280,720))
        bg_rect = scaled_bg.get_rect(x=0,y=0)
        
        textbox = pygame.image.load('assets/textbox.png')
        scaled_texbox = pygame.transform.scale(textbox, (850,200))
        textbox_rect = scaled_texbox.get_rect(x=220,y=500)

        screen.blit(scaled_bg, bg_rect)
        PAUSE.update(SCREEN)
        PAUSE.changeColor(MENU_MOUSE_POS)
        mc(270,1)
        walter(670,130)
        screen.blit(scaled_texbox, textbox_rect)

        timer.tick(60)
        if counter < speed * len(message):
            counter += 1

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PAUSE.checkForInput(MENU_MOUSE_POS):
                    pausemenu()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if counter >= speed * len(message) and active_message < len(messages) - 1:
                        active_message += 1
                        message = messages[active_message]
                        counter = 0
                    else:
                        counter = speed * len(message)
                if active_message == 15:
                    dialogue6()

        snip = font.render(message[0:counter//speed], True, 'white')
        screen.blit(snip, (280, 570))

        pygame.display.flip()

def dialogue6():
    font = pygame.font.Font('assets/ARCADE.TTF', 24)
    screen = pygame.display.set_mode ([1280, 720])
    timer = pygame.time.Clock()
    messages = ('As they\'re busy quarrelling...',
                'A figure watches them from the far row of the table.',
                'Mysterious Man : ...',
                'MC : ...uhh, why I suddenly got the shivers?',
                'NPC : Guess the effects had kicked in eh?',
                'MC : Bruh, the food ain\'t that bad dude.',
                'MC : But... just to make sure, I\'m throwing it away.',
                'NPC : Told ya.',
                'NPC : Hurry up, the roll call\'s about to begin.',
                'MC : Relax... They treat me like I\'m the son of the wardens.',
                'NPC : *whisper* ...more like son of the b*tches.',
                'MC : The f*ck did you say...?',
                'NPC : Nothing.',
                'NPC : Now stop yappin\' and move your *ss.',
                'MC : Alright alright let\'s move on...',
                '...')
    snip = font.render('', True, 'white')
    counter = 0
    speed = 1
    active_message = 0
    message = messages[active_message]

    run = True
    while run:

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        PAUSE = Button(image=pygame.image.load("assets/pause.png"), pos=(50, 50), 
                            text_input="           ", font=textbutton_font(21), base_color="black", hovering_color="#FF3131")

        bg = pygame.image.load('assets/cafeteriabg.jpg')
        scaled_bg = pygame.transform.scale(bg, (1280,720))
        bg_rect = scaled_bg.get_rect(x=0,y=0)
        
        textbox = pygame.image.load('assets/textbox.png')
        scaled_texbox = pygame.transform.scale(textbox, (850,200))
        textbox_rect = scaled_texbox.get_rect(x=220,y=500)

        screen.blit(scaled_bg, bg_rect)
        PAUSE.update(SCREEN)
        PAUSE.changeColor(MENU_MOUSE_POS)
        mc(200,1)
        walter(350,115)
        silhoutte(400,200)
        screen.blit(scaled_texbox, textbox_rect)

        timer.tick(60)
        if counter < speed * len(message):
            counter += 1

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PAUSE.checkForInput(MENU_MOUSE_POS):
                    pausemenu()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if counter >= speed * len(message) and active_message < len(messages) - 1:
                        active_message += 1
                        message = messages[active_message]
                        counter = 0
                    else:
                        counter = speed * len(message)
                if active_message == 15:
                    dialogue7()

        snip = font.render(message[0:counter//speed], True, 'white')
        screen.blit(snip, (280, 570))

        pygame.display.flip()

def dialogue7():
    font = pygame.font.Font('assets/ARCADE.TTF', 24)
    screen = pygame.display.set_mode ([1280, 720])
    timer = pygame.time.Clock()
    messages = ('Mysterious Man : ...',
                'Mysterious Man : I\'ll make sure I\'ll kill you, in this dreaded place, MC...',
                'Mysterious Man : And my vengeance will be paid off...',
                'Mysterious Man : I\'ll live a peaceful life after that!',
                'Mysterious Man : MWAHAHAHAHAHA!!!',
                '*SMACK*',
                'Mysterious Man : ???????',
                'Mysterious Man : Who dares defies me!?',
                '...')
    snip = font.render('', True, 'white')
    counter = 0
    speed = 1
    active_message = 0
    message = messages[active_message]

    run = True
    while run:

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        PAUSE = Button(image=pygame.image.load("assets/pause.png"), pos=(50, 50), 
                            text_input="           ", font=textbutton_font(21), base_color="black", hovering_color="#FF3131")

        bg = pygame.image.load('assets/cafeteriabg.jpg')
        scaled_bg = pygame.transform.scale(bg, (1280,720))
        bg_rect = scaled_bg.get_rect(x=0,y=0)
        
        textbox = pygame.image.load('assets/textbox.png')
        scaled_texbox = pygame.transform.scale(textbox, (850,200))
        textbox_rect = scaled_texbox.get_rect(x=220,y=500)

        screen.blit(scaled_bg, bg_rect)
        PAUSE.update(SCREEN)
        PAUSE.changeColor(MENU_MOUSE_POS)
        silhoutte(150,200)
        screen.blit(scaled_texbox, textbox_rect)

        timer.tick(60)
        if counter < speed * len(message):
            counter += 1

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PAUSE.checkForInput(MENU_MOUSE_POS):
                    pausemenu()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if counter >= speed * len(message) and active_message < len(messages) - 1:
                        active_message += 1
                        message = messages[active_message]
                        counter = 0
                    else:
                        counter = speed * len(message)
                if active_message == 8:
                    dialogue8()

        snip = font.render(message[0:counter//speed], True, 'white')
        screen.blit(snip, (280, 570))

        pygame.display.flip()

def dialogue8():
    font = pygame.font.Font('assets/ARCADE.TTF', 24)
    screen = pygame.display.set_mode ([1280, 720])
    timer = pygame.time.Clock()
    messages = ('Warden : ...',
                'Mysterious Man : uhh... *gulps*',
                'Warden : Why not get going to the roll call, than be a total maniac?',
                'Warden : Laughing maniacally out of nowhere, are you finally losing it?',
                'Mysterious Man : ...',   
                'Warden : WHAT ARE YOU STARING AT FOR, MOVE YOUR BIG *SS UP!',
                'Mysterious Man : Y-YES SIR!',
                'Mysterious Man : Tch... You\'re gonna pay for this, MC...',
                'Mysterious Man : For being the cause of degradation of my dignity...',
                'Mysterious Man : I\'LL NOT FORGIVE YOU- I mean...',
                'Mysterious Man : *whispers* i\'ll not forgive you, MC...',
                '...')
    snip = font.render('', True, 'white')
    counter = 0
    speed = 1
    active_message = 0
    message = messages[active_message]

    run = True
    while run:

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        PAUSE = Button(image=pygame.image.load("assets/pause.png"), pos=(50, 50), 
                            text_input="           ", font=textbutton_font(21), base_color="black", hovering_color="#FF3131")

        bg = pygame.image.load('assets/cafeteriabg.jpg')
        scaled_bg = pygame.transform.scale(bg, (1280,720))
        bg_rect = scaled_bg.get_rect(x=0,y=0)
        
        textbox = pygame.image.load('assets/textbox.png')
        scaled_texbox = pygame.transform.scale(textbox, (850,200))
        textbox_rect = scaled_texbox.get_rect(x=220,y=500)

        screen.blit(scaled_bg, bg_rect)
        PAUSE.update(SCREEN)
        PAUSE.changeColor(MENU_MOUSE_POS)
        silhoutte(-80,200)
        warden(640,170)
        screen.blit(scaled_texbox, textbox_rect)

        timer.tick(60)
        if counter < speed * len(message):
            counter += 1

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PAUSE.checkForInput(MENU_MOUSE_POS):
                    pausemenu()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if counter >= speed * len(message) and active_message < len(messages) - 1:
                        active_message += 1
                        message = messages[active_message]
                        counter = 0
                    else:
                        counter = speed * len(message)
                if active_message == 11:
                    dialogue9()

        snip = font.render(message[0:counter//speed], True, 'white')
        screen.blit(snip, (280, 570))

        pygame.display.flip()

def dialogue9():
    font = pygame.font.Font('assets/ARCADE.TTF', 24)
    screen = pygame.display.set_mode ([1280, 720])
    timer = pygame.time.Clock()
    messages = ('MC : Achoo! Goddamit...',
                'MC : Getting shivers and cold at the same time...?',
                'NPC : You okay bro?',
                'MC : Hmm? Ohh...',
                'MC : O noble Prince NPC, I beseech thee to alleviate my burden...',
                'MC : And rescue me from the depths of despair...',
                'NPC : What a f*ckin annoying piece of sh*t...',
                '...')
    snip = font.render('', True, 'white')
    counter = 0
    speed = 1
    active_message = 0
    message = messages[active_message]

    run = True
    while run:

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        PAUSE = Button(image=pygame.image.load("assets/pause.png"), pos=(50, 50), 
                            text_input="           ", font=textbutton_font(21), base_color="black", hovering_color="#FF3131")

        bg = pygame.image.load('assets/prisonhallway.png')
        scaled_bg = pygame.transform.scale(bg, (1280,720))
        bg_rect = scaled_bg.get_rect(x=0,y=0)
        
        textbox = pygame.image.load('assets/textbox.png')
        scaled_texbox = pygame.transform.scale(textbox, (850,200))
        textbox_rect = scaled_texbox.get_rect(x=220,y=500)

        screen.blit(scaled_bg, bg_rect)
        PAUSE.update(SCREEN)
        PAUSE.changeColor(MENU_MOUSE_POS)
        mc(270,1)
        walter(670,130)
        screen.blit(scaled_texbox, textbox_rect)

        timer.tick(60)
        if counter < speed * len(message):
            counter += 1

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PAUSE.checkForInput(MENU_MOUSE_POS):
                    pausemenu()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if counter >= speed * len(message) and active_message < len(messages) - 1:
                        active_message += 1
                        message = messages[active_message]
                        counter = 0
                    else:
                        counter = speed * len(message)
                if active_message == 7:
                    chap1v2_opening()

        snip = font.render(message[0:counter//speed], True, 'white')
        screen.blit(snip, (280, 570))

        pygame.display.flip()

def chap1v2_opening():
    timer = pygame.time.Clock()

    run = True
    while run:

        timer.tick(60)

        bg = pygame.image.load('assets/prisongymblur.jpg')
        scaled_bg = pygame.transform.scale(bg, (1280,720))
        bg_rect = scaled_bg.get_rect(x=0,y=0)
        SCREEN.blit(scaled_bg, bg_rect)

        box = pygame.image.load('assets/Play Rect.png')
        scaled_box = pygame.transform.scale(box, (640,240))
        box_rect = scaled_box.get_rect(x=320,y=250)
        SCREEN.blit(scaled_box, box_rect)

        end = prologuefont(40).render("Chapter 1 - Act 2", True, "White")
        end_rect = end.get_rect(x=340, y=320)
        SCREEN.blit(end,end_rect)

        troll = prologuefont(22).render("Time to bulk up guys...", True, "White")
        troll_rect = troll.get_rect(x=343, y=370)
        SCREEN.blit(troll,troll_rect)

        info = textbutton_font(19).render("New Klang Private Penitentiary - Activity Area - 12:30:41 PM", True, "White")
        info_rect = end.get_rect(x=343, y=450)
        SCREEN.blit(info,info_rect)

        info = textbutton_font(24).render("(click Enter to continue...)", True, "White")
        info_rect = end.get_rect(x=500, y=600)
        SCREEN.blit(info,info_rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    dialogue10()

        pygame.display.flip()

def dialogue10():
    font = pygame.font.Font('assets/ARCADE.TTF', 24)
    screen = pygame.display.set_mode ([1280, 720])
    timer = pygame.time.Clock()
    messages = ('NPC : Ergh...',
                'NPC : I don\'t wanna do this...',
                'MC : Look, this is the reason you didn\'t pull a bitch, NPC.',
                'MC : Your body\'s so small-',
                'MC : ...even KFC\'s chicken is bigger compared to you',
                '...')
    snip = font.render('', True, 'white')
    counter = 0
    speed = 1
    active_message = 0
    message = messages[active_message]

    run = True
    while run:

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        PAUSE = Button(image=pygame.image.load("assets/pause.png"), pos=(50, 50), 
                            text_input="           ", font=textbutton_font(21), base_color="black", hovering_color="#FF3131")

        bg = pygame.image.load('assets/prisongym.jpeg')
        scaled_bg = pygame.transform.scale(bg, (1280,720))
        bg_rect = scaled_bg.get_rect(x=0,y=0)
        
        textbox = pygame.image.load('assets/textbox.png')
        scaled_texbox = pygame.transform.scale(textbox, (850,200))
        textbox_rect = scaled_texbox.get_rect(x=220,y=500)

        screen.blit(scaled_bg, bg_rect)
        PAUSE.update(SCREEN)
        PAUSE.changeColor(MENU_MOUSE_POS)
        mc(270,1)
        walter(670,130)
        screen.blit(scaled_texbox, textbox_rect)

        timer.tick(60)
        if counter < speed * len(message):
            counter += 1

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PAUSE.checkForInput(MENU_MOUSE_POS):
                    pausemenu()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if counter >= speed * len(message) and active_message < len(messages) - 1:
                        active_message += 1
                        message = messages[active_message]
                        counter = 0
                    else:
                        counter = speed * len(message)
                if active_message == 5:
                    dialogue11()
        snip = font.render(message[0:counter//speed], True, 'white')
        screen.blit(snip, (280, 570))

        pygame.display.flip()

def dialogue11():
    font = pygame.font.Font('assets/ARCADE.TTF', 24)
    screen = pygame.display.set_mode ([1280, 720])
    timer = pygame.time.Clock()
    messages = ('NPC : You want me...',
                'NPC : to pull these gorillas...?',
                'NPC : Nah man, my ding-a-long will get...',
                'NPC : (imagine yourself la haiya)',
                'NPC : ...if they got me.',
                'MC : Wow, I wish I could unhear that.',
                'MC : Hope our audience won\'t get traumatized by that.',
                '...')
    snip = font.render('', True, 'white')
    counter = 0
    speed = 1
    active_message = 0
    message = messages[active_message]

    run = True
    while run:

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        PAUSE = Button(image=pygame.image.load("assets/pause.png"), pos=(50, 50), 
                            text_input="           ", font=textbutton_font(21), base_color="black", hovering_color="#FF3131")

        bg = pygame.image.load('assets/womaninmates.jpg')
        scaled_bg = pygame.transform.scale(bg, (1280,720))
        bg_rect = scaled_bg.get_rect(x=0,y=0)
        
        textbox = pygame.image.load('assets/textbox.png')
        scaled_texbox = pygame.transform.scale(textbox, (850,200))
        textbox_rect = scaled_texbox.get_rect(x=220,y=500)

        screen.blit(scaled_bg, bg_rect)
        PAUSE.update(SCREEN)
        PAUSE.changeColor(MENU_MOUSE_POS)
        screen.blit(scaled_texbox, textbox_rect)

        timer.tick(60)
        if counter < speed * len(message):
            counter += 1

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PAUSE.checkForInput(MENU_MOUSE_POS):
                    pausemenu()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if counter >= speed * len(message) and active_message < len(messages) - 1:
                        active_message += 1
                        message = messages[active_message]
                        counter = 0
                    else:
                        counter = speed * len(message)
                if active_message == 7:
                    dialogue12()

        snip = font.render(message[0:counter//speed], True, 'white')
        screen.blit(snip, (280, 570))

        pygame.display.flip()
        introbgm.stop()
        bgmusic.play()

def dialogue12():
    font = pygame.font.Font('assets/ARCADE.TTF', 24)
    screen = pygame.display.set_mode ([1280, 720])
    timer = pygame.time.Clock()
    messages = ('MC : Nevermind then, not gonna wait for you.',
                'MC : Go sit there, with the fodders alright, NPC?',
                'NPC : Tch... yeah yeah whatever.',
                'MC : Good boy.',
                'NPC : ????????',
                'MC : Ya know, the gayest man is the straightest one.',
                'NPC : *loss at words*',
                'MC : (laughs) Alrighty, I\'ll start away',
                '...')
    snip = font.render('', True, 'white')
    counter = 0
    speed = 1
    active_message = 0
    message = messages[active_message]

    run = True
    while run:

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        PAUSE = Button(image=pygame.image.load("assets/pause.png"), pos=(50, 50), 
                            text_input="           ", font=textbutton_font(21), base_color="black", hovering_color="#FF3131")

        bg = pygame.image.load('assets/prisongym.jpeg')
        scaled_bg = pygame.transform.scale(bg, (1280,720))
        bg_rect = scaled_bg.get_rect(x=0,y=0)
        
        textbox = pygame.image.load('assets/textbox.png')
        scaled_texbox = pygame.transform.scale(textbox, (850,200))
        textbox_rect = scaled_texbox.get_rect(x=220,y=500)

        screen.blit(scaled_bg, bg_rect)
        PAUSE.update(SCREEN)
        PAUSE.changeColor(MENU_MOUSE_POS)
        mc(270,1)
        walter(670,130)
        screen.blit(scaled_texbox, textbox_rect)

        timer.tick(60)
        if counter < speed * len(message):
            counter += 1

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PAUSE.checkForInput(MENU_MOUSE_POS):
                    pausemenu()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if counter >= speed * len(message) and active_message < len(messages) - 1:
                        active_message += 1
                        message = messages[active_message]
                        counter = 0
                    else:
                        counter = speed * len(message)
                if active_message == 7:
                    dialogue13()

        snip = font.render(message[0:counter//speed], True, 'white')
        screen.blit(snip, (280, 570))

        pygame.display.flip()

def dialogue13():
    font = pygame.font.Font('assets/ARCADE.TTF', 24)
    screen = pygame.display.set_mode ([1280, 720])
    timer = pygame.time.Clock()
    messages = ('Mysterious Man : This is my chance.',
                'Mysterious Man : I\'ll rig one of the gym equipment...',
                'Mysterious Man : ...and he\'ll die because of accident!',
                'Mysterious Man : MWAHAHAHAHAHA!!!',
                'Mysterious Man : HUH??? *looks around*',
                'Mysterious Man got PTSD from the previous warden...',
                '...')
    snip = font.render('', True, 'white')
    counter = 0
    speed = 1
    active_message = 0
    message = messages[active_message]

    run = True
    while run:

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        PAUSE = Button(image=pygame.image.load("assets/pause.png"), pos=(50, 50), 
                            text_input="           ", font=textbutton_font(21), base_color="black", hovering_color="#FF3131")

        bg = pygame.image.load('assets/prisongym.jpeg')
        scaled_bg = pygame.transform.scale(bg, (1280,720))
        bg_rect = scaled_bg.get_rect(x=0,y=0)
        
        textbox = pygame.image.load('assets/textbox.png')
        scaled_texbox = pygame.transform.scale(textbox, (850,200))
        textbox_rect = scaled_texbox.get_rect(x=220,y=500)

        screen.blit(scaled_bg, bg_rect)
        PAUSE.update(SCREEN)
        PAUSE.changeColor(MENU_MOUSE_POS)
        silhoutte(150,200)
        screen.blit(scaled_texbox, textbox_rect)

        timer.tick(60)
        if counter < speed * len(message):
            counter += 1

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PAUSE.checkForInput(MENU_MOUSE_POS):
                    pausemenu()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if counter >= speed * len(message) and active_message < len(messages) - 1:
                        active_message += 1
                        message = messages[active_message]
                        counter = 0
                    else:
                        counter = speed * len(message)
                if active_message == 6:
                    dialogue14()

        snip = font.render(message[0:counter//speed], True, 'white')
        screen.blit(snip, (280, 570))

        pygame.display.flip()

def dialogue14():
    font = pygame.font.Font('assets/ARCADE.TTF', 24)
    screen = pygame.display.set_mode ([1280, 720])
    timer = pygame.time.Clock()
    messages = ('MC : Now, which one should I start first?',
                '...')
    snip = font.render('', True, 'white')
    counter = 0
    speed = 1
    active_message = 0
    message = messages[active_message]

    run = True
    while run:

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        PAUSE = Button(image=pygame.image.load("assets/pause.png"), pos=(50, 50), 
                            text_input="           ", font=textbutton_font(21), base_color="black", hovering_color="#FF3131")

        bg = pygame.image.load('assets/prisongym.jpeg')
        scaled_bg = pygame.transform.scale(bg, (1280,720))
        bg_rect = scaled_bg.get_rect(x=0,y=0)
        
        textbox = pygame.image.load('assets/textbox.png')
        scaled_texbox = pygame.transform.scale(textbox, (850,200))
        textbox_rect = scaled_texbox.get_rect(x=220,y=500)

        screen.blit(scaled_bg, bg_rect)
        PAUSE.update(SCREEN)
        PAUSE.changeColor(MENU_MOUSE_POS)
        mc(475,1)
        screen.blit(scaled_texbox, textbox_rect)

        timer.tick(60)
        if counter < speed * len(message):
            counter += 1

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PAUSE.checkForInput(MENU_MOUSE_POS):
                    pausemenu()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if counter >= speed * len(message) and active_message < len(messages) - 1:
                        active_message += 1
                        message = messages[active_message]
                        counter = 0
                    else:
                        counter = speed * len(message)
                if active_message == 1:
                    choice2()

        snip = font.render(message[0:counter//speed], True, 'white')
        screen.blit(snip, (280, 570))

        pygame.display.flip()

def dialogue15():
    font = pygame.font.Font('assets/ARCADE.TTF', 24)
    screen = pygame.display.set_mode ([1280, 720])
    timer = pygame.time.Clock()
    messages = ('MC : Gotta train my legs for now.',
                'MC : Never know when these legs gonna be in extreme situation.',
                'MC started to run on the treadmill...',
                '...')
    snip = font.render('', True, 'white')
    counter = 0
    speed = 2
    active_message = 0
    message = messages[active_message]

    run = True

    while run:

        timer = pygame.time.Clock()

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        PAUSE = Button(image=pygame.image.load("assets/pause.png"), pos=(50, 50), 
                            text_input="           ", font=textbutton_font(21), base_color="black", hovering_color="#FF3131")

        bg = pygame.image.load('assets/prisongym.jpeg')
        scaled_bg = pygame.transform.scale(bg, (1280,720))
        bg_rect = scaled_bg.get_rect(x=0,y=0)
        
        textbox = pygame.image.load('assets/textbox.png')
        scaled_texbox = pygame.transform.scale(textbox, (850,200))
        textbox_rect = scaled_texbox.get_rect(x=220,y=500)

        SCREEN.blit(scaled_bg, bg_rect)
        PAUSE.update(SCREEN)
        PAUSE.changeColor(MENU_MOUSE_POS)
        mc(475,1)
        SCREEN.blit(scaled_texbox, textbox_rect)

        timer.tick(60)
        if counter < speed * len(message):
            counter += 1

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PAUSE.checkForInput(MENU_MOUSE_POS):
                    pausemenu()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if counter >= speed * len(message) and active_message < len(messages) - 1:
                        active_message += 1
                        message = messages[active_message]
                        counter = 0
                    else:
                        counter = speed * len(message)
                if active_message == 2:
                    dialogue16()

        snip = font.render(message[0:counter//speed], True, 'white')
        screen.blit(snip, (280, 570))

        pygame.display.flip()

def dialogue15v2():
    font = pygame.font.Font('assets/ARCADE.TTF', 24)
    screen = pygame.display.set_mode ([1280, 720])
    timer = pygame.time.Clock()
    messages = ('MC : My back is quite sore right now.',
                'MC : But I guess, I can handle this much.',
                'MC : Who knows if I gotta be pulling something right?',
                'MC : ...except for pulling some bitches.',
                '...')
    snip = font.render('', True, 'white')
    counter = 0
    speed = 2
    active_message = 0
    message = messages[active_message]

    run = True

    while run:

        timer = pygame.time.Clock()

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        PAUSE = Button(image=pygame.image.load("assets/pause.png"), pos=(50, 50), 
                            text_input="           ", font=textbutton_font(21), base_color="black", hovering_color="#FF3131")

        bg = pygame.image.load('assets/prisongym.jpeg')
        scaled_bg = pygame.transform.scale(bg, (1280,720))
        bg_rect = scaled_bg.get_rect(x=0,y=0)
        
        textbox = pygame.image.load('assets/textbox.png')
        scaled_texbox = pygame.transform.scale(textbox, (850,200))
        textbox_rect = scaled_texbox.get_rect(x=220,y=500)

        SCREEN.blit(scaled_bg, bg_rect)
        PAUSE.update(SCREEN)
        PAUSE.changeColor(MENU_MOUSE_POS)
        mc(475,1)
        SCREEN.blit(scaled_texbox, textbox_rect)

        timer.tick(60)
        if counter < speed * len(message):
            counter += 1

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PAUSE.checkForInput(MENU_MOUSE_POS):
                    pausemenu()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if counter >= speed * len(message) and active_message < len(messages) - 1:
                        active_message += 1
                        message = messages[active_message]
                        counter = 0
                    else:
                        counter = speed * len(message)
                if active_message == 4:
                    dialogue16v2()

        snip = font.render(message[0:counter//speed], True, 'white')
        screen.blit(snip, (280, 570))

        pygame.display.flip()

def dialogue16v2():
    font = pygame.font.Font('assets/ARCADE.TTF', 24)
    screen = pygame.display.set_mode ([1280, 720])
    timer = pygame.time.Clock()
    messages = ('MC started doing the pulldown...',
                'He can feel the muscle straining and expanding as he pulls down the bar!',
                'Strength attribute obtained!',
                '...')
    snip = font.render('', True, 'white')
    counter = 0
    speed = 2
    active_message = 0
    message = messages[active_message]

    run = True

    while run:

        timer = pygame.time.Clock()

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        PAUSE = Button(image=pygame.image.load("assets/pause.png"), pos=(50, 50), 
                            text_input="           ", font=textbutton_font(21), base_color="black", hovering_color="#FF3131")

        bg = pygame.image.load('assets/mcpullup.jpg')
        scaled_bg = pygame.transform.scale(bg, (1280,720))
        bg_rect = scaled_bg.get_rect(x=0,y=0)
        
        textbox = pygame.image.load('assets/textbox.png')
        scaled_texbox = pygame.transform.scale(textbox, (850,200))
        textbox_rect = scaled_texbox.get_rect(x=220,y=500)

        SCREEN.blit(scaled_bg, bg_rect)
        PAUSE.update(SCREEN)
        PAUSE.changeColor(MENU_MOUSE_POS)
        SCREEN.blit(scaled_texbox, textbox_rect)

        timer.tick(60)
        if counter < speed * len(message):
            counter += 1

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PAUSE.checkForInput(MENU_MOUSE_POS):
                    pausemenu()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if counter >= speed * len(message) and active_message < len(messages) - 1:
                        active_message += 1
                        message = messages[active_message]
                        counter = 0
                    else:
                        counter = speed * len(message)
                if active_message == 3:
                    dialogue17()

        snip = font.render(message[0:counter//speed], True, 'white')
        screen.blit(snip, (280, 570))

        pygame.display.flip()

def dialogue16():
    font = pygame.font.Font('assets/ARCADE.TTF', 24)
    screen = pygame.display.set_mode ([1280, 720])
    timer = pygame.time.Clock()
    messages = ('MC started to run on the treadmill...',
                'He can feel a surge of adrenaline flowing constantly inside of him!',
                'Speed attribute obtained!',
                '...')
    snip = font.render('', True, 'white')
    counter = 0
    speed = 2
    active_message = 0
    message = messages[active_message]

    run = True

    while run:

        timer = pygame.time.Clock()

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        PAUSE = Button(image=pygame.image.load("assets/pause.png"), pos=(50, 50), 
                            text_input="           ", font=textbutton_font(21), base_color="black", hovering_color="#FF3131")

        bg = pygame.image.load('assets/mctreadmill.jpg')
        scaled_bg = pygame.transform.scale(bg, (1280,720))
        bg_rect = scaled_bg.get_rect(x=0,y=0)
        
        textbox = pygame.image.load('assets/textbox.png')
        scaled_texbox = pygame.transform.scale(textbox, (850,200))
        textbox_rect = scaled_texbox.get_rect(x=220,y=500)

        SCREEN.blit(scaled_bg, bg_rect)
        PAUSE.update(SCREEN)
        PAUSE.changeColor(MENU_MOUSE_POS)
        SCREEN.blit(scaled_texbox, textbox_rect)

        timer.tick(60)
        if counter < speed * len(message):
            counter += 1

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PAUSE.checkForInput(MENU_MOUSE_POS):
                    pausemenu()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if counter >= speed * len(message) and active_message < len(messages) - 1:
                        active_message += 1
                        message = messages[active_message]
                        counter = 0
                    else:
                        counter = speed * len(message)
                if active_message == 3:
                    dialogue17()

        snip = font.render(message[0:counter//speed], True, 'white')
        screen.blit(snip, (280, 570))

        pygame.display.flip()

def dialogue17():
    font = pygame.font.Font('assets/ARCADE.TTF', 24)
    screen = pygame.display.set_mode ([1280, 720])
    timer = pygame.time.Clock()
    messages = ('Mysterious Man : Tch! Why must he be doing all of that-',
                'Mysterious Man : Except for deadlifting!?',
                'Mysterious Man : Know your place, kiddo...',
                'Mysterious Man : That brittle body of yours really annoys me!',
                'Mysterious Man : You should focusing on buffing up your tiny muscles!',
                'Mysterious Man : Dammit! *punches the dumbbell rack*',
                'Mysterious Man : Uhh... Oh no...',
                'The rack begins to broke apart...',
                '...and the dumbbells fall on top of his foot.',
                '*thud*',
                '...')
    snip = font.render('', True, 'white')
    counter = 0
    speed = 2
    active_message = 0
    message = messages[active_message]

    run = True

    while run:

        timer = pygame.time.Clock()

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        PAUSE = Button(image=pygame.image.load("assets/pause.png"), pos=(50, 50), 
                            text_input="           ", font=textbutton_font(21), base_color="black", hovering_color="#FF3131")

        bg = pygame.image.load('assets/prisongym.jpeg')
        scaled_bg = pygame.transform.scale(bg, (1280,720))
        bg_rect = scaled_bg.get_rect(x=0,y=0)
        
        textbox = pygame.image.load('assets/textbox.png')
        scaled_texbox = pygame.transform.scale(textbox, (850,200))
        textbox_rect = scaled_texbox.get_rect(x=220,y=500)

        SCREEN.blit(scaled_bg, bg_rect)
        PAUSE.update(SCREEN)
        PAUSE.changeColor(MENU_MOUSE_POS)
        silhoutte(150,200)
        SCREEN.blit(scaled_texbox, textbox_rect)

        timer.tick(60)
        if counter < speed * len(message):
            counter += 1

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PAUSE.checkForInput(MENU_MOUSE_POS):
                    pausemenu()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if counter >= speed * len(message) and active_message < len(messages) - 1:
                        active_message += 1
                        message = messages[active_message]
                        counter = 0
                    else:
                        counter = speed * len(message)
                if active_message == 10:
                    dialogue18()

        snip = font.render(message[0:counter//speed], True, 'white')
        screen.blit(snip, (280, 570))

        pygame.display.flip()

def dialogue18():
    font = pygame.font.Font('assets/ARCADE.TTF', 24)
    screen = pygame.display.set_mode ([1280, 720])
    timer = pygame.time.Clock()
    messages = ('Distant voice : AAAAAAAAAAGHHHH!!!',
                'MC : Huh, someone\'s losing their mind right now.',
                'MC : To be honest, everything feels weird suddenly.',
                'MC : Now to think of it, where\'s NPC?',
                'MC : Oh, there he is.',
                'MC : Yo NP- HUH???',
                '...')
    snip = font.render('', True, 'white')
    counter = 0
    speed = 2
    active_message = 0
    message = messages[active_message]

    run = True

    while run:

        timer = pygame.time.Clock()

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        PAUSE = Button(image=pygame.image.load("assets/pause.png"), pos=(50, 50), 
                            text_input="           ", font=textbutton_font(21), base_color="black", hovering_color="#FF3131")

        bg = pygame.image.load('assets/prisongym.jpeg')
        scaled_bg = pygame.transform.scale(bg, (1280,720))
        bg_rect = scaled_bg.get_rect(x=0,y=0)
        
        textbox = pygame.image.load('assets/textbox.png')
        scaled_texbox = pygame.transform.scale(textbox, (850,200))
        textbox_rect = scaled_texbox.get_rect(x=220,y=500)

        SCREEN.blit(scaled_bg, bg_rect)
        PAUSE.update(SCREEN)
        PAUSE.changeColor(MENU_MOUSE_POS)
        mc(475,1)
        SCREEN.blit(scaled_texbox, textbox_rect)

        timer.tick(60)
        if counter < speed * len(message):
            counter += 1

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PAUSE.checkForInput(MENU_MOUSE_POS):
                    pausemenu()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if counter >= speed * len(message) and active_message < len(messages) - 1:
                        active_message += 1
                        message = messages[active_message]
                        counter = 0
                    else:
                        counter = speed * len(message)
                if active_message == 6:
                    dialogue19()

        snip = font.render(message[0:counter//speed], True, 'white')
        screen.blit(snip, (280, 570))

        pygame.display.flip()

def dialogue19():
    font = pygame.font.Font('assets/ARCADE.TTF', 24)
    screen = pygame.display.set_mode ([1280, 720])
    timer = pygame.time.Clock()
    messages = ('MC : EVEN NPC HAS PULLED A BITCH???',
                'MC : This can\'t be real...',
                'MC : Nah nah this can\'t be happening...',
                'MC move towards NPC and pull his shoulder from behind.',
                'MC : DUDE?!',
                '...')
    snip = font.render('', True, 'white')
    counter = 0
    speed = 2
    active_message = 0
    message = messages[active_message]

    run = True

    while run:

        timer = pygame.time.Clock()

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        PAUSE = Button(image=pygame.image.load("assets/pause.png"), pos=(50, 50), 
                            text_input="           ", font=textbutton_font(21), base_color="black", hovering_color="#FF3131")

        bg = pygame.image.load('assets/walterngf.jpg')
        scaled_bg = pygame.transform.scale(bg, (1280,720))
        bg_rect = scaled_bg.get_rect(x=0,y=0)
        
        textbox = pygame.image.load('assets/textbox.png')
        scaled_texbox = pygame.transform.scale(textbox, (850,200))
        textbox_rect = scaled_texbox.get_rect(x=220,y=500)

        SCREEN.blit(scaled_bg, bg_rect)
        PAUSE.update(SCREEN)
        PAUSE.changeColor(MENU_MOUSE_POS)
        mc(270,1)
        SCREEN.blit(scaled_texbox, textbox_rect)

        timer.tick(60)
        if counter < speed * len(message):
            counter += 1

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PAUSE.checkForInput(MENU_MOUSE_POS):
                    pausemenu()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if counter >= speed * len(message) and active_message < len(messages) - 1:
                        active_message += 1
                        message = messages[active_message]
                        counter = 0
                    else:
                        counter = speed * len(message)
                if active_message == 5:
                    dialogue20()

        snip = font.render(message[0:counter//speed], True, 'white')
        screen.blit(snip, (280, 570))

        pygame.display.flip()

def dialogue20():
    font = pygame.font.Font('assets/ARCADE.TTF', 24)
    screen = pygame.display.set_mode ([1280, 720])
    timer = pygame.time.Clock()
    messages = ('NPC : What?',
                'MC : WHAT YOU MEAN \'What?\'???',
                'MC : I was busy doing some workout, and you casually...',
                'MC : PULLED A GIRLFRIEND OUT OF NOWHERE???',
                'MC : And???',
                'MC : AND IT CERTAINLY NOT AN EASY THING TO DO BRO.',
                'NPC : *smirks* Skill issue, bro!',
                'NPC\'s GF : Let\'s go babe... This crazy guy is scaring me...',
                'NPC : Oh, I\'m so sorry sweetie... Let\'s go somewhere else...',
                'MC : *CURSING VIOLENTLY*',
                '...')
    snip = font.render('', True, 'white')
    counter = 0
    speed = 2
    active_message = 0
    message = messages[active_message]

    run = True

    while run:

        timer = pygame.time.Clock()

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        PAUSE = Button(image=pygame.image.load("assets/pause.png"), pos=(50, 50), 
                            text_input="           ", font=textbutton_font(21), base_color="black", hovering_color="#FF3131")

        bg = pygame.image.load('assets/walterngf.jpg')
        scaled_bg = pygame.transform.scale(bg, (1280,720))
        bg_rect = scaled_bg.get_rect(x=0,y=0)
        
        textbox = pygame.image.load('assets/textbox.png')
        scaled_texbox = pygame.transform.scale(textbox, (850,200))
        textbox_rect = scaled_texbox.get_rect(x=220,y=500)

        SCREEN.blit(scaled_bg, bg_rect)
        PAUSE.update(SCREEN)
        PAUSE.changeColor(MENU_MOUSE_POS)
        mc(270,1)
        walter(670,130)
        SCREEN.blit(scaled_texbox, textbox_rect)

        timer.tick(60)
        if counter < speed * len(message):
            counter += 1

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PAUSE.checkForInput(MENU_MOUSE_POS):
                    pausemenu()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if counter >= speed * len(message) and active_message < len(messages) - 1:
                        active_message += 1
                        message = messages[active_message]
                        counter = 0
                    else:
                        counter = speed * len(message)
                if active_message == 8:
                    dialogue21()

        snip = font.render(message[0:counter//speed], True, 'white')
        screen.blit(snip, (280, 570))

        pygame.display.flip()

def dialogue21():
    font = pygame.font.Font('assets/ARCADE.TTF', 24)
    screen = pygame.display.set_mode ([1280, 720])
    timer = pygame.time.Clock()
    messages = ('Meanwhile, Mysterious Man timeout\'d himself at the corner of the gym...',
                'Mysterious Man : ...you audiences must think I\'m a fool, right?',
                'Mysterious Man : ...well, maybe you\'re right though.',
                'Mysterious Man : ...that kind of evil plot won\'t kill someone easily...',
                'Mysterious Man : ...I give up. You can live your life peacefully, MC.',
                'Mysterious Man : ...',
                'Mysterious Man : ...',
                'Mysterious Man suddenly stood up with full of spirits.',
                'Mysterious Man : NOT SO FAST THERE, MYSELF!',
                'Mysterious Man : I DIDN\'T WASTE MY TIME...',
                'Mysterious man : GETTING INTO PRISON INTENTIONALLY...',
                'Mysterious Man : ONLY FOR ME TO *bleep* UP HERE!',
                'Mysterious Man : Alrighty alright, let\'s devise a new plan shall we?',
                'Mysterious Man : I shall vanish for now...',
                'Mysterious Man : See you later, MC...',
                'Mysterious Man : ...mwahahaha... MWAHAHAHAHA!!!',
                '...')
    snip = font.render('', True, 'white')
    counter = 0
    speed = 2
    active_message = 0
    message = messages[active_message]

    run = True

    while run:

        timer = pygame.time.Clock()

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        PAUSE = Button(image=pygame.image.load("assets/pause.png"), pos=(50, 50), 
                            text_input="           ", font=textbutton_font(21), base_color="black", hovering_color="#FF3131")

        bg = pygame.image.load('assets/prisongym.jpeg')
        scaled_bg = pygame.transform.scale(bg, (1280,720))
        bg_rect = scaled_bg.get_rect(x=0,y=0)
        
        textbox = pygame.image.load('assets/textbox.png')
        scaled_texbox = pygame.transform.scale(textbox, (850,200))
        textbox_rect = scaled_texbox.get_rect(x=220,y=500)

        SCREEN.blit(scaled_bg, bg_rect)
        PAUSE.update(SCREEN)
        PAUSE.changeColor(MENU_MOUSE_POS)
        silhoutte(150,200)
        SCREEN.blit(scaled_texbox, textbox_rect)

        timer.tick(60)
        if counter < speed * len(message):
            counter += 1

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PAUSE.checkForInput(MENU_MOUSE_POS):
                    pausemenu()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if counter >= speed * len(message) and active_message < len(messages) - 1:
                        active_message += 1
                        message = messages[active_message]
                        counter = 0
                    else:
                        counter = speed * len(message)
                if active_message == 16:
                    chap1v3_opening()

        snip = font.render(message[0:counter//speed], True, 'white')
        screen.blit(snip, (280, 570))

        pygame.display.flip()

def chap1v3_opening():
    timer = pygame.time.Clock()

    run = True
    while run:

        timer.tick(60)

        bg = pygame.image.load('assets/prisoncellblur.jpg')
        scaled_bg = pygame.transform.scale(bg, (1280,720))
        bg_rect = scaled_bg.get_rect(x=0,y=0)
        SCREEN.blit(scaled_bg, bg_rect)

        box = pygame.image.load('assets/Play Rect.png')
        scaled_box = pygame.transform.scale(box, (640,240))
        box_rect = scaled_box.get_rect(x=320,y=250)
        SCREEN.blit(scaled_box, box_rect)

        end = prologuefont(40).render("Chapter 1 - Act 3", True, "White")
        end_rect = end.get_rect(x=340, y=320)
        SCREEN.blit(end,end_rect)

        troll = prologuefont(22).render("Something Big\'s happening?", True, "White")
        troll_rect = troll.get_rect(x=343, y=370)
        SCREEN.blit(troll,troll_rect)

        info = textbutton_font(19).render("New Klang Private Penitentiary - Activity Area - 4:43:09 PM", True, "White")
        info_rect = end.get_rect(x=343, y=450)
        SCREEN.blit(info,info_rect)

        info = textbutton_font(24).render("(click Enter to continue...)", True, "White")
        info_rect = end.get_rect(x=500, y=600)
        SCREEN.blit(info,info_rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    dialogue22()

        pygame.display.flip()

def dialogue22():
    font = pygame.font.Font('assets/ARCADE.TTF', 24)
    screen = pygame.display.set_mode ([1280, 720])
    timer = pygame.time.Clock()
    messages = ('MC : ...',
                'MC : I don\'t wanna live anymore...',
                'MC : Another 5 years to serve...',
                'MC : Before I start my own journey, to find a girlfriend...',
                'MC : I don\'t want to die a virgin man...',
                'MC : But, finding a girlfriend ain\'t an easy task though.',
                'MC : What if, it took me 10 more years until I find mine?',
                'MC : I\'ll be around 30 to 40 at that time...',
                'MC : ...',
                'MC : *tugging the cell bars* LET ME OUT, LET ME OUT PLEASE!',
                'MC : I DON\'T WANNA DATE AN OLD WOMAN WHEN I GOT OUT!',
                'MC : GOD, LET ME OUT!',
                'Unknown Voice : Whoa there buddy...',
                'Unknown Voice : You look terribly pathetic right now.',
                'Unknown Voice : Something I can help?',
                '...')
    snip = font.render('', True, 'white')
    counter = 0
    speed = 2
    active_message = 0
    message = messages[active_message]

    run = True

    while run:

        timer = pygame.time.Clock()

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        PAUSE = Button(image=pygame.image.load("assets/pause.png"), pos=(50, 50), 
                            text_input="           ", font=textbutton_font(21), base_color="black", hovering_color="#FF3131")

        bg = pygame.image.load('assets/prisoncell.jpg')
        scaled_bg = pygame.transform.scale(bg, (1280,720))
        bg_rect = scaled_bg.get_rect(x=0,y=0)
        
        textbox = pygame.image.load('assets/textbox.png')
        scaled_texbox = pygame.transform.scale(textbox, (850,200))
        textbox_rect = scaled_texbox.get_rect(x=220,y=500)

        SCREEN.blit(scaled_bg, bg_rect)
        PAUSE.update(SCREEN)
        PAUSE.changeColor(MENU_MOUSE_POS)
        mc(475,1)
        SCREEN.blit(scaled_texbox, textbox_rect)

        timer.tick(60)
        if counter < speed * len(message):
            counter += 1

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PAUSE.checkForInput(MENU_MOUSE_POS):
                    pausemenu()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if counter >= speed * len(message) and active_message < len(messages) - 1:
                        active_message += 1
                        message = messages[active_message]
                        counter = 0
                    else:
                        counter = speed * len(message)
                if active_message == 15:
                    dialogue23()

        snip = font.render(message[0:counter//speed], True, 'white')
        screen.blit(snip, (280, 570))

        pygame.display.flip()

def dialogue23():
    font = pygame.font.Font('assets/ARCADE.TTF', 24)
    screen = pygame.display.set_mode ([1280, 720])
    timer = pygame.time.Clock()
    messages = ('MC sees someone outside his cell.',
                'MC : Who\'re you?',
                'Unknown Person : I heard something about \'getting out\'?',
                'Unknown Person : It might be risky...',
                'Unknown Person : But I can help you with that.',
                'Unknown Person : You said something about \'girlfriend\' too?',
                'Unknown Person : Yeah yeah I can help you with that too.',
                'MC : Hold the *bleep* up, All-Knowing-Dude. One at a time.',
                'MC : And again, who the *bleep* are you?',
                'Unknown Person : What kind of girlfriend do you desire?',
                'Unknown Person : A cute one? A mommy one? A shy one?',
                'Unknown Person : Tall or short? Clingy or independent?',
                'Unknown Person : Flat is justice? Medium is premium? Oppai is truth?',
                'MC : CHILL UP DUDE. STOP WITH THE ONE-SIDED CONVERSATION!',
                'Unknown Person : Your name\'s MC right? Around 20? ',
                'MC : I\'m not gonna entertain you if you won\'t tell me your name first.',
                'Unknown Person : Sorry for the rapid exchange of communication.',
                'CJ : Just call me CJ.',
                'MC : CJ...?',
                'CJ : Let\'s talk business, shall we?',
                'CJ : Do you want to get out of this prison?',
                'MC : Yes?',
                'CJ : Alright, deal has been made. Good to be working with you!',
                'MC : WHO SAID THAT?!',
                'CJ : Meet me at tonight\'s dinner. Don\'t be late, alright? See ya.',
                '...')
    snip = font.render('', True, 'white')
    counter = 0
    speed = 2
    active_message = 0
    message = messages[active_message]

    run = True

    while run:

        timer = pygame.time.Clock()

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        PAUSE = Button(image=pygame.image.load("assets/pause.png"), pos=(50, 50), 
                            text_input="           ", font=textbutton_font(21), base_color="black", hovering_color="#FF3131")

        bg = pygame.image.load('assets/prisoncell.jpg')
        scaled_bg = pygame.transform.scale(bg, (1280,720))
        bg_rect = scaled_bg.get_rect(x=0,y=0)
        
        textbox = pygame.image.load('assets/textbox.png')
        scaled_texbox = pygame.transform.scale(textbox, (850,200))
        textbox_rect = scaled_texbox.get_rect(x=220,y=500)

        SCREEN.blit(scaled_bg, bg_rect)
        PAUSE.update(SCREEN)
        PAUSE.changeColor(MENU_MOUSE_POS)
        mc(270,1)
        villain(670,1)
        SCREEN.blit(scaled_texbox, textbox_rect)

        timer.tick(60)
        if counter < speed * len(message):
            counter += 1

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PAUSE.checkForInput(MENU_MOUSE_POS):
                    pausemenu()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if counter >= speed * len(message) and active_message < len(messages) - 1:
                        active_message += 1
                        message = messages[active_message]
                        counter = 0
                    else:
                        counter = speed * len(message)
                if active_message == 25:
                    dialogue24()

        snip = font.render(message[0:counter//speed], True, 'white')
        screen.blit(snip, (280, 570))

        pygame.display.flip()


def dialogue24():
    font = pygame.font.Font('assets/ARCADE.TTF', 24)
    screen = pygame.display.set_mode ([1280, 720])
    timer = pygame.time.Clock()
    messages = ('CJ immediately leaves the place, leaving MC dumbfounded...',
                'MC : W-wait! I\'m not done with you!',
                '...')
    snip = font.render('', True, 'white')
    counter = 0
    speed = 2
    active_message = 0
    message = messages[active_message]

    run = True

    while run:

        timer = pygame.time.Clock()

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        PAUSE = Button(image=pygame.image.load("assets/pause.png"), pos=(50, 50), 
                            text_input="           ", font=textbutton_font(21), base_color="black", hovering_color="#FF3131")

        bg = pygame.image.load('assets/prisoncell.jpg')
        scaled_bg = pygame.transform.scale(bg, (1280,720))
        bg_rect = scaled_bg.get_rect(x=0,y=0)
        
        textbox = pygame.image.load('assets/textbox.png')
        scaled_texbox = pygame.transform.scale(textbox, (850,200))
        textbox_rect = scaled_texbox.get_rect(x=220,y=500)

        SCREEN.blit(scaled_bg, bg_rect)
        PAUSE.update(SCREEN)
        PAUSE.changeColor(MENU_MOUSE_POS)
        mc(475,1)
        SCREEN.blit(scaled_texbox, textbox_rect)

        timer.tick(60)
        if counter < speed * len(message):
            counter += 1

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PAUSE.checkForInput(MENU_MOUSE_POS):
                    pausemenu()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if counter >= speed * len(message) and active_message < len(messages) - 1:
                        active_message += 1
                        message = messages[active_message]
                        counter = 0
                    else:
                        counter = speed * len(message)
                if active_message == 2:
                    dialogue25()

        snip = font.render(message[0:counter//speed], True, 'white')
        screen.blit(snip, (280, 570))

        pygame.display.flip()

def dialogue25():
    font = pygame.font.Font('assets/ARCADE.TTF', 24)
    screen = pygame.display.set_mode ([1280, 720])
    timer = pygame.time.Clock()
    messages = ('NPC : Done with what?',
                'MC : Ah- Nothing...',
                'NPC : Who\'s that guy earlier?',
                'MC : I... don\'t know...',
                'MC : I\'m going to bed for now...',
                'NPC : Uh, Alright.',
                'NPC : By the way, having a girlfriend sure changes thing a lot!',
                'MC : I don\'t care about your crap...',
                'MC : Let me clear my mind...',
                'NPC : Tch, being salty for no reason.',
                'MC went to bed to wait for tonight\'s dinner...',
                '...')
    snip = font.render('', True, 'white')
    counter = 0
    speed = 2
    active_message = 0
    message = messages[active_message]

    run = True

    while run:

        timer = pygame.time.Clock()

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        PAUSE = Button(image=pygame.image.load("assets/pause.png"), pos=(50, 50), 
                            text_input="           ", font=textbutton_font(21), base_color="black", hovering_color="#FF3131")

        bg = pygame.image.load('assets/prisoncell.jpg')
        scaled_bg = pygame.transform.scale(bg, (1280,720))
        bg_rect = scaled_bg.get_rect(x=0,y=0)
        
        textbox = pygame.image.load('assets/textbox.png')
        scaled_texbox = pygame.transform.scale(textbox, (850,200))
        textbox_rect = scaled_texbox.get_rect(x=220,y=500)

        SCREEN.blit(scaled_bg, bg_rect)
        PAUSE.update(SCREEN)
        PAUSE.changeColor(MENU_MOUSE_POS)
        mc(270,1)
        walter(670,130)
        SCREEN.blit(scaled_texbox, textbox_rect)

        timer.tick(60)
        if counter < speed * len(message):
            counter += 1

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PAUSE.checkForInput(MENU_MOUSE_POS):
                    pausemenu()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if counter >= speed * len(message) and active_message < len(messages) - 1:
                        active_message += 1
                        message = messages[active_message]
                        counter = 0
                    else:
                        counter = speed * len(message)
                if active_message == 11:
                    chap1v4_opening()

        snip = font.render(message[0:counter//speed], True, 'white')
        screen.blit(snip, (280, 570))

        pygame.display.flip()

def chap1v4_opening():
    timer = pygame.time.Clock()

    run = True
    while run:

        timer.tick(60)

        bg = pygame.image.load('assets/cafeteriabgblur.jpg')
        scaled_bg = pygame.transform.scale(bg, (1280,720))
        bg_rect = scaled_bg.get_rect(x=0,y=0)
        SCREEN.blit(scaled_bg, bg_rect)

        box = pygame.image.load('assets/Play Rect.png')
        scaled_box = pygame.transform.scale(box, (640,240))
        box_rect = scaled_box.get_rect(x=320,y=250)
        SCREEN.blit(scaled_box, box_rect)

        end = prologuefont(40).render("Chapter 1 - Act 4", True, "White")
        end_rect = end.get_rect(x=340, y=320)
        SCREEN.blit(end,end_rect)

        troll = prologuefont(22).render("Eternal Dawn Befalls", True, "White")
        troll_rect = troll.get_rect(x=343, y=370)
        SCREEN.blit(troll,troll_rect)

        info = textbutton_font(19).render("New Klang Private Penitentiary - Cafeteria - 9:17:37 PM", True, "White")
        info_rect = end.get_rect(x=343, y=450)
        SCREEN.blit(info,info_rect)

        info = textbutton_font(24).render("(click Enter to continue...)", True, "White")
        info_rect = end.get_rect(x=500, y=600)
        SCREEN.blit(info,info_rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    dialogue26()

        pygame.display.flip()

def dialogue26():
    font = pygame.font.Font('assets/ARCADE.TTF', 24)
    screen = pygame.display.set_mode ([1280, 720])
    timer = pygame.time.Clock()
    messages = ('MC : This is where I suppose to meet CJ...',
                'MC : Didn\'t see him anywhere.',
                'MC : Am I being trolled?',
                'MC : Let\'s just wait for a few minutes more...',
                'MC waits for 10 minutes more...',
                'MC : ...',
                'MC : ...',
                'MC : ...yeah. Definitely got trolled.',
                'MC : It\'s just too good to be true.',
                'MC : A plan to get out of this prison? Pfft, bullshit.',
                'MC : I\'m the idiot one for believing him.',
                'Suddenly, his shoulder are being patted on.',
                '...')
    snip = font.render('', True, 'white')
    counter = 0
    speed = 2
    active_message = 0
    message = messages[active_message]

    run = True

    while run:

        timer = pygame.time.Clock()

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        PAUSE = Button(image=pygame.image.load("assets/pause.png"), pos=(50, 50), 
                            text_input="           ", font=textbutton_font(21), base_color="black", hovering_color="#FF3131")

        bg = pygame.image.load('assets/cafeteriabg.jpg')
        scaled_bg = pygame.transform.scale(bg, (1280,720))
        bg_rect = scaled_bg.get_rect(x=0,y=0)
        
        textbox = pygame.image.load('assets/textbox.png')
        scaled_texbox = pygame.transform.scale(textbox, (850,200))
        textbox_rect = scaled_texbox.get_rect(x=220,y=500)

        SCREEN.blit(scaled_bg, bg_rect)
        PAUSE.update(SCREEN)
        PAUSE.changeColor(MENU_MOUSE_POS)
        mc(475,1)
        SCREEN.blit(scaled_texbox, textbox_rect)

        timer.tick(60)
        if counter < speed * len(message):
            counter += 1

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PAUSE.checkForInput(MENU_MOUSE_POS):
                    pausemenu()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if counter >= speed * len(message) and active_message < len(messages) - 1:
                        active_message += 1
                        message = messages[active_message]
                        counter = 0
                    else:
                        counter = speed * len(message)
                if active_message == 12:
                    dialogue27()

        snip = font.render(message[0:counter//speed], True, 'white')
        screen.blit(snip, (280, 570))

        pygame.display.flip()

def dialogue27():
    font = pygame.font.Font('assets/ARCADE.TTF', 24)
    screen = pygame.display.set_mode ([1280, 720])
    timer = pygame.time.Clock()
    messages = ('CJ : Yo, Sorry for the delay.',
                'MC : Finally, I nearly thought you were some scammer.',
                'CJ : *laughs* Itching to escape this prison, eh?',
                'CJ : What? You\'re eager to get a girlfriend? *laughs*',
                'MC : ...shut up.',
                'MC : If you got nothing good to say, I\'ll just leave.',
                'CJ : Whoa, chill dude! Have a sit first.',
                'MC : Ugh, fine...',
                'CJ : I\'ll get straight to the point. Don\'t wanna waste the time here.',
                '...')
    snip = font.render('', True, 'white')
    counter = 0
    speed = 2
    active_message = 0
    message = messages[active_message]

    run = True

    while run:

        timer = pygame.time.Clock()

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        PAUSE = Button(image=pygame.image.load("assets/pause.png"), pos=(50, 50), 
                            text_input="           ", font=textbutton_font(21), base_color="black", hovering_color="#FF3131")

        bg = pygame.image.load('assets/cafeteriabg.jpg')
        scaled_bg = pygame.transform.scale(bg, (1280,720))
        bg_rect = scaled_bg.get_rect(x=0,y=0)
        
        textbox = pygame.image.load('assets/textbox.png')
        scaled_texbox = pygame.transform.scale(textbox, (850,200))
        textbox_rect = scaled_texbox.get_rect(x=220,y=500)

        SCREEN.blit(scaled_bg, bg_rect)
        PAUSE.update(SCREEN)
        PAUSE.changeColor(MENU_MOUSE_POS)
        mc(270,1)
        villain(670,1)
        SCREEN.blit(scaled_texbox, textbox_rect)

        timer.tick(60)
        if counter < speed * len(message):
            counter += 1

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PAUSE.checkForInput(MENU_MOUSE_POS):
                    pausemenu()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if counter >= speed * len(message) and active_message < len(messages) - 1:
                        active_message += 1
                        message = messages[active_message]
                        counter = 0
                    else:
                        counter = speed * len(message)
                if active_message == 9:
                    dialogue28()

        snip = font.render(message[0:counter//speed], True, 'white')
        screen.blit(snip, (280, 570))

        pygame.display.flip()

def dialogue28():
    font = pygame.font.Font('assets/ARCADE.TTF', 24)
    screen = pygame.display.set_mode ([1280, 720])
    timer = pygame.time.Clock()
    messages = ('CJ : First, we\'re gonna sneak through the vent.',
                'CJ : The vent leads our way to the control room-',
                'CJ : -where the master keycard is located.',
                'CJ : Once we get the master keycard...',
                '...')
    snip = font.render('', True, 'white')
    counter = 0
    speed = 2
    active_message = 0
    message = messages[active_message]

    run = True

    while run:

        timer = pygame.time.Clock()

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        PAUSE = Button(image=pygame.image.load("assets/pause.png"), pos=(50, 50), 
                            text_input="           ", font=textbutton_font(21), base_color="black", hovering_color="#FF3131")

        bg = pygame.image.load('assets/vents.png')
        scaled_bg = pygame.transform.scale(bg, (1280,720))
        bg_rect = scaled_bg.get_rect(x=0,y=0)
        
        textbox = pygame.image.load('assets/textbox.png')
        scaled_texbox = pygame.transform.scale(textbox, (850,200))
        textbox_rect = scaled_texbox.get_rect(x=220,y=500)

        SCREEN.blit(scaled_bg, bg_rect)
        PAUSE.update(SCREEN)
        PAUSE.changeColor(MENU_MOUSE_POS)
        SCREEN.blit(scaled_texbox, textbox_rect)

        timer.tick(60)
        if counter < speed * len(message):
            counter += 1

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PAUSE.checkForInput(MENU_MOUSE_POS):
                    pausemenu()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if counter >= speed * len(message) and active_message < len(messages) - 1:
                        active_message += 1
                        message = messages[active_message]
                        counter = 0
                    else:
                        counter = speed * len(message)
                if active_message == 3:
                    dialogue29()

        snip = font.render(message[0:counter//speed], True, 'white')
        screen.blit(snip, (280, 570))

        pygame.display.flip()

def dialogue29():
    font = pygame.font.Font('assets/ARCADE.TTF', 24)
    screen = pygame.display.set_mode ([1280, 720])
    timer = pygame.time.Clock()
    messages = ('CJ : We have to find the warden with the car keys.',
                'CJ : Grab his outfits, and use his car to escape.',
                '...')
    snip = font.render('', True, 'white')
    counter = 0
    speed = 2
    active_message = 0
    message = messages[active_message]

    run = True

    while run:

        timer = pygame.time.Clock()

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        PAUSE = Button(image=pygame.image.load("assets/pause.png"), pos=(50, 50), 
                            text_input="           ", font=textbutton_font(21), base_color="black", hovering_color="#FF3131")

        bg = pygame.image.load('assets/sneakwarden.jpg')
        scaled_bg = pygame.transform.scale(bg, (1280,720))
        bg_rect = scaled_bg.get_rect(x=0,y=0)
        
        textbox = pygame.image.load('assets/textbox.png')
        scaled_texbox = pygame.transform.scale(textbox, (850,200))
        textbox_rect = scaled_texbox.get_rect(x=220,y=500)

        SCREEN.blit(scaled_bg, bg_rect)
        PAUSE.update(SCREEN)
        PAUSE.changeColor(MENU_MOUSE_POS)
        SCREEN.blit(scaled_texbox, textbox_rect)

        timer.tick(60)
        if counter < speed * len(message):
            counter += 1

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PAUSE.checkForInput(MENU_MOUSE_POS):
                    pausemenu()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if counter >= speed * len(message) and active_message < len(messages) - 1:
                        active_message += 1
                        message = messages[active_message]
                        counter = 0
                    else:
                        counter = speed * len(message)
                if active_message == 2:
                    dialogue30()

        snip = font.render(message[0:counter//speed], True, 'white')
        screen.blit(snip, (280, 570))

        pygame.display.flip()

def dialogue30():
    font = pygame.font.Font('assets/ARCADE.TTF', 24)
    screen = pygame.display.set_mode ([1280, 720])
    timer = pygame.time.Clock()
    messages = ('CJ : Then BOOM, I get my freedom, you get a girlfriend.',
                'MC : ...',
                'MC : Easier said than done, dumbass.',
                'CJ : Trust me, It\'s easy enough.',
                'CJ : You watched too many prison-related movies dude.',
                'MC : Well... you ain\'t wrong',
                'CJ : So, what do you say? You in?',
                'CJ : It\'s not like you have a choice. You HAVE to join me.',
                'MC : Whatever you say, boss.',
                'MC : So, when do we start?',
                'CJ : *smirks*',
                'MC : Yeah, I understand... Tomorrow it is...',
                'CJ : Good! So this is where our meeting is conluded',
                'CJ : LOOK, A BIG CHUNGUS!',
                'MC : WHERE?',
                '...')
    snip = font.render('', True, 'white')
    counter = 0
    speed = 2
    active_message = 0
    message = messages[active_message]

    run = True

    while run:

        timer = pygame.time.Clock()

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        PAUSE = Button(image=pygame.image.load("assets/pause.png"), pos=(50, 50), 
                            text_input="           ", font=textbutton_font(21), base_color="black", hovering_color="#FF3131")

        bg = pygame.image.load('assets/cafeteriabg.jpg')
        scaled_bg = pygame.transform.scale(bg, (1280,720))
        bg_rect = scaled_bg.get_rect(x=0,y=0)
        
        textbox = pygame.image.load('assets/textbox.png')
        scaled_texbox = pygame.transform.scale(textbox, (850,200))
        textbox_rect = scaled_texbox.get_rect(x=220,y=500)

        SCREEN.blit(scaled_bg, bg_rect)
        PAUSE.update(SCREEN)
        PAUSE.changeColor(MENU_MOUSE_POS)
        mc(270,1)
        villain(670,1)
        SCREEN.blit(scaled_texbox, textbox_rect)

        timer.tick(60)
        if counter < speed * len(message):
            counter += 1

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PAUSE.checkForInput(MENU_MOUSE_POS):
                    pausemenu()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if counter >= speed * len(message) and active_message < len(messages) - 1:
                        active_message += 1
                        message = messages[active_message]
                        counter = 0
                    else:
                        counter = speed * len(message)
                if active_message == 15:
                    dialogue31()

        snip = font.render(message[0:counter//speed], True, 'white')
        screen.blit(snip, (280, 570))

        pygame.display.flip()

def dialogue31():
    font = pygame.font.Font('assets/ARCADE.TTF', 24)
    screen = pygame.display.set_mode ([1280, 720])
    timer = pygame.time.Clock()
    messages = ('As MC averts his attention, CJ quickly run away and disappeared',
                'MC : *bleep*, I GOT FOOLED THE SECOND TIME.',
                '...')
    snip = font.render('', True, 'white')
    counter = 0
    speed = 2
    active_message = 0
    message = messages[active_message]

    run = True

    while run:

        timer = pygame.time.Clock()

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        PAUSE = Button(image=pygame.image.load("assets/pause.png"), pos=(50, 50), 
                            text_input="           ", font=textbutton_font(21), base_color="black", hovering_color="#FF3131")

        bg = pygame.image.load('assets/cafeteriabg.jpg')
        scaled_bg = pygame.transform.scale(bg, (1280,720))
        bg_rect = scaled_bg.get_rect(x=0,y=0)
        
        textbox = pygame.image.load('assets/textbox.png')
        scaled_texbox = pygame.transform.scale(textbox, (850,200))
        textbox_rect = scaled_texbox.get_rect(x=220,y=500)

        SCREEN.blit(scaled_bg, bg_rect)
        PAUSE.update(SCREEN)
        PAUSE.changeColor(MENU_MOUSE_POS)
        mc(475,1)
        SCREEN.blit(scaled_texbox, textbox_rect)

        timer.tick(60)
        if counter < speed * len(message):
            counter += 1

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PAUSE.checkForInput(MENU_MOUSE_POS):
                    pausemenu()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if counter >= speed * len(message) and active_message < len(messages) - 1:
                        active_message += 1
                        message = messages[active_message]
                        counter = 0
                    else:
                        counter = speed * len(message)
                if active_message == 10:
                    chap1v5_opening()

        snip = font.render(message[0:counter//speed], True, 'white')
        screen.blit(snip, (280, 570))

        pygame.display.flip()

def chap1v5_opening():
    timer = pygame.time.Clock()

    run = True
    while run:

        timer.tick(60)

        bg = pygame.image.load('assets/hallwayblur.jpg')
        scaled_bg = pygame.transform.scale(bg, (1280,720))
        bg_rect = scaled_bg.get_rect(x=0,y=0)
        SCREEN.blit(scaled_bg, bg_rect)

        box = pygame.image.load('assets/Play Rect.png')
        scaled_box = pygame.transform.scale(box, (640,240))
        box_rect = scaled_box.get_rect(x=320,y=250)
        SCREEN.blit(scaled_box, box_rect)

        end = prologuefont(40).render("Chapter 1 - Act 5", True, "White")
        end_rect = end.get_rect(x=340, y=320)
        SCREEN.blit(end,end_rect)

        troll = prologuefont(22).render("Operation : Pablo Escobar", True, "White")
        troll_rect = troll.get_rect(x=343, y=370)
        SCREEN.blit(troll,troll_rect)

        info = textbutton_font(19).render("New Klang Private Penitentiary - Prison Hallway - 9:07:10 AM", True, "White")
        info_rect = end.get_rect(x=343, y=450)
        SCREEN.blit(info,info_rect)

        info = textbutton_font(24).render("(click Enter to continue...)", True, "White")
        info_rect = end.get_rect(x=500, y=600)
        SCREEN.blit(info,info_rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    dialogue32()

        pygame.display.flip()

def dialogue32():
    font = pygame.font.Font('assets/ARCADE.TTF', 24)
    screen = pygame.display.set_mode ([1280, 720])
    timer = pygame.time.Clock()
    messages = ('It\'s 9 in the morning.',
                'All inmates are heading to the cafeteria for breakfast',
                '...')
    snip = font.render('', True, 'white')
    counter = 0
    speed = 1
    active_message = 0
    message = messages[active_message]

    run = True

    while run:

        timer = pygame.time.Clock()

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        PAUSE = Button(image=pygame.image.load("assets/pause.png"), pos=(50, 50), 
                            text_input="           ", font=textbutton_font(21), base_color="black", hovering_color="#FF3131")

        bg = pygame.image.load('assets/prisonhallway.png')
        scaled_bg = pygame.transform.scale(bg, (1280,720))
        bg_rect = scaled_bg.get_rect(x=0,y=0)
        
        textbox = pygame.image.load('assets/textbox.png')
        scaled_texbox = pygame.transform.scale(textbox, (850,200))
        textbox_rect = scaled_texbox.get_rect(x=220,y=500)

        SCREEN.blit(scaled_bg, bg_rect)
        PAUSE.update(SCREEN)
        PAUSE.changeColor(MENU_MOUSE_POS)
        SCREEN.blit(scaled_texbox, textbox_rect)

        timer.tick(60)
        if counter < speed * len(message):
            counter += 1

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PAUSE.checkForInput(MENU_MOUSE_POS):
                    pausemenu()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if counter >= speed * len(message) and active_message < len(messages) - 1:
                        active_message += 1
                        message = messages[active_message]
                        counter = 0
                    else:
                        counter = speed * len(message)
                if active_message == 2:
                    dialogue33()

        snip = font.render(message[0:counter//speed], True, 'white')
        screen.blit(snip, (280, 570))

        pygame.display.flip()

def dialogue33():
    font = pygame.font.Font('assets/ARCADE.TTF', 24)
    screen = pygame.display.set_mode ([1280, 720])
    timer = pygame.time.Clock()
    messages = ('EXCEPT for MC, who\'s waiting for the right timing...',
                'MC : ...',
                'After confirming that no one\'s around, he makes the first move.',
                'He heads towards the path that leads to the security room.',
                'He hid behind a wall, observing the guard who is patrolling there.',
                'The guard seems to be following a fixed route...',
                'MC : Wait for it...',
                'After the guard has left the area...',
                'MC : Now\'s the chance!',
                'He dashed to the vent connected to the security room.',
                '...')
    snip = font.render('', True, 'white')
    counter = 0
    speed = 1
    active_message = 0
    message = messages[active_message]

    run = True

    while run:

        timer = pygame.time.Clock()

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        PAUSE = Button(image=pygame.image.load("assets/pause.png"), pos=(50, 50), 
                            text_input="           ", font=textbutton_font(21), base_color="black", hovering_color="#FF3131")

        bg = pygame.image.load('assets/prisonhallway.png')
        scaled_bg = pygame.transform.scale(bg, (1280,720))
        bg_rect = scaled_bg.get_rect(x=0,y=0)
        
        textbox = pygame.image.load('assets/textbox.png')
        scaled_texbox = pygame.transform.scale(textbox, (850,200))
        textbox_rect = scaled_texbox.get_rect(x=220,y=500)

        SCREEN.blit(scaled_bg, bg_rect)
        PAUSE.update(SCREEN)
        PAUSE.changeColor(MENU_MOUSE_POS)
        mc(475,1)
        SCREEN.blit(scaled_texbox, textbox_rect)

        timer.tick(60)
        if counter < speed * len(message):
            counter += 1

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PAUSE.checkForInput(MENU_MOUSE_POS):
                    pausemenu()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if counter >= speed * len(message) and active_message < len(messages) - 1:
                        active_message += 1
                        message = messages[active_message]
                        counter = 0
                    else:
                        counter = speed * len(message)
                if active_message == 10:
                    dialogue34()

        snip = font.render(message[0:counter//speed], True, 'white')
        screen.blit(snip, (280, 570))

        pygame.display.flip()

def dialogue34():
    font = pygame.font.Font('assets/ARCADE.TTF', 24)
    screen = pygame.display.set_mode ([1280, 720])
    timer = pygame.time.Clock()
    messages = ('MC : So this is the vent that CJ are talking about.',
                '...')
    snip = font.render('', True, 'white')
    counter = 0
    speed = 1
    active_message = 0
    message = messages[active_message]

    run = True

    while run:

        timer = pygame.time.Clock()

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        PAUSE = Button(image=pygame.image.load("assets/pause.png"), pos=(50, 50), 
                            text_input="           ", font=textbutton_font(21), base_color="black", hovering_color="#FF3131")

        bg = pygame.image.load('assets/vents.png')
        scaled_bg = pygame.transform.scale(bg, (1280,720))
        bg_rect = scaled_bg.get_rect(x=0,y=0)
        
        textbox = pygame.image.load('assets/textbox.png')
        scaled_texbox = pygame.transform.scale(textbox, (850,200))
        textbox_rect = scaled_texbox.get_rect(x=220,y=500)

        SCREEN.blit(scaled_bg, bg_rect)
        PAUSE.update(SCREEN)
        PAUSE.changeColor(MENU_MOUSE_POS)
        SCREEN.blit(scaled_texbox, textbox_rect)

        timer.tick(60)
        if counter < speed * len(message):
            counter += 1

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PAUSE.checkForInput(MENU_MOUSE_POS):
                    pausemenu()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if counter >= speed * len(message) and active_message < len(messages) - 1:
                        active_message += 1
                        message = messages[active_message]
                        counter = 0
                    else:
                        counter = speed * len(message)
                if active_message == 1:
                    choice5()

        snip = font.render(message[0:counter//speed], True, 'white')
        screen.blit(snip, (280, 570))

        pygame.display.flip()

def dialogue35():
    font = pygame.font.Font('assets/ARCADE.TTF', 24)
    screen = pygame.display.set_mode ([1280, 720])
    timer = pygame.time.Clock()
    messages = ('The vent easily creaks open...',
                'MC : Huh, piece of cake',
                'MC quickly crawls into the vent, before the guard patrols there.',
                '...')
    snip = font.render('', True, 'white')
    counter = 0
    speed = 2
    active_message = 0
    message = messages[active_message]

    run = True

    while run:

        timer = pygame.time.Clock()

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        PAUSE = Button(image=pygame.image.load("assets/pause.png"), pos=(50, 50), 
                            text_input="           ", font=textbutton_font(21), base_color="black", hovering_color="#FF3131")

        bg = pygame.image.load('assets/openingvent.png')
        scaled_bg = pygame.transform.scale(bg, (1280,720))
        bg_rect = scaled_bg.get_rect(x=0,y=0)
        
        textbox = pygame.image.load('assets/textbox.png')
        scaled_texbox = pygame.transform.scale(textbox, (850,200))
        textbox_rect = scaled_texbox.get_rect(x=220,y=500)

        SCREEN.blit(scaled_bg, bg_rect)
        PAUSE.update(SCREEN)
        PAUSE.changeColor(MENU_MOUSE_POS)
        SCREEN.blit(scaled_texbox, textbox_rect)

        timer.tick(60)
        if counter < speed * len(message):
            counter += 1

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PAUSE.checkForInput(MENU_MOUSE_POS):
                    pausemenu()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if counter >= speed * len(message) and active_message < len(messages) - 1:
                        active_message += 1
                        message = messages[active_message]
                        counter = 0
                    else:
                        counter = speed * len(message)
                if active_message == 3:
                    dialogue36v2()

        snip = font.render(message[0:counter//speed], True, 'white')
        screen.blit(snip, (280, 570))

        pygame.display.flip()

def dialogue35v2():
    font = pygame.font.Font('assets/ARCADE.TTF', 24)
    screen = pygame.display.set_mode ([1280, 720])
    timer = pygame.time.Clock()
    messages = ('Uh oh... It seems that you are not strong enough to do it.',
                'MC : Hnghhh! Come on, open up!!!',
                'MC : *creaks* Almost...!!!',
                'Guard : Hey, what\'re you doing?!',
                'MC : Shoot! I didn\'t make it in time. Hafta force my way!',
                '...')
    snip = font.render('', True, 'white')
    counter = 0
    speed = 2
    active_message = 0
    message = messages[active_message]

    run = True

    while run:

        timer = pygame.time.Clock()

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        PAUSE = Button(image=pygame.image.load("assets/pause.png"), pos=(50, 50), 
                            text_input="           ", font=textbutton_font(21), base_color="black", hovering_color="#FF3131")

        bg = pygame.image.load('assets/openingvent.png')
        scaled_bg = pygame.transform.scale(bg, (1280,720))
        bg_rect = scaled_bg.get_rect(x=0,y=0)
        
        textbox = pygame.image.load('assets/textbox.png')
        scaled_texbox = pygame.transform.scale(textbox, (850,200))
        textbox_rect = scaled_texbox.get_rect(x=220,y=500)

        SCREEN.blit(scaled_bg, bg_rect)
        PAUSE.update(SCREEN)
        PAUSE.changeColor(MENU_MOUSE_POS)
        SCREEN.blit(scaled_texbox, textbox_rect)

        timer.tick(60)
        if counter < speed * len(message):
            counter += 1

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PAUSE.checkForInput(MENU_MOUSE_POS):
                    pausemenu()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if counter >= speed * len(message) and active_message < len(messages) - 1:
                        active_message += 1
                        message = messages[active_message]
                        counter = 0
                    else:
                        counter = speed * len(message)
                if active_message == 5:
                    dialogue36()

        snip = font.render(message[0:counter//speed], True, 'white')
        screen.blit(snip, (280, 570))

        pygame.display.flip()

def dialogue36():
    font = pygame.font.Font('assets/ARCADE.TTF', 24)
    screen = pygame.display.set_mode ([1280, 720])
    timer = pygame.time.Clock()
    messages = ('MC : Change of plan. Gonna beat up this guard.',
                'MC : C\'mere boy.',
                'MC waits for first strike from the guard.',
                'As the guard let out a right punch, MC dodges and counters her.',
                'MC kicks behind the guard\'s knee, forcing her to kneel down',
                'Then, a powerful uppercut from MC knocks out the guard.',
                'MC : That was too easy. Expected more from her.',
                'MC : Have to thank CJ.', 
                'MC : Haven\'t got a good fight like this in a long time.',
                'MC takes the guard\'s keycard and heads towards the security room.',
                '...')
    snip = font.render('', True, 'white')
    counter = 0
    speed = 1
    active_message = 0
    message = messages[active_message]

    run = True

    while run:

        timer = pygame.time.Clock()

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        PAUSE = Button(image=pygame.image.load("assets/pause.png"), pos=(50, 50), 
                            text_input="           ", font=textbutton_font(21), base_color="black", hovering_color="#FF3131")

        bg = pygame.image.load('assets/fight.jpg')
        scaled_bg = pygame.transform.scale(bg, (1280,720))
        bg_rect = scaled_bg.get_rect(x=0,y=0)
        
        textbox = pygame.image.load('assets/textbox.png')
        scaled_texbox = pygame.transform.scale(textbox, (850,200))
        textbox_rect = scaled_texbox.get_rect(x=220,y=500)

        SCREEN.blit(scaled_bg, bg_rect)
        PAUSE.update(SCREEN)
        PAUSE.changeColor(MENU_MOUSE_POS)
        SCREEN.blit(scaled_texbox, textbox_rect)

        timer.tick(60)
        if counter < speed * len(message):
            counter += 1

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PAUSE.checkForInput(MENU_MOUSE_POS):
                    pausemenu()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if counter >= speed * len(message) and active_message < len(messages) - 1:
                        active_message += 1
                        message = messages[active_message]
                        counter = 0
                    else:
                        counter = speed * len(message)
                if active_message == 10:
                    dialogue36v3()

        snip = font.render(message[0:counter//speed], True, 'white')
        screen.blit(snip, (280, 570))

        pygame.display.flip()

def dialogue36v2():
    font = pygame.font.Font('assets/ARCADE.TTF', 24)
    screen = pygame.display.set_mode ([1280, 720])
    timer = pygame.time.Clock()
    messages = ('MC : Hmm...',
                'MC : CJ kind of suspicious...',
                'MC : How does he know about my identity?',
                'MC : And he seems eager to help me get out.',
                'MC : Anyways, gotta keep my eyes on him...',
                'He continues to crawl inside the vent, until he reach the end.',
                'He then jump down to get into the security room sneakily.',
                'Or... so he thought.',
                '...')
    snip = font.render('', True, 'white')
    counter = 0
    speed = 2
    active_message = 0
    message = messages[active_message]

    run = True

    while run:

        timer = pygame.time.Clock()

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        PAUSE = Button(image=pygame.image.load("assets/pause.png"), pos=(50, 50), 
                            text_input="           ", font=textbutton_font(21), base_color="black", hovering_color="#FF3131")

        bg = pygame.image.load('assets/insidevent.jpg')
        scaled_bg = pygame.transform.scale(bg, (1280,720))
        bg_rect = scaled_bg.get_rect(x=0,y=0)
        
        textbox = pygame.image.load('assets/textbox.png')
        scaled_texbox = pygame.transform.scale(textbox, (850,200))
        textbox_rect = scaled_texbox.get_rect(x=220,y=500)

        SCREEN.blit(scaled_bg, bg_rect)
        PAUSE.update(SCREEN)
        PAUSE.changeColor(MENU_MOUSE_POS)
        SCREEN.blit(scaled_texbox, textbox_rect)

        timer.tick(60)
        if counter < speed * len(message):
            counter += 1

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PAUSE.checkForInput(MENU_MOUSE_POS):
                    pausemenu()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if counter >= speed * len(message) and active_message < len(messages) - 1:
                        active_message += 1
                        message = messages[active_message]
                        counter = 0
                    else:
                        counter = speed * len(message)
                if active_message == 8:
                    dialogue37()

        snip = font.render(message[0:counter//speed], True, 'white')
        screen.blit(snip, (280, 570))

        pygame.display.flip()

def dialogue36v3():
    font = pygame.font.Font('assets/ARCADE.TTF', 24)
    screen = pygame.display.set_mode ([1280, 720])
    timer = pygame.time.Clock()
    messages = ('Beep! The sound of the door unlocked after scanning the keycard.',
                'MC : CJ\'s right though. Escaping a prison IS easy.',
                'MC : Now, moving on to the next phase.',
                'MC : Finding the master keycard.',
                'MC enters the security room...',
                '...')
    snip = font.render('', True, 'white')
    counter = 0
    speed = 2
    active_message = 0
    message = messages[active_message]

    run = True

    while run:

        timer = pygame.time.Clock()

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        PAUSE = Button(image=pygame.image.load("assets/pause.png"), pos=(50, 50), 
                            text_input="           ", font=textbutton_font(21), base_color="black", hovering_color="#FF3131")

        bg = pygame.image.load('assets/securitydoor.jpg')
        scaled_bg = pygame.transform.scale(bg, (1280,720))
        bg_rect = scaled_bg.get_rect(x=0,y=0)
        
        textbox = pygame.image.load('assets/textbox.png')
        scaled_texbox = pygame.transform.scale(textbox, (850,200))
        textbox_rect = scaled_texbox.get_rect(x=220,y=500)

        SCREEN.blit(scaled_bg, bg_rect)
        PAUSE.update(SCREEN)
        PAUSE.changeColor(MENU_MOUSE_POS)
        SCREEN.blit(scaled_texbox, textbox_rect)

        timer.tick(60)
        if counter < speed * len(message):
            counter += 1

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PAUSE.checkForInput(MENU_MOUSE_POS):
                    pausemenu()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if counter >= speed * len(message) and active_message < len(messages) - 1:
                        active_message += 1
                        message = messages[active_message]
                        counter = 0
                    else:
                        counter = speed * len(message)
                if active_message == 5:
                    dialogue37()

        snip = font.render(message[0:counter//speed], True, 'white')
        screen.blit(snip, (280, 570))

        pygame.display.flip()

def dialogue37():
    font = pygame.font.Font('assets/ARCADE.TTF', 24)
    screen = pygame.display.set_mode ([1280, 720])
    timer = pygame.time.Clock()
    messages = ('MC : Shoot! There\'s guard!',
                '...')
    snip = font.render('', True, 'white')
    counter = 0
    speed = 2
    active_message = 0
    message = messages[active_message]

    run = True

    while run:

        timer = pygame.time.Clock()

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        PAUSE = Button(image=pygame.image.load("assets/pause.png"), pos=(50, 50), 
                            text_input="           ", font=textbutton_font(21), base_color="black", hovering_color="#FF3131")

        bg = pygame.image.load('assets/securityroom.jpg')
        scaled_bg = pygame.transform.scale(bg, (1280,720))
        bg_rect = scaled_bg.get_rect(x=0,y=0)
        
        textbox = pygame.image.load('assets/textbox.png')
        scaled_texbox = pygame.transform.scale(textbox, (850,200))
        textbox_rect = scaled_texbox.get_rect(x=220,y=500)

        SCREEN.blit(scaled_bg, bg_rect)
        PAUSE.update(SCREEN)
        PAUSE.changeColor(MENU_MOUSE_POS)
        mc(270,1)
        SCREEN.blit(scaled_texbox, textbox_rect)

        timer.tick(60)
        if counter < speed * len(message):
            counter += 1

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PAUSE.checkForInput(MENU_MOUSE_POS):
                    pausemenu()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if counter >= speed * len(message) and active_message < len(messages) - 1:
                        active_message += 1
                        message = messages[active_message]
                        counter = 0
                    else:
                        counter = speed * len(message)
                if active_message == 1:
                    dialogue38()

        snip = font.render(message[0:counter//speed], True, 'white')
        screen.blit(snip, (280, 570))

        pygame.display.flip()

def dialogue38():
    font = pygame.font.Font('assets/ARCADE.TTF', 24)
    screen = pygame.display.set_mode ([1280, 720])
    timer = pygame.time.Clock()
    messages = ('MC : Shoot! There\'s guard!',
                '...')
    snip = font.render('', True, 'white')
    counter = 0
    speed = 1
    active_message = 0
    message = messages[active_message]

    run = True

    while run:

        timer = pygame.time.Clock()

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        PAUSE = Button(image=pygame.image.load("assets/pause.png"), pos=(50, 50), 
                            text_input="           ", font=textbutton_font(21), base_color="black", hovering_color="#FF3131")

        bg = pygame.image.load('assets/securityroom.jpg')
        scaled_bg = pygame.transform.scale(bg, (1280,720))
        bg_rect = scaled_bg.get_rect(x=0,y=0)
        
        textbox = pygame.image.load('assets/textbox.png')
        scaled_texbox = pygame.transform.scale(textbox, (850,200))
        textbox_rect = scaled_texbox.get_rect(x=220,y=500)

        SCREEN.blit(scaled_bg, bg_rect)
        PAUSE.update(SCREEN)
        PAUSE.changeColor(MENU_MOUSE_POS)
        mc(250,1)
        guard(550,170)
        SCREEN.blit(scaled_texbox, textbox_rect)

        timer.tick(60)
        if counter < speed * len(message):
            counter += 1

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PAUSE.checkForInput(MENU_MOUSE_POS):
                    pausemenu()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if counter >= speed * len(message) and active_message < len(messages) - 1:
                        active_message += 1
                        message = messages[active_message]
                        counter = 0
                    else:
                        counter = speed * len(message)
                if active_message == 1:
                    choice5()

        snip = font.render(message[0:counter//speed], True, 'white')
        screen.blit(snip, (280, 570))

        pygame.display.flip()
chap1v2_opening()