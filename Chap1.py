import pygame, sys
from config import *
from button import Button
pygame.init()

bgmusic = pygame.mixer.Sound("assets/bgmtwo.mp3")
sadbgm = pygame.mixer.Sound("assets/sadbgm.mp3")
introbgm = pygame.mixer.Sound("assets/introbgm.mp3")
steps = pygame.mixer.Sound("assets/footsteps.mp3")
gaycounter = 0

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


def choice1():
    global gaycounter
    while True:

        timer = pygame.time.Clock()

        current  = textbutton_font(24).render("NPC : ...go on your own...?", True, "White")
        current_rect = current.get_rect(x=280, y=570)

        bg = pygame.image.load('assets/prisoncell.jpg')
        scaled_bg = pygame.transform.scale(bg, (1280,720))
        bg_rect = scaled_bg.get_rect(x=0,y=0)
        
        textbox = pygame.image.load('assets/textbox.png')
        scaled_texbox = pygame.transform.scale(textbox, (850,200))
        textbox_rect = scaled_texbox.get_rect(x=220,y=500)

        c1 = pygame.image.load('assets/cbutton.png')
        scaled_c1 = pygame.transform.scale(c1, (500,70))
        c1_rect = scaled_texbox.get_rect(x=400,y=228)

        c2 = pygame.image.load('assets/cbutton.png')
        scaled_c2 = pygame.transform.scale(c2, (500,70))
        c2_rect = scaled_texbox.get_rect(x=400,y=328)

        c3 = pygame.image.load('assets/cbutton.png')
        scaled_c3 = pygame.transform.scale(c3, (500,70))
        c3_rect = scaled_texbox.get_rect(x=400,y=428)

        SCREEN.blit(scaled_bg, bg_rect)
        mcdark()
        walterdark()
        SCREEN.blit(scaled_texbox, textbox_rect)
        SCREEN.blit(current, current_rect)
        SCREEN.blit(scaled_c1, c1_rect)
        SCREEN.blit(scaled_c2, c2_rect)
        SCREEN.blit(scaled_c3, c3_rect)

        timer.tick(60)

        MENU_MOUSE_POS = pygame.mouse.get_pos()  #detecting mouse position

        CHOICE1 = Button(image=pygame.image.load("assets/transparent.png"), pos=(650, 265), 
                            text_input="I\'m waiting for you baby...", font=textbutton_font(21), base_color="black", hovering_color="#FF3131") #find better colour
        
        CHOICE2 = Button(image=pygame.image.load("assets/transparent.png"), pos=(650, 365), 
                            text_input="Because I\'m a good friend.", font=textbutton_font(21), base_color="black", hovering_color="#FF3131")

        CHOICE3 = Button(image=pygame.image.load("assets/transparent.png"), pos=(650, 465), 
                            text_input="I\'m scared...", font=textbutton_font(21), base_color="black", hovering_color="#FF3131")

        PAUSE = Button(image=pygame.image.load("assets/pause.png"), pos=(50, 50), 
                            text_input="           ", font=textbutton_font(21), base_color="black", hovering_color="#FF3131")

        for button in [CHOICE1,CHOICE2,CHOICE3,PAUSE]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)

        for event in pygame.event.get():

            if event.type == pygame.QUIT: #if pressing x button on window screen
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if CHOICE1.checkForInput(MENU_MOUSE_POS):
                    gaycounter += 1
                    dialogue4v2()
                if CHOICE2.checkForInput(MENU_MOUSE_POS):
                    dialogue4()
                if CHOICE3.checkForInput(MENU_MOUSE_POS):
                    dialogue4v2()
                if PAUSE.checkForInput(MENU_MOUSE_POS):
                    pausemenu()

            pygame.display.flip()

