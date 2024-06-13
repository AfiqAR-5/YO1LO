import pygame
import random
import sys
from button import Button

pygame.init()
pygame.display.set_caption("YO1LO") #window name

pygame.mixer.music.load('assets/Audio/normalendfight.mp3')  
pygame.mixer.music.play(-1)

screen_width = 1280
screen_height = 720
screen = pygame.display.set_mode((screen_width, screen_height))

font = pygame.font.Font(None, 50)
dialogue_font = pygame.font.Font(None, 36)

white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)

arrow_up_image = pygame.transform.scale(pygame.image.load("assets/up_button.png"), (150,150))
arrow_down_image = pygame.transform.scale(pygame.image.load("assets/down_button.png"), (150,150))
arrow_left_image = pygame.transform.scale(pygame.image.load("assets/left_button.png"), (150,150))
arrow_right_image = pygame.transform.scale(pygame.image.load("assets/right_button.png"), (150,150))

arrow_images = [
    arrow_up_image, arrow_down_image, arrow_left_image, arrow_right_image,
    arrow_up_image, arrow_left_image, arrow_down_image, arrow_right_image,
    arrow_up_image, arrow_down_image, arrow_left_image, arrow_right_image,
    arrow_up_image, arrow_left_image, arrow_down_image
]

background_images_original = [
    'assets/punches/lefthook.png', 'assets/punches/uppercut.png', 'assets/punches/righthook.png', 'assets/punches/lefthook.png',
    'assets/punches/uppercut.png', 'assets/punches/righthook.png', 'assets/punches/uppercut.png', 'assets/punches/lefthook.png',
    'assets/punches/righthook.png', 'assets/punches/uppercut.png', 'assets/punches/righthook.png', 'assets/punches/lefthook.png',
    'assets/punches/uppercut.png', 'assets/punches/righthook.png', 'assets/punches/uppercut.png'
]
background_images_scaled = [pygame.transform.scale(pygame.image.load(image_path), (1280, 720)) for image_path in background_images_original]

def textbutton_font(size):   
    return pygame.font.Font("assets/Font/ARCADE.TTF", size)

def roman(xpos, ypos):
     roman = pygame.image.load('assets/seriousmc.png')
     roman_rect = roman.get_rect(x=xpos, y=ypos)

     return screen.blit(roman,roman_rect)

def lover(xpos, ypos):
    lover = pygame.image.load('assets/Chapter2/lover2.png')
    lover_rect = lover.get_rect(x=xpos, y=ypos)

    return screen.blit(lover, lover_rect)

def nurse(xpos, ypos):
     nurse = pygame.image.load('assets/countrynurse.png')
     nurse_rect = nurse.get_rect(x=xpos, y=ypos)

     return screen.blit(nurse,nurse_rect)

def doctor(xpos, ypos):
     doctor = pygame.image.load('assets/countrydoc.png')
     doctor_rect = doctor.get_rect(x=xpos, y=ypos)

     return screen.blit(doctor ,doctor_rect)

