import pygame
import random
import sys
from button import Button

pygame.init()
pygame.display.set_caption("YO1LO")

screen_width = 1280
screen_height = 720
screen = pygame.display.set_mode((screen_width, screen_height))

font = pygame.font.Font(None, 50)
dialogue_font = pygame.font.Font(None, 36)

white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)

drive = pygame.mixer.Sound("assets/Audio/driving.mp3")
shootout = pygame.mixer.Sound("assets/Audio/shootout.mp3")
shoot = pygame.mixer.Sound("assets/Audio/shoot_sound.wav")

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
     roman = pygame.image.load('assets/mcbefore.png')
     roman_rect = roman.get_rect(x=xpos, y=ypos)

     return screen.blit(roman,roman_rect)

def romanafter(xpos, ypos):
     romanafter = pygame.image.load('assets/mcafter.png')
     romanafter_rect = romanafter.get_rect(x=xpos, y=ypos)

     return screen.blit(romanafter,romanafter_rect)

def romanskip(xpos, ypos):
     romanskip = pygame.image.load('assets/mctimeskip.png')
     romanskip_rect = romanskip.get_rect(x=xpos, y=ypos)

     return screen.blit(romanskip,romanskip_rect)

def lover(xpos, ypos):
    lover = pygame.image.load('assets/Chapter2/lovercalm.png')
    lover_rect = lover.get_rect(x=xpos, y=ypos)

    return screen.blit(lover, lover_rect)

def loverafter(xpos, ypos):
    loverafter = pygame.image.load('assets/loverafter.png')
    loverafter_rect = loverafter.get_rect(x=xpos, y=ypos)

    return screen.blit(loverafter, loverafter_rect)

def loverskip(xpos, ypos):
     loverskip = pygame.image.load('assets/loverskip.png')
     loverskip_rect = loverskip.get_rect(x=xpos, y=ypos)

     return screen.blit(loverskip,loverskip_rect)

def lovergun(xpos, ypos):
     lovergun = pygame.image.load('assets/Chapter2/lovershoot1.png')
     lovergun_rect = lovergun.get_rect(x=xpos, y=ypos)

     return screen.blit(lovergun,lovergun_rect)

def henchman(xpos, ypos):
     henchman = pygame.image.load('assets/Chapter2/konco2.png')
     henchman_rect = henchman.get_rect(x=xpos, y=ypos)

     return screen.blit(henchman,henchman_rect)

def henchmanded(xpos, ypos):
     henchmanded= pygame.image.load('assets/Chapter2/konco2dead.png')
     henchmanded_rect = henchmanded.get_rect(x=xpos, y=ypos)

     return screen.blit(henchmanded,henchmanded_rect)

def villain(xpos, ypos):
     villain = pygame.image.load('assets/Chapter2/villainnormal.png')
     villain_rect = villain.get_rect(x=xpos, y=ypos)

     return screen.blit(villain,villain_rect)

def villainded(xpos, ypos):
     villainded= pygame.image.load('assets/Chapter2/villainnormaldead.png')
     villainded_rect = villainded.get_rect(x=xpos, y=ypos)

     return screen.blit(villainded,villainded_rect)

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
                    qte()

    pygame.time.delay(500)

def qte():
    pygame.mixer.music.load('assets/Audio/normalendfight.mp3')
    pygame.mixer.music.play(-1)

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