def choice2():
    global gaycounter
    while True:

        timer = pygame.time.Clock()

        current  = textbutton_font(24).render("NPC : ...", True, "White")
        current_rect = current.get_rect(x=280, y=570)

        bg = pygame.image.load('assets/prisoncell.jpg')
        scaled_bg = pygame.transform.scale(bg, (1280,720))
        bg_rect = scaled_bg.get_rect(x=0,y=0)
        
        textbox = pygame.image.load('assets/textbox.png')
        scaled_texbox = pygame.transform.scale(textbox, (850,200))
        textbox_rect = scaled_texbox.get_rect(x=220,y=500)

        c1 = pygame.image.load('assets/cbutton.png')
        scaled_c1 = pygame.transform.scale(c1, (500,70))
        c1_rect = scaled_texbox.get_rect(x=400,y=228)

        c2 = pygame.image.load('assets/cbutton.png')
        scaled_c2 = pygame.transform.scale(c2, (500,70))
        c2_rect = scaled_texbox.get_rect(x=400,y=328)

        SCREEN.blit(scaled_bg, bg_rect)
        mcdark()
        walterdark()
        SCREEN.blit(scaled_texbox, textbox_rect)
        SCREEN.blit(current, current_rect)
        SCREEN.blit(scaled_c1, c1_rect)
        SCREEN.blit(scaled_c2, c2_rect)

        timer.tick(60)

        MENU_MOUSE_POS = pygame.mouse.get_pos()  #detecting mouse position

        CHOICE1 = Button(image=pygame.image.load("assets/transparent.png"), pos=(650, 265), 
                            text_input="So, are you going to touch me :3 ?", font=textbutton_font(21), base_color="black", hovering_color="#FF3131") #find better colour
        
        CHOICE1v2 = Button(image=pygame.image.load("assets/transparent.png"), pos=(650, 265), 
                            text_input="Haha, I guess...?", font=textbutton_font(21), base_color="black", hovering_color="#FF3131") #find better colour
        
        CHOICE2 = Button(image=pygame.image.load("assets/transparent.png"), pos=(650, 365), 
                            text_input="I'll just... forget about this.", font=textbutton_font(21), base_color="black", hovering_color="#FF3131")

        PAUSE = Button(image=pygame.image.load("assets/pause.png"), pos=(50, 50), 
                            text_input="           ", font=textbutton_font(21), base_color="black", hovering_color="#FF3131")

        for button in [CHOICE1v2 if gaycounter != 1 else CHOICE1,CHOICE2,PAUSE]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if gaycounter == 1:
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if CHOICE1.checkForInput(MENU_MOUSE_POS):
                            gaycounter += 1
                            print(gaycounter)
                            dialogue5()
                        if CHOICE2.checkForInput(MENU_MOUSE_POS):
                            dialogue5v2()
                else:
                    # If gaycounter is not 1, disable CHOICE1 functionality
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if CHOICE1v2.checkForInput(MENU_MOUSE_POS):
                            print(gaycounter)
                            dialogue5v3()
                        if CHOICE2.checkForInput(MENU_MOUSE_POS):
                            dialogue5v2()
                if PAUSE.checkForInput(MENU_MOUSE_POS):
                    pausemenu()

            pygame.display.flip()

