import pygame, sys, random, time
from config import *
from button import Button
from subprocess import call

pygame.init()

pygame.mixer.init()

width, height = 1280, 720
window = pygame.display.set_mode((width, height))
screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("YO1LO")

chap2_bgm = pygame.mixer.Sound("assets/Audio/chap2_opening.mp3")
bgmusic = pygame.mixer.Sound("assets/Audio/bgmtwo.mp3")
bgsound = pygame.mixer.Sound("assets/Audio/gta.wav")
boomsound = pygame.mixer.Sound("assets/Audio/shoot_sound.wav")
window_sound = pygame.mixer.Sound("assets/Audio/Window.mp3")
keyboard = pygame.mixer.Sound("assets/Audio/keyboard.mp3")
chap2_bgm = pygame.mixer.Sound("assets/Audio/chap2_opening.mp3")
phone = pygame.mixer.Sound("assets/Audio/phone.mp3")

# findclues music
bg_music = pygame.mixer.Sound('assets/Audio/qtebgm.mp3')

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

#colours
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)

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

def mc(xpos, ypos):
     mc = pygame.image.load('assets/mc.png')
     mc_rect = mc.get_rect(x=xpos, y=ypos)

     return SCREEN.blit(mc,mc_rect)

def prologuefont(size):
    return pygame.font.Font("assets/Font/Cinzel.ttf", size)

def textbutton_font(size):
    return pygame.font.Font("assets/Font/ARCADE.TTF", size)

def button_font(size): 
    return pygame.font.Font("assets/Font/buttonfont.ttf", size)\
    
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

