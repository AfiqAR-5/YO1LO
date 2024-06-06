import pygame, sys
from config import *
from button import Button
from shootgame import *

pygame.init()

pygame.mixer.init()

screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Luna Side Story")

bgsound = pygame.mixer.Sound("assets/gta.wav")
boomsound = pygame.mixer.Sound("assets/shoot_sound.wav")

def mc(xpos, ypos):
     mc = pygame.image.load('assets/mc.png')
     mc_rect = mc.get_rect(x=xpos, y=ypos)

     return SCREEN.blit(mc,mc_rect)

def villain(xpos, ypos):
     villain = pygame.image.load('assets/villain.png')
     villain_rect = villain.get_rect(x=xpos,y=ypos)

     return SCREEN.blit(villain, villain_rect)

def lover(xpos, ypos):
    lover = pygame.image.load('assets/Chapter2/lover2.png')
    lover_rect = lover.get_rect(x=xpos, y=ypos)

    return SCREEN.blit(lover, lover_rect)

def prologuefont(size):
    return pygame.font.Font("assets/Cinzel.ttf", size)

def textbutton_font(size):
    return pygame.font.Font("assets/ARCADE.TTF", size)

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

def chap2_opening():
    timer = pygame.time.Clock()

    run = True
    while run:

        timer.tick(60)

        bg = pygame.image.load('assets/Chapter2/chap2blur.png')
        scaled_bg = pygame.transform.scale(bg, (1280,720))
        bg_rect = scaled_bg.get_rect(x=0,y=0)
        SCREEN.blit(scaled_bg, bg_rect)

        box = pygame.image.load('assets/Play Rect.png')
        scaled_box = pygame.transform.scale(box, (640,240))
        box_rect = scaled_box.get_rect(x=320,y=250)
        SCREEN.blit(scaled_box, box_rect)

        title = prologuefont(40).render("Chapter II", True, "White")
        title_rect = title.get_rect(x=340, y=265)
        SCREEN.blit(title, title_rect)

        head = prologuefont(22).render("Things Are Getting Worse", True, "White")
        head_rect = head.get_rect(x=343, y=320)
        SCREEN.blit(head,head_rect)

        info = textbutton_font(19).render("Somewhere Around New Klang - Abandoned Warehouse - 12:42:30 AM", True, "White")
        info_rect = title.get_rect(x=343, y=450)
        SCREEN.blit(info,info_rect)
        pygame.draw.rect(SCREEN, 'white', (343, 360, 590, 75))

        text1 = prologuefont(13).render("After Luna failed to convince the MC, she was left alone in this warehouse.", True, "black")
        text1_rect = text1.get_rect(x=350, y=370)
        SCREEN.blit(text1,text1_rect)

        text2 = prologuefont(13).render("She is very upset with MC and is thinking about how to overcome the odds.", True, "black")
        text2_rect = text2.get_rect(x=350, y=390)
        SCREEN.blit(text2,text2_rect)

        text2 = prologuefont(13).render("Will Luna's journey end here or will she be able to overcome this obstacle?.....", True, "black")
        text2_rect = text2.get_rect(x=350, y=410)
        SCREEN.blit(text2,text2_rect)

        info = textbutton_font(24).render("(click Enter to continue...)", True, "White")
        info_rect = title.get_rect(x=500, y=600)
        SCREEN.blit(info,info_rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    dialogue1()
                    
        pygame.display.flip()


def dialogue1():

    font = pygame.font.Font('assets/ARCADE.TTF', 24)
    screen = pygame.display.set_mode ([1280, 720])
    timer = pygame.time.Clock()
    messages = ('Luna : ARRRRGGHHHHHHHHHH!!!',
                'Luna : Why is he so stubborn in not believing me?',
                'Luna : What a BASTARD!',
                'Luna : What did he give you-',
                'Luna : -that makes you suck up to him so much?',
                'Luna : Huuuurrrrmmmmmmm!',
                'Luna : I must do something.',
                'Luna : I must come up with a new plan to convince him-',
                'Luna : -that the VILLAIN is the murderer.',
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

        bg = pygame.image.load('assets/Chapter2/chap2.png')
        scaled_bg = pygame.transform.scale(bg, (1280,720))
        bg_rect = scaled_bg.get_rect(x=0,y=0)
        
        textbox = pygame.image.load('assets/textboxlover.png')
        scaled_texbox = pygame.transform.scale(textbox, (850,450))
        textbox_rect = scaled_texbox.get_rect(x=220,y=410)

        screen.blit(scaled_bg, bg_rect)
        PAUSE.update(SCREEN)
        PAUSE.changeColor(MENU_MOUSE_POS)
        lover(475,-0.5)
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
                        choice1()
    
        snip = font.render(message[0:counter//speed], True, 'white')
        screen.blit(snip, (295, 600))

        pygame.display.flip()

def choice1():
    while True:

        timer = pygame.time.Clock()

        bg = pygame.image.load('assets/Chapter2/chap2blur.png')
        scaled_bg = pygame.transform.scale(bg, (1280,720))
        bg_rect = scaled_bg.get_rect(x=0,y=0)

        lover = pygame.image.load('assets/Chapter2/lover2.png')
        scaled_lover = pygame.transform.scale(lover, (330,500))
        lover_rect = scaled_lover.get_rect(x=525,y=120)

        c2 = pygame.image.load('assets/cbutton.png')
        scaled_c2 = pygame.transform.scale(c2, (300,70))
        c2_rect = scaled_c2.get_rect(x=525,y=600)

        SCREEN.blit(scaled_bg, bg_rect)
        SCREEN.blit(scaled_lover, lover_rect)
        SCREEN.blit(scaled_c2, c2_rect)
    

        timer.tick(60)

        MENU_MOUSE_POS = pygame.mouse.get_pos()  #detecting mouse position
        
        CHOICE1 = Button(image=pygame.image.load("assets/transparent.png"), pos=(675, 637), 
                            text_input="GO HOME", font=textbutton_font(21), base_color="black", hovering_color="#FF3131")

        PAUSE = Button(image=pygame.image.load("assets/pause.png"), pos=(50, 50), 
                            text_input="           ", font=textbutton_font(21), base_color="black", hovering_color="#FF3131")

        for button in [CHOICE1,PAUSE]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)

        for event in pygame.event.get():

            if event.type == pygame.QUIT: #if pressing x button on window screen
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if CHOICE1.checkForInput(MENU_MOUSE_POS):
                    chap2_act2()
                if PAUSE.checkForInput(MENU_MOUSE_POS):
                    pausemenu()

            pygame.display.flip()

def chap2_act2():
    timer = pygame.time.Clock()

    run = True
    while run:

        timer.tick(60)

        bg = pygame.image.load('assets/Chapter2/houseloverblur.png')
        scaled_bg = pygame.transform.scale(bg, (1280,720))
        bg_rect = scaled_bg.get_rect(x=0,y=0)
        SCREEN.blit(scaled_bg, bg_rect)

        box = pygame.image.load('assets/Play Rect.png')
        scaled_box = pygame.transform.scale(box, (640,210))
        box_rect = scaled_box.get_rect(x=320,y=250)
        SCREEN.blit(scaled_box, box_rect)

        title = prologuefont(40).render("Chapter II Act 2", True, "White")
        title_rect = title.get_rect(x=340, y=265)
        SCREEN.blit(title, title_rect)

        head = prologuefont(22).render("PLAN A? PLAN B?..... PLAN C?", True, "White")
        head_rect = head.get_rect(x=343, y=320)
        SCREEN.blit(head,head_rect)

        info = textbutton_font(19).render("Damansare Heights - Mansion - 1:05:58 AM", True, "White")
        info_rect = title.get_rect(x=343, y=425)
        SCREEN.blit(info,info_rect)
        pygame.draw.rect(SCREEN, 'white', (343, 360, 590, 45))

        text1 = prologuefont(13).render("Luna seems to have gotten an idea to convince Ieman. Hope still exists for Luna.", True, "black")
        text1_rect = text1.get_rect(x=350, y=362.5)
        SCREEN.blit(text1,text1_rect)

        text2 = prologuefont(13).render("Is the plan devised by Luna able to overcome this problem? STAY TUNED.....", True, "black")
        text2_rect = text2.get_rect(x=350, y=382.5)
        SCREEN.blit(text2,text2_rect)

        info = textbutton_font(24).render("(click Enter to continue...)", True, "White")
        info_rect = title.get_rect(x=500, y=600)
        SCREEN.blit(info,info_rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    dialogue2()
                    
        pygame.display.flip()

def dialogue2():

    font = pygame.font.Font('assets/ARCADE.TTF', 24)
    screen = pygame.display.set_mode ([1280, 720])
    timer = pygame.time.Clock()
    messages = ('Luna : GULPPP... (Drinking Coffee)',
                'Luna : I need to calm my mind.',
                'Luna : SIGHHH... (Take a deep breath)',
                'Luna : <Looking around for Inspiration>',
                'Luna : What\'s so hard for him to believe me?',
                'Luna : How can I convince him?',
                'Luna : I feel like I have an idea.',
                'Luna : I need to think like the VILLAIN.',
                'Luna : Let me make a plan first.',
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

        bg = pygame.image.load('assets/Chapter2/houselover.png')
        scaled_bg = pygame.transform.scale(bg, (1280,720))
        bg_rect = scaled_bg.get_rect(x=0,y=0)

        lover = pygame.image.load('assets/Chapter2/lover4.png')
        scaled_lover = pygame.transform.scale(lover, (330,600))
        lover_rect = scaled_lover.get_rect(x=500,y= -20)
        
        textbox = pygame.image.load('assets/textboxlover.png')
        scaled_texbox = pygame.transform.scale(textbox, (850,450))
        textbox_rect = scaled_texbox.get_rect(x=220,y=410)

        screen.blit(scaled_bg, bg_rect)
        PAUSE.update(SCREEN)
        PAUSE.changeColor(MENU_MOUSE_POS)
        screen.blit(scaled_texbox, textbox_rect)
        SCREEN.blit(scaled_lover, lover_rect)

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
                        choice2()
    
        snip = font.render(message[0:counter//speed], True, 'white')
        screen.blit(snip, (295, 600))

        pygame.display.flip()

def choice2():
    while True:

        timer = pygame.time.Clock()

        current  = textbutton_font(24).render("PLEASE MAKE YOUR CHOICE", True, "White")
        current_rect = current.get_rect(x=485,y=625)

        bg = pygame.image.load('assets/Chapter2/houseloverblur.png')
        scaled_bg = pygame.transform.scale(bg, (1280,720))
        bg_rect = scaled_bg.get_rect(x=0,y=0)

        lover = pygame.image.load('assets/Chapter2/lover4blur.png')
        lover_rect = lover.get_rect(x=470,y=-90)

        textbox = pygame.image.load('assets/textboxlover.png')
        scaled_texbox = pygame.transform.scale(textbox, (850,450))
        textbox_rect = scaled_texbox.get_rect(x=220,y=410)

        c1 = pygame.image.load('assets/cbutton.png')
        scaled_c1 = pygame.transform.scale(c1, (500,70))
        c1_rect = scaled_c1.get_rect(x=400,y=250)

        c2 = pygame.image.load('assets/cbutton.png')
        scaled_c2 = pygame.transform.scale(c2, (500,70))
        c2_rect = scaled_c2.get_rect(x=400,y=435)

        SCREEN.blit(scaled_bg, bg_rect)
        SCREEN.blit(lover, lover_rect)
        SCREEN.blit(scaled_c1, c1_rect)
        SCREEN.blit(scaled_c2, c2_rect)
        SCREEN.blit(scaled_texbox, textbox_rect)
        SCREEN.blit(current, current_rect)

        timer.tick(60)

        MENU_MOUSE_POS = pygame.mouse.get_pos()  #detecting mouse position

        CHOICE1 = Button(image=pygame.image.load("assets/transparent.png"), pos=(650,290), 
                            text_input="PLAN A", font=textbutton_font(30), base_color="black", hovering_color="#FF3131")

        CHOICE2 = Button(image=pygame.image.load("assets/transparent.png"), pos=(650, 475), 
                            text_input="PLAN B", font=textbutton_font(30), base_color="black", hovering_color="#FF3131")

        PAUSE = Button(image=pygame.image.load("assets/pause.png"), pos=(50, 50), 
                            text_input="           ", font=textbutton_font(21), base_color="black", hovering_color="#FF3131")

        for button in [PAUSE,CHOICE1,CHOICE2,]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)

        for event in pygame.event.get():

            if event.type == pygame.QUIT: #if pressing x button on window screen
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if CHOICE1.checkForInput(MENU_MOUSE_POS):
                    print('PLAN A CHOOSED')
                    dialogue3()
                
                if CHOICE2.checkForInput(MENU_MOUSE_POS):
                    print('PLAN B CHOOSED')
                    dialogue3()

                if PAUSE.checkForInput(MENU_MOUSE_POS):
                    pausemenu()

            pygame.display.flip()

    
def dialogue3():

    font = pygame.font.Font('assets/ARCADE.TTF', 24)
    screen = pygame.display.set_mode ([1280, 720])
    timer = pygame.time.Clock()
    messages = ('Luna : I feel like this is a solid idea.',
                'Luna : I hope my plan works this time.',
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

        bg = pygame.image.load('assets/Chapter2/houselover.png')
        scaled_bg = pygame.transform.scale(bg, (1280,720))
        bg_rect = scaled_bg.get_rect(x=0,y=0)

        lover = pygame.image.load('assets/Chapter2/lover4.png')
        scaled_lover = pygame.transform.scale(lover, (330,600))
        lover_rect = scaled_lover.get_rect(x=500,y= -20)
        
        textbox = pygame.image.load('assets/textboxlover.png')
        scaled_texbox = pygame.transform.scale(textbox, (850,450))
        textbox_rect = scaled_texbox.get_rect(x=220,y=410)

        screen.blit(scaled_bg, bg_rect)
        PAUSE.update(SCREEN)
        PAUSE.changeColor(MENU_MOUSE_POS)
        screen.blit(scaled_texbox, textbox_rect)
        SCREEN.blit(scaled_lover, lover_rect)

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
                        dialogue4()
    
        snip = font.render(message[0:counter//speed], True, 'white')
        screen.blit(snip, (295, 600))

        pygame.display.flip()

def dialogue4():

    font = pygame.font.Font('assets/ARCADE.TTF', 24)
    screen = pygame.display.set_mode ([1280, 720])
    timer = pygame.time.Clock()
    messages = ('<BOOM> <BOOM> SOUND OF WINDOW BROKEN!!!',
                'LUNA IS VERY SHOCKED AND PUZZLED!!!',
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

        bg = pygame.image.load('assets/Chapter2/houselover.png')
        scaled_bg = pygame.transform.scale(bg, (1280,720))
        bg_rect = scaled_bg.get_rect(x=0,y=0)

        lover = pygame.image.load('assets/Chapter2/lovershock.png')
        scaled_lover = pygame.transform.scale(lover, (300,330))
        lover_rect = scaled_lover.get_rect(x=500,y=250)
        
        textbox = pygame.image.load('assets/textboxlover.png')
        scaled_texbox = pygame.transform.scale(textbox, (850,450))
        textbox_rect = scaled_texbox.get_rect(x=220,y=410)

        screen.blit(scaled_bg, bg_rect)
        PAUSE.update(SCREEN)
        PAUSE.changeColor(MENU_MOUSE_POS)
        screen.blit(scaled_texbox, textbox_rect)
        SCREEN.blit(scaled_lover, lover_rect)

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
                        dialogue5()
    
        snip = font.render(message[0:counter//speed], True, 'white')
        screen.blit(snip, (295, 600))

        pygame.display.flip()

def dialogue5():

    font = pygame.font.Font('assets/ARCADE.TTF', 24)
    screen = pygame.display.set_mode ([1280, 720])
    timer = pygame.time.Clock()
    messages = ('Luna : WHO THE HECK IS RAIDING MY HOUSE!!!',
                'Luna : CRAZY AS* MOTHERFUC*ER!!!',
                'Luna : Are they trying to kill me?',
                'Luna : I\'m not gonna let those bastards kill me.',
                'Luna : GONNA TEACH THOSE BASTARDS A LESSON!',
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

        bg = pygame.image.load('assets/Chapter2/houselover.png')
        scaled_bg = pygame.transform.scale(bg, (1280,720))
        bg_rect = scaled_bg.get_rect(x=0,y=0)

        lover = pygame.image.load('assets/Chapter2/lover3.png')
        scaled_lover = pygame.transform.scale(lover, (300,330))
        lover_rect = scaled_lover.get_rect(x=500,y=280)
        
        textbox = pygame.image.load('assets/textboxlover.png')
        scaled_texbox = pygame.transform.scale(textbox, (850,450))
        textbox_rect = scaled_texbox.get_rect(x=220,y=410)

        screen.blit(scaled_bg, bg_rect)
        PAUSE.update(SCREEN)
        PAUSE.changeColor(MENU_MOUSE_POS)
        SCREEN.blit(scaled_lover, lover_rect)
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
                        choice3()
    
        snip = font.render(message[0:counter//speed], True, 'white')
        screen.blit(snip, (295, 600))

        pygame.display.flip()

def choice3():
    while True:

        timer = pygame.time.Clock()

        bg = pygame.image.load('assets/Chapter2/gunbackground.png')
        scaled_bg = pygame.transform.scale(bg, (1280,720))
        bg_rect = scaled_bg.get_rect(x=0,y=0)

        lover = pygame.image.load('assets/Chapter2/lover3.png')
        scaled_lover = pygame.transform.scale(lover, (350,450))
        lover_rect = scaled_lover.get_rect(x=525,y=180)

        c2 = pygame.image.load('assets/cbutton.png')
        scaled_c2 = pygame.transform.scale(c2, (300,70))
        c2_rect = scaled_c2.get_rect(x=525,y=600)

        SCREEN.blit(scaled_bg, bg_rect)
        SCREEN.blit(scaled_lover, lover_rect)
        SCREEN.blit(scaled_c2, c2_rect)
        
    

        timer.tick(60)

        MENU_MOUSE_POS = pygame.mouse.get_pos()  #detecting mouse position
        
        CHOICE1 = Button(image=pygame.image.load("assets/transparent.png"), pos=(675, 637), 
                            text_input="PICK A GUN", font=textbutton_font(21), base_color="black", hovering_color="#FF3131")

        PAUSE = Button(image=pygame.image.load("assets/pause.png"), pos=(50, 50), 
                            text_input="           ", font=textbutton_font(21), base_color="black", hovering_color="#FF3131")

        for button in [CHOICE1,PAUSE]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)

        for event in pygame.event.get():

            if event.type == pygame.QUIT: #if pressing x button on window screen
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if CHOICE1.checkForInput(MENU_MOUSE_POS):
                    dialogue6()
                if PAUSE.checkForInput(MENU_MOUSE_POS):
                    pausemenu()

            pygame.display.flip()

def dialogue6():

    font = pygame.font.Font('assets/ARCADE.TTF', 24)
    screen = pygame.display.set_mode ([1280, 720])
    timer = pygame.time.Clock()
    messages = ('Luna : WHO TF IS THERE?',
                'Luna : GET THE FUC* OUT OF MY HOUSE!!!',
                'Luna : OR ELSE I\'LL KILL ALL YOU BASTARDS!',
                'Luna : SHOW ME YOUR FACES!',
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

        bg = pygame.image.load('assets/Chapter2/houselover.png')
        scaled_bg = pygame.transform.scale(bg, (1280,720))
        bg_rect = scaled_bg.get_rect(x=0,y=0)

        lover = pygame.image.load('assets/Chapter2/lover3.png')
        scaled_lover = pygame.transform.scale(lover, (300,330))
        lover_rect = scaled_lover.get_rect(x=500,y=280)
        
        textbox = pygame.image.load('assets/textboxlover.png')
        scaled_texbox = pygame.transform.scale(textbox, (850,450))
        textbox_rect = scaled_texbox.get_rect(x=220,y=410)

        screen.blit(scaled_bg, bg_rect)
        PAUSE.update(SCREEN)
        PAUSE.changeColor(MENU_MOUSE_POS)
        SCREEN.blit(scaled_lover, lover_rect)
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
                        dialogue7()
    
        snip = font.render(message[0:counter//speed], True, 'white')
        screen.blit(snip, (295, 600))

        pygame.display.flip()

def dialogue7():

    font = pygame.font.Font('assets/ARCADE.TTF', 24)
    screen = pygame.display.set_mode ([1280, 720])
    timer = pygame.time.Clock()
    messages = ('Suddenly, five men appear with their mask on...',
                'Luna felt strange with their presence...',
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

        bg = pygame.image.load('assets/Chapter2/houselover.png')
        scaled_bg = pygame.transform.scale(bg, (1280,720))
        bg_rect = scaled_bg.get_rect(x=0,y=0)

        lover = pygame.image.load('assets/Chapter2/robbers.png')
        scaled_lover = pygame.transform.scale(lover, (500,400))
        lover_rect = scaled_lover.get_rect(x=400,y=280)
        
        textbox = pygame.image.load('assets/textboxlover.png')
        scaled_texbox = pygame.transform.scale(textbox, (850,450))
        textbox_rect = scaled_texbox.get_rect(x=220,y=410)

        screen.blit(scaled_bg, bg_rect)
        PAUSE.update(SCREEN)
        PAUSE.changeColor(MENU_MOUSE_POS)
        SCREEN.blit(scaled_lover, lover_rect)
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
                        dialogue8()
    
        snip = font.render(message[0:counter//speed], True, 'white')
        screen.blit(snip, (295, 600))

        pygame.display.flip()

def dialogue8():

    font = pygame.font.Font('assets/ARCADE.TTF', 24)
    screen = pygame.display.set_mode ([1280, 720])
    timer = pygame.time.Clock()
    messages = ('Luna : What the fuc* do you want from me?',
                'Luna : Answer me or I will fuc*king kill you all!',
                'Suddenly, they move aggressively towards Luna...',
                'Luna : Stay the fuc* out of my face!',
                'They didn\'t listen to Luna and starting to grab her...',
                'Luna : FUC*, You all crosed the line, DAMN IT!',
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

        bg = pygame.image.load('assets/Chapter2/houselover.png')
        scaled_bg = pygame.transform.scale(bg, (1280,720))
        bg_rect = scaled_bg.get_rect(x=0,y=0)
       
        lover = pygame.image.load('assets/Chapter2/lover3.png')
        scaled_lover = pygame.transform.scale(lover, (300,330))
        lover_rect = scaled_lover.get_rect(x=500,y=280)
        
        textbox = pygame.image.load('assets/textboxlover.png')
        scaled_texbox = pygame.transform.scale(textbox, (850,450))
        textbox_rect = scaled_texbox.get_rect(x=220,y=410)

        screen.blit(scaled_bg, bg_rect)
        PAUSE.update(SCREEN)
        PAUSE.changeColor(MENU_MOUSE_POS)
        SCREEN.blit(scaled_lover, lover_rect)
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
                        choice4()
    
        snip = font.render(message[0:counter//speed], True, 'white')
        screen.blit(snip, (295, 600))

        pygame.display.flip()

def choice4():
    while True:

        timer = pygame.time.Clock()

        bg = pygame.image.load('assets/Chapter2/houseloverblur.png')
        scaled_bg = pygame.transform.scale(bg, (1280,720))
        bg_rect = scaled_bg.get_rect(x=0,y=0)

        lover = pygame.image.load('assets/Chapter2/lover3.png')
        scaled_lover = pygame.transform.scale(lover, (350,450))
        lover_rect = scaled_lover.get_rect(x=525,y=180)

        c2 = pygame.image.load('assets/cbutton.png')
        scaled_c2 = pygame.transform.scale(c2, (300,70))
        c2_rect = scaled_c2.get_rect(x=525,y=600)

        SCREEN.blit(scaled_bg, bg_rect)
        SCREEN.blit(scaled_lover, lover_rect)
        SCREEN.blit(scaled_c2, c2_rect)
        
        timer.tick(60)

        MENU_MOUSE_POS = pygame.mouse.get_pos()  #detecting mouse position
        
        CHOICE1 = Button(image=pygame.image.load("assets/transparent.png"), pos=(675, 637), 
                            text_input="KILL THEM ALL", font=textbutton_font(21), base_color="black", hovering_color="#FF3131")

        PAUSE = Button(image=pygame.image.load("assets/pause.png"), pos=(50, 50), 
                            text_input="           ", font=textbutton_font(21), base_color="black", hovering_color="#FF3131")

        for button in [CHOICE1,PAUSE]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)

        for event in pygame.event.get():

            if event.type == pygame.QUIT: #if pressing x button on window screen
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if CHOICE1.checkForInput(MENU_MOUSE_POS):
                    shootgame()
                if PAUSE.checkForInput(MENU_MOUSE_POS):
                    pausemenu()

            pygame.display.flip()

choice4()