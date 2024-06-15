import pygame, sys, random
from config import *
from button import Button
from findclues import *
pygame.init()

# BGM n sound effect
keyboard = pygame.mixer.Sound("assets/Audio/keyboard.mp3")
chap2_bgm = pygame.mixer.Sound("assets/Audio/chap2_opening.mp3")
chap2_ending = pygame.mixer.Sound("assets/Audio/chap2_ending.mp3")
phone = pygame.mixer.Sound("assets/Audio/phone.mp3")
rifleshoot = pygame.mixer.Sound("assets/Audio/rifle.mp3")
tirescreech = pygame.mixer.Sound("assets/Audio/tirescreech.mp3")

# background image + scaling
background_images_original = ['assets/cluesbg/clock.png', 'assets/cluesbg/dadstudy.png', 'assets/cluesbg/backyard.png', 'assets/cluesbg/livingroom.png', 'assets/cluesbg/mcroom.png', 'assets/cluesbg/shattered.png', 'assets/cluesbg/neighbourbg.png']
background_images_scaled = [pygame.transform.scale(pygame.image.load(image_path), (1280, 720)) for image_path in background_images_original]

# prompt images + scaling
prompt_images_original = ['assets/cluesimg/document.png', 'assets/cluesimg/daddiary.png', 'assets/cluesimg/bullet.png', 'assets/cluesimg/oldknife.png', 'assets/cluesimg/mcfavbook.png', 'assets/cluesimg/familyframe.png', 'assets/cluesimg/polaroid.png']
prompt_images_scaled = [pygame.transform.scale(pygame.image.load(image_path), (150, 115)) for image_path in prompt_images_original]

background_index = 0
prompt_index = 0
background_image = background_images_scaled[background_index]
image = prompt_images_scaled[prompt_index]
image_rect = image.get_rect()

# font
font_file = 'assets/Font/ARCADECLASSIC.ttf'
custom_font = pygame.font.Font(font_file, 74)
timer_font = pygame.font.Font(font_file, 50)

# variables
qte_time = 3  # Time in seconds to respond to the QTE
qte_triggered = False
qte_start_time = 0
success_count = 0
max_successes = 7  # Maximum number of successes in the game

def draw_text(text, font, color, surface, x, y, alpha=255):
    text_obj = font.render(text, True, color)
    text_obj.set_alpha(alpha)
    text_rect = text_obj.get_rect()
    text_rect.center = (x, y)
    surface.blit(text_obj, text_rect)

def reset_qte():
    global qte_triggered, qte_start_time, image_rect, background_image, image, success_count, background_index, prompt_index
    qte_triggered = True
    qte_start_time = time.time()
    background_index = (background_index + 1) % len(background_images_scaled)
    prompt_index = (prompt_index + 1) % len(prompt_images_scaled)
    background_image = background_images_scaled[background_index]
    image = prompt_images_scaled[prompt_index]
    image_rect = image.get_rect()
    image_rect.x = random.randint(0, width - image_rect.width)
    image_rect.y = random.randint(0, height - image_rect.height)