def create_random_button():
    button_width = 150
    button_height = 115
    x_pos = random.randint(button_width // 2, screen_width - button_width // 2)
    y_pos = random.randint(button_height // 2, screen_height - button_height // 2)
    button = Button(image=arrow_up_image, pos=(x_pos, y_pos), text_input=None, font=font, base_color=white, hovering_color=red)
    return button

def draw_text(text, font, color, surface, x, y, alpha=255):
    text_obj = font.render(text, True, color)
    text_obj.set_alpha(alpha)
    text_rect = text_obj.get_rect()
    text_rect.center = (x, y)
    surface.blit(text_obj, text_rect)

def retry_screen():
    pygame.mixer.music.load('assets/Audio/retry.mp3')
    pygame.mixer.music.play()
    retry_background_image = pygame.image.load("assets/blackscreen.png")
    retry_alpha = 0
    font = pygame.font.Font("assets/Font/ARCADE.TTF", 46)  
    text1 = "You have been knocked out.."
    text2 = "Would you like to retry?"
    text3 = "Press Enter"
    text_height = font.size(" ")[1]  

    while retry_alpha < 255:
        screen.fill(black)
        retry_background_image.set_alpha(retry_alpha)
        screen.blit(retry_background_image, (0, 0))
        draw_text(text1, font, red, screen, screen_width // 2, screen_height // 2 - text_height, alpha=retry_alpha)
        draw_text(text2, font, white, screen, screen_width // 2, screen_height // 2, alpha=retry_alpha)
        draw_text(text3, font, white, screen, screen_width // 2, screen_height // 2 + text_height, alpha=retry_alpha)
        pygame.display.flip()
        pygame.time.delay(10)
        retry_alpha += 1

    running = True
    while running:
         
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    pygame.mixer.music.load('assets/Audio/normalendfight.mp3')  
                    pygame.mixer.music.play(-1)
                    main()

    pygame.time.delay(500)

def pausemenu():
    run = True

    while run:
        pygame.mixer.music.pause()

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        bg = pygame.image.load('assets/background.png')
        scaled_bg = pygame.transform.scale(bg, (1280,720))
        bg_rect = scaled_bg.get_rect(x=0,y=0)
        
        pmenu = pygame.image.load('assets/Play Rect.png')
        scaled_pmenu = pygame.transform.scale(pmenu, (1280,720))
        pmenu_rect = scaled_pmenu.get_rect(x=0,y=0)

        screen.blit(scaled_bg, bg_rect)
        screen.blit(scaled_pmenu, pmenu_rect)

        RESUME = Button(image=pygame.image.load("assets/transparent.png"), pos=(640, 300), 
                            text_input="RESUME", font=textbutton_font(100), base_color="white", hovering_color="red") #find better colour
        
        QUIT = Button(image=pygame.image.load("assets/transparent.png"), pos=(640, 500), 
                            text_input="QUIT", font=textbutton_font(100), base_color="white", hovering_color="red")
        
        for button in [RESUME,QUIT]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(screen)

        for event in pygame.event.get():

            if event.type == pygame.QUIT: #if pressing x button on window screen
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if RESUME.checkForInput(MENU_MOUSE_POS):
                    run = False
                    pygame.mixer.music.unpause()
                if QUIT.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.flip()

def fightdialogue1():   # roman textbox
    font = pygame.font.Font("assets/Font/ARCADE.TTF", 24)
    timer = pygame.time.Clock()
    messages = ('Roman : Why!!!!!!!!',
                'Roman : Why did you kill him !!!!!!',
                "Roman : He was going to give me my answer!",
                "Roman : About everything that happened that night!!",
                "...")
    snip = font.render('', True, white)
    counter = 0
    speed = 1
    active_message = 0
    message = messages[active_message]
    continue_button_press = False

    run = True
    while run:
        MENU_MOUSE_POS = pygame.mouse.get_pos()

        PAUSE = Button(image=pygame.image.load("assets/pause.png"), pos=(50, 50), 
                            text_input="           ", font=textbutton_font(21), base_color="black", hovering_color="#FF3131")

        bg = pygame.image.load('assets/background2.png')
        scaled_bg = pygame.transform.scale(bg, (1280,720))
        bg_rect = scaled_bg.get_rect(x=0,y=0)
        
        textbox = pygame.image.load('assets/textbox.png')
        scaled_texbox = pygame.transform.scale(textbox, (850,250))
        textbox_rect = scaled_texbox.get_rect(x=220,y=475)

        screen.blit(scaled_bg, bg_rect)
        PAUSE.update(screen)
        PAUSE.changeColor(MENU_MOUSE_POS)
        roman(475,-0.5)
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
                    if active_message == 4:               # adjust sini kalau ada byk message
                        continue_button_press = True
                if continue_button_press:
                    return

        snip = font.render(message[0:counter//speed], True, 'white')
        screen.blit(snip, (275, 570))

        pygame.display.flip()

def fightdialogue2():  # black/narrator textbox
    font = pygame.font.Font("assets/Font/ARCADE.TTF", 24)
    timer = pygame.time.Clock()
    messages = ('In the midst of his barrage of fists',
                'I couldn\'t help but feel-',
                'that maybe he was right..',
                'maybe..',
                'murder wasn\'t the answer..',
                'but I can\'t take the chance.',
                'There\'s no way I could let that man live..',
                "...")
    snip = font.render('', True, white)
    counter = 0
    speed = 1
    active_message = 0
    message = messages[active_message]
    continue_button_press = False

    dialogue_box_width = 1160  
    dialogue_box_height = 200  
    dialogue_box_alpha = 225

    run = True
    while run:
        MENU_MOUSE_POS = pygame.mouse.get_pos()

        PAUSE = Button(image=pygame.image.load("assets/pause.png"), pos=(50, 50), 
                            text_input="           ", font=textbutton_font(21), base_color="black", hovering_color="#FF3131")

        bg_image = pygame.image.load("assets/background2.png")
        screen.blit(bg_image, (0, 0))

        PAUSE.update(screen)
        PAUSE.changeColor(MENU_MOUSE_POS)

        dialog_x = (screen.get_width() - dialogue_box_width) // 2
        dialog_y = (screen.get_height() - dialogue_box_height) - 25    # adjust dialogue box sini

        dialogue_box = pygame.Surface((dialogue_box_width, dialogue_box_height), pygame.SRCALPHA)
        dialogue_box.fill((0, 0, 0, dialogue_box_alpha))

        screen.blit(dialogue_box, (dialog_x, dialog_y))

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
                    if active_message == 7:               # adjust sini kalau ada byk message
                        continue_button_press = True
                if continue_button_press:
                    return

        snip = font.render(message[0:counter // speed], True, white)
        screen.blit(snip, (dialog_x + 50, dialog_y + 30))  # adjust text pos sini

        pygame.display.flip()

def fightdialogue3():   # roman textbox
    font = pygame.font.Font("assets/Font/ARCADE.TTF", 24)
    timer = pygame.time.Clock()
    messages = ('Roman : Why!!!!!!!!',
                'Roman : Why must you always get in my way like this !!!!!!',
                "Roman : LUUNAAAAAA !!!!!!",
                "...")
    snip = font.render('', True, white)
    counter = 0
    speed = 1
    active_message = 0
    message = messages[active_message]
    continue_button_press = False

    run = True
    while run:
        MENU_MOUSE_POS = pygame.mouse.get_pos()

        PAUSE = Button(image=pygame.image.load("assets/pause.png"), pos=(50, 50), 
                            text_input="           ", font=textbutton_font(21), base_color="black", hovering_color="#FF3131")

        bg = pygame.image.load('assets/background2.png')
        scaled_bg = pygame.transform.scale(bg, (1280,720))
        bg_rect = scaled_bg.get_rect(x=0,y=0)
        
        textbox = pygame.image.load('assets/textbox.png')
        scaled_texbox = pygame.transform.scale(textbox, (850,250))
        textbox_rect = scaled_texbox.get_rect(x=220,y=475)

        screen.blit(scaled_bg, bg_rect)
        PAUSE.update(screen)
        PAUSE.changeColor(MENU_MOUSE_POS)
        roman(475,-0.5)
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
                    if active_message == 3:               # adjust sini kalau ada byk message
                        continue_button_press = True
                if continue_button_press:
                    return

        snip = font.render(message[0:counter//speed], True, 'white')
        screen.blit(snip, (275, 570))

        pygame.display.flip()

def dialogue1():  # black/narrator textbox
    font = pygame.font.Font("assets/Font/ARCADE.TTF", 24)
    timer = pygame.time.Clock()
    messages = ('*POOOOOW*',
                '...')
    snip = font.render('', True, white)
    counter = 0
    speed = 1
    active_message = 0
    message = messages[active_message]
    continue_button_press = False

    dialogue_box_width = 1160  
    dialogue_box_height = 200  
    dialogue_box_alpha = 225   

    run = True
    while run:
        bg_image = pygame.image.load("assets/punches/lefthook.png")
        screen.blit(bg_image, (0, 0))

        dialog_x = (screen.get_width() - dialogue_box_width) // 2
        dialog_y = (screen.get_height() - dialogue_box_height) - 25    # adjust dialogue box sini

        dialogue_box = pygame.Surface((dialogue_box_width, dialogue_box_height), pygame.SRCALPHA)
        dialogue_box.fill((0, 0, 0, dialogue_box_alpha))

        screen.blit(dialogue_box, (dialog_x, dialog_y))

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
                    if active_message == 1:               # adjust sini kalau ada byk message
                        continue_button_press = True
                        dialogue2()
                if continue_button_press:
                    return

        snip = font.render(message[0:counter // speed], True, white)
        screen.blit(snip, (dialog_x + 50, dialog_y + 30))  # adjust text pos sini

        pygame.display.flip()

def dialogue2():  # pygame time delay not working
    bg_image = pygame.image.load("assets/blackscreen.png")
    start_time = pygame.time.get_ticks()  
    pygame.mixer.music.pause()
    pygame.mixer.music.load("assets/Audio/normalendsad.mp3")

    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.blit(bg_image, (0, 0))

        if pygame.time.get_ticks() - start_time >= 4000:
            pygame.mixer.music.play(-1)
            dialogue3()
            return 
        
        pygame.display.flip()

def dialogue3():  # black/narrator textbox
    font = pygame.font.Font("assets/Font/ARCADE.TTF", 24)
    timer = pygame.time.Clock()
    messages = ('.....',
                '.....',
                '.....',
                '...',)
    snip = font.render('', True, white)
    counter = 0
    speed = 1
    active_message = 0
    message = messages[active_message]
    continue_button_press = False
    dialogue_box_width = 1160  
    dialogue_box_height = 200  
    dialogue_box_alpha = 225   

    run = True
    while run:
        bg_image = pygame.image.load("assets/background2.png")
        screen.blit(bg_image, (0, 0))

        dialog_x = (screen.get_width() - dialogue_box_width) // 2
        dialog_y = (screen.get_height() - dialogue_box_height) - 25    # adjust dialogue box sini

        dialogue_box = pygame.Surface((dialogue_box_width, dialogue_box_height), pygame.SRCALPHA)
        dialogue_box.fill((0, 0, 0, dialogue_box_alpha))

        screen.blit(dialogue_box, (dialog_x, dialog_y))

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
                    if active_message == 3:
                        continue_button_press = True               # adjust sini kalau ada byk message
                        dialogue4()
                if continue_button_press:
                    return

        snip = font.render(message[0:counter // speed], True, white)
        screen.blit(snip, (dialog_x + 50, dialog_y + 30))  # adjust text pos sini

        pygame.display.flip()

def dialogue4():   # roman textbox
    font = pygame.font.Font("assets/Font/ARCADE.TTF", 24)
    timer = pygame.time.Clock()
    messages = ('Roman : Luna..?',
                "...")
    snip = font.render('', True, white)
    counter = 0
    speed = 1
    active_message = 0
    message = messages[active_message]
    continue_button_press = False

    run = True
    while run:
        MENU_MOUSE_POS = pygame.mouse.get_pos()

        PAUSE = Button(image=pygame.image.load("assets/pause.png"), pos=(50, 50), 
                            text_input="           ", font=textbutton_font(21), base_color="black", hovering_color="#FF3131")

        bg = pygame.image.load('assets/background2.png')
        scaled_bg = pygame.transform.scale(bg, (1280,720))
        bg_rect = scaled_bg.get_rect(x=0,y=0)
        
        textbox = pygame.image.load('assets/textbox.png')
        scaled_texbox = pygame.transform.scale(textbox, (850,250))
        textbox_rect = scaled_texbox.get_rect(x=220,y=475)

        screen.blit(scaled_bg, bg_rect)
        PAUSE.update(screen)
        PAUSE.changeColor(MENU_MOUSE_POS)
        roman(475,-0.5)
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
                        continue_button_press = True                # adjust sini kalau ada byk message
                        dialogue5()
                if continue_button_press:
                    return

        snip = font.render(message[0:counter//speed], True, 'white')
        screen.blit(snip, (275, 570))

        pygame.display.flip()

def dialogue5():   # lover textbox
    font = pygame.font.Font("assets/Font/ARCADE.TTF", 24)
    timer = pygame.time.Clock()
    messages = ('Luna : It\'s alright..',
                'Luna : Everything\'s fine now..',
                'Luna : It\'s not your fault...',
                '...',
                '...')
    snip = font.render('', True, white)
    counter = 0
    speed = 1
    active_message = 0
    message = messages[active_message]
    continue_button_press = False

    run = True
    while run:
        MENU_MOUSE_POS = pygame.mouse.get_pos()

        PAUSE = Button(image=pygame.image.load("assets/pause.png"), pos=(50, 50), 
                            text_input="           ", font=textbutton_font(21), base_color="black", hovering_color="#FF3131")

        bg = pygame.image.load('assets/background2.png')
        scaled_bg = pygame.transform.scale(bg, (1280,720))
        bg_rect = scaled_bg.get_rect(x=0,y=0)
        
        textbox = pygame.image.load('assets/textboxlover.png')
        scaled_texbox = pygame.transform.scale(textbox, (850,450))
        textbox_rect = scaled_texbox.get_rect(x=220,y=410)

        screen.blit(scaled_bg, bg_rect)
        PAUSE.update(screen)
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
                    if active_message == 4:               # adjust sini kalau ada byk message
                        continue_button_press = True
                        dialogue6()
                if continue_button_press:
                    return

        snip = font.render(message[0:counter//speed], True, 'white')
        screen.blit(snip, (295, 600))

        pygame.display.flip()

def dialogue6():   # roman textbox
    font = pygame.font.Font("assets/Font/ARCADE.TTF", 24)
    timer = pygame.time.Clock()
    messages = ('Roman : LUNA !!',
                'Roman : Oh god...',
                'Roman : You\'re bleeding!',
                'Roman : I\'m so sorry!',
                'Roman : Luna, I\'ll bring you to a hospital',
                'Roman : So please, bear with me..',
                '...')
    snip = font.render('', True, white)
    counter = 0
    speed = 1
    active_message = 0
    message = messages[active_message]
    continue_button_press = False

    run = True
    while run:
        MENU_MOUSE_POS = pygame.mouse.get_pos()

        PAUSE = Button(image=pygame.image.load("assets/pause.png"), pos=(50, 50), 
                            text_input="           ", font=textbutton_font(21), base_color="black", hovering_color="#FF3131")

        bg = pygame.image.load('assets/background2.png')
        scaled_bg = pygame.transform.scale(bg, (1280,720))
        bg_rect = scaled_bg.get_rect(x=0,y=0)
        
        textbox = pygame.image.load('assets/textbox.png')
        scaled_texbox = pygame.transform.scale(textbox, (850,250))
        textbox_rect = scaled_texbox.get_rect(x=220,y=475)

        screen.blit(scaled_bg, bg_rect)
        PAUSE.update(screen)
        PAUSE.changeColor(MENU_MOUSE_POS)
        roman(475,-0.5)
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
                        continue_button_press = True                # adjust sini kalau ada byk message
                        dialogue7()
                if continue_button_press:
                    return

        snip = font.render(message[0:counter//speed], True, 'white')
        screen.blit(snip, (275, 570))

        pygame.display.flip()

def dialogue7():  # black/narrator textbox
    font = pygame.font.Font("assets/Font/ARCADE.TTF", 24)
    timer = pygame.time.Clock()
    messages = ('Roman picked up Luna-',
                'and began to run in a direction he picked randomly',
                'hoping that-',
                'wherever he might end up..',
                'maybe..',
                'maybe a hospital, or a clinic..',
                'atleast, that way he can get some help.',
                "...")
    snip = font.render('', True, white)
    counter = 0
    speed = 1
    active_message = 0
    message = messages[active_message]
    continue_button_press = False

    dialogue_box_width = 1160  
    dialogue_box_height = 200  
    dialogue_box_alpha = 225

    run = True
    while run:
        MENU_MOUSE_POS = pygame.mouse.get_pos()

        PAUSE = Button(image=pygame.image.load("assets/pause.png"), pos=(50, 50), 
                            text_input="           ", font=textbutton_font(21), base_color="black", hovering_color="#FF3131")

        bg_image = pygame.image.load("assets/bgspeedlines.png")
        screen.blit(bg_image, (0, 0))

        PAUSE.update(screen)
        PAUSE.changeColor(MENU_MOUSE_POS)

        dialog_x = (screen.get_width() - dialogue_box_width) // 2
        dialog_y = (screen.get_height() - dialogue_box_height) - 25    # adjust dialogue box sini

        dialogue_box = pygame.Surface((dialogue_box_width, dialogue_box_height), pygame.SRCALPHA)
        dialogue_box.fill((0, 0, 0, dialogue_box_alpha))

        screen.blit(dialogue_box, (dialog_x, dialog_y))

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
                    if active_message == 7:               # adjust sini kalau ada byk message
                        continue_button_press = True
                        dialogue8()
                if continue_button_press:
                    return

        snip = font.render(message[0:counter // speed], True, white)
        screen.blit(snip, (dialog_x + 50, dialog_y + 30))  # adjust text pos sini

        pygame.display.flip()

def dialogue8():   # roman textbox
    font = pygame.font.Font("assets/Font/ARCADE.TTF", 24)
    timer = pygame.time.Clock()
    messages = ('Roman : Please..',
                'Roman : Please for the love of god..',
                'Roman : PLEASE, HELP! ANYONE!!!!',
                'Roman : Luna, please hang in there',
                'Roman : I will make sure you get some help',
                '...')
    snip = font.render('', True, white)
    counter = 0
    speed = 1
    active_message = 0
    message = messages[active_message]
    continue_button_press = False

    run = True
    while run:
        MENU_MOUSE_POS = pygame.mouse.get_pos()

        PAUSE = Button(image=pygame.image.load("assets/pause.png"), pos=(50, 50), 
                            text_input="           ", font=textbutton_font(21), base_color="black", hovering_color="#FF3131")

        bg = pygame.image.load('assets/bgspeedlines.png')
        scaled_bg = pygame.transform.scale(bg, (1280,720))
        bg_rect = scaled_bg.get_rect(x=0,y=0)
        
        textbox = pygame.image.load('assets/textbox.png')
        scaled_texbox = pygame.transform.scale(textbox, (850,250))
        textbox_rect = scaled_texbox.get_rect(x=220,y=475)

        screen.blit(scaled_bg, bg_rect)
        PAUSE.update(screen)
        PAUSE.changeColor(MENU_MOUSE_POS)
        roman(475,-0.5)
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
                        continue_button_press = True                # adjust sini kalau ada byk message
                        dialogue9()
                if continue_button_press:
                    return

        snip = font.render(message[0:counter//speed], True, 'white')
        screen.blit(snip, (275, 570))

        pygame.display.flip()

def dialogue9():  # black/narrator textbox
    font = pygame.font.Font("assets/Font/ARCADE.TTF", 24)
    timer = pygame.time.Clock()
    messages = ('Where he ran..',
                'Where he might end up..',
                'He knows not..',
                'He only knows that all he can do now..',
                'All he can do to prevent tragedy from happening..',
                'is to keep running',
                '...')
    snip = font.render('', True, white)
    counter = 0
    speed = 1
    active_message = 0
    message = messages[active_message]
    continue_button_press = False

    dialogue_box_width = 1160  
    dialogue_box_height = 200  
    dialogue_box_alpha = 225

    run = True
    while run:
        MENU_MOUSE_POS = pygame.mouse.get_pos()

        PAUSE = Button(image=pygame.image.load("assets/pause.png"), pos=(50, 50), 
                            text_input="           ", font=textbutton_font(21), base_color="black", hovering_color="#FF3131")

        bg_image = pygame.image.load("assets/bgspeedlines.png")
        screen.blit(bg_image, (0, 0))

        PAUSE.update(screen)
        PAUSE.changeColor(MENU_MOUSE_POS)

        dialog_x = (screen.get_width() - dialogue_box_width) // 2
        dialog_y = (screen.get_height() - dialogue_box_height) - 25    # adjust dialogue box sini

        dialogue_box = pygame.Surface((dialogue_box_width, dialogue_box_height), pygame.SRCALPHA)
        dialogue_box.fill((0, 0, 0, dialogue_box_alpha))

        screen.blit(dialogue_box, (dialog_x, dialog_y))

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
                    if active_message == 6:               # adjust sini kalau ada byk message
                        continue_button_press = True
                        dialogue10()
                if continue_button_press:
                    return

        snip = font.render(message[0:counter // speed], True, white)
        screen.blit(snip, (dialog_x + 50, dialog_y + 30))  # adjust text pos sini

        pygame.display.flip()

def dialogue10():  # black/narrator textbox
    font = pygame.font.Font("assets/Font/ARCADE.TTF", 24)
    timer = pygame.time.Clock()
    messages = ('Then..',
                'As if a miracle had occured..',
                'As if his prayers were being answered..',
                'At the edge of the forest..',
                'he saw a shape of a building..',
                '...')
    snip = font.render('', True, white)
    counter = 0
    speed = 1
    active_message = 0
    message = messages[active_message]
    continue_button_press = False

    dialogue_box_width = 1160  
    dialogue_box_height = 200  
    dialogue_box_alpha = 225

    run = True
    while run:
        MENU_MOUSE_POS = pygame.mouse.get_pos()

        PAUSE = Button(image=pygame.image.load("assets/pause.png"), pos=(50, 50), 
                            text_input="           ", font=textbutton_font(21), base_color="black", hovering_color="#FF3131")

        bg_image = pygame.image.load("assets/bgspeedlines2.png")
        screen.blit(bg_image, (0, 0))

        PAUSE.update(screen)
        PAUSE.changeColor(MENU_MOUSE_POS)

        dialog_x = (screen.get_width() - dialogue_box_width) // 2
        dialog_y = (screen.get_height() - dialogue_box_height) - 25    # adjust dialogue box sini

        dialogue_box = pygame.Surface((dialogue_box_width, dialogue_box_height), pygame.SRCALPHA)
        dialogue_box.fill((0, 0, 0, dialogue_box_alpha))

        screen.blit(dialogue_box, (dialog_x, dialog_y))

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
                    if active_message == 5:               # adjust sini kalau ada byk message
                        continue_button_press = True
                        dialogue11()
                if continue_button_press:
                    return

        snip = font.render(message[0:counter // speed], True, white)
        screen.blit(snip, (dialog_x + 50, dialog_y + 30))  # adjust text pos sini

        pygame.display.flip()

def dialogue11():  # black/narrator textbox
    font = pygame.font.Font("assets/Font/ARCADE.TTF", 24)
    timer = pygame.time.Clock()
    messages = ('What came into view',
                'was what looks like a clinic',
                'an old run-down countryside clinic',
                'Roman doesn\'t know whether it still runs or not',
                'All he knows...',
                'Is that help is here!',
                '...')
    snip = font.render('', True, white)
    counter = 0
    speed = 1
    active_message = 0
    message = messages[active_message]
    continue_button_press = False

    dialogue_box_width = 1160  
    dialogue_box_height = 200  
    dialogue_box_alpha = 225

    run = True
    while run:
        MENU_MOUSE_POS = pygame.mouse.get_pos()

        PAUSE = Button(image=pygame.image.load("assets/pause.png"), pos=(50, 50), 
                            text_input="           ", font=textbutton_font(21), base_color="black", hovering_color="#FF3131")

        bg = pygame.image.load('assets/countryhosp.png')
        scaled_bg = pygame.transform.scale(bg, (1280,720))
        bg_rect = scaled_bg.get_rect(x=0,y=0)
        screen.blit(scaled_bg, bg_rect)

        PAUSE.update(screen)
        PAUSE.changeColor(MENU_MOUSE_POS)

        dialog_x = (screen.get_width() - dialogue_box_width) // 2
        dialog_y = (screen.get_height() - dialogue_box_height) - 25    # adjust dialogue box sini

        dialogue_box = pygame.Surface((dialogue_box_width, dialogue_box_height), pygame.SRCALPHA)
        dialogue_box.fill((0, 0, 0, dialogue_box_alpha))

        screen.blit(dialogue_box, (dialog_x, dialog_y))

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
                    if active_message == 6:               # adjust sini kalau ada byk message
                        continue_button_press = True
                        dialogue12()
                if continue_button_press:
                    return

        snip = font.render(message[0:counter // speed], True, white)
        screen.blit(snip, (dialog_x + 50, dialog_y + 30))  # adjust text pos sini

        pygame.display.flip()

def dialogue12():   # roman textbox
    font = pygame.font.Font("assets/Font/ARCADE.TTF", 24)
    timer = pygame.time.Clock()
    messages = ('Roman : HELP!!',
                'Roman : HELP PLEASE!!',
                'Roman : SOMEONE\'S UNCONSCIOUS!!',
                'Roman : IS ANYONE THERE?!?!',
                '...')
    snip = font.render('', True, white)
    counter = 0
    speed = 1
    active_message = 0
    message = messages[active_message]
    continue_button_press = False

    run = True
    while run:
        MENU_MOUSE_POS = pygame.mouse.get_pos()

        PAUSE = Button(image=pygame.image.load("assets/pause.png"), pos=(50, 50), 
                            text_input="           ", font=textbutton_font(21), base_color="black", hovering_color="#FF3131")

        bg = pygame.image.load('assets/countryhosp.png')
        scaled_bg = pygame.transform.scale(bg, (1280,720))
        bg_rect = scaled_bg.get_rect(x=0,y=0)
        
        textbox = pygame.image.load('assets/textbox.png')
        scaled_texbox = pygame.transform.scale(textbox, (850,250))
        textbox_rect = scaled_texbox.get_rect(x=220,y=475)

        screen.blit(scaled_bg, bg_rect)
        PAUSE.update(screen)
        PAUSE.changeColor(MENU_MOUSE_POS)
        roman(475,-0.5)
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
                        continue_button_press = True                # adjust sini kalau ada byk message
                        dialogue13()
                if continue_button_press:
                    return

        snip = font.render(message[0:counter//speed], True, 'white')
        screen.blit(snip, (275, 570))

        pygame.display.flip()

def dialogue13():  # black/narrator textbox
    font = pygame.font.Font("assets/Font/ARCADE.TTF", 24)
    timer = pygame.time.Clock()
    messages = ('Frantically knocking on the door',
                'He hoped that someone would answer..',
                'Begged even..',
                'All that was going through his mind was',
                'PLEASE SOMEONE ANSWER THE DOOR',
                '...')
    snip = font.render('', True, white)
    counter = 0
    speed = 1
    active_message = 0
    message = messages[active_message]
    continue_button_press = False

    dialogue_box_width = 1160  
    dialogue_box_height = 200  
    dialogue_box_alpha = 225

    run = True
    while run:
        MENU_MOUSE_POS = pygame.mouse.get_pos()

        PAUSE = Button(image=pygame.image.load("assets/pause.png"), pos=(50, 50), 
                            text_input="           ", font=textbutton_font(21), base_color="black", hovering_color="#FF3131")

        bg = pygame.image.load('assets/countryhosp.png')
        scaled_bg = pygame.transform.scale(bg, (1280,720))
        bg_rect = scaled_bg.get_rect(x=0,y=0)
        screen.blit(scaled_bg, bg_rect)

        PAUSE.update(screen)
        PAUSE.changeColor(MENU_MOUSE_POS)

        dialog_x = (screen.get_width() - dialogue_box_width) // 2
        dialog_y = (screen.get_height() - dialogue_box_height) - 25    # adjust dialogue box sini

        dialogue_box = pygame.Surface((dialogue_box_width, dialogue_box_height), pygame.SRCALPHA)
        dialogue_box.fill((0, 0, 0, dialogue_box_alpha))

        screen.blit(dialogue_box, (dialog_x, dialog_y))

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
                    if active_message == 5:               # adjust sini kalau ada byk message
                        continue_button_press = True
                        dialogue14()
                if continue_button_press:
                    return

        snip = font.render(message[0:counter // speed], True, white)
        screen.blit(snip, (dialog_x + 50, dialog_y + 30))  # adjust text pos sini

        pygame.display.flip()

def dialogue14():  # black/narrator textbox
    font = pygame.font.Font("assets/Font/ARCADE.TTF", 24)
    timer = pygame.time.Clock()
    messages = ('Suddenly, a knock is heard on the door.',
                '"Coming!", a voice responded from behind the door',
                '...')
    snip = font.render('', True, white)
    counter = 0
    speed = 1
    active_message = 0
    message = messages[active_message]
    continue_button_press = False

    dialogue_box_width = 1160  
    dialogue_box_height = 200  
    dialogue_box_alpha = 225

    run = True
    while run:
        MENU_MOUSE_POS = pygame.mouse.get_pos()

        PAUSE = Button(image=pygame.image.load("assets/pause.png"), pos=(50, 50), 
                            text_input="           ", font=textbutton_font(21), base_color="black", hovering_color="#FF3131")

        bg = pygame.image.load('assets/countryhosp.png')
        scaled_bg = pygame.transform.scale(bg, (1280,720))
        bg_rect = scaled_bg.get_rect(x=0,y=0)
        screen.blit(scaled_bg, bg_rect)

        PAUSE.update(screen)
        PAUSE.changeColor(MENU_MOUSE_POS)

        dialog_x = (screen.get_width() - dialogue_box_width) // 2
        dialog_y = (screen.get_height() - dialogue_box_height) - 25    # adjust dialogue box sini

        dialogue_box = pygame.Surface((dialogue_box_width, dialogue_box_height), pygame.SRCALPHA)
        dialogue_box.fill((0, 0, 0, dialogue_box_alpha))

        screen.blit(dialogue_box, (dialog_x, dialog_y))

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
                    if active_message == 2:               # adjust sini kalau ada byk message
                        continue_button_press = True
                        dialogue15()
                if continue_button_press:
                    return

        snip = font.render(message[0:counter // speed], True, white)
        screen.blit(snip, (dialog_x + 50, dialog_y + 30))  # adjust text pos sini

        pygame.display.flip()

def dialogue15():  # black/narrator textbox
    font = pygame.font.Font("assets/Font/ARCADE.TTF", 24)
    timer = pygame.time.Clock()
    messages = ('Nurse : Is something wrong?',
                'A nurse came out',
                'An immense feeling of relief',
                'came over Roman',
                '...')
    snip = font.render('', True, white)
    counter = 0
    speed = 1
    active_message = 0
    message = messages[active_message]
    continue_button_press = False

    dialogue_box_width = 1160  
    dialogue_box_height = 200  
    dialogue_box_alpha = 225

    run = True
    while run:
        MENU_MOUSE_POS = pygame.mouse.get_pos()

        PAUSE = Button(image=pygame.image.load("assets/pause.png"), pos=(50, 50), 
                            text_input="           ", font=textbutton_font(21), base_color="black", hovering_color="#FF3131")

        bg = pygame.image.load('assets/countryhosp.png')
        scaled_bg = pygame.transform.scale(bg, (1280,720))
        bg_rect = scaled_bg.get_rect(x=0,y=0)
        screen.blit(scaled_bg, bg_rect)

        PAUSE.update(screen)
        PAUSE.changeColor(MENU_MOUSE_POS)
        nurse(400, 130)

        dialog_x = (screen.get_width() - dialogue_box_width) // 2
        dialog_y = (screen.get_height() - dialogue_box_height) - 25    # adjust dialogue box sini

        dialogue_box = pygame.Surface((dialogue_box_width, dialogue_box_height), pygame.SRCALPHA)
        dialogue_box.fill((0, 0, 0, dialogue_box_alpha))

        screen.blit(dialogue_box, (dialog_x, dialog_y))

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
                    if active_message == 4:               # adjust sini kalau ada byk message
                        continue_button_press = True
                        dialogue16()
                if continue_button_press:
                    return

        snip = font.render(message[0:counter // speed], True, white)
        screen.blit(snip, (dialog_x + 50, dialog_y + 30))  # adjust text pos sini

        pygame.display.flip()

def dialogue16():   # roman textbox
    font = pygame.font.Font("assets/Font/ARCADE.TTF", 24)
    timer = pygame.time.Clock()
    messages = ('Roman : Please..',
                'Roman : She\'s lost a lot of blood..',
                'Roman : And she\'s losing her consciousness..',
                'Nurse : Alright, I\'ll bring her in to get some proper treatment',
                'Nurse : Fortunately, the doctor\'s still here',
                'Nurse : For now, you can come inside.',
                'Roman : Thank you so much..',
                '...')
    snip = font.render('', True, white)
    counter = 0
    speed = 1
    active_message = 0
    message = messages[active_message]
    continue_button_press = False

    run = True
    while run:
        MENU_MOUSE_POS = pygame.mouse.get_pos()

        PAUSE = Button(image=pygame.image.load("assets/pause.png"), pos=(50, 50), 
                            text_input="           ", font=textbutton_font(21), base_color="black", hovering_color="#FF3131")

        bg = pygame.image.load('assets/countryhosp.png')
        scaled_bg = pygame.transform.scale(bg, (1280,720))
        bg_rect = scaled_bg.get_rect(x=0,y=0)
        
        textbox = pygame.image.load('assets/textbox.png')
        scaled_texbox = pygame.transform.scale(textbox, (850,250))
        textbox_rect = scaled_texbox.get_rect(x=220,y=475)

        screen.blit(scaled_bg, bg_rect)
        PAUSE.update(screen)
        PAUSE.changeColor(MENU_MOUSE_POS)
        roman(175,-0.5)
        nurse(600, 130)
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
                        continue_button_press = True                # adjust sini kalau ada byk message
                        dialogue17()
                if continue_button_press:
                    return

        snip = font.render(message[0:counter//speed], True, 'white')
        screen.blit(snip, (275, 570))

        pygame.display.flip()

def dialogue17():  # black/narrator textbox
    font = pygame.font.Font("assets/Font/ARCADE.TTF", 24)
    timer = pygame.time.Clock()
    messages = ('Nurse : Make yourself comfortable',
                'Nurse : have a sit while I call for the doctor',
                '...')
    snip = font.render('', True, white)
    counter = 0
    speed = 1
    active_message = 0
    message = messages[active_message]
    continue_button_press = False

    dialogue_box_width = 1160  
    dialogue_box_height = 200  
    dialogue_box_alpha = 225

    run = True
    while run:
        MENU_MOUSE_POS = pygame.mouse.get_pos()

        PAUSE = Button(image=pygame.image.load("assets/pause.png"), pos=(50, 50), 
                            text_input="           ", font=textbutton_font(21), base_color="black", hovering_color="#FF3131")

        bg = pygame.image.load('assets/countrynursehosp.png')
        scaled_bg = pygame.transform.scale(bg, (1280,720))
        bg_rect = scaled_bg.get_rect(x=0,y=0)
        screen.blit(scaled_bg, bg_rect)

        PAUSE.update(screen)
        PAUSE.changeColor(MENU_MOUSE_POS)

        dialog_x = (screen.get_width() - dialogue_box_width) // 2
        dialog_y = (screen.get_height() - dialogue_box_height) - 25    # adjust dialogue box sini

        dialogue_box = pygame.Surface((dialogue_box_width, dialogue_box_height), pygame.SRCALPHA)
        dialogue_box.fill((0, 0, 0, dialogue_box_alpha))

        screen.blit(dialogue_box, (dialog_x, dialog_y))

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
                    if active_message == 2:               # adjust sini kalau ada byk message
                        continue_button_press = True
                        dialogue18()
                if continue_button_press:
                    return

        snip = font.render(message[0:counter // speed], True, white)
        screen.blit(snip, (dialog_x + 50, dialog_y + 30))  # adjust text pos sini

        pygame.display.flip()

def dialogue18():  # black/narrator textbox
    font = pygame.font.Font("assets/Font/ARCADE.TTF", 24)
    timer = pygame.time.Clock()
    messages = ('Nurse : Make yourself comfortable',
                'Nurse : have a sit while I call for the doctor',
                '...')
    snip = font.render('', True, white)
    counter = 0
    speed = 1
    active_message = 0
    message = messages[active_message]
    continue_button_press = False

    dialogue_box_width = 1160  
    dialogue_box_height = 200  
    dialogue_box_alpha = 225

    run = True
    while run:
        MENU_MOUSE_POS = pygame.mouse.get_pos()

        PAUSE = Button(image=pygame.image.load("assets/pause.png"), pos=(50, 50), 
                            text_input="           ", font=textbutton_font(21), base_color="black", hovering_color="#FF3131")

        bg = pygame.image.load('assets/countrynursehosp.png')
        scaled_bg = pygame.transform.scale(bg, (1280,720))
        bg_rect = scaled_bg.get_rect(x=0,y=0)
        screen.blit(scaled_bg, bg_rect)

        PAUSE.update(screen)
        PAUSE.changeColor(MENU_MOUSE_POS)

        dialog_x = (screen.get_width() - dialogue_box_width) // 2
        dialog_y = (screen.get_height() - dialogue_box_height) - 25    # adjust dialogue box sini

        dialogue_box = pygame.Surface((dialogue_box_width, dialogue_box_height), pygame.SRCALPHA)
        dialogue_box.fill((0, 0, 0, dialogue_box_alpha))

        screen.blit(dialogue_box, (dialog_x, dialog_y))

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
                    if active_message == 2:               # adjust sini kalau ada byk message
                        continue_button_press = True
                        dialogue19()
                if continue_button_press:
                    return

        snip = font.render(message[0:counter // speed], True, white)
        screen.blit(snip, (dialog_x + 50, dialog_y + 30))  # adjust text pos sini

        pygame.display.flip()

def dialogue19():  # black/narrator textbox
    font = pygame.font.Font("assets/Font/ARCADE.TTF", 24)
    timer = pygame.time.Clock()
    messages = ('Roman, a bit uneasy',
                'figured that the best way to calm down',
                'was to take her up on her offer and sit down',
                'though his mind was racing, he can only wait for the doctor',
                '*AFTER A FEW MINUTES*',
                'The door to the room suddenly opens',
                '...')
    snip = font.render('', True, white)
    counter = 0
    speed = 1
    active_message = 0
    message = messages[active_message]
    continue_button_press = False

    dialogue_box_width = 1160  
    dialogue_box_height = 200  
    dialogue_box_alpha = 225

    run = True
    while run:
        MENU_MOUSE_POS = pygame.mouse.get_pos()

        PAUSE = Button(image=pygame.image.load("assets/pause.png"), pos=(50, 50), 
                            text_input="           ", font=textbutton_font(21), base_color="black", hovering_color="#FF3131")

        bg = pygame.image.load('assets/countryhosp2.png')
        scaled_bg = pygame.transform.scale(bg, (1280,720))
        bg_rect = scaled_bg.get_rect(x=0,y=0)
        screen.blit(scaled_bg, bg_rect)

        PAUSE.update(screen)
        PAUSE.changeColor(MENU_MOUSE_POS)

        dialog_x = (screen.get_width() - dialogue_box_width) // 2
        dialog_y = (screen.get_height() - dialogue_box_height) - 25    # adjust dialogue box sini

        dialogue_box = pygame.Surface((dialogue_box_width, dialogue_box_height), pygame.SRCALPHA)
        dialogue_box.fill((0, 0, 0, dialogue_box_alpha))

        screen.blit(dialogue_box, (dialog_x, dialog_y))

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
                    if active_message == 6:               # adjust sini kalau ada byk message
                        continue_button_press = True
                        dialogue20()
                if continue_button_press:
                    return

        snip = font.render(message[0:counter // speed], True, white)
        screen.blit(snip, (dialog_x + 50, dialog_y + 30))  # adjust text pos sini

        pygame.display.flip()

def dialogue20():  # black/narrator textbox
    font = pygame.font.Font("assets/Font/ARCADE.TTF", 24)
    timer = pygame.time.Clock()
    messages = ('A long haired person walks into the room',
                'They made their approach to Roman',
                'Doctor : Are you the one who brought in the girl?',
                'Roman was taken aback',
                '...')
    snip = font.render('', True, white)
    counter = 0
    speed = 1
    active_message = 0
    message = messages[active_message]
    continue_button_press = False

    dialogue_box_width = 1160  
    dialogue_box_height = 200  
    dialogue_box_alpha = 225

    run = True
    while run:
        MENU_MOUSE_POS = pygame.mouse.get_pos()

        PAUSE = Button(image=pygame.image.load("assets/pause.png"), pos=(50, 50), 
                            text_input="           ", font=textbutton_font(21), base_color="black", hovering_color="#FF3131")

        bg = pygame.image.load('assets/countryhosp2.png')
        scaled_bg = pygame.transform.scale(bg, (1280,720))
        bg_rect = scaled_bg.get_rect(x=0,y=0)
        screen.blit(scaled_bg, bg_rect)

        PAUSE.update(screen)
        PAUSE.changeColor(MENU_MOUSE_POS)
        doctor(380 , 85)

        dialog_x = (screen.get_width() - dialogue_box_width) // 2
        dialog_y = (screen.get_height() - dialogue_box_height) - 25    # adjust dialogue box sini

        dialogue_box = pygame.Surface((dialogue_box_width, dialogue_box_height), pygame.SRCALPHA)
        dialogue_box.fill((0, 0, 0, dialogue_box_alpha))

        screen.blit(dialogue_box, (dialog_x, dialog_y))

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
                    if active_message == 4:               # adjust sini kalau ada byk message
                        continue_button_press = True
                        dialogue21()
                if continue_button_press:
                    return

        snip = font.render(message[0:counter // speed], True, white)
        screen.blit(snip, (dialog_x + 50, dialog_y + 30))  # adjust text pos sini

        pygame.display.flip()

def dialogue21():   # roman textbox
    font = pygame.font.Font("assets/Font/ARCADE.TTF", 24)
    timer = pygame.time.Clock()
    messages = ('Roman : Yes I am..',
                'Roman : How\'s her condition..?',
                'Doctor : She seems fine for now',
                'Doctor : The bleeding\'s stopped and she only have a bruise on her face',
                'Doctor : If I may..',
                'Doctor : Can I ask exactly what happened to her?',
                'Roman : ...',
                'Roman : I\'m sorry..',
                'Roman : It\'s a long story..',
                'Doctor : I\'m sure it is.',
                'Doctor : Don\'t worry, I\'m not gonna pry',
                'Doctor : However, If you have any further business',
                'Doctor : It\'s gonna have to wait until she recovers..',
                'Doctor : She was hit pretty hard.',
                'Roman : Alright, thank you doctor.',
                'Roman : Doctor.. I have a favour to ask of you',
                'Doctor : What is it?',
                'Roman : After she recovers..',
                'Roman : Could I get a ride out to the nearest town?',
                'Doctor : Alright, consider it done..',
                'Doctor : ')
    snip = font.render('', True, white)
    counter = 0
    speed = 1
    active_message = 0
    message = messages[active_message]
    continue_button_press = False

    run = True
    while run:
        MENU_MOUSE_POS = pygame.mouse.get_pos()

        PAUSE = Button(image=pygame.image.load("assets/pause.png"), pos=(50, 50), 
                            text_input="           ", font=textbutton_font(21), base_color="black", hovering_color="#FF3131")

        bg = pygame.image.load('assets/countryhosp2.png')
        scaled_bg = pygame.transform.scale(bg, (1280,720))
        bg_rect = scaled_bg.get_rect(x=0,y=0)
        
        textbox = pygame.image.load('assets/textbox.png')
        scaled_texbox = pygame.transform.scale(textbox, (1100,250))
        textbox_rect = scaled_texbox.get_rect(x=80,y=475)

        screen.blit(scaled_bg, bg_rect)
        PAUSE.update(screen)
        PAUSE.changeColor(MENU_MOUSE_POS)
        roman(175,-0.5)
        doctor(600, 80)
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
                        continue_button_press = True                # adjust sini kalau ada byk message
                        
                if continue_button_press:
                    return

        snip = font.render(message[0:counter//speed], True, 'white')
        screen.blit(snip, (150, 570))

        pygame.display.flip()

# the actual game starts here lol
def main():
    running = True
    clock = pygame.time.Clock()
    button = create_random_button()
    button_timer = 5000
    button_start_time = pygame.time.get_ticks()
    button_press_count = 0
    show_dialogue_1 = False
    show_dialogue_2 = False
    show_dialogue_3 = False

    directions = [
        pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT,
        pygame.K_UP, pygame.K_LEFT, pygame.K_DOWN, pygame.K_RIGHT,
        pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT,
        pygame.K_UP, pygame.K_LEFT, pygame.K_DOWN
    ]
    current_direction = 0

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == directions[current_direction]:
                    current_direction += 1
                    if current_direction >= len(directions):
                        dialogue1()
                    else:
                        button = create_random_button()
                        button.image = arrow_images[current_direction]  # Change the button image
                        button_start_time = pygame.time.get_ticks()
                else:
                    retry_screen()

        mouse_pos = pygame.mouse.get_pos()
        button.changeColor(mouse_pos)

        screen.blit(background_images_scaled[current_direction], [0, 0])

        button.update(screen)

        if pygame.time.get_ticks() - button_start_time > button_timer:
            print("Button timer expired!")
            retry_screen()
            running = False

        if current_direction == 4 and not show_dialogue_1:
            show_dialogue_1 = True
            button_timer = 15000
            button_start_time = pygame.time.get_ticks()
            fightdialogue1()
            button_timer = 5000
            button_start_time = pygame.time.get_ticks()

        if current_direction == 9 and not show_dialogue_2:
            show_dialogue_2 = True
            button_timer = 15000
            button_start_time = pygame.time.get_ticks()
            fightdialogue2()
            button_timer =5000
            button_start_time = pygame.time.get_ticks()

        if current_direction == 12 and not show_dialogue_3:
            show_dialogue_3 = True
            button_timer = 15000
            button_start_time = pygame.time.get_ticks()
            fightdialogue3()
            button_timer = 5000
            button_start_time = pygame.time.get_ticks()

        pygame.display.flip()

        clock.tick(30)

    pygame.quit()

main()