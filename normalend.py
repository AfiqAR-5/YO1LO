import pygame
import random
import sys
from button import Button

pygame.init()
pygame.display.set_caption("YO1LO") #window name

bg_music = pygame.mixer.music.load('assets/Audio/normalendost.mp3')  
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

def mc(xpos, ypos):
     mc = pygame.image.load('assets/mc.png')
     mc_rect = mc.get_rect(x=xpos, y=ypos)

     return screen.blit(mc,mc_rect)

def lover(xpos, ypos):
    lover = pygame.image.load('assets/Chapter2/lover2.png')
    lover_rect = lover.get_rect(x=xpos, y=ypos)

    return screen.blit(lover, lover_rect)

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
                    pygame.mixer.music.load('assets/Audio/normalendost.mp3')  
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

def fightdialogue1():   # mc textbox
    font = pygame.font.Font("assets/Font/ARCADE.TTF", 24)
    timer = pygame.time.Clock()
    messages = ('MC : Why!!!!!!!!',
                'MC : Why did you kill him !!!!!!',
                "MC : He was going to give me my answer!",
                "MC : About everything that happened that night!!",
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
        mc(475,-0.5)
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

def fightdialogue2():  #black/narrator textbox
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

def fightdialogue3():   # mc textbox
    font = pygame.font.Font("assets/Font/ARCADE.TTF", 24)
    timer = pygame.time.Clock()
    messages = ('MC : Why!!!!!!!!',
                'MC : Why must you always get in my way like this !!!!!!',
                "MC : LUUNAAAAAA !!!!!!",
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
        mc(475,-0.5)
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

    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.blit(bg_image, (0, 0))

        if pygame.time.get_ticks() - start_time >= 4000:
            pygame.mixer.music.unpause()
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

def dialogue4():   # mc textbox
    font = pygame.font.Font("assets/Font/ARCADE.TTF", 24)
    timer = pygame.time.Clock()
    messages = ('MC : Luna..?',
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
        mc(475,-0.5)
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
                'Luna : It\'s all over...',
                '...'
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

def dialogue6():   # mc textbox
    font = pygame.font.Font("assets/Font/ARCADE.TTF", 24)
    timer = pygame.time.Clock()
    messages = ('MC : LUNA !!',
                'MC : Oh god...',
                'MC : What have I done...',
                'MC : Luna, I will get you to a hospital!',
                'MC : So please..',
                'MC : Bear with me..'
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
        mc(475,-0.5)
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

def dialogue7():  #black/narrator textbox
    font = pygame.font.Font("assets/Font/ARCADE.TTF", 24)
    timer = pygame.time.Clock()
    messages = ('The MC, having picked up her lover Luna-',
                'began to run in a direction he picked randomly',
                'hoping that-',
                'wherever he might end up..',
                'maybe..',
                'maybe a hospital, or a clinic..',
                'atleast, that way there\'s a chance at redemption.',
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
                        dialogue8()
                if continue_button_press:
                    return

        snip = font.render(message[0:counter // speed], True, white)
        screen.blit(snip, (dialog_x + 50, dialog_y + 30))  # adjust text pos sini

        pygame.display.flip()

def dialogue8():   # mc textbox
    font = pygame.font.Font("assets/Font/ARCADE.TTF", 24)
    timer = pygame.time.Clock()
    messages = ('MC : Please..',
                'MC : Please for the love of god..',
                'MC : PLEASE LET THERE BE A HOSPITAL!',
                'MC : Luna, I will get you to a hospital!',
                'MC : So please..',
                'MC : Bear with me..'
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
        mc(475,-0.5)
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
                        
                if continue_button_press:
                    return

        snip = font.render(message[0:counter//speed], True, 'white')
        screen.blit(snip, (275, 570))

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

if __name__ == "__main__":
    main()
