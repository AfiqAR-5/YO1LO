import pygame
import random
import sys
from button import Button

pygame.init()

screen_width = 1280
screen_height = 720
screen = pygame.display.set_mode((screen_width, screen_height))

font = pygame.font.Font(None, 50)
dialogue_font = pygame.font.Font(None, 36)

base_color = (255, 255, 255)
hovering_color = (255, 0, 0)
dead_screen_color = (0, 0, 0)
dead_screen_text_color = (255, 255, 255)

arrow_up_image = pygame.image.load("up_button.png")
arrow_down_image = pygame.image.load("down_button.png")
arrow_left_image = pygame.image.load("left_button.png")
arrow_right_image = pygame.image.load("right_button.png")

arrow_images = [arrow_up_image, arrow_down_image, arrow_left_image, arrow_right_image, arrow_up_image, arrow_left_image]

background_images_original = ['qtebg/clock.png', 'qtebg/dadstudy.png', 'qtebg/backyard.png', 'qtebg/livingroom.png', 'qtebg/mcroom.png', 'qtebg/shattered.png', 'qtebg/neighbourbg.png']
background_images_scaled = [pygame.transform.scale(pygame.image.load(image_path), (1280, 720)) for image_path in background_images_original]

def create_random_button():
    button_width = 150
    button_height = 115
    x_pos = random.randint(button_width // 2, screen_width - button_width // 2)
    y_pos = random.randint(button_height // 2, screen_height - button_height // 2)
    button = Button(image=arrow_up_image, pos=(x_pos, y_pos), text_input=None, font=font, base_color=base_color, hovering_color=hovering_color)
    return button

def you_are_dead_screen():
    screen.fill(dead_screen_color)
    text = font.render("You are dead!", True, dead_screen_text_color)
    text_rect = text.get_rect(center=(screen_width // 2, screen_height // 2))
    screen.blit(text, text_rect)
    pygame.display.flip()
    pygame.time.delay(2000)
    pygame.quit()

def you_win():
    screen.fill(dead_screen_color)
    text = font.render("You Win!", True, dead_screen_text_color)
    text_rect = text.get_rect(center=(screen_width // 2, screen_height // 2))
    screen.blit(text, text_rect)
    pygame.display.flip()
    pygame.time.delay(2000)
    pygame.quit()

def qtebdialogue1():
    font = pygame.font.Font(None, 24)
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
    continue_button_press = False

    run = True
    while run:

        screen.fill("white")  #replace this with bg

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
                        continue_button_press = True
                if continue_button_press:
                    return

        snip = font.render(message[0:counter//speed], True, 'black')
        screen.blit(snip, (300, 360))

        pygame.display.flip()

def qtebdialogue2():
    font = pygame.font.Font(None, 24)
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
    continue_button_press = False

    run = True
    while run:

        screen.fill("white")

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
                        continue_button_press = True
                if continue_button_press:
                    return

        snip = font.render(message[0:counter//speed], True, 'black')
        screen.blit(snip, (300, 360))

        pygame.display.flip()


def qtebdialogue3():
    font = pygame.font.Font(None, 24)
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
    continue_button_press = False

    run = True
    while run:

        screen.fill("white")

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
                        continue_button_press = True
                if continue_button_press:
                    return

        snip = font.render(message[0:counter//speed], True, 'black')
        screen.blit(snip, (300, 360))

        pygame.display.flip()


def main():
    running = True
    clock = pygame.time.Clock()
    button = create_random_button()
    button_timer = 3000
    button_start_time = pygame.time.get_ticks()
    button_press_count = 0
    show_dialogue_1 = False
    show_dialogue_2 = False
    show_dialogue_3 = False

    directions = [pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_LEFT]
    current_direction = 0

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == directions[current_direction]:
                    current_direction += 1
                    if current_direction >= len(directions):
                        print("You Win!")
                        you_win()
                        running = False
                    else:
                        button = create_random_button()
                        button.image = arrow_images[current_direction]  # Change the button image
                        button_start_time = pygame.time.get_ticks()
                else:
                    print("Wrong key pressed!")
                    you_are_dead_screen()
                    running = False

        mouse_pos = pygame.mouse.get_pos()
        button.changeColor(mouse_pos)

        screen.blit(background_images_scaled[current_direction], [0, 0])

        button.update(screen)

        if pygame.time.get_ticks() - button_start_time > button_timer:
            print("Button timer expired!")
            you_are_dead_screen()
            running = False

        if current_direction == 2 and not show_dialogue_1:
            show_dialogue_1 = True
            button_timer = 15000
            button_start_time = pygame.time.get_ticks()
            qtebdialogue1()
            button_timer = 3000
            button_start_time = pygame.time.get_ticks()

        if current_direction == 4 and not show_dialogue_2:
            show_dialogue_2 = True
            button_timer = 15000
            button_start_time = pygame.time.get_ticks()
            qtebdialogue2()
            button_timer = 3000
            button_start_time = pygame.time.get_ticks()

        if current_direction == 6 and not show_dialogue_3:
            show_dialogue_3 = True
            button_timer = 15000
            button_start_time = pygame.time.get_ticks()
            qtebdialogue3()
            button_timer = 3000
            button_start_time = pygame.time.get_ticks()

        pygame.display.flip()

        clock.tick(30)

    pygame.quit()

if __name__ == "__main__":
    main()
