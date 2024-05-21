import pygame, sys
from config import *
from button import Button
pygame.init()

bgmusic = pygame.mixer.Sound("assets/bgmtwo.mp3")
sadbgm = pygame.mixer.Sound("assets/sadbgm.mp3")
introbgm = pygame.mixer.Sound("assets/introbgm.mp3")
gaycounter = 0

def textbutton_font(size):   
    return pygame.font.Font("assets/ARCADE.TTF", size)

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

def dialogue1():
    font = pygame.font.Font('assets/ARCADE.TTF', 24)
    screen = pygame.display.set_mode ([1280, 720])
    timer = pygame.time.Clock()
    messages = ('...',
                '...',
                '...',
                'It\'s early in the morning, where the Sun shines the brightest.',
                'Birds chirping... laughter of kids can be heard outside...',
                'Birds...? Kids...?',
                'W-wait, something\'s wrong...',
                'This doesn\'t feel like... home?',
                '...')
    snip = font.render('', True, 'white')
    counter = 0
    speed = 1
    active_message = 0
    message = messages[active_message]

    run = True
    while run:

        SCREEN.fill('black')

        timer.tick(60)

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
                if active_message == 8:
                    dialogue1v2()

        snip = font.render(message[0:counter//speed], True, 'white')
        screen.blit(snip, (100, 360))

        pygame.display.flip()
        introbgm.stop()
        sadbgm.play()

def dialogue1v2():
    font = pygame.font.Font('assets/ARCADE.TTF', 24)
    screen = pygame.display.set_mode ([1280, 720])
    timer = pygame.time.Clock()
    messages = ('Whoa! What\'s with the bright light!!!',
                'I can\'t see anything...',
                'It\'s getting brighter!',
                'Nghhh...!!!',
                '...',
                '...',
                '...')
    snip = font.render('', True, 'black')
    counter = 0
    speed = 1
    active_message = 0
    message = messages[active_message]

    run = True
    while run:

        bg = pygame.image.load("assets/blackwhite.jpg")
        scaled_bg = pygame.transform.scale(bg, (1280,720))
        bg_rect = scaled_bg.get_rect(x=0,y=0)

        SCREEN.blit(scaled_bg,bg_rect)

        timer.tick(60)

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
                if active_message == 6:
                    dialogue1v3()

        snip = font.render(message[0:counter//speed], True, 'black')
        screen.blit(snip, (100, 360))

        pygame.display.flip()

def dialogue1v3():
    font = pygame.font.Font('assets/ARCADE.TTF', 24)
    screen = pygame.display.set_mode ([1280, 720])
    timer = pygame.time.Clock()
    messages = ('Hmm...?',
                'W-who\'s that...?',
                'Mysterious Person : How have you been doing... MC...?',
                'H-huh...?',
                'Mysterious Person : I miss you so much...',
                'Mysterious Person : I\'m just hoping that...',
                'Mysterious Person : Everything will be back to normal...',
                'Mysterious Person : But it seems that...',
                'Mysterious Person : I failed to make you live a happy life...',
                'Mysterious Person : I\'m sorry... MC...',
                'Mysterious Person : I\'m so sorry...',
                'Huh? I don\'t understand...?',
                'Mysterious Person : I love you, my dear MC...',
                'W-wait! Who are you?!',
                'H-hey!',
                'Sh*t! The light\'s getting brighter!',
                'Ahhhhh-!',
                '...',
                '...',
                '...',
                '...')
    snip = font.render('', True, 'black')
    counter = 0
    speed = 1
    active_message = 0
    message = messages[active_message]

    run = True
    while run:

        bg = pygame.image.load("assets/white.jpg")
        scaled_bg = pygame.transform.scale(bg, (1280,720))
        bg_rect = scaled_bg.get_rect(x=0,y=0)

        mother = pygame.image.load("assets/mother.png")
        mother_rect = mother.get_rect(x=800,y=100)

        SCREEN.blit(scaled_bg,bg_rect)
        SCREEN.blit(mother,mother_rect)

        timer.tick(60)

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
                if active_message == 20:
                    dialogue2()

        snip = font.render(message[0:counter//speed], True, 'black')
        screen.blit(snip, (100, 360))

        pygame.display.flip()

def dialogue2():
    font = pygame.font.Font('assets/ARCADE.TTF', 24)
    screen = pygame.display.set_mode ([1280, 720])
    timer = pygame.time.Clock()
    messages = ('MC : Huhhhh!?',
                'MC : What was that dream...?',
                'MC : There\'s a silhoutte of a lady inside my dream...',
                'MC : And it seems to know me...?',
                'MC : Ack! My head hurts!',
                'MC : I guess... I\'ll just fill up my belly first.',
                'MC : Hey NPC, wake up...',
                'MC : Today\'s food\'s already been served.',
                'MC : Let\'s go dude.',
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
                if active_message == 9:
                    dialogue3()

        snip = font.render(message[0:counter//speed], True, 'white')
        screen.blit(snip, (280, 570))

        pygame.display.flip()

def dialogue3():
    font = pygame.font.Font('assets/ARCADE.TTF', 24)
    screen = pygame.display.set_mode ([1280, 720])
    timer = pygame.time.Clock()
    messages = ('NPC : Ngh... Don\'t care about me...',
                'NPC : Let me sleep bro...',
                'MC : Come on dude, wake your ahh up!',
                'MC shakes NPC body violently...',
                'NPC : lemme SLEEP BRO!!!',
                'MC : Gahhh!?',
                'NPC : Frickin annoying...',
                'NPC : I\'m in such a good dream, until you ruin it.',
                'NPC : Why must you invite me, could you not...',
                'NPC : ...go on your own...?',
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
                if active_message == 10:
                    choice1()

        snip = font.render(message[0:counter//speed], True, 'white')
        screen.blit(snip, (280, 570))

        pygame.display.flip()
        sadbgm.stop()
        bgmusic.play()

def dialogue4():
    font = pygame.font.Font('assets/ARCADE.TTF', 24)
    screen = pygame.display.set_mode ([1280, 720])
    timer = pygame.time.Clock()
    messages = ('NPC : Self-proclaimed \'good friend\' huh?',
                'NPC : Well... If you ARE a good friend...',
                'NPC : Why up until now, you\'re not considering-' ,
                'NPC : -to help me escape?',
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
                if active_message == 4:
                    dialogue6()

        snip = font.render(message[0:counter//speed], True, 'white')
        screen.blit(snip, (280, 570))

        pygame.display.flip()

def dialogue4v2():
    font = pygame.font.Font('assets/ARCADE.TTF', 24)
    screen = pygame.display.set_mode ([1280, 720])
    timer = pygame.time.Clock()
    messages = ('NPC : Alright bro, c\'mere',
                'MC sits besides NPC and ready to hear what he wanna say.',
                'NPC : Observe your surrounding...' ,
                'NPC : Tell me, is there anyone else in here?',
                'MC : Uhh no?',
                'NPC : Right. It\'s just you and me now.',
                'NPC : And I\'m gonna touch you.',
                'MC : Alright dude-',
                'MC : -what the flip?',
                'NPC : ...',
                'MC : ...',
                'NPC : ...',
                'MC : ...',
                'NPC : ...',
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
                if active_message == 14:
                    choice2()

        snip = font.render(message[0:counter//speed], True, 'white')
        screen.blit(snip, (280, 570))

        pygame.display.flip()

def dialogue5():
    font = pygame.font.Font('assets/ARCADE.TTF', 24)
    screen = pygame.display.set_mode ([1280, 720])
    timer = pygame.time.Clock()
    messages = ('NPC : W-what!? Ugh... I didn\'t ask you to play along!',
                'NPC grabs MC\'s collar and threathened him.',
                'NPC : Come on, can\'t you be a bit serious?',
                'NPC : You don\'t want to piss me off, MC...',
                'NPC : ...or you won\'t make it out of this prison alive.',
                'NPC : Understood?',
                'MC : Y-yes, sir!',
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
                if active_message == 5:
                    dialogue5v2()

        snip = font.render(message[0:counter//speed], True, 'white')
        screen.blit(snip, (280, 570))

        pygame.display.flip()

def dialogue5v2():
    font = pygame.font.Font('assets/ARCADE.TTF', 24)
    screen = pygame.display.set_mode ([1280, 720])
    timer = pygame.time.Clock()
    messages = ('NPC : Yeah... That\'s more like it.',
                'NPC : Rather than wasting time being confused about our-',
                'NPC : -sexual identity...',
                'NPC : Why don\'t you plot out a plan for us to escape?',
                'NPC : We\'ve stuck in this prison for nearly 10 years now...',   
                'NPC : ...and I\'m sure you\'re just as sick of it as I am.',
                'NPC : And the worst thing is, we got imprisoned by-',
                'NPC : -crimes we didn\'t even commit!',
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
                    dialogue6()

        snip = font.render(message[0:counter//speed], True, 'white')
        screen.blit(snip, (280, 570))

        pygame.display.flip()

def dialogue5v3():
    font = pygame.font.Font('assets/ARCADE.TTF', 24)
    screen = pygame.display.set_mode ([1280, 720])
    timer = pygame.time.Clock()
    messages = ('NPC chokeholded MC and covered his mouth.',
                'NPC : Pretend you didn\'t hear what I said-',
                'NPC : -and I\'ll spare you.',
                'MC taps NPC\'s arm, indicating that he understood NPC',
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
                if active_message == 4:
                    dialogue5v2()

        snip = font.render(message[0:counter//speed], True, 'white')
        screen.blit(snip, (280, 570))

        pygame.display.flip()

def dialogue6():
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

def dialogue7():
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
                    pygame.quit()
                    sys.exit()

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
                    dialogue7v2()

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