def win_screen():
    bg_music.stop()
    win_background_image = pygame.image.load('assets/background.png')
    win_alpha = 0
    pygame.mixer.music.load('assets/Audio/yay.mp3')
    pygame.mixer.music.play()
    while win_alpha < 255:
        SCREEN.fill(BLACK)
        win_background_image.set_alpha(win_alpha)
        SCREEN.blit(win_background_image, (0, 0))
        draw_text('You found all the clues!', custom_font, white, SCREEN, width // 2, height // 2, alpha=win_alpha)
        pygame.display.flip()
        pygame.time.delay(10)
        win_alpha += 1
    if win_alpha == 255:
        dialogue4()
    pygame.time.delay(4000)

def start_screen():
    bg_music.play(-1)
    start_background_image = pygame.image.load('assets/background.png')
    start_alpha = 255
    while start_alpha > 0:
        SCREEN.fill(BLACK)
        start_background_image.set_alpha(start_alpha)
        window.blit(start_background_image, (0, 0))
        draw_text('Find all clues!', custom_font, white, SCREEN, width // 2, height // 2, alpha=start_alpha)
        pygame.display.flip()
        pygame.time.delay(10)
        start_alpha -= 1
    pygame.time.delay(2000)


def start():
    global success_count
    start_screen()

    running = True
    reset_qte()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if qte_triggered and image_rect.collidepoint(event.pos):
                    if time.time() - qte_start_time < qte_time:
                        success_count += 1
                        draw_text('You found a clue!', custom_font, white, window, width // 2, height // 2, alpha=255)
                        pygame.display.flip()
                        pygame.time.delay(2000)
                        if success_count < max_successes:
                            reset_qte()
                        else:
                            win_screen()
                            running = False
                    else:
                        if success_count < max_successes:
                            draw_text('Too Late!', custom_font, red, window, width // 2, height // 2, alpha=255)
                            pygame.display.flip()
                            pygame.time.delay(1000)
                            reset_qte()

        SCREEN.blit(background_image, (0, 0))

        if qte_triggered:
            time_left = qte_time - (time.time() - qte_start_time)
            if time_left > 0:
                SCREEN.blit(image, image_rect)
            else:
                if success_count < max_successes:
                    draw_text('Too Late!', custom_font, red, window, width // 2, height // 2, alpha=255)
                    pygame.display.flip()
                    pygame.time.delay(1000)
                    reset_qte()

        pygame.display.flip()
        pygame.time.Clock().tick(30)

def textbutton_font(size):   
    return pygame.font.Font("assets/Font/ARCADE.TTF", size)

def prologuefont(size):
    return pygame.font.Font("assets/Font/Cinzel.ttf", size)

def button_font(size): 
    return pygame.font.Font("assets/Font/buttonfont.ttf", size)

def char(file_path, xpos, ypos):
    char = pygame.image.load(file_path)
    char_rect = char.get_rect(x=xpos, y=ypos)
    return SCREEN.blit(char, char_rect)

def pausemenu():

    run = True

    while run:
        MENU_MOUSE_POS = pygame.mouse.get_pos()

        bg = pygame.image.load('assets/pausebg.png')
        scaled_bg = pygame.transform.scale(bg, (1280,720))
        bg_rect = scaled_bg.get_rect(x=0,y=0)
        
        pmenu = pygame.image.load('assets/Play Rect.png')
        scaled_pmenu = pygame.transform.scale(pmenu, (1280,720))
        pmenu_rect = scaled_pmenu.get_rect(x=0,y=0)

        SCREEN.blit(scaled_bg, bg_rect)
        SCREEN.blit(scaled_pmenu, pmenu_rect)

        RESUME = Button(image=pygame.image.load("assets/transparent.png"), pos=(640, 300), 
                            text_input="RESUME", font=button_font(100), base_color="white", hovering_color="red") #find better colour
        
        QUIT = Button(image=pygame.image.load("assets/transparent.png"), pos=(640, 500), 
                            text_input="QUIT", font=button_font(100), base_color="white", hovering_color="red")
        
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

        end = textbutton_font(40).render("CHOOSE YOUR TARGET WISELY", True, "White")
        end_rect = end.get_rect(x=340, y=320)
        SCREEN.blit(end,end_rect)

        bg = pygame.image.load('assets/3car.png')
        scaled_bg = pygame.transform.scale(bg, (1280,720))
        bg_rect = scaled_bg.get_rect(x=0,y=0)

        c1 = pygame.image.load('assets/cbutton.png')
        scaled_c1 = pygame.transform.scale(c1, (500,70))
        c1_rect = scaled_c1.get_rect(x=400,y=550)

        c2 = pygame.image.load('assets/cbutton.png')
        scaled_c2 = pygame.transform.scale(c2, (500,70))
        c2_rect = scaled_c2.get_rect(x=400,y=550)

        c3 = pygame.image.load('assets/cbutton.png')
        scaled_c3 = pygame.transform.scale(c3, (500,70))
        c3_rect = scaled_c3.get_rect(x=400,y=550)

        SCREEN.blit(scaled_bg, bg_rect)
        SCREEN.blit(scaled_c1, c1_rect)
        SCREEN.blit(scaled_c2, c2_rect)
        SCREEN.blit(scaled_c3, c3_rect)

        timer.tick(60)

        MENU_MOUSE_POS = pygame.mouse.get_pos()  #detecting mouse position

        CHOICE3 = Button(image=pygame.image.load("assets/transparent.png"), pos=(1150, 365), 
                            text_input="SHOOT", font=textbutton_font(21), base_color="black", hovering_color="#FF3131") #find better colour
        
        CHOICE2 = Button(image=pygame.image.load("assets/transparent.png"), pos=(130, 365), 
                            text_input="SHOOT", font=textbutton_font(21), base_color="black", hovering_color="#FF3131")

        CHOICE1 = Button(image=pygame.image.load("assets/transparent.png"), pos=(650, 590), 
                            text_input="SHOOT", font=textbutton_font(30), base_color="black", hovering_color="#FF3131")

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
                    dialogue22()
                if CHOICE2.checkForInput(MENU_MOUSE_POS):
                    dialogue22()
                if CHOICE3.checkForInput(MENU_MOUSE_POS):
                    dialogue22()
                if PAUSE.checkForInput(MENU_MOUSE_POS):
                    pausemenu()

            pygame.display.flip()

def choice2():
    while True:

        timer = pygame.time.Clock()

        bg = pygame.image.load('assets/2car.png')
        scaled_bg = pygame.transform.scale(bg, (1280,720))
        bg_rect = scaled_bg.get_rect(x=0,y=0)

        c1 = pygame.image.load('assets/cbutton.png')
        scaled_c1 = pygame.transform.scale(c1, (500,70))
        c1_rect = scaled_c1.get_rect(x=400,y=550)

        c2 = pygame.image.load('assets/cbutton.png')
        scaled_c2 = pygame.transform.scale(c2, (500,70))
        c2_rect = scaled_c2.get_rect(x=400,y=550)

        SCREEN.blit(scaled_bg, bg_rect)
        SCREEN.blit(scaled_c1, c1_rect)
        SCREEN.blit(scaled_c2, c2_rect)

        timer.tick(60)

        MENU_MOUSE_POS = pygame.mouse.get_pos()  #detecting mouse position
        
        CHOICE2 = Button(image=pygame.image.load("assets/transparent.png"), pos=(130, 365), 
                            text_input="SHOOT", font=textbutton_font(21), base_color="black", hovering_color="#FF3131")

        CHOICE1 = Button(image=pygame.image.load("assets/transparent.png"), pos=(650, 590), 
                            text_input="SHOOT", font=textbutton_font(21), base_color="black", hovering_color="#FF3131")

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
                    dialogue23()
                if CHOICE2.checkForInput(MENU_MOUSE_POS):
                    dialogue23()
                if PAUSE.checkForInput(MENU_MOUSE_POS):
                    pausemenu()

            pygame.display.flip()

def choice3():
    while True:

        timer = pygame.time.Clock()

        bg = pygame.image.load('assets/1car.png')
        scaled_bg = pygame.transform.scale(bg, (1280,720))
        bg_rect = scaled_bg.get_rect(x=0,y=0)

        c1 = pygame.image.load('assets/cbutton.png')
        scaled_c1 = pygame.transform.scale(c1, (500,70))
        c1_rect = scaled_c1.get_rect(x=400,y=550)

        SCREEN.blit(scaled_bg, bg_rect)
        SCREEN.blit(scaled_c1, c1_rect)

        timer.tick(60)

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        CHOICE1 = Button(image=pygame.image.load("assets/transparent.png"), pos=(650, 590), 
                            text_input="SHOOT", font=textbutton_font(30), base_color="black", hovering_color="#FF3131")

        PAUSE = Button(image=pygame.image.load("assets/pause.png"), pos=(50, 50), 
                            text_input="           ", font=textbutton_font(21), base_color="black", hovering_color="#FF3131")

        for button in [PAUSE,CHOICE1]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)

        for event in pygame.event.get():

            if event.type == pygame.QUIT: #if pressing x button on window screen
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if CHOICE1.checkForInput(MENU_MOUSE_POS):
                    dialogue24()
                if PAUSE.checkForInput(MENU_MOUSE_POS):
                    pausemenu()

            pygame.display.flip()

def transition():
    start_background_image = pygame.image.load('assets/black.png')
    start_alpha = 0

    while start_alpha < 255:
        SCREEN.fill(BLACK)
        start_background_image.set_alpha(start_alpha)
        SCREEN.blit(start_background_image, (0, 0))
        draw_text('CHAPTER II', prologuefont(100), WHITE, SCREEN, 640, 360, alpha=start_alpha)
        draw_text('Amour, or Malevolence?', prologuefont(30), WHITE, SCREEN, 640, 450, alpha=start_alpha)
        pygame.display.flip()
        pygame.time.delay(10)
        start_alpha += 1
    if start_alpha == 255:
        transition2()
    pygame.time.delay(10000)

def transition1():
    chap2_bgm.play()
    start_alpha = 255

    bg = pygame.image.load('assets/ss.png')
    scaled_bg = pygame.transform.scale(bg, (1280,720))
    bg_rect = scaled_bg.get_rect(x=0,y=0)
    
    while start_alpha > 0:
        SCREEN.fill(BLACK)
        scaled_bg.set_alpha(start_alpha)
        SCREEN.blit(scaled_bg, bg_rect)
        pygame.display.flip()
        pygame.time.delay(10)
        start_alpha -= 1
    if start_alpha == 0:
        transition()
    pygame.time.delay(100000)

def transition2():
    start_background_image = pygame.image.load('assets/black.png')
    start_alpha = 255
    
    while start_alpha > 0:
        SCREEN.fill(BLACK)
        start_background_image.set_alpha(start_alpha)
        SCREEN.blit(start_background_image, (0, 0))
        draw_text('CHAPTER II', prologuefont(100), WHITE, SCREEN, 640, 360, alpha=start_alpha)
        draw_text('Amour, or Malevolence?', prologuefont(30), WHITE, SCREEN, 640, 450, alpha=start_alpha)
        pygame.display.flip()
        pygame.time.delay(10)
        start_alpha -= 1
    if start_alpha == 0:
        chap2_bgm.stop()
        dialogue7()
    pygame.time.delay(100000)


def chap2_opening():
    win_alpha = 0
    bg = pygame.image.load('assets/Chapter2/houselover.png')
    scaled_bg = pygame.transform.scale(bg, (1280,720))
    bg_rect = scaled_bg.get_rect(x=0,y=0)

    while win_alpha < 255:
        SCREEN.fill(BLACK)
        scaled_bg.set_alpha(win_alpha)
        SCREEN.blit(scaled_bg, bg_rect)
        pygame.display.flip()
        pygame.time.delay(10)
        win_alpha += 1
    if win_alpha == 255:
        dialogue1()
    pygame.time.delay(4000)

def dialogue1():
    font = pygame.font.Font('assets/Font/ARCADE.TTF', 24)
    screen = pygame.display.set_mode ([1280, 720])
    timer = pygame.time.Clock()
    messages = ('Damansara Villa - Mansion - 7:49:35 PM',
                'Such a magnificent house...',
                'Wonder who lives here...',
                'Oh, it seems that, it\'s the house of a certain person...',
                'A person who\'s closely related to Roman...',
                'Well, the prison break is just the beginning...',
                '...')
    snip = font.render('', True, 'black')
    counter = 0
    speed = 1
    active_message = 0
    message = messages[active_message]

    run = True
    while run:

        MENU_MOUSE_POS = pygame.mouse.get_pos()
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
                if active_message == 6:
                    dialogue2()

        snip = font.render(message[0:counter//speed], True, 'white')
        screen.blit(snip, (295, 600))

        pygame.display.flip()

def dialogue2():
    font = pygame.font.Font('assets/Font/ARCADE.TTF', 24)
    screen = pygame.display.set_mode ([1280, 720])
    timer = pygame.time.Clock()
    messages = ('*click clack*',
                'A certain figure of a woman... who\'s a former detective.',
                'She\'s been investigating something to help her long lost lover-',
                '-Roman.',
                'It has taken years for her, to solve the puzzle-',
                '-behind the murder of Roman\'s mother.',
                'And now, the clues behind the case has started to piece together.',
                '??? : If this thing\'s related to this, then this would be like this.',
                '??? : Yes, yes, it all started to make sense...',
                '??? : Finally! One step closer to solve this...',
                '??? : Now I\'ve to go the places I marked-',
                '??? : And see if I can confirm my suspicions...',
                '...')
    snip = font.render('', True, 'black')
    counter = 0
    speed = 1
    active_message = 0
    message = messages[active_message]
    keyboard.play()

    run = True
    while run:

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        PAUSE = Button(image=pygame.image.load("assets/pause.png"), pos=(50, 50), 
                            text_input="           ", font=textbutton_font(21), base_color="black", hovering_color="#FF3131")

        bg = pygame.image.load('assets/introlover.jpg')
        scaled_bg = pygame.transform.scale(bg, (1280,720))
        bg_rect = scaled_bg.get_rect(x=0,y=0)
        
        textbox = pygame.image.load('assets/textboxlover.png')
        scaled_texbox = pygame.transform.scale(textbox, (850,450))
        textbox_rect = scaled_texbox.get_rect(x=220,y=410)

        screen.blit(scaled_bg, bg_rect)
        PAUSE.update(SCREEN)
        PAUSE.changeColor(MENU_MOUSE_POS)
        char('assets/mc.png',430,1)
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
                if active_message == 12:
                    keyboard.stop()
                    dialogue3()

        snip = font.render(message[0:counter//speed], True, 'white')
        screen.blit(snip, (295, 600))

        pygame.display.flip()
        

def dialogue3():
    font = pygame.font.Font('assets/Font/ARCADE.TTF', 24)
    screen = pygame.display.set_mode ([1280, 720])
    timer = pygame.time.Clock()
    messages = ('??? : Let\'s finish the job, shall we?',
                '??? : We\'ll be reunited, my dear Roman.',
                '??? : Wait for me...',
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

        bg = pygame.image.load('assets/lovergoout.jpg')
        scaled_bg = pygame.transform.scale(bg, (1280,720))
        bg_rect = scaled_bg.get_rect(x=0,y=0)
        
        textbox = pygame.image.load('assets/textboxlover.png')
        scaled_texbox = pygame.transform.scale(textbox, (850,450))
        textbox_rect = scaled_texbox.get_rect(x=220,y=410)

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
                if active_message == 3:
                    start()

        snip = font.render(message[0:counter//speed], True, 'white')
        screen.blit(snip, (295, 600))

        pygame.display.flip()

def dialogue4():
    font = pygame.font.Font('assets/Font/ARCADE.TTF', 24)
    screen = pygame.display.set_mode ([1280, 720])
    timer = pygame.time.Clock()
    messages = ('After traversing around the New Klang county-',
                'She came back home with all clues in her hand.',
                '??? : With all these clues-',
                '??? : -I can finally use \'em to prove that-',
                '??? : -Roman\'s not guilty!',
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
        
        textbox = pygame.image.load('assets/textboxlover.png')
        scaled_texbox = pygame.transform.scale(textbox, (850,450))
        textbox_rect = scaled_texbox.get_rect(x=220,y=410)

        screen.blit(scaled_bg, bg_rect)
        PAUSE.update(SCREEN)
        PAUSE.changeColor(MENU_MOUSE_POS)
        char('assets/mc.png',430,1)
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
                    dialogue5()

        snip = font.render(message[0:counter//speed], True, 'white')
        screen.blit(snip, (295, 600))

        pygame.display.flip()

def dialogue5():
    font = pygame.font.Font('assets/Font/ARCADE.TTF', 24)
    screen = pygame.display.set_mode ([1280, 720])
    timer = pygame.time.Clock()
    messages = ('*phone rings*',
                '??? : !?',
                '??? : ...unknown number?' ,
                '??? : <picks up call> Hello...?',
                'Unknown Caller : Ah, hello! Uhh, is this...',
                '...')
    snip = font.render('', True, 'white')
    counter = 0
    speed = 1
    active_message = 0
    message = messages[active_message]
    phone.play()

    run = True
    while run:

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        PAUSE = Button(image=pygame.image.load("assets/pause.png"), pos=(50, 50), 
                            text_input="           ", font=textbutton_font(21), base_color="black", hovering_color="#FF3131")

        bg = pygame.image.load('assets/phoneringing.jpg')
        scaled_bg = pygame.transform.scale(bg, (1280,720))
        bg_rect = scaled_bg.get_rect(x=0,y=0)
        
        textbox = pygame.image.load('assets/textboxlover.png')
        scaled_texbox = pygame.transform.scale(textbox, (850,450))
        textbox_rect = scaled_texbox.get_rect(x=220,y=410)

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
                if active_message == 5:
                    dialogue6()

        snip = font.render(message[0:counter//speed], True, 'white')
        screen.blit(snip, (295, 600))

        pygame.display.flip()

def dialogue6():
    font = pygame.font.Font('assets/Font/ARCADE.TTF', 24)
    screen = pygame.display.set_mode ([1280, 720])
    timer = pygame.time.Clock()
    messages = ('Unknown Caller : ...the residence of Luna?',
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

        bg = pygame.image.load('assets/black.png')
        scaled_bg = pygame.transform.scale(bg, (1280,720))
        bg_rect = scaled_bg.get_rect(x=0,y=0)
        
        textbox = pygame.image.load('assets/textboxlover.png')
        scaled_texbox = pygame.transform.scale(textbox, (850,450))
        textbox_rect = scaled_texbox.get_rect(x=220,y=410)

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
                if active_message == 1:
                    transition1()

        snip = font.render(message[0:counter//speed], True, 'white')
        screen.blit(snip, (295, 600))

        pygame.display.flip()

def dialogue7():
    font = pygame.font.Font('assets/Font/ARCADE.TTF', 24)
    screen = pygame.display.set_mode ([1280, 720])
    timer = pygame.time.Clock()
    messages = ('Unknown Caller : Ah, hello! Uhh, is this...',
                'Unknown Caller : ...the residence of Luna?',
                'Luna : Who\'re you?',
                'Unknown Caller : Are you Luna?',
                'Luna : <in serious tone> You\'ve mistaken me with someone else.',
                'Unknown Caller : Oh, I apologize.', 
                'Unknown Caller : I must have gotten the wrong number...',
                'Luna : (This caller seems... innocent?)',
                'Luna : W-wait! Yes, I\'m Luna. What do you want from me?',
                'Unknown Caller : <giggles> Nothing, just wanna tell you...',
                'Unknown Caller : ...that it\'s me, Roman!',
                'Luna : <stunned> R-Roman?!',
                'Luna : Since when did you get out?!',
                'Roman : It\'s a long story. Let\'s meet somewhere.',
                'Luna : I\'ll give you the location',
                'Luna : B-but, how did you get out?',
                'Luna : You\'re doing it alone or what?',
                'Roman : <laughs> I\'ll tell you when we meet.',
                'Luna : <sighs> Fine. I\'ll see you there.',
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
        
        textbox = pygame.image.load('assets/textboxlover.png')
        scaled_texbox = pygame.transform.scale(textbox, (850,450))
        textbox_rect = scaled_texbox.get_rect(x=220,y=410)

        screen.blit(scaled_bg, bg_rect)
        PAUSE.update(SCREEN)
        PAUSE.changeColor(MENU_MOUSE_POS)
        char('assets/silhoutte.png',400,1)
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
                if active_message == 19:
                    dialogue8()

        snip = font.render(message[0:counter//speed], True, 'white')
        screen.blit(snip, (295, 600))

        pygame.display.flip()

def dialogue8():
    font = pygame.font.Font('assets/Font/ARCADE.TTF', 24)
    screen = pygame.display.set_mode ([1280, 720])
    timer = pygame.time.Clock()
    messages = ('Luna : <hangs up and sighs> Roman...',
                'Luna : I don\'t know... if I\'m happy or not.',
                'Luna : You better explain youself when I get there, Roman.',
                'Luna : Oh yeah, gotta discuss the clues with Roman.',
                'Luna carries the clues with her-',
                '-and immdiately goes to the specified location.',
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

        bg = pygame.image.load('assets/bedroom.jpg')
        scaled_bg = pygame.transform.scale(bg, (1280,720))
        bg_rect = scaled_bg.get_rect(x=0,y=0)
        
        textbox = pygame.image.load('assets/textboxlover.png')
        scaled_texbox = pygame.transform.scale(textbox, (850,450))
        textbox_rect = scaled_texbox.get_rect(x=220,y=410)

        screen.blit(scaled_bg, bg_rect)
        PAUSE.update(SCREEN)
        PAUSE.changeColor(MENU_MOUSE_POS)
        char('assets/Chapter2/lovercalm.png',450,180)
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
                    dialogue9()

        snip = font.render(message[0:counter//speed], True, 'white')
        screen.blit(snip, (295, 600))

        pygame.display.flip()

def dialogue9():
    font = pygame.font.Font('assets/Font/ARCADE.TTF', 24)
    screen = pygame.display.set_mode ([1280, 720])
    timer = pygame.time.Clock()
    messages = ('Somewhere Around New Klang - Abandoned Warehouse - 10:42:30 PM',
                'A BMW sedan pulls up at the location...',
                'Luna gets out from the car, feeling eager to reunite with Roman.',
                'Luna : Now, where is he...',
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

        bg = pygame.image.load('assets/chap2.png')
        scaled_bg = pygame.transform.scale(bg, (1280,720))
        bg_rect = scaled_bg.get_rect(x=0,y=0)
        
        textbox = pygame.image.load('assets/textboxlover.png')
        scaled_texbox = pygame.transform.scale(textbox, (850,450))
        textbox_rect = scaled_texbox.get_rect(x=220,y=410)

        screen.blit(scaled_bg, bg_rect)
        PAUSE.update(SCREEN)
        PAUSE.changeColor(MENU_MOUSE_POS)
        char('assets/Chapter2/lover4.png',500,-20)
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
                    dialogue10()

        snip = font.render(message[0:counter//speed], True, 'white')
        screen.blit(snip, (295, 600))

        pygame.display.flip()

def dialogue10():
    font = pygame.font.Font('assets/Font/ARCADE.TTF', 24)
    screen = pygame.display.set_mode ([1280, 720])
    timer = pygame.time.Clock()
    messages = ('Roman : Luna!!!',
                'Luna : <suprised> Roman!?',
                'They both hugged each other...',
                '...embracing themselves in a warm hug.',
                'Roman : Oh, it\'s like a dream...',
                'Roman : After so long, we reunite again, Luna...',
                'Roman : I miss you so much...',
                'Luna : <sobs> I miss you more, Roman...',
                'Luna pinches Roman\'s waist so hard as a punishment.',
                'Roman : Owwww!!!',
                'Luna : Care to explain?',
                'Roman : Yes, ma\'am...',
                'Roman : Long story short, I escaped with the help of someone.',
                'Roman : Meet Emir. He helped me a lot.',
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
        
        textbox = pygame.image.load('assets/textboxlover.png')
        scaled_texbox = pygame.transform.scale(textbox, (850,450))
        textbox_rect = scaled_texbox.get_rect(x=220,y=410)

        screen.blit(scaled_bg, bg_rect)
        PAUSE.update(SCREEN)
        PAUSE.changeColor(MENU_MOUSE_POS)
        char('assets/Chapter2/lover4.png',270,1)
        char('assets/mc.png',630,20)
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
        screen.blit(snip, (295, 600))

        pygame.display.flip()

def dialogue11():
    font = pygame.font.Font('assets/Font/ARCADE.TTF', 24)
    screen = pygame.display.set_mode ([1280, 720])
    timer = pygame.time.Clock()
    messages = ('Emir : Yo, nice to meet ya. ',
                'Luna : <surprised> (That face looks familiar!)',
                'Luna : (Isn\'t he the who\'s responsible...)',
                'Emir : (...for making Roman\'s life miserable!?)',
                'Luna : Y-you!',
                'Emir : Hmm? Something\'s wrong?',
                'Luna : Roman, he\'s the one who killed your mother!!!',
                'Roman : <shocked> W-what? Are you for real...?',
                'Emir : What? Is this some kind of a prank?',
                'Roman : Luna, I think you\'ve mistaken him with someone else...',
                'Luna : No! I got the evidences with me!',
                'Luna : Ngh, come with me! You\'re coming too, Emir!',
                'Luna : Don\'t you dare go anywhere...',
                'Emir : Wha- <sighs> ...alright.',
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
        
        textbox = pygame.image.load('assets/textboxlover.png')
        scaled_texbox = pygame.transform.scale(textbox, (850,450))
        textbox_rect = scaled_texbox.get_rect(x=220,y=410)

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
                if active_message == 14:
                    dialogue12()

        snip = font.render(message[0:counter//speed], True, 'white')
        screen.blit(snip, (295, 600))

        pygame.display.flip()

def dialogue12():
    font = pygame.font.Font('assets/Font/ARCADE.TTF', 24)
    screen = pygame.display.set_mode ([1280, 720])
    timer = pygame.time.Clock()
    messages = ('All of them move to Luna\'s car, to see what Luna have to show.',
                'Luna : <searching> Where is it...',
                'Roman : Luna...',
                'Emir : ...',
                'Luna : Tch, I swear I brought it with me!',
                'Roman : <tugs Luna\'s hand> Luna, quit it, you\'re embarassing me!',
                'Luna : What? And let loose of you mother\'s killer?',
                'Roman : N-no! What kind of murderer-',
                'Roman : -helps a person who\'s related to someone they killed?!',
                'Luna : So, you won\'t believe me...?',
                'Roman : N-no, but...',
                'Roman : (Well, I\'ve some kind of suspicions towards Emir though.)',
                'Roman : (And it seems, Luna has brought her evidences...)',
                'Roman : (But it suddenly got lost. Something\'s not right...)',
                'Roman moves away a bit from Emir.',
                'Emir : For real? After what we\'ve been through together...',
                'Emir : You still don\'t trust me?',
                'Roman : Something\'s not right about you...',
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
        
        textbox = pygame.image.load('assets/textboxlover.png')
        scaled_texbox = pygame.transform.scale(textbox, (850,450))
        textbox_rect = scaled_texbox.get_rect(x=220,y=410)

        screen.blit(scaled_bg, bg_rect)
        PAUSE.update(SCREEN)
        PAUSE.changeColor(MENU_MOUSE_POS)
        char('assets/mc.png',270,1)
        char('assets/confusedwalter.png',600,20)
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
                if active_message == 18:
                    dialogue13()

        snip = font.render(message[0:counter//speed], True, 'white')
        screen.blit(snip, (295, 600))

        pygame.display.flip()

def dialogue13():
    font = pygame.font.Font('assets/Font/ARCADE.TTF', 24)
    screen = pygame.display.set_mode ([1280, 720])
    timer = pygame.time.Clock()
    messages = ('Emir : <smirks> So this is how you wanna play the game, huh?',
                'Emir : Well, it can\'t be helped...',
                'Roman : So it\'s true!!!',
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
        
        textbox = pygame.image.load('assets/textboxlover.png')
        scaled_texbox = pygame.transform.scale(textbox, (850,450))
        textbox_rect = scaled_texbox.get_rect(x=220,y=410)

        screen.blit(scaled_bg, bg_rect)
        PAUSE.update(SCREEN)
        PAUSE.changeColor(MENU_MOUSE_POS)
        char('assets/silhoutte.png',475,1)
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
                    dialogue14()

        snip = font.render(message[0:counter//speed], True, 'white')
        screen.blit(snip, (295, 600))

        pygame.display.flip()

def dialogue14():
    font = pygame.font.Font('assets/Font/ARCADE.TTF', 24)
    screen = pygame.display.set_mode ([1280, 720])
    timer = pygame.time.Clock()
    messages = ('Police siren can be heard near their location.',
                'Roman : Tch, how does the police knows our location immediately?!',
                'Emir : <smirks> It seems like our time is up.',
                'Emir : Till we meet again, Roman.',
                'Roman : Oh, you don\'t!',
                'Roman tries to subdue Emir, but the polices are coming.',
                '...')
    snip = font.render('', True, 'white')
    counter = 0
    speed = 1
    active_message = 0
    message = messages[active_message]
    siren.play()

    run = True
    while run:

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        PAUSE = Button(image=pygame.image.load("assets/pause.png"), pos=(50, 50), 
                            text_input="           ", font=textbutton_font(21), base_color="black", hovering_color="#FF3131")

        bg = pygame.image.load('assets/prisongym.jpeg')
        scaled_bg = pygame.transform.scale(bg, (1280,720))
        bg_rect = scaled_bg.get_rect(x=0,y=0)
        
        textbox = pygame.image.load('assets/textboxlover.png')
        scaled_texbox = pygame.transform.scale(textbox, (850,450))
        textbox_rect = scaled_texbox.get_rect(x=220,y=410)

        screen.blit(scaled_bg, bg_rect)
        PAUSE.update(SCREEN)
        PAUSE.changeColor(MENU_MOUSE_POS)
        char('assets/mc.png',430,1)
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
                    choice2()

        snip = font.render(message[0:counter//speed], True, 'white')
        screen.blit(snip, (295, 600))

        pygame.display.flip()

def dialogue15():
    font = pygame.font.Font('assets/Font/ARCADE.TTF', 24)
    screen = pygame.display.set_mode ([1280, 720])
    timer = pygame.time.Clock()
    messages = ('Police : Over there!',
                'Roman : (Thank god Luna\'s car is not at the police\'s location.)',
                'Roman : Luna, to your car!',
                'Luna : Y-yes! ',
                'Fortunately, they both succeeded in escaping the police raid.',
                'But they knew they couldn\'t let Emir in the loose.',
                'They had to come up with a plan to take him down.',
                'But for now, they\'ve to retreat to Luna\'s home first.',
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

        bg = pygame.image.load('assets/prisongym.jpeg')
        scaled_bg = pygame.transform.scale(bg, (1280,720))
        bg_rect = scaled_bg.get_rect(x=0,y=0)
        
        textbox = pygame.image.load('assets/textboxlover.png')
        scaled_texbox = pygame.transform.scale(textbox, (850,450))
        textbox_rect = scaled_texbox.get_rect(x=220,y=410)

        SCREEN.blit(scaled_bg, bg_rect)
        PAUSE.update(SCREEN)
        PAUSE.changeColor(MENU_MOUSE_POS)
        char("assets/mc.png",450,1)
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
                    transition2()

        snip = font.render(message[0:counter//speed], True, 'white')
        screen.blit(snip, (295, 600))

        pygame.display.flip()

def transition3():
    start_alpha = 255

    bg = pygame.image.load('assets/warehouse.png')
    scaled_bg = pygame.transform.scale(bg, (1280,720))
    bg_rect = scaled_bg.get_rect(x=0,y=0)

    current  = textbutton_font(24).render("But for now, they\'ve to retreat to Luna\'s home first.", True, "White")
    current_rect = current.get_rect(x=290, y=570)

    textbox = pygame.image.load('assets/textboxlover.png')
    scaled_texbox = pygame.transform.scale(textbox, (850,200))
    textbox_rect = scaled_texbox.get_rect(x=220,y=500)
    
    while start_alpha > 0:
        SCREEN.fill(BLACK)
        scaled_bg.set_alpha(start_alpha)
        SCREEN.blit(scaled_bg, bg_rect)
        SCREEN.blit(scaled_texbox, textbox_rect)
        SCREEN.blit(current, current_rect)
        pygame.display.flip()
        pygame.time.delay(10)
        start_alpha -= 1
    if start_alpha == 0:
        transition4()
    pygame.time.delay(2000)

def transition4():
    start_background_image = pygame.image.load('assets/houselover.png')
    start_alpha = 0

    while start_alpha < 255:
        SCREEN.fill(BLACK)
        start_background_image.set_alpha(start_alpha)
        SCREEN.blit(start_background_image, (0, 0))
        pygame.display.flip()
        pygame.time.delay(10)
        start_alpha += 1
    if start_alpha == 255:
        dialogue16()
    pygame.time.delay(10000)

def dialogue16():
    font = pygame.font.Font('assets/Font/ARCADE.TTF', 24)
    screen = pygame.display.set_mode ([1280, 720])
    timer = pygame.time.Clock()
    messages = ('Somewhere Around New Klang - Mansion - 10:42:30 PM',
                'Roman and Luna arrives at her home...',
                'Luna : <sighs> Finally, we made it.',
                'Luna : Oh yeah, lemme show you the evidences I collected.',
                'Roman : Wait, I thought it has lost?',
                'Luna : Well, the thing is...',
                'Luna : I actually forgot to bring it when meeting you.',
                'Luna : Tehe :3 !',
                'Roman : Wha- you! <sighs> You didn\'t change at all, Luna.',
                'Roman : <smiles> Always being clumsy when you\'re around me.',
                'Roman : Back when you\'re a detective, you always being serious.',
                'Luna : <giggles> Hehe, sorry Roman!',
                'Luna : Now, let me brief you about the evidences. Come inside.',
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

        bg = pygame.image.load('assets/Chapter2/houselover.png')
        scaled_bg = pygame.transform.scale(bg, (1280,720))
        bg_rect = scaled_bg.get_rect(x=0,y=0)
        
        textbox = pygame.image.load('assets/textboxlover.png')
        scaled_texbox = pygame.transform.scale(textbox, (850,450))
        textbox_rect = scaled_texbox.get_rect(x=220,y=410)

        SCREEN.blit(scaled_bg, bg_rect)
        PAUSE.update(SCREEN)
        PAUSE.changeColor(MENU_MOUSE_POS)
        char('assets/mc.png',430,1)
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
                if active_message == 13:
                    transition5()

        snip = font.render(message[0:counter//speed], True, 'white')
        screen.blit(snip, (295, 600))

        pygame.display.flip()

def transition5():
    start_alpha = 255

    bg = pygame.image.load('assets/Chapter2/houselover.png')
    scaled_bg = pygame.transform.scale(bg, (1280,720))
    bg_rect = scaled_bg.get_rect(x=0,y=0)

    current  = textbutton_font(24).render("Luna : Now, let me brief you about the evidences. Come inside.", True, "White")
    current_rect = current.get_rect(x=290, y=570)

    textbox = pygame.image.load('assets/textboxlover.png')
    scaled_texbox = pygame.transform.scale(textbox, (850,200))
    textbox_rect = scaled_texbox.get_rect(x=220,y=500)
    
    while start_alpha > 0:
        SCREEN.fill(BLACK)
        scaled_bg.set_alpha(start_alpha)
        SCREEN.blit(scaled_bg, bg_rect)
        SCREEN.blit(scaled_texbox, textbox_rect)
        SCREEN.blit(current, current_rect)
        pygame.display.flip()
        pygame.time.delay(10)
        start_alpha -= 1
    if start_alpha == 0:
        transition6()
    pygame.time.delay(2000)

def transition6():
    start_background_image = pygame.image.load('assets/bedroom.jpg')
    start_alpha = 0

    bg = pygame.image.load('assets/bedroom.jpg')
    scaled_bg = pygame.transform.scale(bg, (1280,720))
    bg_rect = scaled_bg.get_rect(x=0,y=0)

    while start_alpha < 255:
        SCREEN.fill(BLACK)
        start_background_image.set_alpha(start_alpha)
        SCREEN.blit(start_background_image, (0, 0))
        pygame.display.flip()
        pygame.time.delay(10)
        start_alpha += 1
    if start_alpha == 255:
        dialogue17()
    pygame.time.delay(10000)

def dialogue17():
    font = pygame.font.Font('assets/Font/ARCADE.TTF', 24)
    screen = pygame.display.set_mode ([1280, 720])
    timer = pygame.time.Clock()
    messages = ('Luna then briefs her evidences towards Roman.',
                'Luna : But what Emir doesn\'t know is-',
                'Luna : -I\'ve already pinpointed his hideout!',
                'Roman : Woah, good job, Luna! Now we can go kick his ass!',
                'Luna : Tomorrow\'s night the day, so... recharge yourself.',
                'Luna : And... sleep at the other room, will you?',
                'Roman : Of course, why did you say that?',
                'Luna : N-nothing...',
                'Roman : Okay..? Well, goodnight!',
                'Luna : Goodnight too...',
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

        bg = pygame.image.load('assets/bedroom.jpg')
        scaled_bg = pygame.transform.scale(bg, (1280,720))
        bg_rect = scaled_bg.get_rect(x=0,y=0)
        
        textbox = pygame.image.load('assets/textboxlover.png')
        scaled_texbox = pygame.transform.scale(textbox, (850,450))
        textbox_rect = scaled_texbox.get_rect(x=220,y=410)

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
                    transition7()

        snip = font.render(message[0:counter//speed], True, 'white')
        screen.blit(snip, (295, 600))

        pygame.display.flip()

def transition7():
    start_alpha = 255

    bg = pygame.image.load('assets/bedroom.jpg')
    scaled_bg = pygame.transform.scale(bg, (1280,720))
    bg_rect = scaled_bg.get_rect(x=0,y=0)

    current  = textbutton_font(24).render("Luna : Goodnight too...", True, "White")
    current_rect = current.get_rect(x=290, y=570)

    textbox = pygame.image.load('assets/textboxlover.png')
    scaled_texbox = pygame.transform.scale(textbox, (850,200))
    textbox_rect = scaled_texbox.get_rect(x=220,y=500)
    
    while start_alpha > 0:
        SCREEN.fill(BLACK)
        scaled_bg.set_alpha(start_alpha)
        SCREEN.blit(scaled_bg, bg_rect)
        SCREEN.blit(scaled_texbox, textbox_rect)
        SCREEN.blit(current, current_rect)
        pygame.display.flip()
        pygame.time.delay(10)
        start_alpha -= 1
    if start_alpha == 0:
        transition8()
    pygame.time.delay(2000)

def transition8():
    start_alpha = 0

    bg = pygame.image.load('assets/drivewayblur.jpg')
    scaled_bg = pygame.transform.scale(bg, (1280,720))
    bg_rect = scaled_bg.get_rect(x=0,y=0)

    box = pygame.image.load('assets/Play Rect.png')
    scaled_box = pygame.transform.scale(box, (640,240))
    box_rect = scaled_box.get_rect(x=320,y=250)

    while start_alpha < 255:
        SCREEN.fill(BLACK)
        scaled_bg.set_alpha(start_alpha)
        scaled_box.set_alpha(start_alpha)
        SCREEN.blit(scaled_bg, bg_rect)
        SCREEN.blit(scaled_box, box_rect)
        pygame.display.flip()
        pygame.time.delay(10)
        start_alpha += 1
    if start_alpha == 255:
        transition9()
    pygame.time.delay(10000)

def transition9():
    start_alpha = 255

    bg = pygame.image.load('assets/drivewayblur.jpg')
    scaled_bg = pygame.transform.scale(bg, (1280,720))
    bg_rect = scaled_bg.get_rect(x=0,y=0)

    box = pygame.image.load('assets/Play Rect.png')
    scaled_box = pygame.transform.scale(box, (640,240))
    box_rect = scaled_box.get_rect(x=320,y=250)
    
    while start_alpha > 0:
        SCREEN.fill(BLACK)
        scaled_bg.set_alpha(start_alpha)
        scaled_box.set_alpha(start_alpha)
        SCREEN.blit(scaled_bg, bg_rect)
        SCREEN.blit(scaled_box, box_rect)
        pygame.display.flip()
        pygame.time.delay(10)
        start_alpha -= 1
    if start_alpha == 0:
        dialogue18()
    pygame.time.delay(2000)

def dialogue18():
    font = pygame.font.Font('assets/Font/ARCADE.TTF', 24)
    screen = pygame.display.set_mode ([1280, 720])
    timer = pygame.time.Clock()
    messages = ('That night, Roman and Luna are packing up some stuff.',
                'Guns, rifles, medkit, anything crucial for the operation.',
                'That night, is an important night, to edn it all.',
                'Roman : Alright, everything\'s ready.',
                'Luna : Let\'s roll out!',
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

        bg = pygame.image.load('assets/prisongym.jpeg')
        scaled_bg = pygame.transform.scale(bg, (1280,720))
        bg_rect = scaled_bg.get_rect(x=0,y=0)
        
        textbox = pygame.image.load('assets/textboxlover.png')
        scaled_texbox = pygame.transform.scale(textbox, (850,450))
        textbox_rect = scaled_texbox.get_rect(x=220,y=410)

        SCREEN.blit(scaled_bg, bg_rect)
        PAUSE.update(SCREEN)
        PAUSE.changeColor(MENU_MOUSE_POS)
        char('assets/mc.png',430,1)
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
                    dialogue19()

        snip = font.render(message[0:counter//speed], True, 'white')
        screen.blit(snip, (295, 600))

        pygame.display.flip()

def dialogue19():
    font = pygame.font.Font('assets/Font/ARCADE.TTF', 24)
    screen = pygame.display.set_mode ([1280, 720])
    timer = pygame.time.Clock()
    messages = ('They both now on the way to Emir\'s hideout.',
                'The highway\'s dark and long, so boring.',
                'Roman : So, are we there yet?',
                'Luna : About 20 km more.',
                'Roman : Oh...',
                'Roman : Are... we there yet?',
                'Luna : You just asked that, Roman. No, we\'re not there yet.',
                'Roman : Okay.',
                'Roman : ...',
                'Roman : Are we-',
                'Luna : FOR GODSAKE, ROMAN. NO WE\'RE FAR AWAY FROM THE HIDEOUT.',
                'Roman : <laughs uncontrollably> I love teasing you...',
                'Luna : <blushes> Ugh...',
                'Luna : ...',
                'Luna : ...you know, ever since we became best friend back in high school.',
                'Luna : I always wanted to talk with you. And that feeling grew up.',
                'Luna : Just when I wanted to talk about my feelings...',
                'Luna : You got accused of killing your own mother, and imprisoned.',
                'Luna : I gave up. For you to get imprisoned for that many years...',
                'Luna : I thought you would forget me, and I would never see you again...',
                'Luna : But... fate brought us here now.',
                'Luna : So, I just wanted to tell you, that...',
                'Luna : ...',
                'Roman : ...what?',
                'Luna : ...that I lo-',
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

        bg = pygame.image.load('assets/driving.jpg')
        scaled_bg = pygame.transform.scale(bg, (1280,720))
        bg_rect = scaled_bg.get_rect(x=0,y=0)
        
        textbox = pygame.image.load('assets/textboxlover.png')
        scaled_texbox = pygame.transform.scale(textbox, (850,450))
        textbox_rect = scaled_texbox.get_rect(x=220,y=410)

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
                if active_message == 25:
                    dialogue20()

        snip = font.render(message[0:counter//speed], True, 'white')
        screen.blit(snip, (295, 600))

        pygame.display.flip()

def dialogue20():
    font = pygame.font.Font('assets/Font/ARCADE.TTF', 24)
    screen = pygame.display.set_mode ([1280, 720])
    timer = pygame.time.Clock()
    messages = ('Just when things get romantic, their car got attacked!',
                'Roman : WOAH, WHO THE HELL?',
                'Luna : I don\'t know but now\'s the perfect time-',
                'Luna : -to use that beauty!',
                'Roman : Hell yeah!',
                '...')
    snip = font.render('', True, 'white')
    counter = 0
    speed = 1
    active_message = 0
    message = messages[active_message]
    rifleshoot.play(-1)
    tirescreech.play()

    run = True

    while run:

        timer = pygame.time.Clock()

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        PAUSE = Button(image=pygame.image.load("assets/pause.png"), pos=(50, 50), 
                            text_input="           ", font=textbutton_font(21), base_color="black", hovering_color="#FF3131")

        bg = pygame.image.load('assets/cargotshot.jpg')
        scaled_bg = pygame.transform.scale(bg, (1280,720))
        bg_rect = scaled_bg.get_rect(x=0,y=0)
        
        textbox = pygame.image.load('assets/textboxlover.png')
        scaled_texbox = pygame.transform.scale(textbox, (850,450))
        textbox_rect = scaled_texbox.get_rect(x=220,y=410)

        SCREEN.blit(scaled_bg, bg_rect)
        PAUSE.update(SCREEN)
        PAUSE.changeColor(MENU_MOUSE_POS)
        char('assets/surprisedmc.png',270,-50)
        char('assets/casualwalter.png',630,20)
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
                    dialogue21()

        snip = font.render(message[0:counter//speed], True, 'white')
        screen.blit(snip, (295, 600))

        pygame.display.flip()

def dialogue21():
    font = pygame.font.Font('assets/Font/ARCADE.TTF', 24)
    screen = pygame.display.set_mode ([1280, 720])
    timer = pygame.time.Clock()
    messages = ('Roman whips out the modded M249, and ready to spray it.',
                'Roman : You troublemakers gonna regret this!',
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

        bg = pygame.image.load('assets/romanshoot.jpg')
        scaled_bg = pygame.transform.scale(bg, (1280,720))
        bg_rect = scaled_bg.get_rect(x=0,y=0)
        
        textbox = pygame.image.load('assets/textboxlover.png')
        scaled_texbox = pygame.transform.scale(textbox, (850,450))
        textbox_rect = scaled_texbox.get_rect(x=220,y=410)

        SCREEN.blit(scaled_bg, bg_rect)
        PAUSE.update(SCREEN)
        PAUSE.changeColor(MENU_MOUSE_POS)
        char('assets/silhoutte.png',400,1)
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
                    choice1()

        snip = font.render(message[0:counter//speed], True, 'white')
        screen.blit(snip, (295, 600))

        pygame.display.flip()

def dialogue22():
    font = pygame.font.Font('assets/Font/ARCADE.TTF', 24)
    screen = pygame.display.set_mode ([1280, 720])
    timer = pygame.time.Clock()
    messages = ('Roman : One down, two more!',
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

        bg = pygame.image.load('assets/2car.png')
        scaled_bg = pygame.transform.scale(bg, (1280,720))
        bg_rect = scaled_bg.get_rect(x=0,y=0)
        
        textbox = pygame.image.load('assets/textboxlover.png')
        scaled_texbox = pygame.transform.scale(textbox, (850,450))
        textbox_rect = scaled_texbox.get_rect(x=220,y=410)

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
                    choice2()

        snip = font.render(message[0:counter//speed], True, 'white')
        screen.blit(snip, (295, 600))

        pygame.display.flip()

def dialogue23():
    font = pygame.font.Font('assets/Font/ARCADE.TTF', 24)
    screen = pygame.display.set_mode ([1280, 720])
    timer = pygame.time.Clock()
    messages = ('Roman : The last of \'em!',
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

        bg = pygame.image.load('assets/1car.png')
        scaled_bg = pygame.transform.scale(bg, (1280,720))
        bg_rect = scaled_bg.get_rect(x=0,y=0)
        
        textbox = pygame.image.load('assets/textboxlover.png')
        scaled_texbox = pygame.transform.scale(textbox, (850,450))
        textbox_rect = scaled_texbox.get_rect(x=220,y=410)

        SCREEN.blit(scaled_bg, bg_rect)
        PAUSE.update(SCREEN)
        PAUSE.changeColor(MENU_MOUSE_POS)
        char('assets/casualmc.png',270,1)
        char('assets/casualemir.png',670,50)
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
                    choice3()

        snip = font.render(message[0:counter//speed], True, 'white')
        screen.blit(snip, (295, 600))

        pygame.display.flip()


def dialogue24():
    font = pygame.font.Font('assets/Font/ARCADE.TTF', 24)
    screen = pygame.display.set_mode ([1280, 720])
    timer = pygame.time.Clock()
    messages = ('Roman : Damn!',
                'Luna : Way to go, Roman!',
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

        bg = pygame.image.load('assets/0car.png')
        scaled_bg = pygame.transform.scale(bg, (1280,720))
        bg_rect = scaled_bg.get_rect(x=0,y=0)
        
        textbox = pygame.image.load('assets/textboxlover.png')
        scaled_texbox = pygame.transform.scale(textbox, (850,450))
        textbox_rect = scaled_texbox.get_rect(x=220,y=410)

        SCREEN.blit(scaled_bg, bg_rect)
        PAUSE.update(SCREEN)
        PAUSE.changeColor(MENU_MOUSE_POS)
        char('assets/mc.png',430,1)
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
        screen.blit(snip, (295, 600))

        pygame.display.flip()

def dialogue25():
    font = pygame.font.Font('assets/Font/ARCADE.TTF', 24)
    screen = pygame.display.set_mode ([1280, 720])
    timer = pygame.time.Clock()
    messages = ('Roman : Let me make a guess...',
                'Roman : They\'re Emir\'s henchmen, right?',
                'Luna : Since we\'re 10 km away from Emir\'s hideout... ',
                'Luna : It\'s definitely his.',
                'Roman : Too bad for \'em that we have some preparation!',
                'Luna : <laughs> Yeah, they stood no chance!',
                'Roman : Did you see how I-.',
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

        bg = pygame.image.load('assets/driving.jpg')
        scaled_bg = pygame.transform.scale(bg, (1280,720))
        bg_rect = scaled_bg.get_rect(x=0,y=0)
        
        textbox = pygame.image.load('assets/textboxlover.png')
        scaled_texbox = pygame.transform.scale(textbox, (850,450))
        textbox_rect = scaled_texbox.get_rect(x=220,y=410)

        SCREEN.blit(scaled_bg, bg_rect)
        PAUSE.update(SCREEN)
        PAUSE.changeColor(MENU_MOUSE_POS)
        char('assets/seriousmc.png',320,50)
        char('assets/confusedwalter.png',600,20)
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
                if active_message == 7:
                    dialogue26()

        snip = font.render(message[0:counter//speed], True, 'white')
        screen.blit(snip, (295, 600))

        pygame.display.flip()

def dialogue26():
    font = pygame.font.Font('assets/Font/ARCADE.TTF', 24)
    screen = pygame.display.set_mode ([1280, 720])
    timer = pygame.time.Clock()
    messages = ('Before Roman finished his sentence...',
                'A giant truck hit them out of nowhere.',
                'Then, everything goes dark for both of them.',
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

        bg = pygame.image.load('assets/cargethit.jpg')
        scaled_bg = pygame.transform.scale(bg, (1280,720))
        bg_rect = scaled_bg.get_rect(x=0,y=0)
        
        textbox = pygame.image.load('assets/textboxlover.png')
        scaled_texbox = pygame.transform.scale(textbox, (850,450))
        textbox_rect = scaled_texbox.get_rect(x=220,y=410)

        SCREEN.blit(scaled_bg, bg_rect)
        PAUSE.update(SCREEN)
        PAUSE.changeColor(MENU_MOUSE_POS)
        char('assets/mc.png',430,1)
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
                    transition10()

        snip = font.render(message[0:counter//speed], True, 'white')
        screen.blit(snip, (295, 600))

        pygame.display.flip()

def transition10():
    start_alpha = 255

    bg = pygame.image.load('assets/cargethit.jpg')
    scaled_bg = pygame.transform.scale(bg, (1280,720))
    bg_rect = scaled_bg.get_rect(x=0,y=0)
    
    while start_alpha > 0:
        SCREEN.fill(BLACK)
        scaled_bg.set_alpha(start_alpha)
        SCREEN.blit(scaled_bg, bg_rect)
        pygame.display.flip()
        pygame.time.delay(10)
        start_alpha -= 1
    if start_alpha == 0:
        transition11()
    pygame.time.delay(2000)

def transition11():
    start_alpha = 0

    bg = pygame.image.load('assets/white.png')
    scaled_bg = pygame.transform.scale(bg, (1280,720))
    bg_rect = scaled_bg.get_rect(x=0,y=0)

    while start_alpha < 255:
        SCREEN.fill(BLACK)
        scaled_bg.set_alpha(start_alpha)
        SCREEN.blit(scaled_bg, bg_rect)
        pygame.display.flip()
        pygame.time.delay(10)
        start_alpha += 1
    if start_alpha == 255:
        dialogue27()
    pygame.time.delay(1000)

def dialogue27():
    font = pygame.font.Font('assets/Font/ARCADE.TTF', 24)
    screen = pygame.display.set_mode ([1280, 720])
    timer = pygame.time.Clock()
    messages = ('...',
                '...',
                '...up.',
                '...man ...up.',
                'Ro... man... wake... up...',
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

        bg = pygame.image.load('assets/black.png')
        scaled_bg = pygame.transform.scale(bg, (1280,720))
        bg_rect = scaled_bg.get_rect(x=0,y=0)
        
        textbox = pygame.image.load('assets/textboxlover.png')
        scaled_texbox = pygame.transform.scale(textbox, (850,450))
        textbox_rect = scaled_texbox.get_rect(x=220,y=410)

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
                    dialogue28()

        snip = font.render(message[0:counter//speed], True, 'white')
        screen.blit(snip, (295, 600))

        pygame.display.flip()

def dialogue28():
    font = pygame.font.Font('assets/Font/ARCADE.TTF', 24)
    screen = pygame.display.set_mode ([1280, 720])
    timer = pygame.time.Clock()
    messages = ('Luna : Roman, wake up!',
                'Roman : !?',
                'Roman : ...what happened?',
                'Luna : I don\'t know, but the last thing I know is...',
                'Luna : ...we\'ve been hit by a sand truck.',
                'Roman : The fuck...?',
                'Roman : Ngh... I can\'t get up.',
                'Luna : Same here...',
                '??? : ahaha...',
                '??? : AHAHAHAHA!!!',
                'Roman and Luna : Huh!?',
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

        bg = pygame.image.load('assets/roadside.jpg')
        scaled_bg = pygame.transform.scale(bg, (1280,720))
        bg_rect = scaled_bg.get_rect(x=0,y=0)
        
        textbox = pygame.image.load('assets/textboxlover.png')
        scaled_texbox = pygame.transform.scale(textbox, (850,450))
        textbox_rect = scaled_texbox.get_rect(x=220,y=410)

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
                if active_message == 11:
                    dialogue29()

        snip = font.render(message[0:counter//speed], True, 'white')
        screen.blit(snip, (295, 600))

        pygame.display.flip()

def dialogue29():
    font = pygame.font.Font('assets/font/ARCADE.TTF', 24)
    screen = pygame.display.set_mode ([1280, 720])
    timer = pygame.time.Clock()
    messages = ('Emir : Ah... It\'s pleasuring to see you both got hit.',
                'Emir : <laughs> Can we repeat that again?',
                'Roman : What\'s so funny, Emir!?',
                'Emir : Nothing much. But the thoughts of killing you both here...',
                'Emir : <laughs> It\'s just too amusing!',
                'Emir : <laughs> I get to kill two birds with a stone!',
                'Roman : Two birds...? Wait, you didn\'t mean...',
                'Emir : <laughs> Oh, yes! I did!',
                'Roman : Let go of Luna, Emir! She has nothing to do with this!',
                'Emir : Oh, yeah... you\'re right, I\'ll let her go...',
                'Emir : ...to the afterlife!!!',
                'Emir points his gun towards Luna\'s head.',
                'Roman : Goddammit, Emir!',
                'The trigger of the gun is being pulled...',
                'Roman : You fucker!!!',
                'Roman throws some dust towards Emir\'s eyes.',
                'Emir : Ngh! My eyes!',
                'Roman charges towards Emir.',
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

        bg = pygame.image.load('assets/sneakwarden.jpg')
        scaled_bg = pygame.transform.scale(bg, (1280,720))
        bg_rect = scaled_bg.get_rect(x=0,y=0)
        
        textbox = pygame.image.load('assets/textboxlover.png')
        scaled_texbox = pygame.transform.scale(textbox, (850,450))
        textbox_rect = scaled_texbox.get_rect(x=220,y=410)

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
                if active_message == 18:
                    dialogue30()

        snip = font.render(message[0:counter//speed], True, 'white')
        screen.blit(snip, (295, 600))

        pygame.display.flip()

def dialogue30():
    font = pygame.font.Font('assets/Font/ARCADE.TTF', 24)
    screen = pygame.display.set_mode ([1280, 720])
    timer = pygame.time.Clock()
    messages = ('Roman charges, landing a punch to Emir\'s jaw.', 
                'Emir recovers quickly, kicking Roman\'s side.',
                'The fight is fierce, each blow filled with anger and resolve.',
                'Roman : <dodging a punch> Get out of my fucking life!.',
                'Emir : <throwing a punch> Nope, I\'m craving for your blood!',
                'Roman ducks, counters with rapid punches.',
                'Emir grunts, grabs Roman\'s arm, twisting it.',
                'Roman grits his teeth, elbows Emir\'s face, stumbles him back.',
                'Roman: <breathing heavily> You\'re a fucking maniac, Emir!',
                'Emir: <panting, wiping blood> Well, yes I am!',
                'Roman: <shouting> Fucking annoying!!!',
                'As Emir throws a punch towards Roman, he dodges it...',
                '...and kicks behind his knee, immobilizes him.',
                'A last powerful kick sent towards Emir\'s jaw, stumbling him.',
                'Roman uses this chance to grab a piece of metal from the car...',
                'Roman : So long, psycho.',
                'With a final, powerful strike...', 
                'Roman stabs Emir\'s chest with the metal, defeated.',
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

        bg = pygame.image.load('assets/roadside.jpg')
        scaled_bg = pygame.transform.scale(bg, (1280,720))
        bg_rect = scaled_bg.get_rect(x=0,y=0)
        
        textbox = pygame.image.load('assets/textboxlover.png')
        scaled_texbox = pygame.transform.scale(textbox, (850,450))
        textbox_rect = scaled_texbox.get_rect(x=220,y=410)

        SCREEN.blit(scaled_bg, bg_rect)
        PAUSE.update(SCREEN)
        PAUSE.changeColor(MENU_MOUSE_POS)
        char('assets/fightingmc.png',270,1)
        char('assets/Chapter2/villainnormal.png',650,20)
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
                if active_message == 18:
                    dialogue31()

        snip = font.render(message[0:counter//speed], True, 'white')
        screen.blit(snip, (295, 600))

        pygame.display.flip()

def dialogue31():
    font = pygame.font.Font('assets/Font/ARCADE.TTF', 24)
    screen = pygame.display.set_mode ([1280, 720])
    timer = pygame.time.Clock()
    messages = ('Roman : <laughs> Luna, It\'s finally over...',
                'Roman hugs Luna, who\'s on the ground.',
                'Luna : Yes, it\'s finally over, Roman.',
                '...')
    snip = font.render('', True, 'white')
    counter = 0
    speed = 1
    active_message = 0
    message = messages[active_message]
    chap2_ending.play(-1)

    run = True

    while run:

        timer = pygame.time.Clock()

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        PAUSE = Button(image=pygame.image.load("assets/pause.png"), pos=(50, 50), 
                            text_input="           ", font=textbutton_font(21), base_color="black", hovering_color="#FF3131")

        bg = pygame.image.load('assets/roadside.jpg')
        scaled_bg = pygame.transform.scale(bg, (1280,720))
        bg_rect = scaled_bg.get_rect(x=0,y=0)
        
        textbox = pygame.image.load('assets/textboxlover.png')
        scaled_texbox = pygame.transform.scale(textbox, (850,450))
        textbox_rect = scaled_texbox.get_rect(x=220,y=410)

        SCREEN.blit(scaled_bg, bg_rect)
        PAUSE.update(SCREEN)
        PAUSE.changeColor(MENU_MOUSE_POS)
        char('assets/mc.png',270,1)
        char('assets/Chapter2/loverOTW.png',670,1)
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
                    dialogue32()

        snip = font.render(message[0:counter//speed], True, 'white')
        screen.blit(snip, (295, 600))

        pygame.display.flip()

def dialogue32():
    font = pygame.font.Font('assets/Font/ARCADE.TTF', 24)
    screen = pygame.display.set_mode ([1280, 720])
    timer = pygame.time.Clock()
    messages = ('At last, the dreaded battle has finally come to and end.',
                'The two embrace themselves in warm hug and kiss.',
                'With the battle\'s echoes fading into the night.',
                'Roman looked towards the horizon, the weight of his past lifting.',
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

        bg = pygame.image.load('assets/roadside.jpg')
        scaled_bg = pygame.transform.scale(bg, (1280,720))
        bg_rect = scaled_bg.get_rect(x=0,y=0)
        
        textbox = pygame.image.load('assets/textboxlover.png')
        scaled_texbox = pygame.transform.scale(textbox, (850,450))
        textbox_rect = scaled_texbox.get_rect(x=220,y=410)

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
                if active_message == 4:
                    transition12()

        snip = font.render(message[0:counter//speed], True, 'white')
        screen.blit(snip, (295, 600))

        pygame.display.flip()

def transition12():
    start_alpha = 255

    bg = pygame.image.load('assets/roadside.jpg')
    scaled_bg = pygame.transform.scale(bg, (1280,720))
    bg_rect = scaled_bg.get_rect(x=0,y=0)
    
    while start_alpha > 0:
        SCREEN.fill(BLACK)
        scaled_bg.set_alpha(start_alpha)
        SCREEN.blit(scaled_bg, bg_rect)
        pygame.display.flip()
        pygame.time.delay(5)
        start_alpha -= 1
    if start_alpha == 0:
        transition13()
    pygame.time.delay(2000)

def transition13():
    start_alpha = 0

    bg = pygame.image.load('assets/marriage.jpg')
    scaled_bg = pygame.transform.scale(bg, (1280,720))
    bg_rect = scaled_bg.get_rect(x=0,y=0)

    while start_alpha < 255:
        SCREEN.fill(BLACK)
        scaled_bg.set_alpha(start_alpha)
        SCREEN.blit(scaled_bg, bg_rect)
        pygame.display.flip()
        pygame.time.delay(5)
        start_alpha += 1
    if start_alpha == 255:
        dialogue33()
    pygame.time.delay(10000)

def dialogue33():
    font = pygame.font.Font('assets/Font/ARCADE.TTF', 24)
    screen = pygame.display.set_mode ([1280, 720])
    timer = pygame.time.Clock()
    messages = ('Months later, he stood in a lush garden...',
                'Far from the hustle of the city, with Luna, his beloved.',
                'Their wedding day was bright and clear.',
                'Under an arch of blooming flowers...',
                'They exchanged vows surrounded by friends and loved ones.',
                'The air was filled with laughter and the scent of blossoms...',
                'A stark contrast to their past struggles.',
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

        bg = pygame.image.load('assets/marriage.jpg')
        scaled_bg = pygame.transform.scale(bg, (1280,720))
        bg_rect = scaled_bg.get_rect(x=0,y=0)
        
        textbox = pygame.image.load('assets/textboxlover.png')
        scaled_texbox = pygame.transform.scale(textbox, (850,450))
        textbox_rect = scaled_texbox.get_rect(x=220,y=410)

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
                if active_message == 7:
                    transition14()

        snip = font.render(message[0:counter//speed], True, 'white')
        screen.blit(snip, (295, 600))

        pygame.display.flip()

def transition14():
    start_alpha = 255

    bg = pygame.image.load('assets/marriage.jpg')
    scaled_bg = pygame.transform.scale(bg, (1280,720))
    bg_rect = scaled_bg.get_rect(x=0,y=0)
    
    while start_alpha > 0:
        SCREEN.fill(BLACK)
        scaled_bg.set_alpha(start_alpha)
        SCREEN.blit(scaled_bg, bg_rect)
        pygame.display.flip()
        pygame.time.delay(5)
        start_alpha -= 1
    if start_alpha == 0:
        transition15()
    pygame.time.delay(2000)

def transition15():
    start_alpha = 0

    bg = pygame.image.load('assets/baby.jpg')
    scaled_bg = pygame.transform.scale(bg, (1280,720))
    bg_rect = scaled_bg.get_rect(x=0,y=0)

    while start_alpha < 255:
        SCREEN.fill(BLACK)
        scaled_bg.set_alpha(start_alpha)
        SCREEN.blit(scaled_bg, bg_rect)
        pygame.display.flip()
        pygame.time.delay(5)
        start_alpha += 1
    if start_alpha == 255:
        dialogue34()
    pygame.time.delay(10000)

def dialogue34():
    font = pygame.font.Font('assets/Font/ARCADE.TTF', 24)
    screen = pygame.display.set_mode ([1280, 720])
    timer = pygame.time.Clock()
    messages = ('In the years that followed...', 
                'Roman and Luna built a life of love and joy.',
                'They created a home...', 
                'Where peace and contentment replaced memories of pain.',
                'Together, they walked a path of happiness...',
                'Hand in hand, their future bright under the stars.',
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

        bg = pygame.image.load('assets/baby.jpg')
        scaled_bg = pygame.transform.scale(bg, (1280,720))
        bg_rect = scaled_bg.get_rect(x=0,y=0)
        
        textbox = pygame.image.load('assets/textboxlover.png')
        scaled_texbox = pygame.transform.scale(textbox, (850,450))
        textbox_rect = scaled_texbox.get_rect(x=220,y=410)

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
                if active_message == 6:
                    transition16()

        snip = font.render(message[0:counter//speed], True, 'white')
        screen.blit(snip, (295, 600))

        pygame.display.flip()

def transition16():
    start_alpha = 255

    bg = pygame.image.load('assets/ss2.png')
    scaled_bg = pygame.transform.scale(bg, (1280,720))
    bg_rect = scaled_bg.get_rect(x=0,y=0)
    
    while start_alpha > 0:
        SCREEN.fill(BLACK)
        scaled_bg.set_alpha(start_alpha)
        SCREEN.blit(scaled_bg, bg_rect)
        pygame.display.flip()
        pygame.time.delay(10)
        start_alpha -= 1
    if start_alpha == 0:
        dialogue35()
    pygame.time.delay(2000)

def dialogue35():
    font = pygame.font.Font('assets/Font/ARCADE.TTF', 24)
    screen = pygame.display.set_mode ([1280, 720])
    timer = pygame.time.Clock()
    messages = ('And so...', 
                'They lived happily ever after, their love a triumph over adversity.',
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

        bg = pygame.image.load('assets/black.png')
        scaled_bg = pygame.transform.scale(bg, (1280,720))
        bg_rect = scaled_bg.get_rect(x=0,y=0)

        SCREEN.blit(scaled_bg, bg_rect)
        PAUSE.update(SCREEN)
        PAUSE.changeColor(MENU_MOUSE_POS)

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
                    transition17()

        snip = font.render(message[0:counter//speed], True, 'white')
        screen.blit(snip, (295, 600))

        pygame.display.flip()

def transition17():
    start_alpha = 255

    bg = pygame.image.load('assets/black.png')
    scaled_bg = pygame.transform.scale(bg, (1280,720))
    bg_rect = scaled_bg.get_rect(x=0,y=0)
    
    while start_alpha > 0:
        SCREEN.fill(BLACK)
        scaled_bg.set_alpha(start_alpha)
        SCREEN.blit(scaled_bg, bg_rect)
        draw_text('Thanks for playing until the ending', prologuefont(100), WHITE, SCREEN, 640, 360, alpha=start_alpha)
        draw_text('Hope you\'re touched by the story...', prologuefont(30), WHITE, SCREEN, 640, 450, alpha=start_alpha)
        draw_text('Congratulations, you\'ve unlocked true ending!', prologuefont(100), WHITE, SCREEN, 640, 360, alpha=start_alpha)
        pygame.display.flip()
        pygame.time.delay(10)
        start_alpha -= 1
    if start_alpha == 0:
        transition()
    pygame.time.delay(100000)

def transition18():
    start_background_image = pygame.image.load('assets/black.png')
    start_alpha = 0

    while start_alpha < 255:
        SCREEN.fill(BLACK)
        start_background_image.set_alpha(start_alpha)
        SCREEN.blit(start_background_image, (0, 0))
        draw_text('CHAPTER II', prologuefont(100), WHITE, SCREEN, 640, 360, alpha=start_alpha)
        draw_text('Amour, or Malevolence?', prologuefont(30), WHITE, SCREEN, 640, 450, alpha=start_alpha)
        pygame.display.flip()
        pygame.time.delay(10)
        start_alpha += 1
    if start_alpha == 255:
        transition2()
    pygame.time.delay(10000)



def transition2():
    start_background_image = pygame.image.load('assets/black.png')
    start_alpha = 255
    
    while start_alpha > 0:
        SCREEN.fill(BLACK)
        start_background_image.set_alpha(start_alpha)
        SCREEN.blit(start_background_image, (0, 0))
        draw_text('CHAPTER II', prologuefont(100), WHITE, SCREEN, 640, 360, alpha=start_alpha)
        draw_text('Amour, or Malevolence?', prologuefont(30), WHITE, SCREEN, 640, 450, alpha=start_alpha)
        pygame.display.flip()
        pygame.time.delay(10)
        start_alpha -= 1
    if start_alpha == 0:
        chap2_bgm.stop()
        dialogue7()
    pygame.time.delay(1000)