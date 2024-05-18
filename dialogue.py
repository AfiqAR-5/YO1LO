import pygame, sys
from config import *
from button import Button
pygame.init()

bgmusic = pygame.mixer.Sound("assets/bgmtwo.mp3")

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
                            text_input="I\'m waiting for you baby...", font=textbutton_font(21), base_color="black", hovering_color="#FF3131") #find better colour
        
        CHOICE2 = Button(image=pygame.image.load("assets/transparent.png"), pos=(650, 365), 
                            text_input="Because I\'m such a good friend.", font=textbutton_font(21), base_color="black", hovering_color="#FF3131")

        PAUSE = Button(image=pygame.image.load("assets/pause.png"), pos=(0, 0), 
                            text_input="           ", font=textbutton_font(21), base_color="black", hovering_color="#FF3131")

        for button in [CHOICE1,CHOICE2,PAUSE]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)

        for event in pygame.event.get():

            if event.type == pygame.QUIT: #if pressing x button on window screen
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if CHOICE1.checkForInput(MENU_MOUSE_POS):
                    dialogue4()
                if CHOICE2.checkForInput(MENU_MOUSE_POS):
                    dialogue4v2()
                if PAUSE.checkForInput(MENU_MOUSE_POS):
                    pausemenu()

            pygame.display.flip()

def choice2():

    while True:

        timer = pygame.time.Clock()

        current  = textbutton_font(24).render("NPC : ...I might feel something shoved to my butt...", True, "White")
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
                            text_input="Oh baby come on :3", font=textbutton_font(21), base_color="black", hovering_color="#FF3131") #find better colour
        
        CHOICE2 = Button(image=pygame.image.load("assets/transparent.png"), pos=(650, 365), 
                            text_input="Chill dude I\'m just joking around sheesh...", font=textbutton_font(21), base_color="black", hovering_color="#FF3131")

        PAUSE = Button(image=pygame.image.load("assets/pause.png"), pos=(0, 0), 
                            text_input="           ", font=textbutton_font(21), base_color="black", hovering_color="#FF3131")

        for button in [CHOICE1,CHOICE2,PAUSE]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)

        for event in pygame.event.get():

            if event.type == pygame.QUIT: #if pressing x button on window screen
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if CHOICE1.checkForInput(MENU_MOUSE_POS):
                    dialogue5()
                if CHOICE2.checkForInput(MENU_MOUSE_POS):
                    dialogue5v2()
                if PAUSE.checkForInput(MENU_MOUSE_POS):
                    pausemenu()

            pygame.display.flip()

def choice3():

    while True:

        timer = pygame.time.Clock()

        current  = textbutton_font(24).render("NPC : So, made up your mind?", True, "White")
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
                            text_input="I've made up my mind. I'm gonna be your baby :3", font=textbutton_font(21), base_color="black", hovering_color="#FF3131") #find better colour
        
        CHOICE2 = Button(image=pygame.image.load("assets/transparent.png"), pos=(650, 365), 
                            text_input="...give me some time, would ya?", font=textbutton_font(21), base_color="black", hovering_color="#FF3131")

        PAUSE = Button(image=pygame.image.load("assets/pause.png"), pos=(0, 0), 
                            text_input="           ", font=textbutton_font(21), base_color="black", hovering_color="#FF3131")

        for button in [CHOICE1,CHOICE2,PAUSE]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)

        for event in pygame.event.get():

            if event.type == pygame.QUIT: #if pressing x button on window screen
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if CHOICE1.checkForInput(MENU_MOUSE_POS):
                    dialogue7()
                if CHOICE2.checkForInput(MENU_MOUSE_POS):
                    dialogue7v2()
                if PAUSE.checkForInput(MENU_MOUSE_POS):
                    pausemenu()

            pygame.display.flip()