def choice3():
    global gaycounter
    while True:

        timer = pygame.time.Clock()

        current  = textbutton_font(24).render("NPC : So, ya made up your mind?", True, "White")
        current_rect = current.get_rect(x=280, y=570)

        bg = pygame.image.load('assets/prisoncell.jpg')
        scaled_bg = pygame.transform.scale(bg, (1280,720))
        bg_rect = scaled_bg.get_rect(x=0,y=0)
        
        textbox = pygame.image.load('assets/textbox.png')
        scaled_textbox = pygame.transform.scale(textbox, (850,200))
        textbox_rect = scaled_textbox.get_rect(x=220,y=500)

        c1 = pygame.image.load('assets/cbutton.png')
        scaled_c1 = pygame.transform.scale(c1, (500,70))
        c1_rect = scaled_c1.get_rect(x=400,y=228)

        c2 = pygame.image.load('assets/cbutton.png')
        scaled_c2 = pygame.transform.scale(c2, (500,70))
        c2_rect = scaled_c2.get_rect(x=400,y=328)

        c3 = pygame.image.load('assets/cbutton.png')
        scaled_c3 = pygame.transform.scale(c3, (500,70))
        c3_rect = scaled_c3.get_rect(x=400,y=428)

        SCREEN.blit(scaled_bg, bg_rect)
        mcdark()
        walterdark()
        SCREEN.blit(scaled_textbox, textbox_rect)
        SCREEN.blit(current, current_rect)
        SCREEN.blit(scaled_c1, c1_rect)
        SCREEN.blit(scaled_c2, c2_rect)
        if gaycounter == 2:
            SCREEN.blit(scaled_c3, c3_rect)

        timer.tick(60)

        MENU_MOUSE_POS = pygame.mouse.get_pos()  #detecting mouse position

        CHOICE1 = Button(image=pygame.image.load("assets/transparent.png"), pos=(650, 465), 
                            text_input="...can I be your baby :3?", font=textbutton_font(17), base_color="black", hovering_color="#FF3131")

        
        CHOICE1v2 = Button(image=pygame.image.load("assets/transparent.png"), pos=(650, 265), 
                            text_input="Nah man, not gonna do some crazy shit like that.", font=textbutton_font(17), base_color="black", hovering_color="#FF3131")

        CHOICE2 = Button(image=pygame.image.load("assets/transparent.png"), pos=(650, 365), 
                            text_input="...give me some time, would ya?", font=textbutton_font(21), base_color="black", hovering_color="#FF3131")

        PAUSE = Button(image=pygame.image.load("assets/pause.png"), pos=(50, 50), 
                            text_input="           ", font=textbutton_font(21), base_color="black", hovering_color="#FF3131")

        for button in [CHOICE1v2,CHOICE1,CHOICE2,PAUSE if gaycounter == 2 else CHOICE1v2,CHOICE2,PAUSE]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)

        for event in pygame.event.get():

            if event.type == pygame.QUIT: #if pressing x button on window screen
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if gaycounter == 2:
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if CHOICE1.checkForInput(MENU_MOUSE_POS):
                            print(gaycounter)
                            dialogue7()
                        if CHOICE1v2.checkForInput(MENU_MOUSE_POS):
                            dialogue7v3()
                        if CHOICE2.checkForInput(MENU_MOUSE_POS):
                            dialogue7v2()
                else:
                    # If gaycounter is not 2, disable CHOICE1 functionality
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if CHOICE1v2.checkForInput(MENU_MOUSE_POS):
                            dialogue7v3()
                        if CHOICE2.checkForInput(MENU_MOUSE_POS):
                            dialogue7v2()
                if PAUSE.checkForInput(MENU_MOUSE_POS):
                    pausemenu()

            pygame.display.flip()