def dialoguebf1():  # lover textbox
    pygame.mixer.music.load("assets/Audio/confront.mp3")
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.5)

    font = pygame.font.Font("assets/Font/ARCADE.TTF", 24)
    timer = pygame.time.Clock()
    messages = ('Luna : I should lay low...',
                'Luna : And take them out one by one..',
                'Luna : I can\'t afford to attract attention...',
                'Luna : ...',
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

        bg = pygame.image.load('assets/Chapter2/Warehousecari.png')
        scaled_bg = pygame.transform.scale(bg, (1280,720))
        bg_rect = scaled_bg.get_rect(x=0,y=0)
        
        textbox = pygame.image.load('assets/textboxlover.png')
        scaled_texbox = pygame.transform.scale(textbox, (850,450))
        textbox_rect = scaled_texbox.get_rect(x=220,y=410)

        screen.blit(scaled_bg, bg_rect)
        PAUSE.update(screen)
        PAUSE.changeColor(MENU_MOUSE_POS)
        lover(420, 130)
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
                        dialoguebf2()
                if continue_button_press:
                    return

        snip = font.render(message[0:counter//speed], True, 'white')
        screen.blit(snip, (295, 600))

        pygame.display.flip()

def dialoguebf2():  # lover textbox
    font = pygame.font.Font("assets/Font/ARCADE.TTF", 24)
    timer = pygame.time.Clock()
    messages = ('Luna : Someone\'s there!',
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

        bg = pygame.image.load('assets/Chapter2/Warehousecari.png')
        scaled_bg = pygame.transform.scale(bg, (1280,720))
        bg_rect = scaled_bg.get_rect(x=0,y=0)
        
        textbox = pygame.image.load('assets/textboxlover.png')
        scaled_texbox = pygame.transform.scale(textbox, (850,450))
        textbox_rect = scaled_texbox.get_rect(x=220,y=410)

        screen.blit(scaled_bg, bg_rect)
        PAUSE.update(screen)
        PAUSE.changeColor(MENU_MOUSE_POS)
        lover(420, 130)
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
                    if active_message == 1:               # adjust sini kalau ada byk message
                        continue_button_press = True
                        dialoguebf3()
                if continue_button_press:
                    return

        snip = font.render(message[0:counter//speed], True, 'white')
        screen.blit(snip, (295, 600))

        pygame.display.flip()

def dialoguebf3():  # roman textbox
    font = pygame.font.Font("assets/Font/ARCADE.TTF", 24)
    timer = pygame.time.Clock()
    messages = ('Henchman 1 : Who\'s there?!',
                '<STABS>',
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

        bg = pygame.image.load('assets/Chapter2/Warehousecari.png')
        scaled_bg = pygame.transform.scale(bg, (1280,720))
        bg_rect = scaled_bg.get_rect(x=0,y=0)
        
        textbox = pygame.image.load('assets/textbox.png')
        scaled_texbox = pygame.transform.scale(textbox, (1100,250))
        textbox_rect = scaled_texbox.get_rect(x=80,y=475)

        screen.blit(scaled_bg, bg_rect)
        PAUSE.update(screen)
        PAUSE.changeColor(MENU_MOUSE_POS)

        henchman(450, -1)

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
                        continue_button_press = True                # adjust sini kalau ada byk message
                        dialoguebf4()
                if continue_button_press:
                    return
                
        snip = font.render(message[0:counter//speed], True, 'white')
        screen.blit(snip, (200, 570))

        pygame.display.flip()

def dialoguebf4():  # roman textbox
    font = pygame.font.Font("assets/Font/ARCADE.TTF", 24)
    timer = pygame.time.Clock()
    messages = ('Henchman 1 : AGHHHH',
                '*DIES*',
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

        bg = pygame.image.load('assets/Chapter2/Warehousecari.png')
        scaled_bg = pygame.transform.scale(bg, (1280,720))
        bg_rect = scaled_bg.get_rect(x=0,y=0)
        
        textbox = pygame.image.load('assets/textbox.png')
        scaled_texbox = pygame.transform.scale(textbox, (1100,250))
        textbox_rect = scaled_texbox.get_rect(x=80,y=475)

        screen.blit(scaled_bg, bg_rect)
        PAUSE.update(screen)
        PAUSE.changeColor(MENU_MOUSE_POS)

        henchmanded(450, -1)

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
                        continue_button_press = True                # adjust sini kalau ada byk message
                        dialoguebf5()
                if continue_button_press:
                    return
                
        snip = font.render(message[0:counter//speed], True, 'white')
        screen.blit(snip, (200, 570))

        pygame.display.flip()

def dialoguebf5():  # lover textbox
    font = pygame.font.Font("assets/Font/ARCADE.TTF", 24)
    timer = pygame.time.Clock()
    messages = ('Luna : One down.. how many are there left?',
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

        bg = pygame.image.load('assets/Chapter2/Warehousecari.png')
        scaled_bg = pygame.transform.scale(bg, (1280,720))
        bg_rect = scaled_bg.get_rect(x=0,y=0)
        
        textbox = pygame.image.load('assets/textboxlover.png')
        scaled_texbox = pygame.transform.scale(textbox, (850,450))
        textbox_rect = scaled_texbox.get_rect(x=220,y=410)

        screen.blit(scaled_bg, bg_rect)
        PAUSE.update(screen)
        PAUSE.changeColor(MENU_MOUSE_POS)
        lover(420, 130)
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
                    if active_message == 1:               # adjust sini kalau ada byk message
                        continue_button_press = True
                        dialoguebf6()
                if continue_button_press:
                    return

        snip = font.render(message[0:counter//speed], True, 'white')
        screen.blit(snip, (295, 600))

        pygame.display.flip()

def dialoguebf6():  # black/narrator textbox
    font = pygame.font.Font("assets/Font/ARCADE.TTF", 24)
    timer = pygame.time.Clock()
    messages = ('Luna then proceeds to take out the henchman one-by-one...',
                'Until came a certain person...',
                '"LUNA!!"',
                'A voice calls out..',
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

        bg = pygame.image.load('assets/Chapter2/Warehousecari.png')
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
                    if active_message == 4:               # adjust sini kalau ada byk message
                       dialoguebf7()
                if continue_button_press:
                    return

        snip = font.render(message[0:counter // speed], True, white)
        screen.blit(snip, (dialog_x + 50, dialog_y + 30))  # adjust text pos sini

        pygame.display.flip()

def dialoguebf7():  # roman textbox
    font = pygame.font.Font("assets/Font/ARCADE.TTF", 24)
    timer = pygame.time.Clock()
    messages = ('Emir : LUNA!!',
                'Emir : You\'ve finally come!',
                'Emir : Oh I can\'t wait to settle things with you!',
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

        bg = pygame.image.load('assets/Chapter2/Warehousecari.png')
        scaled_bg = pygame.transform.scale(bg, (1280,720))
        bg_rect = scaled_bg.get_rect(x=0,y=0)
        
        textbox = pygame.image.load('assets/textbox.png')
        scaled_texbox = pygame.transform.scale(textbox, (1100,250))
        textbox_rect = scaled_texbox.get_rect(x=80,y=475)

        screen.blit(scaled_bg, bg_rect)
        PAUSE.update(screen)
        PAUSE.changeColor(MENU_MOUSE_POS)

        villain(450, -1)

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
                    if active_message == 3:
                        continue_button_press = True                # adjust sini kalau ada byk message
                        dialoguebf8()
                if continue_button_press:
                    return
                
        snip = font.render(message[0:counter//speed], True, 'white')
        screen.blit(snip, (200, 570))

        pygame.display.flip()

def dialoguebf8():  # lover textbox
    font = pygame.font.Font("assets/Font/ARCADE.TTF", 24)
    timer = pygame.time.Clock()
    messages = ('Luna : As If!',
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

        bg = pygame.image.load('assets/Chapter2/Warehousecari.png')
        scaled_bg = pygame.transform.scale(bg, (1280,720))
        bg_rect = scaled_bg.get_rect(x=0,y=0)
        
        textbox = pygame.image.load('assets/textboxlover.png')
        scaled_texbox = pygame.transform.scale(textbox, (850,450))
        textbox_rect = scaled_texbox.get_rect(x=220,y=410)

        screen.blit(scaled_bg, bg_rect)
        PAUSE.update(screen)
        PAUSE.changeColor(MENU_MOUSE_POS)
        lover(420, 130)
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
                    if active_message == 1:               # adjust sini kalau ada byk message
                        continue_button_press = True
                        dialoguebf9()
                if continue_button_press:
                    return

        snip = font.render(message[0:counter//speed], True, 'white')
        screen.blit(snip, (295, 600))

        pygame.display.flip()

def dialoguebf9():  # lover textbox
    font = pygame.font.Font("assets/Font/ARCADE.TTF", 24)
    timer = pygame.time.Clock()
    messages = ('Luna : You\'re dead meat!',
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

        bg = pygame.image.load('assets/Chapter2/Warehousecari.png')
        scaled_bg = pygame.transform.scale(bg, (1280,720))
        bg_rect = scaled_bg.get_rect(x=0,y=0)
        
        textbox = pygame.image.load('assets/textboxlover.png')
        scaled_texbox = pygame.transform.scale(textbox, (850,450))
        textbox_rect = scaled_texbox.get_rect(x=220,y=410)

        screen.blit(scaled_bg, bg_rect)
        PAUSE.update(screen)
        PAUSE.changeColor(MENU_MOUSE_POS)
        lovergun(420, 130)
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
                    if active_message == 1:               # adjust sini kalau ada byk message
                        continue_button_press = True
                        dialoguebf10()
                if continue_button_press:
                    return

        snip = font.render(message[0:counter//speed], True, 'white')
        screen.blit(snip, (295, 600))

        pygame.display.flip()

def dialoguebf10():  # roman textbox
    font = pygame.font.Font("assets/Font/ARCADE.TTF", 24)
    timer = pygame.time.Clock()
    messages = ('Emir : I\'d like to see you try!',
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

        bg = pygame.image.load('assets/Chapter2/Warehousecari.png')
        scaled_bg = pygame.transform.scale(bg, (1280,720))
        bg_rect = scaled_bg.get_rect(x=0,y=0)
        
        textbox = pygame.image.load('assets/textbox.png')
        scaled_texbox = pygame.transform.scale(textbox, (1100,250))
        textbox_rect = scaled_texbox.get_rect(x=80,y=475)

        screen.blit(scaled_bg, bg_rect)
        PAUSE.update(screen)
        PAUSE.changeColor(MENU_MOUSE_POS)

        villain(450, -1)

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
                        dialoguebf11()
                if continue_button_press:
                    return
                
        snip = font.render(message[0:counter//speed], True, 'white')
        screen.blit(snip, (200, 570))

        pygame.display.flip()

def dialoguebf11():  # black/narrator textbox
    font = pygame.font.Font("assets/Font/ARCADE.TTF", 24)
    timer = pygame.time.Clock()
    messages = ('What followed was an explosive sounds of bullets...',
                'Shooting at each other...',
                'They fired wildly at the sight of each other..',
                'Until...',
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

    shootout.play()

    run = True
    while run:
        MENU_MOUSE_POS = pygame.mouse.get_pos()

        PAUSE = Button(image=pygame.image.load("assets/pause.png"), pos=(50, 50), 
                            text_input="           ", font=textbutton_font(21), base_color="black", hovering_color="#FF3131")

        bg = pygame.image.load('assets/Chapter2/Warehousecari.png')
        scaled_bg = pygame.transform.scale(bg, (1280,720))
        bg_rect = scaled_bg.get_rect(x=0,y=0)
        screen.blit(scaled_bg, bg_rect)

        speedlines = pygame.image.load('assets/speedlines.png')
        scaled_speedlines = pygame.transform.scale(speedlines, (1280,720))
        speedlines_rect = scaled_speedlines.get_rect(x=0,y=0)
        screen.blit(scaled_speedlines, speedlines_rect)

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
                    if active_message == 4:               # adjust sini kalau ada byk message
                       dialoguebf12()
                       pygame.mixer.music.stop()
                if continue_button_press:
                    return

        snip = font.render(message[0:counter // speed], True, white)
        screen.blit(snip, (dialog_x + 50, dialog_y + 30))  # adjust text pos sini

        pygame.display.flip()

def dialoguebf12():  # lover textbox
    font = pygame.font.Font("assets/Font/ARCADE.TTF", 24)
    timer = pygame.time.Clock()
    messages = ('Luna : This isn\'t good..',
                'Luna : I need to gain some distance.',
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

        bg = pygame.image.load('assets/Chapter2/Warehousecari.png')
        scaled_bg = pygame.transform.scale(bg, (1280,720))
        bg_rect = scaled_bg.get_rect(x=0,y=0)
        screen.blit(scaled_bg, bg_rect)


        speedlines = pygame.image.load('assets/speedlines.png')
        scaled_speedlines = pygame.transform.scale(speedlines, (1280,720))
        speedlines_rect = scaled_speedlines.get_rect(x=0,y=0)
        screen.blit(scaled_speedlines, speedlines_rect)
        
        textbox = pygame.image.load('assets/textboxlover.png')
        scaled_texbox = pygame.transform.scale(textbox, (850,450))
        textbox_rect = scaled_texbox.get_rect(x=220,y=410)

        
        PAUSE.update(screen)
        PAUSE.changeColor(MENU_MOUSE_POS)
        lovergun(420, 130)
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
                    if active_message == 2:               # adjust sini kalau ada byk message
                        continue_button_press = True
                        dialoguebf13()
                if continue_button_press:
                    return

        snip = font.render(message[0:counter//speed], True, 'white')
        screen.blit(snip, (295, 600))

        pygame.display.flip()

def dialoguebf13():  # roman textbox
    font = pygame.font.Font("assets/Font/ARCADE.TTF", 24)
    timer = pygame.time.Clock()
    messages = ('Emir : Hey!',
                'Emir : Don\'t you think you can get away!',
                '...')
    snip = font.render('', True, white)
    counter = 0
    speed = 1
    active_message = 0
    message = messages[active_message]
    continue_button_press = False

    shootout.stop()

    run = True
    while run:
        MENU_MOUSE_POS = pygame.mouse.get_pos()

        PAUSE = Button(image=pygame.image.load("assets/pause.png"), pos=(50, 50), 
                            text_input="           ", font=textbutton_font(21), base_color="black", hovering_color="#FF3131")

        bg = pygame.image.load('assets/Chapter2/Warehousecari.png')
        scaled_bg = pygame.transform.scale(bg, (1280,720))
        bg_rect = scaled_bg.get_rect(x=0,y=0)
        
        textbox = pygame.image.load('assets/textbox.png')
        scaled_texbox = pygame.transform.scale(textbox, (1100,250))
        textbox_rect = scaled_texbox.get_rect(x=80,y=475)

        screen.blit(scaled_bg, bg_rect)
        PAUSE.update(screen)
        PAUSE.changeColor(MENU_MOUSE_POS)

        villain(450, -1)

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
                        continue_button_press = True                # adjust sini kalau ada byk message
                        dialoguebf14()
                if continue_button_press:
                    return
                
        snip = font.render(message[0:counter//speed], True, 'white')
        screen.blit(snip, (200, 570))

        pygame.display.flip()

def dialoguebf14():  # black/narrator textbox
    font = pygame.font.Font("assets/Font/ARCADE.TTF", 24)
    timer = pygame.time.Clock()
    messages = ('Luna ran as fast as she could..',
                'Until she reached..',
                'The far side of the forest..',
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

        bg = pygame.image.load('assets/Chapter2/Warehousecari.png')
        scaled_bg = pygame.transform.scale(bg, (1280,720))
        bg_rect = scaled_bg.get_rect(x=0,y=0)
        screen.blit(scaled_bg, bg_rect)

        speedlines = pygame.image.load('assets/speedlines.png')
        scaled_speedlines = pygame.transform.scale(speedlines, (1280,720))
        speedlines_rect = scaled_speedlines.get_rect(x=0,y=0)
        screen.blit(scaled_speedlines, speedlines_rect)

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
                    if active_message == 3:               # adjust sini kalau ada byk message
                       dialoguebf15()
                       pygame.mixer.music.stop()
                if continue_button_press:
                    return

        snip = font.render(message[0:counter // speed], True, white)
        screen.blit(snip, (dialog_x + 50, dialog_y + 30))  # adjust text pos sini

        pygame.display.flip()

def dialoguebf15():  # lover textbox
    font = pygame.font.Font("assets/Font/ARCADE.TTF", 24)
    timer = pygame.time.Clock()
    messages = ('Luna : Where am I..?',
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
        lover(420, 130)
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
                    if active_message == 1:               # adjust sini kalau ada byk message
                        continue_button_press = True
                        dialoguebf16()
                if continue_button_press:
                    return

        snip = font.render(message[0:counter//speed], True, 'white')
        screen.blit(snip, (295, 600))

        pygame.display.flip()

def dialoguebf16():  # roman textbox
    font = pygame.font.Font("assets/Font/ARCADE.TTF", 24)
    timer = pygame.time.Clock()
    messages = ('Emir : Luna!!',
                'Emir : I\'ve caught up to you now!',
                'Emir : You\'ve been such a nuisance..',
                'Emir : because of you..',
                'Emir : Roman\'s having suspicions agains\'t me!',
                'Emir : But not anymore..',
                'Emir : Once I\'m done with you!',
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
        scaled_texbox = pygame.transform.scale(textbox, (1100,250))
        textbox_rect = scaled_texbox.get_rect(x=80,y=475)

        screen.blit(scaled_bg, bg_rect)
        PAUSE.update(screen)
        PAUSE.changeColor(MENU_MOUSE_POS)

        villain(450, -1)

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
                        dialoguebf17()
                if continue_button_press:
                    return
                
        snip = font.render(message[0:counter//speed], True, 'white')
        screen.blit(snip, (200, 570))

        pygame.display.flip()

def dialoguebf17():  # lover textbox
    font = pygame.font.Font("assets/Font/ARCADE.TTF", 24)
    timer = pygame.time.Clock()
    messages = ('Luna : I won\'t let you do whatever you want!',
                'Luna : AAAAHHHHH!!!',
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
        lovergun(420, 130)
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
                    if active_message == 2:               # adjust sini kalau ada byk message
                        continue_button_press = True
                        shoot.play()
                        dialoguebf18()
                if continue_button_press:
                    return

        snip = font.render(message[0:counter//speed], True, 'white')
        screen.blit(snip, (295, 600))

        pygame.display.flip()

def dialoguebf18():  # roman textbox
    font = pygame.font.Font("assets/Font/ARCADE.TTF", 24)
    timer = pygame.time.Clock()
    messages = ('Emir : AAAGGHHHH!!',
                '*DIES*',
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
        scaled_texbox = pygame.transform.scale(textbox, (1100,250))
        textbox_rect = scaled_texbox.get_rect(x=80,y=475)

        screen.blit(scaled_bg, bg_rect)
        PAUSE.update(screen)
        PAUSE.changeColor(MENU_MOUSE_POS)

        villainded(450, -1)

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
                        continue_button_press = True                # adjust sini kalau ada byk message
                        dialoguebf19()
                if continue_button_press:
                    return
                
        snip = font.render(message[0:counter//speed], True, 'white')
        screen.blit(snip, (200, 570))

        pygame.display.flip()

def dialoguebf19():  # lover textbox
    font = pygame.font.Font("assets/Font/ARCADE.TTF", 24)
    timer = pygame.time.Clock()
    messages = ('Luna : Oh god..',
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
        lover(420, 130)
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
                    if active_message == 1:               # adjust sini kalau ada byk message
                        continue_button_press = True
                        dialoguebf20()
                if continue_button_press:
                    return

        snip = font.render(message[0:counter//speed], True, 'white')
        screen.blit(snip, (295, 600))

        pygame.display.flip()

def dialoguebf20():  # roman textbox
    font = pygame.font.Font("assets/Font/ARCADE.TTF", 24)
    timer = pygame.time.Clock()
    messages = ('Roman : Luna..?!',
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
        scaled_texbox = pygame.transform.scale(textbox, (1100,250))
        textbox_rect = scaled_texbox.get_rect(x=80,y=475)

        screen.blit(scaled_bg, bg_rect)
        PAUSE.update(screen)
        PAUSE.changeColor(MENU_MOUSE_POS)
        roman(375,-0.5)
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
                    if active_message == 1:               # adjust sini kalau ada byk message
                        dialoguebf21()
                if continue_button_press:
                    return

        snip = font.render(message[0:counter//speed], True, 'white')
        screen.blit(snip, (200, 570))

        pygame.display.flip()

def dialoguebf21():  # lover textbox
    font = pygame.font.Font("assets/Font/ARCADE.TTF", 24)
    timer = pygame.time.Clock()
    messages = ('Luna : Wait, Roman!',
                'Luna : I can explain!',
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
        lover(420, 130)
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
                    if active_message == 2:               # adjust sini kalau ada byk message
                        continue_button_press = True
                        dialoguebf22()
                if continue_button_press:
                    return

        snip = font.render(message[0:counter//speed], True, 'white')
        screen.blit(snip, (295, 600))

        pygame.display.flip()

def dialoguebf22():  # roman textbox
    font = pygame.font.Font("assets/Font/ARCADE.TTF", 24)
    timer = pygame.time.Clock()
    messages = ('Roman : What have you done..?!',
                'Roman : Luna !!!',
                "...")
    snip = font.render('', True, white)
    counter = 0
    speed = 1
    active_message = 0
    message = messages[active_message]
    continue_button_press = False

    pygame.mixer.music.fadeout(1)

    run = True
    while run:
        MENU_MOUSE_POS = pygame.mouse.get_pos()

        PAUSE = Button(image=pygame.image.load("assets/pause.png"), pos=(50, 50), 
                            text_input="           ", font=textbutton_font(21), base_color="black", hovering_color="#FF3131")

        bg = pygame.image.load('assets/background2.png')
        scaled_bg = pygame.transform.scale(bg, (1280,720))
        bg_rect = scaled_bg.get_rect(x=0,y=0)
        
        textbox = pygame.image.load('assets/textbox.png')
        scaled_texbox = pygame.transform.scale(textbox, (1100,250))
        textbox_rect = scaled_texbox.get_rect(x=80,y=475)

        screen.blit(scaled_bg, bg_rect)
        PAUSE.update(screen)
        PAUSE.changeColor(MENU_MOUSE_POS)
        roman(375,-0.5)
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
                    if active_message == 2:               # adjust sini kalau ada byk message
                        qte()
                if continue_button_press:
                    return

        snip = font.render(message[0:counter//speed], True, 'white')
        screen.blit(snip, (200, 570))

        pygame.display.flip()

def fightdialogue1():  # roman textbox
    font = pygame.font.Font("assets/Font/ARCADE.TTF", 24)
    timer = pygame.time.Clock()
    messages = ('Roman : Why !!!!!!!!',
                'Roman : Why did you kill Emir !!!!!!',
                "Roman : He was my comrade !!!",
                "Roman : My brother in arms !!!",
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
        scaled_texbox = pygame.transform.scale(textbox, (1100,250))
        textbox_rect = scaled_texbox.get_rect(x=80,y=475)

        screen.blit(scaled_bg, bg_rect)
        PAUSE.update(screen)
        PAUSE.changeColor(MENU_MOUSE_POS)
        roman(375,-0.5)
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
        screen.blit(snip, (200, 570))

        pygame.display.flip()

def fightdialogue2():  # black/narrator textbox
    font = pygame.font.Font("assets/Font/ARCADE.TTF", 24)
    timer = pygame.time.Clock()
    messages = ('Unable to accept the situation..',
                'Roman releases a fury of punches...',
                'In the midst of his barrage of fists..',
                'Luna can only dodge and weave..',
                'But I\'t wont be long..',
                'before one of the punches hit..',
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
                    if active_message == 6:               # adjust sini kalau ada byk message
                        continue_button_press = True
                if continue_button_press:
                    return

        snip = font.render(message[0:counter // speed], True, white)
        screen.blit(snip, (dialog_x + 50, dialog_y + 30))  # adjust text pos sini

        pygame.display.flip()

def fightdialogue3():  # roman textbox
    font = pygame.font.Font("assets/Font/ARCADE.TTF", 24)
    timer = pygame.time.Clock()
    messages = ('Roman : Why!!!!!!!!',
                'Roman : Why did you kill emir ?????!!!!!!',
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
        scaled_texbox = pygame.transform.scale(textbox, (1100,250))
        textbox_rect = scaled_texbox.get_rect(x=80,y=475)

        screen.blit(scaled_bg, bg_rect)
        PAUSE.update(screen)
        PAUSE.changeColor(MENU_MOUSE_POS)
        roman(375,-0.5)
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
        screen.blit(snip, (200, 570))

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

def dialogue4():  # roman textbox
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
        scaled_texbox = pygame.transform.scale(textbox, (1100,250))
        textbox_rect = scaled_texbox.get_rect(x=80,y=475)

        screen.blit(scaled_bg, bg_rect)
        PAUSE.update(screen)
        PAUSE.changeColor(MENU_MOUSE_POS)
        roman(375,-0.5)
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
        screen.blit(snip, (200, 570))

        pygame.display.flip()

def dialogue5():  # lover textbox
    font = pygame.font.Font("assets/Font/ARCADE.TTF", 24)
    timer = pygame.time.Clock()
    messages = ('Luna : It\'s alright..',
                'Luna : Everything\'s fine now..',
                'Luna : It\'s not your fault...',
                '*FAINTS*',
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
        lover(420, 130)
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

def dialogue6():  # roman textbox
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
        scaled_texbox = pygame.transform.scale(textbox, (1100,250))
        textbox_rect = scaled_texbox.get_rect(x=80,y=475)

        screen.blit(scaled_bg, bg_rect)
        PAUSE.update(screen)
        PAUSE.changeColor(MENU_MOUSE_POS)
        roman(375,-0.5)
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
        screen.blit(snip, (200, 570))

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

def dialogue8():  # roman textbox
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
        scaled_texbox = pygame.transform.scale(textbox, (1100,250))
        textbox_rect = scaled_texbox.get_rect(x=80,y=475)

        screen.blit(scaled_bg, bg_rect)
        PAUSE.update(screen)
        PAUSE.changeColor(MENU_MOUSE_POS)
        roman(375,-0.5)
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
        screen.blit(snip, (200, 570))

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

def dialogue12():  # roman textbox
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
        scaled_texbox = pygame.transform.scale(textbox, (1100,250))
        textbox_rect = scaled_texbox.get_rect(x=80,y=475)

        screen.blit(scaled_bg, bg_rect)
        PAUSE.update(screen)
        PAUSE.changeColor(MENU_MOUSE_POS)
        roman(375,-0.5)
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
        screen.blit(snip, (200, 570))

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
                '"Coming!"',
                'A voice responded from behind the door',
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
                    if active_message == 3:               # adjust sini kalau ada byk message
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

def dialogue16():  # roman textbox
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
        scaled_texbox = pygame.transform.scale(textbox, (1100,250))
        textbox_rect = scaled_texbox.get_rect(x=80,y=475)

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
        screen.blit(snip, (200, 570))

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

def dialogue21():  # roman textbox
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
                'Doctor : Don\'t worry, I\'m not gonna pry.',
                'Doctor : However, If you have any further business..',
                'Doctor : It\'s gonna have to wait until she recovers..',
                'Doctor : She was hit pretty hard.',
                'Roman : Alright, thank you doctor.',
                'Roman : Doctor.. I have a favour to ask of you',
                'Doctor : What is it?',
                'Roman : After she recovers..',
                'Roman : Could I get me a taxi?',
                'Doctor : Alright, consider it done..',
                'Doctor : I assume you can\'t tell me why either?',
                'Roman : Yes doc, but I don\'t mean any harm',
                'Doctor : Oh I know you don\'t. If you did, you would have done so long ago..',
                'Doctor : For now, get some much needed rest.',
                'Doctor : You can use the guest room over there..',
                'Roman : I appreciate it, doctor..',
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

        bg = pygame.image.load('assets/countryhosp2.png')
        scaled_bg = pygame.transform.scale(bg, (1280,720))
        bg_rect = scaled_bg.get_rect(x=0,y=0)
        
        textbox = pygame.image.load('assets/textbox.png')
        scaled_texbox = pygame.transform.scale(textbox, (1100,250))
        textbox_rect = scaled_texbox.get_rect(x=80,y=475)

        screen.blit(scaled_bg, bg_rect)
        PAUSE.update(screen)
        PAUSE.changeColor(MENU_MOUSE_POS)
        roman(175, -0.5)
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
                    if active_message == 26:
                        continue_button_press = True                # adjust sini kalau ada byk message
                        dialogue22()
                if continue_button_press:
                    return

        snip = font.render(message[0:counter//speed], True, 'white')
        screen.blit(snip, (200, 570))

        pygame.display.flip()

def dialogue22():  # black/narrator textbox
    font = pygame.font.Font("assets/Font/ARCADE.TTF", 24)
    timer = pygame.time.Clock()
    messages = ('Taking the doctor up on their offer..',
                'Roman decided to stay for the night..',
                'As the doctor directed him..',
                'He went to the room on the far left of the clinic',
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
                    if active_message == 4:               # adjust sini kalau ada byk message
                        continue_button_press = True
                        dialogue23()
                if continue_button_press:
                    return

        snip = font.render(message[0:counter // speed], True, white)
        screen.blit(snip, (dialog_x + 50, dialog_y + 30))  # adjust text pos sini

        pygame.display.flip()

def dialogue23():  # roman textbox
    font = pygame.font.Font("assets/Font/ARCADE.TTF", 24)
    timer = pygame.time.Clock()
    messages = ('Roman : Ah.. this should do just nice.',
                'Roman : I should get myself cleaned up..',
                'Roman : Tomorrow, we\'ll talk it out..',
                'Roman : I hope she can forgive me..',
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

        bg = pygame.image.load('assets/countrybed.png')
        scaled_bg = pygame.transform.scale(bg, (1280,720))
        bg_rect = scaled_bg.get_rect(x=0,y=0)
        
        textbox = pygame.image.load('assets/textbox.png')
        scaled_texbox = pygame.transform.scale(textbox, (1100,250))
        textbox_rect = scaled_texbox.get_rect(x=80,y=475)

        screen.blit(scaled_bg, bg_rect)
        PAUSE.update(screen)
        PAUSE.changeColor(MENU_MOUSE_POS)
        roman(375,-0.5)
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
                        dialogue24()
                if continue_button_press:
                    return

        snip = font.render(message[0:counter//speed], True, 'white')
        screen.blit(snip, (200, 570))

        pygame.display.flip()

def dialogue24():  # pygame time delay not working
    bg_image = pygame.image.load("assets/blackscreen.png")
    start_time = pygame.time.get_ticks()  
    pygame.mixer.music.pause()
    pygame.mixer.music.load("assets/Audio/normalendrec.mp3")

    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.blit(bg_image, (0, 0))

        if pygame.time.get_ticks() - start_time >= 2000:
            pygame.mixer.music.play(-1)
            dialogue25()
            return 
        
        pygame.display.flip()

def dialogue25():  # centered textbox
    font = pygame.font.Font("assets/Font/ARCADE.TTF", 74)
    timer = pygame.time.Clock()
    messages = ('THE NEXT DAY', '...')
    snip = font.render('', True, white)
    counter = 0
    speed = 5
    active_message = 0
    message = messages[active_message]
    continue_button_press = False

    dialogue_box_width = 1160  # Increased width
    dialogue_box_height = 400  # Increased height
    dialogue_box_alpha = 225

    run = True
    while run:
        MENU_MOUSE_POS = pygame.mouse.get_pos()

        PAUSE = Button(image=pygame.image.load("assets/pause.png"), pos=(50, 50), 
                            text_input="           ", font=textbutton_font(21), base_color="black", hovering_color="#FF3131")

        bg = pygame.image.load('assets/countrybed.png')
        scaled_bg = pygame.transform.scale(bg, (1280, 720))
        bg_rect = scaled_bg.get_rect(x=0, y=0)
        screen.blit(scaled_bg, bg_rect)

        PAUSE.update(screen)
        PAUSE.changeColor(MENU_MOUSE_POS)

        # Center the dialogue box
        dialog_x = (screen.get_width() - dialogue_box_width) // 2
        dialog_y = (screen.get_height() - dialogue_box_height) // 2

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
                    if active_message == 1:  # Adjust if there are more messages
                        continue_button_press = True
                        dialogue26()
                if continue_button_press:
                    return

        # Render the current part of the message
        snip = font.render(message[0:counter // speed], True, white)
        
        # Get the size of the rendered text
        text_width, text_height = snip.get_size()
        
        # Center the text within the dialogue box
        text_x = dialog_x + (dialogue_box_width - text_width) // 2
        text_y = dialog_y + (dialogue_box_height - text_height) // 2
        
        screen.blit(snip, (text_x, text_y))

        pygame.display.flip()

def dialogue26():  # roman textbox
    font = pygame.font.Font("assets/Font/ARCADE.TTF", 24)
    timer = pygame.time.Clock()
    messages = ('Roman : Alright, all up and ready to go.',
                'Roman : I wonder if I can go see Luna..',
                'Roman : Oh.. Now I\'m getting nervous..',
                'Roman : Still, she also has questions to answer..',
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

        bg = pygame.image.load('assets/countrybed.png')
        scaled_bg = pygame.transform.scale(bg, (1280,720))
        bg_rect = scaled_bg.get_rect(x=0,y=0)
        
        textbox = pygame.image.load('assets/textbox.png')
        scaled_texbox = pygame.transform.scale(textbox, (1100,250))
        textbox_rect = scaled_texbox.get_rect(x=80,y=475)

        screen.blit(scaled_bg, bg_rect)
        PAUSE.update(screen)
        PAUSE.changeColor(MENU_MOUSE_POS)
        romanafter(375,-0.5)
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
                        dialogue27()
                if continue_button_press:
                    return

        snip = font.render(message[0:counter//speed], True, 'white')
        screen.blit(snip, (200, 570))

        pygame.display.flip()

def dialogue27():  # black/narrator textbox
    font = pygame.font.Font("assets/Font/ARCADE.TTF", 24)
    timer = pygame.time.Clock()
    messages = ('After taking a deep breath..',
                'Roman leaves the room..',
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

        bg = pygame.image.load('assets/countrybed.png')
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
                        dialogue28()
                if continue_button_press:
                    return

        snip = font.render(message[0:counter // speed], True, white)
        screen.blit(snip, (dialog_x + 50, dialog_y + 30))  # adjust text pos sini

        pygame.display.flip()

def dialogue28():  # roman textbox
    font = pygame.font.Font("assets/Font/ARCADE.TTF", 24)
    timer = pygame.time.Clock()
    messages = ('Roman : LUNA !',
                'Roman : You\'re all right!',
                'Roman : I didn\'t think you would recover already!',
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

        bg = pygame.image.load('assets/countryhosp2.png')
        scaled_bg = pygame.transform.scale(bg, (1280,720))
        bg_rect = scaled_bg.get_rect(x=0,y=0)
        
        textbox = pygame.image.load('assets/textbox.png')
        scaled_texbox = pygame.transform.scale(textbox, (1100,250))
        textbox_rect = scaled_texbox.get_rect(x=80,y=475)

        screen.blit(scaled_bg, bg_rect)
        PAUSE.update(screen)
        PAUSE.changeColor(MENU_MOUSE_POS)
        romanafter(125,-0.5)
        loverafter(660, 200)
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
                    if active_message == 3:
                        continue_button_press = True                # adjust sini kalau ada byk message
                        dialogue29()
                if continue_button_press:
                    return

        snip = font.render(message[0:counter//speed], True, 'white')
        screen.blit(snip, (200, 570))

        pygame.display.flip()

def dialogue29():  # lover textbox
    font = pygame.font.Font("assets/Font/ARCADE.TTF", 24)
    timer = pygame.time.Clock()
    messages = ('Luna : Hey now..',
                'Luna : What do you mean by that?',
                'Luna : I\'m not that weak now.',
                'Luna : Hehe..',
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

        bg = pygame.image.load('assets/countryhosp2.png')
        scaled_bg = pygame.transform.scale(bg, (1280,720))
        bg_rect = scaled_bg.get_rect(x=0,y=0)
        
        textbox = pygame.image.load('assets/textboxlover.png')
        scaled_texbox = pygame.transform.scale(textbox, (850,450))
        textbox_rect = scaled_texbox.get_rect(x=220,y=410)

        screen.blit(scaled_bg, bg_rect)
        PAUSE.update(screen)
        PAUSE.changeColor(MENU_MOUSE_POS)
        loverafter(660, 200)
        romanafter(125,-0.5)
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
                        dialogue30()
                if continue_button_press:
                    return

        snip = font.render(message[0:counter//speed], True, 'white')
        screen.blit(snip, (295, 600))

        pygame.display.flip()

def dialogue30():  # roman textbox
    font = pygame.font.Font("assets/Font/ARCADE.TTF", 24)
    timer = pygame.time.Clock()
    messages = ('Roman : Of course, of course..',
                'Roman : Luna, we need to-',
                'Doctor : Hey, the both of you!',
                'Doctor : The taxi\'s outside!',
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

        bg = pygame.image.load('assets/countryhosp2.png')
        scaled_bg = pygame.transform.scale(bg, (1280,720))
        bg_rect = scaled_bg.get_rect(x=0,y=0)
        
        textbox = pygame.image.load('assets/textbox.png')
        scaled_texbox = pygame.transform.scale(textbox, (1100,250))
        textbox_rect = scaled_texbox.get_rect(x=80,y=475)

        screen.blit(scaled_bg, bg_rect)
        PAUSE.update(screen)
        PAUSE.changeColor(MENU_MOUSE_POS)
        romanafter(125,-0.5)
        loverafter(660, 200)
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
                    if active_message == 3:
                        continue_button_press = True                # adjust sini kalau ada byk message
                        dialogue31()
                if continue_button_press:
                    return

        snip = font.render(message[0:counter//speed], True, 'white')
        screen.blit(snip, (200, 570))

        pygame.display.flip()

def dialogue31():  # lover textbox
    font = pygame.font.Font("assets/Font/ARCADE.TTF", 24)
    timer = pygame.time.Clock()
    messages = ('Luna : What was it you were going to say?',
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

        bg = pygame.image.load('assets/countryhosp2.png')
        scaled_bg = pygame.transform.scale(bg, (1280,720))
        bg_rect = scaled_bg.get_rect(x=0,y=0)
        
        textbox = pygame.image.load('assets/textboxlover.png')
        scaled_texbox = pygame.transform.scale(textbox, (850,450))
        textbox_rect = scaled_texbox.get_rect(x=220,y=410)

        screen.blit(scaled_bg, bg_rect)
        PAUSE.update(screen)
        PAUSE.changeColor(MENU_MOUSE_POS)
        loverafter(660, 200)
        romanafter(125,-0.5)
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
                    if active_message == 1:               # adjust sini kalau ada byk message
                        continue_button_press = True
                        dialogue32()
                if continue_button_press:
                    return

        snip = font.render(message[0:counter//speed], True, 'white')
        screen.blit(snip, (295, 600))

        pygame.display.flip()

def dialogue32():  # roman textbox
    font = pygame.font.Font("assets/Font/ARCADE.TTF", 24)
    timer = pygame.time.Clock()
    messages = ('Roman : It\'s nothing..',
                'Roman : Come on, we should\'nt keep the doc waiting.',
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

        bg = pygame.image.load('assets/countryhosp2.png')
        scaled_bg = pygame.transform.scale(bg, (1280,720))
        bg_rect = scaled_bg.get_rect(x=0,y=0)
        
        textbox = pygame.image.load('assets/textbox.png')
        scaled_texbox = pygame.transform.scale(textbox, (1100,250))
        textbox_rect = scaled_texbox.get_rect(x=80,y=475)

        screen.blit(scaled_bg, bg_rect)
        PAUSE.update(screen)
        PAUSE.changeColor(MENU_MOUSE_POS)
        romanafter(125,-0.5)
        loverafter(660, 200)
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
                        continue_button_press = True                # adjust sini kalau ada byk message
                        dialogue33()
                if continue_button_press:
                    return

        snip = font.render(message[0:counter//speed], True, 'white')
        screen.blit(snip, (200, 570))

        pygame.display.flip()

def dialogue33():  # roman textbox
    font = pygame.font.Font("assets/Font/ARCADE.TTF", 24)
    timer = pygame.time.Clock()
    messages = ('Roman : We\'re here doc!',
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

        bg = pygame.image.load('assets/countrytaxi.png')
        scaled_bg = pygame.transform.scale(bg, (1280,720))
        bg_rect = scaled_bg.get_rect(x=0,y=0)
        
        textbox = pygame.image.load('assets/textbox.png')
        scaled_texbox = pygame.transform.scale(textbox, (1100,250))
        textbox_rect = scaled_texbox.get_rect(x=80,y=475)

        screen.blit(scaled_bg, bg_rect)
        PAUSE.update(screen)
        PAUSE.changeColor(MENU_MOUSE_POS)
        romanafter(75,-0.5)
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
                        dialogue34()
                if continue_button_press:
                    return

        snip = font.render(message[0:counter//speed], True, 'white')
        screen.blit(snip, (200, 570))

        pygame.display.flip()

def dialogue34():  # roman textbox
    font = pygame.font.Font("assets/Font/ARCADE.TTF", 24)
    timer = pygame.time.Clock()
    messages = ('Roman : Thank you so much for letting us stay here while she recovers doc.',
                'Roman : We really appreciate it.',
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

        bg = pygame.image.load('assets/countrytaxi.png')
        scaled_bg = pygame.transform.scale(bg, (1280,720))
        bg_rect = scaled_bg.get_rect(x=0,y=0)
        
        textbox = pygame.image.load('assets/textbox.png')
        scaled_texbox = pygame.transform.scale(textbox, (1100,250))
        textbox_rect = scaled_texbox.get_rect(x=80,y=475)

        screen.blit(scaled_bg, bg_rect)
        PAUSE.update(screen)
        PAUSE.changeColor(MENU_MOUSE_POS)
        romanafter(350,-0.5)
        doctor(700, 80)
        loverafter(60, 200)
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
                        continue_button_press = True                # adjust sini kalau ada byk message
                        dialogue35()
                if continue_button_press:
                    return

        snip = font.render(message[0:counter//speed], True, 'white')
        screen.blit(snip, (200, 570))

        pygame.display.flip()

def dialogue35():  # lover textbox
    font = pygame.font.Font("assets/Font/ARCADE.TTF", 24)
    timer = pygame.time.Clock()
    messages = ('Luna : You have my gratitude aswell Doctor.',
                'Luna : Thank you so much.',
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

        bg = pygame.image.load('assets/countrytaxi.png')
        scaled_bg = pygame.transform.scale(bg, (1280,720))
        bg_rect = scaled_bg.get_rect(x=0,y=0)
        
        textbox = pygame.image.load('assets/textboxlover.png')
        scaled_texbox = pygame.transform.scale(textbox, (850,450))
        textbox_rect = scaled_texbox.get_rect(x=220,y=410)

        screen.blit(scaled_bg, bg_rect)
        PAUSE.update(screen)
        PAUSE.changeColor(MENU_MOUSE_POS)
        romanafter(350,-0.5)
        doctor(700, 80)
        loverafter(60, 200)
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
                    if active_message == 2:               # adjust sini kalau ada byk message
                        continue_button_press = True
                        dialogue36()
                if continue_button_press:
                    return

        snip = font.render(message[0:counter//speed], True, 'white')
        screen.blit(snip, (295, 600))

        pygame.display.flip()

def dialogue36():  # roman textbox
    font = pygame.font.Font("assets/Font/ARCADE.TTF", 24)
    timer = pygame.time.Clock()
    messages = ('Doctor : Haha, it\'s my pleasure',
                'Doctor : It\'s my job after all!',
                'Doctor : But before you leave',
                'Doctor : I haven\'t quite catch your name yet',
                'Roman : Ah, the name\'s Roman doc, and this is Luna',
                'Doctor : Nice to meet you both, I hope we will cross path in the future',
                'Roman : Again, thank you for everything doc.',
                'Doctor : You\'re welcome, safe travels both of you!',
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

        bg = pygame.image.load('assets/countrytaxi.png')
        scaled_bg = pygame.transform.scale(bg, (1280,720))
        bg_rect = scaled_bg.get_rect(x=0,y=0)
        
        textbox = pygame.image.load('assets/textbox.png')
        scaled_texbox = pygame.transform.scale(textbox, (1100,250))
        textbox_rect = scaled_texbox.get_rect(x=80,y=475)

        screen.blit(scaled_bg, bg_rect)
        PAUSE.update(screen)
        PAUSE.changeColor(MENU_MOUSE_POS)
        romanafter(350,-0.5)
        doctor(700, 80)
        loverafter(60, 200)
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
                        continue_button_press = True                # adjust sini kalau ada byk message
                        dialogue37()
                if continue_button_press:
                    return

        snip = font.render(message[0:counter//speed], True, 'white')
        screen.blit(snip, (200, 570))

        pygame.display.flip()

def dialogue37():  # roman textbox
    font = pygame.font.Font("assets/Font/ARCADE.TTF", 24)
    timer = pygame.time.Clock()
    messages = ('Roman : The doc really is a sweet man',
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

        bg = pygame.image.load('assets/countrytaxi.png')
        scaled_bg = pygame.transform.scale(bg, (1280,720))
        bg_rect = scaled_bg.get_rect(x=0,y=0)
        
        textbox = pygame.image.load('assets/textbox.png')
        scaled_texbox = pygame.transform.scale(textbox, (1100,250))
        textbox_rect = scaled_texbox.get_rect(x=80,y=475)

        screen.blit(scaled_bg, bg_rect)
        PAUSE.update(screen)
        PAUSE.changeColor(MENU_MOUSE_POS)
        romanafter(700,-0.5)
        loverafter(60, 200)
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
                        dialogue38()
                if continue_button_press:
                    return

        snip = font.render(message[0:counter//speed], True, 'white')
        screen.blit(snip, (200, 570))

        pygame.display.flip()

def dialogue38():  # lover textbox
    font = pygame.font.Font("assets/Font/ARCADE.TTF", 24)
    timer = pygame.time.Clock()
    messages = ('Luna : He sure is.',
                'Luna : Now why did you even call a cab in the first place?',
                'Luna : You got somewhere in mind?',
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

        bg = pygame.image.load('assets/countrytaxi.png')
        scaled_bg = pygame.transform.scale(bg, (1280,720))
        bg_rect = scaled_bg.get_rect(x=0,y=0)
        
        textbox = pygame.image.load('assets/textboxlover.png')
        scaled_texbox = pygame.transform.scale(textbox, (850,450))
        textbox_rect = scaled_texbox.get_rect(x=220,y=410)

        screen.blit(scaled_bg, bg_rect)
        PAUSE.update(screen)
        PAUSE.changeColor(MENU_MOUSE_POS)
        romanafter(700,-0.5)
        loverafter(60, 200)
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
                        dialogue39()
                if continue_button_press:
                    return

        snip = font.render(message[0:counter//speed], True, 'white')
        screen.blit(snip, (295, 600))

        pygame.display.flip()

def dialogue39():  # roman textbox
    font = pygame.font.Font("assets/Font/ARCADE.TTF", 24)
    timer = pygame.time.Clock()
    messages = ('Roman : Actually, I don\'t..',
                'Roman : I just wanted to get out of here..',
                'Roman : I can\'t process what just happened..',
                'Roman : To Emir...',
                'Roman : And what you did..',
                'Roman : Sure, I had my suspicions with Emir but..',
                'Roman : ...',
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

        bg = pygame.image.load('assets/countrytaxi.png')
        scaled_bg = pygame.transform.scale(bg, (1280,720))
        bg_rect = scaled_bg.get_rect(x=0,y=0)
        
        textbox = pygame.image.load('assets/textbox.png')
        scaled_texbox = pygame.transform.scale(textbox, (1100,250))
        textbox_rect = scaled_texbox.get_rect(x=80,y=475)

        screen.blit(scaled_bg, bg_rect)
        PAUSE.update(screen)
        PAUSE.changeColor(MENU_MOUSE_POS)
        romanafter(700,-0.5)
        loverafter(60, 200)
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
                        dialogue40()
                if continue_button_press:
                    return

        snip = font.render(message[0:counter//speed], True, 'white')
        screen.blit(snip, (200, 570))

        pygame.display.flip()

def dialogue40():  # lover textbox
    font = pygame.font.Font("assets/Font/ARCADE.TTF", 24)
    timer = pygame.time.Clock()
    messages = ('Luna : ...',
                'Luna : Look, I\'m sure there\'s a lot..',
                'Luna : going on in your head right now..',
                'Luna : I also have to justify what I did..',
                'Luna : So, How about we head back to my place?',
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

        bg = pygame.image.load('assets/countrytaxi.png')
        scaled_bg = pygame.transform.scale(bg, (1280,720))
        bg_rect = scaled_bg.get_rect(x=0,y=0)
        
        textbox = pygame.image.load('assets/textboxlover.png')
        scaled_texbox = pygame.transform.scale(textbox, (850,450))
        textbox_rect = scaled_texbox.get_rect(x=220,y=410)

        screen.blit(scaled_bg, bg_rect)
        PAUSE.update(screen)
        PAUSE.changeColor(MENU_MOUSE_POS)
        romanafter(700,-0.5)
        loverafter(60, 200)
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
                    if active_message == 5:               # adjust sini kalau ada byk message
                        continue_button_press = True
                        dialogue41()
                if continue_button_press:
                    return

        snip = font.render(message[0:counter//speed], True, 'white')
        screen.blit(snip, (295, 600))

        pygame.display.flip()

def dialogue41():  # roman textbox
    font = pygame.font.Font("assets/Font/ARCADE.TTF", 24)
    timer = pygame.time.Clock()
    messages = ('Roman : Sure, I\'m on with that.',
                'Roman : Let\'s get going.',
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

        bg = pygame.image.load('assets/countrytaxi.png')
        scaled_bg = pygame.transform.scale(bg, (1280,720))
        bg_rect = scaled_bg.get_rect(x=0,y=0)
        
        textbox = pygame.image.load('assets/textbox.png')
        scaled_texbox = pygame.transform.scale(textbox, (1100,250))
        textbox_rect = scaled_texbox.get_rect(x=80,y=475)

        screen.blit(scaled_bg, bg_rect)
        PAUSE.update(screen)
        PAUSE.changeColor(MENU_MOUSE_POS)
        romanafter(700,-0.5)
        loverafter(60, 200)
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
                        continue_button_press = True                # adjust sini kalau ada byk message
                        dialogue42()
                if continue_button_press:
                    return

        snip = font.render(message[0:counter//speed], True, 'white')
        screen.blit(snip, (200, 570))

        pygame.display.flip()

def dialogue42():  # black/narrator textbox
    font = pygame.font.Font("assets/Font/ARCADE.TTF", 24)
    timer = pygame.time.Clock()
    messages = ('They both entered the taxi..',
                'Both feeling..',
                'Well..',
                '"Complicated" would be an understatement..',
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

        bg = pygame.image.load('assets/countrytaxi.png')
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
                    if active_message == 4:               # adjust sini kalau ada byk message
                        continue_button_press = True
                        dialogue43()
                if continue_button_press:
                    return

        snip = font.render(message[0:counter // speed], True, white)
        screen.blit(snip, (dialog_x + 50, dialog_y + 30))  # adjust text pos sini

        pygame.display.flip()

def dialogue43():  # black/narrator textbox
    font = pygame.font.Font("assets/Font/ARCADE.TTF", 24)
    timer = pygame.time.Clock()
    messages = ('Nevertheless, the ride went on..',
                'The both of them determined to make things right..',
                'All that they know for sure..',
                'Is that they will get their answers when they get back.',
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

    drive.play(-1)

    run = True
    while run:
        MENU_MOUSE_POS = pygame.mouse.get_pos()

        PAUSE = Button(image=pygame.image.load("assets/pause.png"), pos=(50, 50), 
                            text_input="           ", font=textbutton_font(21), base_color="black", hovering_color="#FF3131")

        bg = pygame.image.load('assets/countryroad.png')
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
                    if active_message == 4:               # adjust sini kalau ada byk message
                        continue_button_press = True
                        drive.stop()
                        dialogue44()
                if continue_button_press:
                    return

        snip = font.render(message[0:counter // speed], True, white)
        screen.blit(snip, (dialog_x + 50, dialog_y + 30))  # adjust text pos sini

        pygame.display.flip()

def dialogue44():  # centered textbox
    font = pygame.font.Font("assets/Font/ARCADE.TTF", 74)
    timer = pygame.time.Clock()
    messages = ('TWO HOURS LATER', '...')
    snip = font.render('', True, white)
    counter = 0
    speed = 5
    active_message = 0
    message = messages[active_message]
    continue_button_press = False

    dialogue_box_width = 1160  # Increased width
    dialogue_box_height = 400  # Increased height
    dialogue_box_alpha = 225

    drive.stop()

    run = True
    while run:
        MENU_MOUSE_POS = pygame.mouse.get_pos()

        PAUSE = Button(image=pygame.image.load("assets/pause.png"), pos=(50, 50), 
                            text_input="           ", font=textbutton_font(21), base_color="black", hovering_color="#FF3131")

        bg = pygame.image.load('assets/blackscreen.png')
        scaled_bg = pygame.transform.scale(bg, (1280, 720))
        bg_rect = scaled_bg.get_rect(x=0, y=0)
        screen.blit(scaled_bg, bg_rect)

        PAUSE.update(screen)
        PAUSE.changeColor(MENU_MOUSE_POS)

        # Center the dialogue box
        dialog_x = (screen.get_width() - dialogue_box_width) // 2
        dialog_y = (screen.get_height() - dialogue_box_height) // 2

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
                    if active_message == 1:  # Adjust if there are more messages
                        continue_button_press = True
                        dialogue45()
                if continue_button_press:
                    return

        # Render the current part of the message
        snip = font.render(message[0:counter // speed], True, white)
        
        # Get the size of the rendered text
        text_width, text_height = snip.get_size()
        
        # Center the text within the dialogue box
        text_x = dialog_x + (dialogue_box_width - text_width) // 2
        text_y = dialog_y + (dialogue_box_height - text_height) // 2
        
        screen.blit(snip, (text_x, text_y))

        pygame.display.flip()

def dialogue45():  # lover textbox
    font = pygame.font.Font("assets/Font/ARCADE.TTF", 24)
    timer = pygame.time.Clock()
    messages = ('Luna : Oh god..',
                'Luna : I never would\'ve thought..',
                'I would be so glad to see my own house.',
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

        bg = pygame.image.load('assets/Chapter2/houselover.png')
        scaled_bg = pygame.transform.scale(bg, (1280,720))
        bg_rect = scaled_bg.get_rect(x=0,y=0)
        
        textbox = pygame.image.load('assets/textboxlover.png')
        scaled_texbox = pygame.transform.scale(textbox, (850,450))
        textbox_rect = scaled_texbox.get_rect(x=220,y=410)

        screen.blit(scaled_bg, bg_rect)
        PAUSE.update(screen)
        PAUSE.changeColor(MENU_MOUSE_POS)
        romanafter(700,-0.5)
        loverafter(60, 200)
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
                        dialogue46()
                if continue_button_press:
                    return

        snip = font.render(message[0:counter//speed], True, 'white')
        screen.blit(snip, (295, 600))

        pygame.display.flip()

def dialogue46():  # roman textbox
    font = pygame.font.Font("assets/Font/ARCADE.TTF", 24)
    timer = pygame.time.Clock()
    messages = ('Roman : Wow! Your house is..',
                'Roman : It\'s not even a house at this point.',
                'Roman : It\'s a mansion!',
                'Roman : I guess I did stay in prison for too long..',
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

        bg = pygame.image.load('assets/Chapter2/houselover.png')
        scaled_bg = pygame.transform.scale(bg, (1280,720))
        bg_rect = scaled_bg.get_rect(x=0,y=0)
        
        textbox = pygame.image.load('assets/textbox.png')
        scaled_texbox = pygame.transform.scale(textbox, (1100,250))
        textbox_rect = scaled_texbox.get_rect(x=80,y=475)

        screen.blit(scaled_bg, bg_rect)
        PAUSE.update(screen)
        PAUSE.changeColor(MENU_MOUSE_POS)
        romanafter(700,-0.5)
        loverafter(60, 200)
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
                        dialogue47()
                if continue_button_press:
                    return
                
        snip = font.render(message[0:counter//speed], True, 'white')
        screen.blit(snip, (200, 570))

        pygame.display.flip()
                
def dialogue47():  # lover textbox
    font = pygame.font.Font("assets/Font/ARCADE.TTF", 24)
    timer = pygame.time.Clock()
    messages = ('Luna : Come on, let\'s head inside.',
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

        bg = pygame.image.load('assets/Chapter2/houselover.png')
        scaled_bg = pygame.transform.scale(bg, (1280,720))
        bg_rect = scaled_bg.get_rect(x=0,y=0)
        
        textbox = pygame.image.load('assets/textboxlover.png')
        scaled_texbox = pygame.transform.scale(textbox, (850,450))
        textbox_rect = scaled_texbox.get_rect(x=220,y=410)

        screen.blit(scaled_bg, bg_rect)
        PAUSE.update(screen)
        PAUSE.changeColor(MENU_MOUSE_POS)
        romanafter(700,-0.5)
        loverafter(60, 200)
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
                    if active_message == 1:               # adjust sini kalau ada byk message
                        continue_button_press = True
                        dialogue48()
                if continue_button_press:
                    return

        snip = font.render(message[0:counter//speed], True, 'white')
        screen.blit(snip, (295, 600))

        pygame.display.flip()

def dialogue48():  # roman textbox
    font = pygame.font.Font("assets/Font/ARCADE.TTF", 24)
    timer = pygame.time.Clock()
    messages = ('Roman : It\'s even crazier on the inside..',
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

        bg = pygame.image.load('assets/loverliving.png')
        scaled_bg = pygame.transform.scale(bg, (1280,720))
        bg_rect = scaled_bg.get_rect(x=0,y=0)
        
        textbox = pygame.image.load('assets/textbox.png')
        scaled_texbox = pygame.transform.scale(textbox, (1100,250))
        textbox_rect = scaled_texbox.get_rect(x=80,y=475)

        screen.blit(scaled_bg, bg_rect)
        PAUSE.update(screen)
        PAUSE.changeColor(MENU_MOUSE_POS)
        romanafter(700,-0.5)
        loverafter(60, 200)
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
                        dialogue49()
                if continue_button_press:
                    return
                
        snip = font.render(message[0:counter//speed], True, 'white')
        screen.blit(snip, (200, 570))

        pygame.display.flip()

def dialogue49():  # lover textbox
    font = pygame.font.Font("assets/Font/ARCADE.TTF", 24)
    timer = pygame.time.Clock()
    messages = ('Luna : Hehe.. You\'re exaggerating.',
                'Luna : It\'s been so long Roman...',
                'Luna : How did things get so wrong..?',
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

        bg = pygame.image.load('assets/loverliving.png')
        scaled_bg = pygame.transform.scale(bg, (1280,720))
        bg_rect = scaled_bg.get_rect(x=0,y=0)
        
        textbox = pygame.image.load('assets/textboxlover.png')
        scaled_texbox = pygame.transform.scale(textbox, (850,450))
        textbox_rect = scaled_texbox.get_rect(x=220,y=410)

        screen.blit(scaled_bg, bg_rect)
        PAUSE.update(screen)
        PAUSE.changeColor(MENU_MOUSE_POS)
        romanafter(700,-0.5)
        loverafter(60, 200)
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
                        dialogue50()
                if continue_button_press:
                    return

        snip = font.render(message[0:counter//speed], True, 'white')
        screen.blit(snip, (295, 600))

        pygame.display.flip()

def dialogue50():  # roman textbox
    font = pygame.font.Font("assets/Font/ARCADE.TTF", 24)
    timer = pygame.time.Clock()
    messages = ('Roman : Luna...',
                'Roman : Why did you kill Emir...',
                'Roman : You even wiped out his subordinates..',
                'Roman : You know I\'m a criminal on the run don\'t you...?',
                'Roman : We had planned on how to avoid the police...',
                'Roman : Why...',
                'Roman : WHY LUNA !!',
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

        bg = pygame.image.load('assets/loverliving.png')
        scaled_bg = pygame.transform.scale(bg, (1280,720))
        bg_rect = scaled_bg.get_rect(x=0,y=0)
        
        textbox = pygame.image.load('assets/textbox.png')
        scaled_texbox = pygame.transform.scale(textbox, (1100,250))
        textbox_rect = scaled_texbox.get_rect(x=80,y=475)

        screen.blit(scaled_bg, bg_rect)
        PAUSE.update(screen)
        PAUSE.changeColor(MENU_MOUSE_POS)
        romanafter(700,-0.5)
        loverafter(60, 200)
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
                        dialogue51()
                if continue_button_press:
                    return
                
        snip = font.render(message[0:counter//speed], True, 'white')
        screen.blit(snip, (200, 570))

        pygame.display.flip()

def dialogue51():  # lover textbox
    font = pygame.font.Font("assets/Font/ARCADE.TTF", 24)
    timer = pygame.time.Clock()
    messages = ('Luna : Calm down Roman.',
                'Luna : I have no idea what you went through with him',
                'Luna : But I have my reasons.',
                'Luna : Take a look at this.',
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

        bg = pygame.image.load('assets/loverliving.png')
        scaled_bg = pygame.transform.scale(bg, (1280,720))
        bg_rect = scaled_bg.get_rect(x=0,y=0)
        
        textbox = pygame.image.load('assets/textboxlover.png')
        scaled_texbox = pygame.transform.scale(textbox, (850,450))
        textbox_rect = scaled_texbox.get_rect(x=220,y=410)

        screen.blit(scaled_bg, bg_rect)
        PAUSE.update(screen)
        PAUSE.changeColor(MENU_MOUSE_POS)
        romanafter(700,-0.5)
        loverafter(60, 200)
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
                        dialogue52()
                if continue_button_press:
                    return

        snip = font.render(message[0:counter//speed], True, 'white')
        screen.blit(snip, (295, 600))

        pygame.display.flip()

def dialogue52():  # lover textbox / showing clues
    font = pygame.font.Font("assets/Font/ARCADE.TTF", 24)
    timer = pygame.time.Clock()
    messages = ('Luna : Documents of my findings..',
                'Luna : Your old man\'s diary..',
                'Luna : A bullet shell from your old house..',
                'Luna : A knife used for stabbing..',
                'Luna : Your old childhood book..',
                'Luna : Your family\'s portrait',
                'Luna : A picture taken from your neighbour that night..')
    snip = font.render('', True, 'white')
    counter = 0
    speed = 1
    active_message = 0
    message = messages[active_message]
    show_prompt = False

    # Prompt images
    prompt_images_original = ['assets/cluesimg/document.png', 'assets/cluesimg/daddiary.png', 'assets/cluesimg/bullet.png', 'assets/cluesimg/oldknife.png', 'assets/cluesimg/mcfavbook.png', 'assets/cluesimg/familyframe.png', 'assets/cluesimg/polaroid.png']
    prompt_images_scaled = [pygame.transform.scale(pygame.image.load(image_path), (150, 115)) for image_path in prompt_images_original]

    run = True
    while run:
        MENU_MOUSE_POS = pygame.mouse.get_pos()

        PAUSE = Button(image=pygame.image.load("assets/pause.png"), pos=(50, 50), 
                            text_input="           ", font=textbutton_font(21), base_color="black", hovering_color="#FF3131")

        bg = pygame.image.load('assets/loverliving.png')
        scaled_bg = pygame.transform.scale(bg, (1280, 720))
        bg_rect = scaled_bg.get_rect(x=0, y=0)
        
        textbox = pygame.image.load('assets/textboxlover.png')
        scaled_texbox = pygame.transform.scale(textbox, (850, 450))
        textbox_rect = scaled_texbox.get_rect(x=220, y=410)

        screen.blit(scaled_bg, bg_rect)
        PAUSE.update(screen)
        PAUSE.changeColor(MENU_MOUSE_POS)
        romanafter(700, -0.5)
        loverafter(60, 200)
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
                        show_prompt = False
                    else:
                        counter = speed * len(message)
                    if active_message >= len(messages) - 1 and counter >= speed * len(message):
                        run = False

        snip = font.render(message[0:counter // speed], True, 'white')
        screen.blit(snip, (295, 600))

        # Display the corresponding prompt image in the middle of the screen
        if active_message < len(prompt_images_scaled):
            prompt_image = prompt_images_scaled[active_message]
            prompt_image_rect = prompt_image.get_rect(center=(640, 360))
            screen.blit(prompt_image, prompt_image_rect)

        pygame.display.flip()

    # Call another function after the dialogue finishes
    dialogue53()

def dialogue53():  # black/narrator textbox
    font = pygame.font.Font("assets/Font/ARCADE.TTF", 24)
    timer = pygame.time.Clock()
    messages = ('Luna then went on about the findings that she found...',
                'Whilst Roman was still in prison...',
                'Roman was absolutely devastated about what she revealed to him...',
                'His own comrade in arms...',
                'His prison-break partner...',
                'was the one who massacred his family...',
                'Luna went on explaining the details of her findings...',
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

        bg = pygame.image.load('assets/loverliving.png')
        scaled_bg = pygame.transform.scale(bg, (1280,720))
        bg_rect = scaled_bg.get_rect(x=0,y=0)
        screen.blit(scaled_bg, bg_rect)

        PAUSE.update(screen)
        PAUSE.changeColor(MENU_MOUSE_POS)

        dialog_x = (screen.get_width() - dialogue_box_width) // 2
        dialog_y = (screen.get_height() - dialogue_box_height) - 25    # adjust dialogue box sini

        dialogue_box = pygame.Surface((dialogue_box_width, dialogue_box_height), pygame.SRCALPHA)
        dialogue_box.fill((0, 0, 0, dialogue_box_alpha))

        romanafter(700,-0.5)
        loverafter(60, 200)

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
                        dialogue54()
                if continue_button_press:
                    return

        snip = font.render(message[0:counter // speed], True, white)
        screen.blit(snip, (dialog_x + 50, dialog_y + 30))  # adjust text pos sini

        pygame.display.flip()

def dialogue54():  # centered textbox
    font = pygame.font.Font("assets/Font/ARCADE.TTF", 74)
    timer = pygame.time.Clock()
    messages = ('AFTER A WHILE', '...')
    snip = font.render('', True, white)
    counter = 0
    speed = 5
    active_message = 0
    message = messages[active_message]
    continue_button_press = False

    dialogue_box_width = 1160  # Increased width
    dialogue_box_height = 500  # Increased height
    dialogue_box_alpha = 225

    run = True
    while run:
        MENU_MOUSE_POS = pygame.mouse.get_pos()

        PAUSE = Button(image=pygame.image.load("assets/pause.png"), pos=(50, 50), 
                            text_input="           ", font=textbutton_font(21), base_color="black", hovering_color="#FF3131")

        bg = pygame.image.load('assets/loverliving.png')
        scaled_bg = pygame.transform.scale(bg, (1280, 720))
        bg_rect = scaled_bg.get_rect(x=0, y=0)
        screen.blit(scaled_bg, bg_rect)

        PAUSE.update(screen)
        PAUSE.changeColor(MENU_MOUSE_POS)

        # Center the dialogue box
        dialog_x = (screen.get_width() - dialogue_box_width) // 2
        dialog_y = (screen.get_height() - dialogue_box_height) // 2

        dialogue_box = pygame.Surface((dialogue_box_width, dialogue_box_height), pygame.SRCALPHA)
        dialogue_box.fill((0, 0, 0, dialogue_box_alpha))

        romanafter(700,-0.5)
        loverafter(60, 200)

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
                    if active_message == 1:  # Adjust if there are more messages
                        continue_button_press = True
                        dialogue55()
                if continue_button_press:
                    return

        # Render the current part of the message
        snip = font.render(message[0:counter // speed], True, white)
        
        # Get the size of the rendered text
        text_width, text_height = snip.get_size()
        
        # Center the text within the dialogue box
        text_x = dialog_x + (dialogue_box_width - text_width) // 2
        text_y = dialog_y + (dialogue_box_height - text_height) // 2
        
        screen.blit(snip, (text_x, text_y))

        pygame.display.flip()

def dialogue55():  # roman textbox
    font = pygame.font.Font("assets/Font/ARCADE.TTF", 24)
    timer = pygame.time.Clock()
    messages = ('Roman : Luna...',
                'Roman : I\'m so sorry that I didn\'t believe you...',
                'Roman : despite you going through these efforts..',
                'Roman : to convince me...',
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

        bg = pygame.image.load('assets/loverliving.png')
        scaled_bg = pygame.transform.scale(bg, (1280,720))
        bg_rect = scaled_bg.get_rect(x=0,y=0)
        
        textbox = pygame.image.load('assets/textbox.png')
        scaled_texbox = pygame.transform.scale(textbox, (1100,250))
        textbox_rect = scaled_texbox.get_rect(x=80,y=475)

        screen.blit(scaled_bg, bg_rect)
        PAUSE.update(screen)
        PAUSE.changeColor(MENU_MOUSE_POS)
        romanafter(700,-0.5)
        loverafter(60, 200)
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
                        dialogue56()
                if continue_button_press:
                    return
                
        snip = font.render(message[0:counter//speed], True, 'white')
        screen.blit(snip, (200, 570))

        pygame.display.flip()

def dialogue56():  # lover textbox
    font = pygame.font.Font("assets/Font/ARCADE.TTF", 24)
    timer = pygame.time.Clock()
    messages = ('Luna : It\'s all in the past now..',
                'Luna : The question is..',
                'Luna : What will you do now..?',
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

        bg = pygame.image.load('assets/loverliving.png')
        scaled_bg = pygame.transform.scale(bg, (1280,720))
        bg_rect = scaled_bg.get_rect(x=0,y=0)
        
        textbox = pygame.image.load('assets/textboxlover.png')
        scaled_texbox = pygame.transform.scale(textbox, (850,450))
        textbox_rect = scaled_texbox.get_rect(x=220,y=410)

        screen.blit(scaled_bg, bg_rect)
        PAUSE.update(screen)
        PAUSE.changeColor(MENU_MOUSE_POS)
        romanafter(700,-0.5)
        loverafter(60, 200)
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
                        dialogue56()
                if continue_button_press:
                    return

        snip = font.render(message[0:counter//speed], True, 'white')
        screen.blit(snip, (295, 600))

        pygame.display.flip()

def dialogue57():  # roman textbox
    font = pygame.font.Font("assets/Font/ARCADE.TTF", 24)
    timer = pygame.time.Clock()
    messages = ('Roman : I...',
                'Roman : I don\'t know...',
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

        bg = pygame.image.load('assets/loverliving.png')
        scaled_bg = pygame.transform.scale(bg, (1280,720))
        bg_rect = scaled_bg.get_rect(x=0,y=0)
        
        textbox = pygame.image.load('assets/textbox.png')
        scaled_texbox = pygame.transform.scale(textbox, (1100,250))
        textbox_rect = scaled_texbox.get_rect(x=80,y=475)

        screen.blit(scaled_bg, bg_rect)
        PAUSE.update(screen)
        PAUSE.changeColor(MENU_MOUSE_POS)
        romanafter(700,-0.5)
        loverafter(60, 200)
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
                        continue_button_press = True
                        pygame.mixer.music.stop()                # adjust sini kalau ada byk message
                        dialogue58()
                if continue_button_press:
                    return
                
        snip = font.render(message[0:counter//speed], True, 'white')
        screen.blit(snip, (200, 570))

        pygame.display.flip()

def dialogue58():  # lover textbox
    font = pygame.font.Font("assets/Font/ARCADE.TTF", 24)
    timer = pygame.time.Clock()
    messages = ('Luna : Roman...',
                'Luna : Come with me...',
                'Luna : Let\'s escape together...',
                '...')
    snip = font.render('', True, white)
    counter = 0
    speed = 1
    active_message = 0
    message = messages[active_message]
    continue_button_press = False

    pygame.mixer.music.load('assets/Audio/normalend.mp3')
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.5)

    run = True
    while run:
        MENU_MOUSE_POS = pygame.mouse.get_pos()

        PAUSE = Button(image=pygame.image.load("assets/pause.png"), pos=(50, 50), 
                            text_input="           ", font=textbutton_font(21), base_color="black", hovering_color="#FF3131")

        bg = pygame.image.load('assets/loverliving.png')
        scaled_bg = pygame.transform.scale(bg, (1280,720))
        bg_rect = scaled_bg.get_rect(x=0,y=0)
        
        textbox = pygame.image.load('assets/textboxlover.png')
        scaled_texbox = pygame.transform.scale(textbox, (850,450))
        textbox_rect = scaled_texbox.get_rect(x=220,y=410)

        screen.blit(scaled_bg, bg_rect)
        PAUSE.update(screen)
        PAUSE.changeColor(MENU_MOUSE_POS)
        romanafter(700,-0.5)
        loverafter(60, 200)
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
                        dialogue59()
                if continue_button_press:
                    return

        snip = font.render(message[0:counter//speed], True, 'white')
        screen.blit(snip, (295, 600))

        pygame.display.flip()

def dialogue59():  # roman textbox
    font = pygame.font.Font("assets/Font/ARCADE.TTF", 24)
    timer = pygame.time.Clock()
    messages = ('Roman : What?!',
                'Roman : Are you serious?!',
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

        bg = pygame.image.load('assets/loverliving.png')
        scaled_bg = pygame.transform.scale(bg, (1280,720))
        bg_rect = scaled_bg.get_rect(x=0,y=0)
        
        textbox = pygame.image.load('assets/textbox.png')
        scaled_texbox = pygame.transform.scale(textbox, (1100,250))
        textbox_rect = scaled_texbox.get_rect(x=80,y=475)

        screen.blit(scaled_bg, bg_rect)
        PAUSE.update(screen)
        PAUSE.changeColor(MENU_MOUSE_POS)
        romanafter(700,-0.5)
        loverafter(60, 200)
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
                        continue_button_press = True                # adjust sini kalau ada byk message
                        dialogue60()
                if continue_button_press:
                    return
                
        snip = font.render(message[0:counter//speed], True, 'white')
        screen.blit(snip, (200, 570))

        pygame.display.flip()

def dialogue60():  # lover textbox
    font = pygame.font.Font("assets/Font/ARCADE.TTF", 24)
    timer = pygame.time.Clock()
    messages = ('Luna : I\'m dead serious...',
                'Luna : Let\'s make up for our lost time...',
                'Luna : Together...',
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

        bg = pygame.image.load('assets/loverliving.png')
        scaled_bg = pygame.transform.scale(bg, (1280,720))
        bg_rect = scaled_bg.get_rect(x=0,y=0)
        
        textbox = pygame.image.load('assets/textboxlover.png')
        scaled_texbox = pygame.transform.scale(textbox, (850,450))
        textbox_rect = scaled_texbox.get_rect(x=220,y=410)

        screen.blit(scaled_bg, bg_rect)
        PAUSE.update(screen)
        PAUSE.changeColor(MENU_MOUSE_POS)
        romanafter(700,-0.5)
        loverafter(60, 200)
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
                        dialogue61()
                if continue_button_press:
                    return

        snip = font.render(message[0:counter//speed], True, 'white')
        screen.blit(snip, (295, 600))

        pygame.display.flip()

def dialogue61():  # roman textbox
    font = pygame.font.Font("assets/Font/ARCADE.TTF", 24)
    timer = pygame.time.Clock()
    messages = ('Roman : Luna..',
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

        bg = pygame.image.load('assets/loverliving.png')
        scaled_bg = pygame.transform.scale(bg, (1280,720))
        bg_rect = scaled_bg.get_rect(x=0,y=0)
        
        textbox = pygame.image.load('assets/textbox.png')
        scaled_texbox = pygame.transform.scale(textbox, (1100,250))
        textbox_rect = scaled_texbox.get_rect(x=80,y=475)

        screen.blit(scaled_bg, bg_rect)
        PAUSE.update(screen)
        PAUSE.changeColor(MENU_MOUSE_POS)
        romanafter(700,-0.5)
        loverafter(60, 200)
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
                        dialogue62()
                if continue_button_press:
                    return
                
        snip = font.render(message[0:counter//speed], True, 'white')
        screen.blit(snip, (200, 570))

        pygame.display.flip()

def dialogue62():  # black/narrator textbox
    font = pygame.font.Font("assets/Font/ARCADE.TTF", 24)
    timer = pygame.time.Clock()
    messages = ('The two.. united in their thoughts left the house in a hurry.',
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

        bg = pygame.image.load('assets/loverliving.png')
        scaled_bg = pygame.transform.scale(bg, (1280,720))
        bg_rect = scaled_bg.get_rect(x=0,y=0)
        screen.blit(scaled_bg, bg_rect)

        PAUSE.update(screen)
        PAUSE.changeColor(MENU_MOUSE_POS)

        dialog_x = (screen.get_width() - dialogue_box_width) // 2
        dialog_y = (screen.get_height() - dialogue_box_height) - 25    # adjust dialogue box sini

        dialogue_box = pygame.Surface((dialogue_box_width, dialogue_box_height), pygame.SRCALPHA)
        dialogue_box.fill((0, 0, 0, dialogue_box_alpha))

        romanafter(700,-0.5)
        loverafter(60, 200)

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
                    if active_message == 1:               # adjust sini kalau ada byk message
                        continue_button_press = True
                        dialogue63()
                if continue_button_press:
                    return

        snip = font.render(message[0:counter // speed], True, white)
        screen.blit(snip, (dialog_x + 50, dialog_y + 30))  # adjust text pos sini

        pygame.display.flip()

def dialogue63():  # black/narrator textbox
    font = pygame.font.Font("assets/Font/ARCADE.TTF", 24)
    timer = pygame.time.Clock()
    messages = ('They ran off into the night..',
                'Not knowing where fate may lead them..',
                'It doesn\'t matter to them however..',
                'For they have each other..',
                'And that\'s all that matters..',
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

        bg = pygame.image.load('assets/Chapter2/houselover.png')
        scaled_bg = pygame.transform.scale(bg, (1280,720))
        bg_rect = scaled_bg.get_rect(x=0,y=0)
        screen.blit(scaled_bg, bg_rect)

        speedlines = pygame.image.load('assets/speedlines.png')
        scaled_speedlines = pygame.transform.scale(speedlines, (1280,720))
        speedlines_rect = scaled_speedlines.get_rect(x=0,y=0)
        screen.blit(scaled_speedlines, speedlines_rect)

        PAUSE.update(screen)
        PAUSE.changeColor(MENU_MOUSE_POS)

        dialog_x = (screen.get_width() - dialogue_box_width) // 2
        dialog_y = (screen.get_height() - dialogue_box_height) - 25    # adjust dialogue box sini

        dialogue_box = pygame.Surface((dialogue_box_width, dialogue_box_height), pygame.SRCALPHA)
        dialogue_box.fill((0, 0, 0, dialogue_box_alpha))

        romanafter(700,-0.5)
        loverafter(60, 200)

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
                        dialogue64()
                if continue_button_press:
                    return

        snip = font.render(message[0:counter // speed], True, white)
        screen.blit(snip, (dialog_x + 50, dialog_y + 30))  # adjust text pos sini

        pygame.display.flip()

def dialogue64():  # pygame time delay not working
    bg_image = pygame.image.load("assets/blackscreen.png")
    start_time = pygame.time.get_ticks()  

    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.blit(bg_image, (0, 0))

        if pygame.time.get_ticks() - start_time >= 2000:
            dialogue65()
        
        pygame.display.flip()

def dialogue65():  # black/narrator textbox
    font = pygame.font.Font("assets/Font/ARCADE.TTF", 24)
    timer = pygame.time.Clock()
    messages = ('The both of them..',
                'Having fled the country and changing their names..',
                'They lived a quiet life..',
                'Free from their haunting past..',
                'And lived happily ever after..',
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

        bg = pygame.image.load('assets/timeskip.png')
        scaled_bg = pygame.transform.scale(bg, (1280,720))
        bg_rect = scaled_bg.get_rect(x=0,y=0)
        screen.blit(scaled_bg, bg_rect)

        PAUSE.update(screen)
        PAUSE.changeColor(MENU_MOUSE_POS)

        dialog_x = (screen.get_width() - dialogue_box_width) // 2
        dialog_y = (screen.get_height() - dialogue_box_height) - 25    # adjust dialogue box sini

        dialogue_box = pygame.Surface((dialogue_box_width, dialogue_box_height), pygame.SRCALPHA)
        dialogue_box.fill((0, 0, 0, dialogue_box_alpha))

        romanskip(700,100)
        loverskip(60, 200)

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
                        dialogue66()
                if continue_button_press:
                    return

        snip = font.render(message[0:counter // speed], True, white)
        screen.blit(snip, (dialog_x + 50, dialog_y + 30))  # adjust text pos sini

        pygame.display.flip()

def dialogue66():  # centered textbox
    font = pygame.font.Font("assets/Font/ARCADE.TTF", 74)
    timer = pygame.time.Clock()
    messages = ('THE END', '...')
    snip = font.render('', True, white)
    counter = 0
    speed = 5
    active_message = 0
    message = messages[active_message]
    continue_button_press = False

    dialogue_box_width = 1160  # Increased width
    dialogue_box_height = 500  # Increased height
    dialogue_box_alpha = 225

    run = True
    while run:

        bg = pygame.image.load('assets/blackscreen.png')
        scaled_bg = pygame.transform.scale(bg, (1280, 720))
        bg_rect = scaled_bg.get_rect(x=0, y=0)
        screen.blit(scaled_bg, bg_rect)

        # Center the dialogue box
        dialog_x = (screen.get_width() - dialogue_box_width) // 2
        dialog_y = (screen.get_height() - dialogue_box_height) // 2

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
                    if active_message == 1:  # Adjust if there are more messages
                        continue_button_press = True
                        dialogue67()
                if continue_button_press:
                    return

        # Render the current part of the message
        snip = font.render(message[0:counter // speed], True, white)
        
        # Get the size of the rendered text
        text_width, text_height = snip.get_size()
        
        # Center the text within the dialogue box
        text_x = dialog_x + (dialogue_box_width - text_width) // 2
        text_y = dialog_y + (dialogue_box_height - text_height) // 2
        
        screen.blit(snip, (text_x, text_y))

        pygame.display.flip()

def dialogue67():  # centered textbox
    font = pygame.font.Font("assets/Font/ARCADE.TTF", 74)
    timer = pygame.time.Clock()
    messages = ('CONGRATULATIONS!', '...')
    snip = font.render('', True, white)
    counter = 0
    speed = 5
    active_message = 0
    message = messages[active_message]
    continue_button_press = False

    dialogue_box_width = 1160  # Increased width
    dialogue_box_height = 500  # Increased height
    dialogue_box_alpha = 225

    run = True
    while run:

        bg = pygame.image.load('assets/blackscreen.png')
        scaled_bg = pygame.transform.scale(bg, (1280, 720))
        bg_rect = scaled_bg.get_rect(x=0, y=0)
        screen.blit(scaled_bg, bg_rect)

        # Center the dialogue box
        dialog_x = (screen.get_width() - dialogue_box_width) // 2
        dialog_y = (screen.get_height() - dialogue_box_height) // 2

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
                    if active_message == 1:  # Adjust if there are more messages
                        continue_button_press = True
                        dialogue68()
                if continue_button_press:
                    return

        # Render the current part of the message
        snip = font.render(message[0:counter // speed], True, white)
        
        # Get the size of the rendered text
        text_width, text_height = snip.get_size()
        
        # Center the text within the dialogue box
        text_x = dialog_x + (dialogue_box_width - text_width) // 2
        text_y = dialog_y + (dialogue_box_height - text_height) // 2
        
        screen.blit(snip, (text_x, text_y))

        pygame.display.flip()

def dialogue68():  # centered textbox
    font = pygame.font.Font("assets/Font/ARCADE.TTF", 74)
    timer = pygame.time.Clock()
    messages = ('YOU HAVE UNLOCKED', 'NORMAL ENDING', '...')
    snip = font.render('', True, white)
    counter = 0
    speed = 5
    active_message = 0
    message = messages[active_message]
    continue_button_press = False

    dialogue_box_width = 1160  # Increased width
    dialogue_box_height = 500  # Increased height
    dialogue_box_alpha = 225

    run = True
    while run:

        bg = pygame.image.load('assets/blackscreen.png')
        scaled_bg = pygame.transform.scale(bg, (1280, 720))
        bg_rect = scaled_bg.get_rect(x=0, y=0)
        screen.blit(scaled_bg, bg_rect)

        # Center the dialogue box
        dialog_x = (screen.get_width() - dialogue_box_width) // 2
        dialog_y = (screen.get_height() - dialogue_box_height) // 2

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
                    if active_message == 2:  # Adjust if there are more messages
                        continue_button_press = True
                        dialogue69()
                if continue_button_press:
                    return

        # Render the current part of the message
        snip = font.render(message[0:counter // speed], True, white)
        
        # Get the size of the rendered text
        text_width, text_height = snip.get_size()
        
        # Center the text within the dialogue box
        text_x = dialog_x + (dialogue_box_width - text_width) // 2
        text_y = dialog_y + (dialogue_box_height - text_height) // 2
        
        screen.blit(snip, (text_x, text_y))

        pygame.display.flip()

def dialogue69():  # centered textbox
    font = pygame.font.Font("assets/Font/ARCADE.TTF", 74)
    timer = pygame.time.Clock()
    messages = ('THANK YOU FOR PLAYING!', '...')
    snip = font.render('', True, white)
    counter = 0
    speed = 5
    active_message = 0
    message = messages[active_message]
    continue_button_press = False

    dialogue_box_width = 1160  # Increased width
    dialogue_box_height = 500  # Increased height
    dialogue_box_alpha = 225

    run = True
    while run:

        bg = pygame.image.load('assets/blackscreen.png')
        scaled_bg = pygame.transform.scale(bg, (1280, 720))
        bg_rect = scaled_bg.get_rect(x=0, y=0)
        screen.blit(scaled_bg, bg_rect)

        # Center the dialogue box
        dialog_x = (screen.get_width() - dialogue_box_width) // 2
        dialog_y = (screen.get_height() - dialogue_box_height) // 2

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
                    if active_message == 1:  # Adjust if there are more messages
                        continue_button_press = True
                        pygame.quit()
                if continue_button_press:
                    return

        # Render the current part of the message
        snip = font.render(message[0:counter // speed], True, white)
        
        # Get the size of the rendered text
        text_width, text_height = snip.get_size()
        
        # Center the text within the dialogue box
        text_x = dialog_x + (dialogue_box_width - text_width) // 2
        text_y = dialog_y + (dialogue_box_height - text_height) // 2
        
        screen.blit(snip, (text_x, text_y))

        pygame.display.flip()

dialoguebf1()