def dialogue():
    font = pygame.font.Font('assets/ARCADE.TTF', 24)
    screen = pygame.display.set_mode ([1280, 720])
    timer = pygame.time.Clock()
    messages = ('Reality is often dissappointing, isn\'t it?',
                'Imagine going through an exhausting day at school...',
                'Only to witness a tragic massacre of your own family...',
                '...and to be accused of the cruelty.',
                '...')
    snip = font.render('', True, 'white')
    counter = 0
    speed = 1
    active_message = 0
    message = messages[active_message]
    done = False

    run = True
    while run:

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        PAUSE = Button(image=pygame.image.load("assets/pause.png"), pos=(0, 0), 
                            text_input="           ", font=textbutton_font(21), base_color="black", hovering_color="#FF3131")
        
        bg = pygame.image.load('assets/prisoncell.jpg')
        scaled_bg = pygame.transform.scale(bg, (1280,720))
        bg_rect = scaled_bg.get_rect(x=0,y=0)
        
        textbox = pygame.image.load('assets/textbox.png')
        scaled_texbox = pygame.transform.scale(textbox, (850,200))
        textbox_rect = scaled_texbox.get_rect(x=220,y=500)

        screen.blit(scaled_bg, bg_rect)
        screen.blit(scaled_texbox, textbox_rect)
        PAUSE.update(SCREEN)
        PAUSE.changeColor(MENU_MOUSE_POS)
        timer.tick(60)

        if counter < speed * len(message):
            counter += 1
        elif counter >= speed * len(message):
            done = True

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PAUSE.checkForInput(MENU_MOUSE_POS):
                    pausemenu()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN and done and active_message < len(messages) - 1:
                    active_message += 1
                    done = False
                    message = messages[active_message]
                    counter = 0
                if active_message == 4:
                    dialogue2()

        snip = font.render(message[0:counter//speed], True, 'white')
        screen.blit(snip, (280, 570))

        pygame.display.flip()
        bgmusic.play()

def dialogue2():
    font = pygame.font.Font('assets/ARCADE.TTF', 24)
    screen = pygame.display.set_mode ([1280, 720])
    timer = pygame.time.Clock()
    messages = ('This is a story about our MC : (Ieman)',
                'MC : *yawns*',
                'MC : Another day, another shitty meal from the warden',
                'MC : You\'re not going to the cafeteria, NPC?',
                '...')
    snip = font.render('', True, 'white')
    counter = 0
    speed = 1
    active_message = 0
    message = messages[active_message]
    done = False

    run = True
    while run:

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        PAUSE = Button(image=pygame.image.load("assets/pause.png"), pos=(0, 0), 
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
        elif counter >= speed * len(message):
            done = True

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PAUSE.checkForInput(MENU_MOUSE_POS):
                    pausemenu()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN and done and active_message < len(messages) - 1:
                    active_message += 1
                    done = False
                    message = messages[active_message]
                    counter = 0
                if active_message == 4:
                    dialogue3()

        snip = font.render(message[0:counter//speed], True, 'white')
        screen.blit(snip, (280, 570))

        pygame.display.flip()

def dialogue3():
    font = pygame.font.Font('assets/ARCADE.TTF', 24)
    screen = pygame.display.set_mode ([1280, 720])
    timer = pygame.time.Clock()
    messages = ('NPC : Could you not wake me up?',
                'NPC : I\'m in such a good dream, until you ruin it.',
                'NPC : Why must you invite me, could you not...',
                'NPC : ...go on your own...?',
                '...')
    snip = font.render('', True, 'white')
    counter = 0
    speed = 1
    active_message = 0
    message = messages[active_message]
    done = False

    run = True
    while run:

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        PAUSE = Button(image=pygame.image.load("assets/pause.png"), pos=(0, 0), 
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
        elif counter >= speed * len(message):
            done = True

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PAUSE.checkForInput(MENU_MOUSE_POS):
                    pausemenu()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN and done and active_message < len(messages) - 1:
                    active_message += 1
                    done = False
                    message = messages[active_message]
                    counter = 0
                if active_message == 4:
                    choice1()

        snip = font.render(message[0:counter//speed], True, 'white')
        screen.blit(snip, (280, 570))

        pygame.display.flip()

def dialogue4():
    font = pygame.font.Font('assets/ARCADE.TTF', 24)
    screen = pygame.display.set_mode ([1280, 720])
    timer = pygame.time.Clock()
    messages = ('NPC : ...',
                'NPC : ...considering your response...',
                'NPC : ...dont frickin invite me to shower...',
                'NPC : ...I might feel something shoved to my butt...',
                '...')
    snip = font.render('', True, 'white')
    counter = 0
    speed = 1
    active_message = 0
    message = messages[active_message]
    done = False

    run = True
    while run:

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        PAUSE = Button(image=pygame.image.load("assets/pause.png"), pos=(0, 0), 
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
        elif counter >= speed * len(message):
            done = True

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PAUSE.checkForInput(MENU_MOUSE_POS):
                    pausemenu()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN and done and active_message < len(messages) - 1:
                    active_message += 1
                    done = False
                    message = messages[active_message]
                    counter = 0
                if active_message == 4:
                    choice2()

        snip = font.render(message[0:counter//speed], True, 'white')
        screen.blit(snip, (280, 570))

        pygame.display.flip()

def dialogue4v2():
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
    done = False

    run = True
    while run:

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        PAUSE = Button(image=pygame.image.load("assets/pause.png"), pos=(0, 0), 
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
        elif counter >= speed * len(message):
            done = True

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PAUSE.checkForInput(MENU_MOUSE_POS):
                    pausemenu()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN and done and active_message < len(messages) - 1:
                    active_message += 1
                    done = False
                    message = messages[active_message]
                    counter = 0
                if active_message == 4:
                    dialogue6()

        snip = font.render(message[0:counter//speed], True, 'white')
        screen.blit(snip, (280, 570))

        pygame.display.flip()

def dialogue5():
    font = pygame.font.Font('assets/ARCADE.TTF', 24)
    screen = pygame.display.set_mode ([1280, 720])
    timer = pygame.time.Clock()
    messages = ('NPC : Keep this up-',
                'NPC : -and don\'t even consider getting out from this prison.',
                'NPC grabs MC\'s collar and threathened him.',
                'NPC : Understood?',
                'MC : Y-yes, sir!',
                '...')
    snip = font.render('', True, 'white')
    counter = 0
    speed = 1
    active_message = 0
    message = messages[active_message]
    done = False

    run = True
    while run:

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        PAUSE = Button(image=pygame.image.load("assets/pause.png"), pos=(0, 0), 
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
        elif counter >= speed * len(message):
            done = True

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PAUSE.checkForInput(MENU_MOUSE_POS):
                    pausemenu()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN and done and active_message < len(messages) - 1:
                    active_message += 1
                    done = False
                    message = messages[active_message]
                    counter = 0
                if active_message == 5:
                    dialogue5v2()

        snip = font.render(message[0:counter//speed], True, 'white')
        screen.blit(snip, (280, 570))

        pygame.display.flip()

def dialogue5v2():
    font = pygame.font.Font('assets/ARCADE.TTF', 24)
    screen = pygame.display.set_mode ([1280, 720])
    timer = pygame.time.Clock()
    messages = ('NPC : That\'s more like it.',
                'NPC : Rather than wasting your time being confused about your-',
                'NPC : -sexual identity...',
                'NPC : Why don\'t you plot out a plan for us to escape?',
                'NPC : We\'ve stuck in this prison for nearly 10 years now...',   
                'NPC : ...and I\'m sure you\'re just as sick of it as I am.',
                'NPC : And the worst thing is, we got imprisoned by-',
                'NPC : crimes we didn\'t even commit!',
                '...')
    snip = font.render('', True, 'white')
    counter = 0
    speed = 1
    active_message = 0
    message = messages[active_message]
    done = False

    run = True
    while run:

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        PAUSE = Button(image=pygame.image.load("assets/pause.png"), pos=(0, 0), 
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
        elif counter >= speed * len(message):
            done = True

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PAUSE.checkForInput(MENU_MOUSE_POS):
                    pausemenu()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN and done and active_message < len(messages) - 1:
                    active_message += 1
                    done = False
                    message = messages[active_message]
                    counter = 0
                if active_message == 6:
                    dialogue6()

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
    done = False

    run = True
    while run:

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        PAUSE = Button(image=pygame.image.load("assets/pause.png"), pos=(0, 0), 
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
        elif counter >= speed * len(message):
            done = True

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PAUSE.checkForInput(MENU_MOUSE_POS):
                    pausemenu()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN and done and active_message < len(messages) - 1:
                    active_message += 1
                    done = False
                    message = messages[active_message]
                    counter = 0
                if active_message == 4:
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
    done = False

    run = True
    while run:

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        PAUSE = Button(image=pygame.image.load("assets/pause.png"), pos=(0, 0), 
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
        elif counter >= speed * len(message):
            done = True

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PAUSE.checkForInput(MENU_MOUSE_POS):
                    pausemenu()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN and done and active_message < len(messages) - 1:
                    active_message += 1
                    done = False
                    message = messages[active_message]
                    counter = 0
                if active_message == 2:
                    choice3()

        snip = font.render(message[0:counter//speed], True, 'white')
        screen.blit(snip, (280, 570))

        pygame.display.flip()

def blackbox():
    pygame.draw.rect(SCREEN, 'black', [0,0,300,100])

def d7troll():
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
    done = False

    run = True

    while run:

        timer = pygame.time.Clock()

        current  = textbutton_font(24).render("NPC : You\'re being timeout\'d.", True, "White")
        current_rect = current.get_rect(x=280, y=570)

        bg = pygame.image.load('assets/prisoncell.jpg')
        scaled_bg = pygame.transform.scale(bg, (1280,720))
        bg_rect = scaled_bg.get_rect(x=0,y=0)
        
        textbox = pygame.image.load('assets/textbox.png')
        scaled_texbox = pygame.transform.scale(textbox, (850,200))
        textbox_rect = scaled_texbox.get_rect(x=220,y=500)

        SCREEN.blit(scaled_bg, bg_rect)
        mc(270,1)
        walter(670,130)
        SCREEN.blit(scaled_texbox, textbox_rect)
        pygame.draw.rect(SCREEN, 'black', [0,0,300,100])
        SCREEN.blit(current, current_rect)

        timer.tick(60)
        if counter < speed * len(message):
            counter += 1
        elif counter >= speed * len(message):
            done = True

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PAUSE.checkForInput(MENU_MOUSE_POS):
                    pausemenu()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN and done and active_message < len(messages) - 1:
                    active_message += 1
                    done = False
                    message = messages[active_message]
                    counter = 0
                if active_message == 2:
                    choice3()

        snip = font.render(message[0:counter//speed], True, 'white')
        screen.blit(snip, (280, 570))

        pygame.display.flip()


choice1()