def chap1_opening():
    timer = pygame.time.Clock()

    run = True
    while run:

        timer.tick(60)

        text = "In the earlier part of the story... The story revolves around MC"

        bg = pygame.image.load('assets/cafeteriabgblur.jpg')
        scaled_bg = pygame.transform.scale(bg, (1280,720))
        bg_rect = scaled_bg.get_rect(x=0,y=0)
        SCREEN.blit(scaled_bg, bg_rect)

        box = pygame.image.load('assets/Play Rect.png')
        scaled_box = pygame.transform.scale(box, (640,240))
        box_rect = scaled_box.get_rect(x=320,y=250)
        SCREEN.blit(scaled_box, box_rect)

        end = prologuefont(40).render("Chapter 1", True, "White")
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
                    steps.stop()
                    chap1()

        snip = font.render(message[0:counter//speed], True, 'white')
        screen.blit(snip, (280, 570))

        pygame.display.flip()
        steps.play()

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
                'NPC : What a f*ckin annoying piece of too-da-loo...',
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
                    pygame.quit()
                    sys.exit()

        snip = font.render(message[0:counter//speed], True, 'white')
        screen.blit(snip, (280, 570))

        pygame.display.flip()

def dialogue6alternate():
    font = pygame.font.Font('assets/ARCADE.TTF', 24)
    screen = pygame.display.set_mode ([1280, 720])
    timer = pygame.time.Clock()
    messages = ('MC : Hmm... You\'re right though.',
                'MC : But this a high security prison...',
                'MC : Either we escape this place and it\'ll be the greatest achievement-',
                'MC : -or we fail and sentenced with more years to serve.',
                'NPC : What are you, a chicken, a coward?',
                'NPC : C\'mon dude, it\'s not like it\'s your first day in prison...',
                'MC : ...',
                'MC : ...',
                'NPC : So, ya made up your mind?',
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

        bg = pygame.image.load('assets/prisoncell.jpg')
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
                if active_message == 9:
                    choice3()
        snip = font.render(message[0:counter//speed], True, 'white')
        screen.blit(snip, (280, 570))

        pygame.display.flip()
        bgmusic.stop()
        introbgm.play()

def dialoguenj7():
    font = pygame.font.Font('assets/ARCADE.TTF', 24)
    screen = pygame.display.set_mode ([1280, 720])
    timer = pygame.time.Clock()
    messages = ('NPC : That\'s it. You\'re done.',
                'NPC : You\'re being timeout\'d.',
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

        bg = pygame.image.load('assets/prisoncell.jpg')
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
                if active_message == 2:
                    d7troll()

        snip = font.render(message[0:counter//speed], True, 'white')
        screen.blit(snip, (280, 570))

        pygame.display.flip()
        introbgm.stop()
        bgmusic.play()

def dialogue7v2():
    font = pygame.font.Font('assets/ARCADE.TTF', 24)
    screen = pygame.display.set_mode ([1280, 720])
    timer = pygame.time.Clock()
    messages = ('NPC : Ya better think it through.',
                'NPC pats MC\'s shoulder and left...',
                'MC : ...',
                'MC : ...',
                'MC : WHERE THE F**K YOU THINK YOU\'RE GOING???',
                'MC : COME JOIN ME AT THE CAFETERIA FIRST DUDE!',
                'MC : For god sake...',
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

        bg = pygame.image.load('assets/prisoncell.jpg')
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
                    dialogue8()

        snip = font.render(message[0:counter//speed], True, 'white')
        screen.blit(snip, (280, 570))

        pygame.display.flip()

def dialogue7v3():
    font = pygame.font.Font('assets/ARCADE.TTF', 24)
    screen = pygame.display.set_mode ([1280, 720])
    timer = pygame.time.Clock()
    messages = ('NPC : You\'re really a boring person...',
                'NPC : But yeah... if you change your mind-',
                'NPC : -come see me.',
                'MC : ...',
                'MC : I\'ll go to the cafeteria first...',
                'MC went to the cafetria alone, as NPC watches him from behind...',
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

        bg = pygame.image.load('assets/prisoncell.jpg')
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
                if active_message == 6:
                    dialogue8()

        snip = font.render(message[0:counter//speed], True, 'white')
        screen.blit(snip, (280, 570))

        pygame.display.flip()

def dialoguegyg8():
    font = pygame.font.Font('assets/ARCADE.TTF', 24)
    screen = pygame.display.set_mode ([1280, 720])
    timer = pygame.time.Clock()
    messages = ('A mysterious person watches MC from afar...',
                'Mysterious Man : ...',
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

        bg = pygame.image.load('assets/prisoncell.jpg')
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
                if active_message == 2:
                    prologue()

        snip = font.render(message[0:counter//speed], True, 'white')
        screen.blit(snip, (280, 570))

        pygame.display.flip()

def d7troll():
    font = pygame.font.Font('assets/ARCADE.TTF', 24)
    screen = pygame.display.set_mode ([1280, 720])
    timer = pygame.time.Clock()
    messages = ('> pygame.quit()',
                '> sys.exit()',
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

        current  = textbutton_font(24).render("NPC : You\'re being timeout\'d.", True, "White")
        current_rect = current.get_rect(x=280, y=570)

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
        pygame.draw.rect(SCREEN, 'black', [50,50,300,100])
        SCREEN.blit(current, current_rect)

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
                    d7final()

        snip = font.render(message[0:counter//speed], True, 'white')
        screen.blit(snip, (70, 70))

        pygame.display.flip()

def d7final():
    SCREEN.fill((0,0,0))

    run = True

    while run:

        end = textbutton_font(90).render("THANKS FOR BEING GAY :D", True, "White")
        end_rect = end.get_rect(x=120, y=300)
        SCREEN.blit(end,end_rect)

        troll = textbutton_font(15).render("u deserve that u gayboi", True, "White")
        troll_rect = troll.get_rect(x=125, y=380)
        SCREEN.blit(troll,troll_rect)

        info = textbutton_font(24).render("(click Enter to continue...)", True, "White")
        info_rect = end.get_rect(x=500, y=460)
        SCREEN.blit(info,info_rect)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    pygame.quit()
                    sys.exit()

        pygame.display.flip()

def prologue():
    font = pygame.font.Font('assets/Cinzel.ttf', 30)
    screen = pygame.display.set_mode([1280, 720])
    timer = pygame.time.Clock()
    messages = ('END OF PROLOGUE',
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
                if active_message == 1:
                    introbgm.stop()
                    pygame.quit()
                    sys.exit()

        snip = font.render(message[0:counter // speed], True, 'white')
        screen.blit(snip, (500, 360))

        pygame.display.flip()