def char(file_path, xpos, ypos):
    char = pygame.image.load(file_path)
    char_rect = char.get_rect(x=xpos, y=ypos)
    return SCREEN.blit(char, char_rect)

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
    win_background_image = pygame.image.load('assets/blackscreen.png')
    win_alpha = 0
    pygame.mixer.music.load('assets/Audio/yay.mp3')
    pygame.mixer.music.play()
    while win_alpha < 255:
        window.fill(black)
        win_background_image.set_alpha(win_alpha)
        window.blit(win_background_image, (0, 0))
        draw_text('You found all the clues!', custom_font, white, window, width // 2, height // 2, alpha=win_alpha)
        pygame.display.flip()
        pygame.time.delay(10)
        win_alpha += 1
    pygame.time.delay(4000)

def start_screen():
    bg_music.play(-1)
    start_background_image = pygame.image.load('assets/blackscreen.png')
    start_alpha = 255
    while start_alpha > 0:
        window.fill(black)
        start_background_image.set_alpha(start_alpha)
        window.blit(start_background_image, (0, 0))
        draw_text('Find all clues!', custom_font, white, window, width // 2, height // 2, alpha=start_alpha)
        pygame.display.flip()
        pygame.time.delay(10)
        start_alpha -= 1
    pygame.time.delay(2000)

def findclues():
    start_screen()
    reset_qte()
    global success_count
    running = True
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
                            dialogue444()
                    else:
                        if success_count < max_successes:
                            draw_text('Too Late!', custom_font, red, window, width // 2, height // 2, alpha=255)
                            pygame.display.flip()
                            pygame.time.delay(1000)
                            reset_qte()

        window.blit(background_image, (0, 0))

        if qte_triggered:
            time_left = qte_time - (time.time() - qte_start_time)
            if time_left > 0:
                window.blit(image, image_rect)
            else:
                if success_count < max_successes:
                    draw_text('Too Late!', custom_font, red, window, width // 2, height // 2, alpha=255)
                    pygame.display.flip()
                    pygame.time.delay(1000)
                    reset_qte()

        pygame.display.flip()
        pygame.time.Clock().tick(30)

    bg_music.stop()
    pygame.quit()

def transition_beginning():
    transition()
    timer = pygame.time.Clock()
    global righteous,sinful

    run = True
    while run:

        timer.tick(60)
        SCREEN.fill('black')

        end = textbutton_font(70).render("Continue?", True, "White")
        end_rect = end.get_rect(x=500, y=260)
        SCREEN.blit(end,end_rect)

        troll = textbutton_font(25).render("Warning : If you choose to quit, then the progress resets.", True, "White")
        troll_rect = troll.get_rect(x=310, y=320)
        SCREEN.blit(troll,troll_rect)

        MENU_MOUSE_POS = pygame.mouse.get_pos()  #detecting mouse position

        CHOICE1 = Button(image=pygame.image.load("assets/transparent.png"), pos=(640, 460), 
                            text_input="CONTINUE", font=textbutton_font(23), base_color="white", hovering_color="#FF3131")
         
        CHOICE2 = Button(image=pygame.image.load("assets/transparent.png"), pos=(640, 550), 
                            text_input="QUIT", font=textbutton_font(23), base_color="white", hovering_color="#FF3131")

        for button in [CHOICE1,CHOICE2]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                    if CHOICE1.checkForInput(MENU_MOUSE_POS):
                        if righteous >= 3:
                            print("righteous")
                            pygame.quit()
                            sys.exit()
                        # righteous_path()
                        elif sinful >= 3:
                            print("sinful")
                            pygame.quit()
                            sys.exit()
                            # sinful_path()
                    if CHOICE2.checkForInput(MENU_MOUSE_POS):
                        pygame.quit()
                        sys.exit()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if righteous >= 3:
                        print("righteous")
                        pygame.quit()
                        sys.exit()
                        # righteous_path()
                    elif sinful >= 3:
                        print("sinful")
                        pygame.quit()
                        sys.exit()
                        # sinful_path()

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
        transition_beginning()
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
        dialogue777()
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
        dialogue111()
    pygame.time.delay(4000)

def dialogue111():
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
    bgmusic.play(-1)

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
                    dialogue222()

        snip = font.render(message[0:counter//speed], True, 'white')
        screen.blit(snip, (295, 600))

        pygame.display.flip()

def dialogue222():
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
                    dialogue333()

        snip = font.render(message[0:counter//speed], True, 'white')
        screen.blit(snip, (295, 600))

        pygame.display.flip()
        
def dialogue333():
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
                    # letak finding clues sini
                    bgmusic.stop()
                    findclues()

        snip = font.render(message[0:counter//speed], True, 'white')
        screen.blit(snip, (295, 600))

        pygame.display.flip()

def dialogue444():
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

    bgmusic.play(-1)

    run = True
    while run:

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        PAUSE = Button(image=pygame.image.load("assets/pause.png"), pos=(50, 50), 
                            text_input="           ", font=textbutton_font(21), base_color="black", hovering_color="#FF3131")

        bg = pygame.image.load('assets/bedroom.jpg')
        scaled_bg = pygame.transform.scale(bg, (1280,720))
        bg_rect = scaled_bg.get_rect(x=0,y=0)

        lover = pygame.image.load('assets/Chapter2/lover2.png')
        scaled_lover = pygame.transform.scale(lover, (330,600))
        lover_rect = scaled_lover.get_rect(x=500,y= 50)
        
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
                    dialogue555()

        snip = font.render(message[0:counter//speed], True, 'white')
        screen.blit(snip, (295, 600))

        pygame.display.flip()

def dialogue555():
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
                    dialogue666()

        snip = font.render(message[0:counter//speed], True, 'white')
        screen.blit(snip, (295, 600))

        pygame.display.flip()

def dialogue666():
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
                    bgmusic.stop()
                    transition1()

        snip = font.render(message[0:counter//speed], True, 'white')
        screen.blit(snip, (295, 600))

        pygame.display.flip()

def dialogue777():
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
    bgmusic.play(-1)
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
                if active_message == 19:
                    dialogue888()

        snip = font.render(message[0:counter//speed], True, 'white')
        screen.blit(snip, (295, 600))

        pygame.display.flip()

def dialogue888():
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

        lover = pygame.image.load('assets/Chapter2/lover2.png')
        scaled_lover = pygame.transform.scale(lover, (330,600))
        lover_rect = scaled_lover.get_rect(x=500,y= 20)
        
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
                    bgmusic.stop()
                    dialogue999()

        snip = font.render(message[0:counter//speed], True, 'white')
        screen.blit(snip, (295, 600))

        pygame.display.flip()

def dialogue999():
    pygame.mixer.music.load("assets/Chapter2/bgsoundchap2.wav")
    pygame.mixer.music.play(-1)  # -1 means the music will loop indefinitely
    pygame.mixer.music.set_volume(0.1)
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

        bg = pygame.image.load('assets/Chapter2/chap2.png')
        scaled_bg = pygame.transform.scale(bg, (1280,720))
        bg_rect = scaled_bg.get_rect(x=0,y=0)

        lover = pygame.image.load('assets/Chapter2/lover2.png')
        scaled_lover = pygame.transform.scale(lover, (330,600))
        lover_rect = scaled_lover.get_rect(x=500,y= 20)
        
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
                    dialogue1000()

        snip = font.render(message[0:counter//speed], True, 'white')
        screen.blit(snip, (295, 600))

        pygame.display.flip()

def dialogue1000():
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

        bg = pygame.image.load('assets/Chapter2/chap2.png')
        scaled_bg = pygame.transform.scale(bg, (1280,720))
        bg_rect = scaled_bg.get_rect(x=0,y=0)
        
        textbox = pygame.image.load('assets/textboxlover.png')
        scaled_texbox = pygame.transform.scale(textbox, (850,450))
        textbox_rect = scaled_texbox.get_rect(x=220,y=410)

        screen.blit(scaled_bg, bg_rect)
        PAUSE.update(SCREEN)
        PAUSE.changeColor(MENU_MOUSE_POS)
        char('assets/Chapter2/lover4.png',635,-70)
        char('assets/mc.png',210,20)
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
                    dialogue1100()
        snip = font.render(message[0:counter//speed], True, 'white')
        screen.blit(snip, (295, 600))

        pygame.display.flip()

def dialogue1100():
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

        bg = pygame.image.load('assets/Chapter2/chap2.png')
        scaled_bg = pygame.transform.scale(bg, (1280,720))
        bg_rect = scaled_bg.get_rect(x=0,y=0)
        
        textbox = pygame.image.load('assets/textboxlover.png')
        scaled_texbox = pygame.transform.scale(textbox, (850,450))
        textbox_rect = scaled_texbox.get_rect(x=220,y=410)

        screen.blit(scaled_bg, bg_rect)
        PAUSE.update(SCREEN)
        PAUSE.changeColor(MENU_MOUSE_POS)
        char('assets/Chapter2/lover4.png',400,-85)
        char('assets/mc.png',170,0)
        char('assets/casualemir.png',750,0)
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
                    dialogue1200()

        snip = font.render(message[0:counter//speed], True, 'white')
        screen.blit(snip, (295, 600))

        pygame.display.flip()

def dialogue1200():
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
                'Roman : (Well, I\'ve some kind of suspicions towards Emir though)',
                'Roman : (And it seems, Luna has brought her evidences...)',
                'Roman : (But it suddenly got lost. Something\'s not right...)',
                'Roman moves away a bit from Emir.',
                'Emir : For real? After what we\'ve been through together...',
                'Emir : You still don\'t trust me?',
                'Roman : No, it\'s not that I don\'t trust you... but...',
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

        bg = pygame.image.load('assets/Chapter2/chap2.png')
        scaled_bg = pygame.transform.scale(bg, (1280,720))
        bg_rect = scaled_bg.get_rect(x=0,y=0)
        
        textbox = pygame.image.load('assets/textboxlover.png')
        scaled_texbox = pygame.transform.scale(textbox, (850,450))
        textbox_rect = scaled_texbox.get_rect(x=220,y=410)

        screen.blit(scaled_bg, bg_rect)
        PAUSE.update(SCREEN)
        PAUSE.changeColor(MENU_MOUSE_POS)
        char('assets/mc.png',250,1)
        char('assets/casualemir.png',670,0)
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
                    dialogue1300()

        snip = font.render(message[0:counter//speed], True, 'white')
        screen.blit(snip, (295, 600))

        pygame.display.flip()

def dialogue1300():
    font = pygame.font.Font('assets/Font/ARCADE.TTF', 24)
    screen = pygame.display.set_mode ([1280, 720])
    timer = pygame.time.Clock()
    messages = ('Emir : But what?',
                'Emir : Are you really doubting me?',
                'Emir : After all that we\'ve been through.',
                'Emir : We literally escaped prison together.',
                'Emir : We\'re basically comrades in arms.',
                'Roman : ...You\'re right!',
                'Luna : Really...',
                'Luna : Are you gonna believe him?',
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

        bg = pygame.image.load('assets/Chapter2/chap2.png')
        scaled_bg = pygame.transform.scale(bg, (1280,720))
        bg_rect = scaled_bg.get_rect(x=0,y=0)
        
        textbox = pygame.image.load('assets/textboxlover.png')
        scaled_texbox = pygame.transform.scale(textbox, (850,450))
        textbox_rect = scaled_texbox.get_rect(x=220,y=410)

        screen.blit(scaled_bg, bg_rect)
        PAUSE.update(SCREEN)
        PAUSE.changeColor(MENU_MOUSE_POS)
        char('assets/Chapter2/lover4.png',400,-85)
        char('assets/mc.png',170,0)
        char('assets/casualemir.png',750,0)
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
                    dialogue1400()

        snip = font.render(message[0:counter//speed], True, 'white')
        screen.blit(snip, (295, 600))

        pygame.display.flip()

def dialogue1400():
    font = pygame.font.Font('assets/Font/ARCADE.TTF', 24)
    screen = pygame.display.set_mode ([1280, 720])
    timer = pygame.time.Clock()
    messages = ('Police siren can be heard near their location.',
                'Emir : Roman, we have to go now!',
                'Roman : ...',
                'Luna : Wait Roman, come back!',
                'Roman : Emir, lets go.',
                'Luna : Noooo... ROMAN!',
                '<Emir and Roman disappear in the dark...>',
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

        bg = pygame.image.load('assets/Chapter2/chap2.png')
        scaled_bg = pygame.transform.scale(bg, (1280,720))
        bg_rect = scaled_bg.get_rect(x=0,y=0)
        
        textbox = pygame.image.load('assets/textboxlover.png')
        scaled_texbox = pygame.transform.scale(textbox, (850,450))
        textbox_rect = scaled_texbox.get_rect(x=220,y=410)

        screen.blit(scaled_bg, bg_rect)
        PAUSE.update(SCREEN)
        PAUSE.changeColor(MENU_MOUSE_POS)
        char('assets/Chapter2/lover4.png',400,-85)
        char('assets/mc.png',170,0)
        char('assets/annoyedemir.png',670,50)
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
                    dialogue1500()

        snip = font.render(message[0:counter//speed], True, 'white')
        screen.blit(snip, (295, 600))

        pygame.display.flip()

def dialogue1500():
    font = pygame.font.Font('assets/Font/ARCADE.TTF', 24)
    screen = pygame.display.set_mode ([1280, 720])
    timer = pygame.time.Clock()
    messages = ('<Luna immediately hide-',
                'from the pursuit behind the warehouse building>',
                '<She waits for the police to leave the place>',
                '<After confirming there is no police anymore>',
                '<She lets out her frustration>',
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

        bg = pygame.image.load('assets/Chapter2/chap2.png')
        scaled_bg = pygame.transform.scale(bg, (1280,720))
        bg_rect = scaled_bg.get_rect(x=0,y=0)
        
        textbox = pygame.image.load('assets/textboxlover.png')
        scaled_texbox = pygame.transform.scale(textbox, (850,450))
        textbox_rect = scaled_texbox.get_rect(x=220,y=410)

        SCREEN.blit(scaled_bg, bg_rect)
        PAUSE.update(SCREEN)
        PAUSE.changeColor(MENU_MOUSE_POS)
        char("assets/Chapter2/lover2.png",450,1)
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
                    dialogue1()

        snip = font.render(message[0:counter//speed], True, 'white')
        screen.blit(snip, (295, 600))

        pygame.display.flip()

def dialogue1():

    font = pygame.font.Font('assets/Font/ARCADE.TTF', 24)
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
                'Luna : -that Emir is the murderer.',
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

        lover = pygame.image.load('assets/Chapter2/lover2.png')
        scaled_lover = pygame.transform.scale(lover, (330,600))
        lover_rect = scaled_lover.get_rect(x=500,y= 20)
        
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
        lover_rect = scaled_lover.get_rect(x=515,y=120)

        c2 = pygame.image.load('assets/cbutton.png')
        scaled_c2 = pygame.transform.scale(c2, (300,70))
        c2_rect = scaled_c2.get_rect(x=515,y=600)

        SCREEN.blit(scaled_bg, bg_rect)
        SCREEN.blit(scaled_lover, lover_rect)
        SCREEN.blit(scaled_c2, c2_rect)
    

        timer.tick(60)

        MENU_MOUSE_POS = pygame.mouse.get_pos()  #detecting mouse position
        
        CHOICE1 = Button(image=pygame.image.load("assets/transparent.png"), pos=(665, 637), 
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
                    chap2_act1()
                if PAUSE.checkForInput(MENU_MOUSE_POS):
                    pausemenu()

            pygame.display.flip()

def chap2_act1():
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

        title = prologuefont(40).render("Chapter II Act I", True, "White")
        title_rect = title.get_rect(x=340, y=265)
        SCREEN.blit(title, title_rect)

        head = prologuefont(22).render("PLAN A? PLAN B?..... PLAN C?", True, "White")
        head_rect = head.get_rect(x=343, y=320)
        SCREEN.blit(head,head_rect)

        info = textbutton_font(19).render("Damansara Villa - Mansion - 1:05:58 AM", True, "White")
        info_rect = title.get_rect(x=343, y=425)
        SCREEN.blit(info,info_rect)
        pygame.draw.rect(SCREEN, 'white', (343, 360, 590, 45))

        text1 = prologuefont(13).render("Luna seems to have gotten an idea to convince Roman. Hope still exists for Luna.", True, "black")
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

    font = pygame.font.Font('assets/Font/ARCADE.TTF', 24)
    screen = pygame.display.set_mode ([1280, 720])
    timer = pygame.time.Clock()
    messages = ('Luna : GULPPP... (Drinking Coffee)',
                'Luna : I need to calm my mind.',
                'Luna : SIGHHH... (Take a deep breath)',
                'Luna : <Looking around for Inspiration>',
                'Luna : What\'s so hard for him to believe me?',
                'Luna : How can I convince him?',
                'Luna : I feel like I have an idea.',
                'Luna : I need to think like Emir.',
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

    font = pygame.font.Font('assets/Font/ARCADE.TTF', 24)
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
    pygame.mixer.music.stop()
    pygame.mixer.music.load("assets/Audio/Intense.mp3")
    pygame.mixer.music.play(-1)  # -1 means the music will loop indefinitely
    pygame.mixer.music.set_volume(0.065)

    font = pygame.font.Font('assets/Font/ARCADE.TTF', 24)
    screen = pygame.display.set_mode ([1280, 720])
    timer = pygame.time.Clock()
    messages = ('<CLINK> <CLINK> SOUND OF WINDOW BROKEN!!!',
                'LUNA IS VERY SHOCKED AND PUZZLED!!!',
              
                '...')
    window_sound.play(1)
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
    pygame.mixer.stop()
    font = pygame.font.Font('assets/Font/ARCADE.TTF', 24)
    screen = pygame.display.set_mode ([1280, 720])
    timer = pygame.time.Clock()
    messages = ('Luna : WHO THE HEL* IS RAIDING MY HOUSE!!!',
                'Luna : CRAZY BASTARDS!!!',
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
        scaled_lover = pygame.transform.scale(lover, (400,450))
        lover_rect = scaled_lover.get_rect(x=460,y=145)
        
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
        lover_rect = lover.get_rect(x=470,y=120)

        c2 = pygame.image.load('assets/cbutton.png')
        scaled_c2 = pygame.transform.scale(c2, (300,70))
        c2_rect = scaled_c2.get_rect(x=515,y=600)

        SCREEN.blit(scaled_bg, bg_rect)
        SCREEN.blit(lover, lover_rect)
        SCREEN.blit(scaled_c2, c2_rect)

        timer.tick(60)

        MENU_MOUSE_POS = pygame.mouse.get_pos()  #detecting mouse position
        
        CHOICE1 = Button(image=pygame.image.load("assets/transparent.png"), pos=(665, 637), 
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

    font = pygame.font.Font('assets/Font/ARCADE.TTF', 24)
    screen = pygame.display.set_mode ([1280, 720])
    timer = pygame.time.Clock()
    messages = ('Luna : WHO THE HECK IS THERE?',
                'Luna : GET THE HEL* OUT OF MY HOUSE!!!',
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
        scaled_lover = pygame.transform.scale(lover, (400,450))
        lover_rect = scaled_lover.get_rect(x=460,y=145)
        
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

    font = pygame.font.Font('assets/Font/ARCADE.TTF', 24)
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
        lover_rect = lover.get_rect(x=335,y=250)
        
        textbox = pygame.image.load('assets/textboxlover.png')
        scaled_texbox = pygame.transform.scale(textbox, (850,450))
        textbox_rect = scaled_texbox.get_rect(x=220,y=410)

        screen.blit(scaled_bg, bg_rect)
        PAUSE.update(SCREEN)
        PAUSE.changeColor(MENU_MOUSE_POS)
        SCREEN.blit(lover, lover_rect)
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

    font = pygame.font.Font('assets/Font/ARCADE.TTF', 24)
    screen = pygame.display.set_mode ([1280, 720])
    timer = pygame.time.Clock()
    messages = ('Luna : What the hel* do you want from me?',
                'Luna : Answer me or I will kill you all!',
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
        scaled_lover = pygame.transform.scale(lover, (400,450))
        lover_rect = scaled_lover.get_rect(x=460,y=145)
        
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
        lover_rect = lover.get_rect(x=470,y=120)

        c2 = pygame.image.load('assets/cbutton.png')
        scaled_c2 = pygame.transform.scale(c2, (300,70))
        c2_rect = scaled_c2.get_rect(x=515,y=600)

        SCREEN.blit(scaled_bg, bg_rect)
        SCREEN.blit(lover, lover_rect)
        SCREEN.blit(scaled_c2, c2_rect)
        
        timer.tick(60)

        MENU_MOUSE_POS = pygame.mouse.get_pos()  #detecting mouse position
        
        CHOICE1 = Button(image=pygame.image.load("assets/transparent.png"), pos=(665, 637), 
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
                    pygame.quit()
                    call(["python", "houseraid.py"])
                if PAUSE.checkForInput(MENU_MOUSE_POS):
                    pausemenu()

            pygame.display.flip()

chap2_opening()