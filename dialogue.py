import pygame, sys
from config import *
pygame.init()

def mc():
     mc = pygame.image.load('assets/mc.png')
     mc_rect = mc.get_rect(x=300,y=180)

     return SCREEN.blit(mc,mc_rect)

def walter():
     walter = pygame.image.load('assets/walter.png')
     walter_rect = walter.get_rect(x=830,y=180)

     return SCREEN.blit(walter, walter_rect)

def dialogue():
    font = pygame.font.Font('assets/ARCADE.TTF', 24)
    screen = pygame.display.set_mode ([1280, 720])
    timer = pygame.time.Clock()
    messages = ('Reality is often dissappointing, isn\'t it?',
                'Imagine going through an exhausting day at school...',
                'Only to witness a tragic massacre of your own family...',
                '...and to be accused of the cruelty.',
                'This is a story about our MC : (Ieman)')
    snip = font.render('', True, 'white')
    counter = 0
    speed = 3
    active_message = 0
    message = messages[active_message]
    done = False

    run = True
    while run:
        bg = pygame.image.load('assets/prisoncell.png')
        scaled_bg = pygame.transform.scale(bg, (1280,720))
        bg_rect = scaled_bg.get_rect(x=0,y=0)
        
        textbox = pygame.image.load('assets/textbox.png')
        scaled_texbox = pygame.transform.scale(textbox, (850,200))
        textbox_rect = scaled_texbox.get_rect(x=220,y=500)

        screen.blit(scaled_bg, bg_rect)
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
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN and done and active_message < len(messages) - 1:
                    active_message += 1
                    done = False
                    message = messages[active_message]
                    counter = 0
                if active_message == 4:
                    dialogue2()

        snip = font.render(message[0:counter//speed], True, 'white')
        screen.blit(snip, (230, 550))

        pygame.display.flip()

def dialogue2():
    font = pygame.font.Font('assets/ARCADE.TTF', 24)
    screen = pygame.display.set_mode ([1280, 720])
    timer = pygame.time.Clock()
    messages = ('This is a story about our MC : (Ieman)',
                'MC : *yawns*',
                'MC : Another day, another shitty meal from the warden',
                'MC : You\'re not going to the cafeteria, NPC?')
    snip = font.render('', True, 'white')
    counter = 0
    speed = 3
    active_message = 0
    message = messages[active_message]
    done = False

    run = True
    while run:
        bg = pygame.image.load('assets/prisoncell.png')
        scaled_bg = pygame.transform.scale(bg, (1280,720))
        bg_rect = scaled_bg.get_rect(x=0,y=0)
        screen.blit(scaled_bg, bg_rect)
        mc()

        timer.tick(60)
        pygame.draw.rect(screen, 'black', [180, 500, 900, 200])
        if counter < speed * len(message):
            counter += 1
        elif counter >= speed * len(message):
            done = True

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN and done and active_message < len(messages) - 1:
                    active_message += 1
                    done = False
                    message = messages[active_message]
                    counter = 0
                if active_message == 3:
                    dialogue3()

        snip = font.render(message[0:counter//speed], True, 'white')
        screen.blit(snip, (280, 550))

        pygame.display.flip()

def dialogue3():
    font = pygame.font.Font('assets/ARCADE.TTF', 24)
    screen = pygame.display.set_mode ([1280, 720])
    timer = pygame.time.Clock()
    messages = ('MC : You\'re not going to the cafeteria, NPC?',
                'Reality is often dissappointing, isn\'t it?',
                'Imagine going through an exhausting day at school...',
                'Only to witness a tragic massacre of your own family...',
                '...and to be accused of the cruelty.',
                'This is a story about our MC : (Suggest name)')
    snip = font.render('', True, 'white')
    counter = 0
    speed = 3
    active_message = 0
    message = messages[active_message]
    done = False

    run = True
    while run:
        bg = pygame.image.load('assets/prisoncell.png')
        scaled_bg = pygame.transform.scale(bg, (1280,720))
        bg_rect = scaled_bg.get_rect(x=0,y=0)
        screen.blit(scaled_bg, bg_rect)
        mc()

        timer.tick(60)
        pygame.draw.rect(screen, 'black', [180, 500, 900, 200])
        if counter < speed * len(message):
            counter += 1
        elif counter >= speed * len(message):
            done = True

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN and done and active_message < len(messages) - 1:
                    active_message += 1
                    done = False
                    message = messages[active_message]
                    counter = 0
                if active_message == 1:
                    walter()


        snip = font.render(message[0:counter//speed], True, 'white')
        screen.blit(snip, (230, 550))

        pygame.display.flip()

dialogue()