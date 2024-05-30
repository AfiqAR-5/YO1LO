import pygame
import random
import time

pygame.init()
pygame.mixer.init()

# Background music
pygame.mixer.music.load('assets/qtebgm.mp3')  
pygame.mixer.music.play(-1)

width, height = 1280, 720
window = pygame.display.set_mode((width, height))
pygame.display.set_caption('finding clues')

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)

# background image + scaling
background_images_original = ['qtebg/clock.png', 'qtebg/dadstudy.png', 'qtebg/backyard.png', 'qtebg/livingroom.png', 'qtebg/mcroom.png', 'qtebg/shattered.png', 'qtebg/neighbourbg.png']
background_images_scaled = [pygame.transform.scale(pygame.image.load(image_path), (1280, 720)) for image_path in background_images_original]

# prompt images + scaling
prompt_images_original = ['qteimage/document.png', 'qteimage/daddiary.png', 'qteimage/bullet.png', 'qteimage/oldknife.png', 'qteimage/mcfavbook.png', 'qteimage/familyframe.png', 'qteimage/polaroid.png']
prompt_images_scaled = [pygame.transform.scale(pygame.image.load(image_path), (150, 115)) for image_path in prompt_images_original]

background_index = 0
prompt_index = 0
background_image = background_images_scaled[background_index]
image = prompt_images_scaled[prompt_index]
image_rect = image.get_rect()

# font
font_file = 'assets/ARCADECLASSIC.ttf'
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
    win_background_image = pygame.image.load('assets/background.png')
    win_alpha = 0
    pygame.mixer.music.load('assets/yay.mp3')
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
    start_background_image = pygame.image.load('assets/background.png')
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

pygame.mixer.music.stop()
pygame.quit()
