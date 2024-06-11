import pygame, sys
import math
import random
from settingshot1 import *
from button import Button
from config import *

pygame.init()

pygame.mixer.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("YO!LO GAME")
clock = pygame.time.Clock()

#loadsoundeffect
shoot_sound = pygame.mixer.Sound("assets/Audio/shoot_sound.wav")
collision_sound = pygame.mixer.Sound("assets/Audio/oof.wav")
dead_sound = pygame.mixer.Sound("assets/Audio/Death_sound.wav")
gta_sound = pygame.mixer.Sound("assets/Audio/gta.wav")

#backgroundimage
background = pygame.transform.scale(pygame.image.load("assets/warehouse.png").convert(), (WIDTH, HEIGHT))

def textbutton_font(size):
    return pygame.font.Font("assets/Font/ARCADE.TTF", size)

def prologuefont(size):
    return pygame.font.Font("assets/Font/Cinzel.ttf", size)

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

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.pos = pygame.math.Vector2(PLAYER_START_X, PLAYER_START_Y)
        self.image = pygame.transform.rotozoom(pygame.image.load("assets/Player11.png").convert_alpha(), 0, PLAYER_SIZE)
        self.base_player_image = self.image
        self.hitbox_rect = self.base_player_image.get_rect(center=self.pos)
        self.rect = self.hitbox_rect.copy()
        self.speed = PLAYER_SPEED
        self.shoot = False
        self.shoot_cooldown = 0
        self.gun_barrel_offset = pygame.math.Vector2(GUN_OFFSET_X, GUN_OFFSET_Y)
        self.max_health = PLAYER_HEALTH
        self.health = self.max_health
        self.health_cooldown = 0
        self.angle = 0  # Initialize the angle attribute

    def reset(self):
        self.pos = pygame.math.Vector2(PLAYER_START_X, PLAYER_START_Y)
        self.health = self.max_health
        self.shoot_cooldown = 0
        self.health_cooldown = 0

    def player_rotation(self):
        self.mouse_coords = pygame.mouse.get_pos()
        self.x_change_mouse_player = (self.mouse_coords[0] - WIDTH // 2)
        self.y_change_mouse_player = (self.mouse_coords[1] - HEIGHT // 2)
        self.angle = math.degrees(math.atan2(self.y_change_mouse_player, self.x_change_mouse_player))
        self.image = pygame.transform.rotate(self.base_player_image, -self.angle)
        self.rect = self.image.get_rect(center=self.hitbox_rect.center)

    def user_input(self):
        self.velocity_x = 0
        self.velocity_y = 0

        keys = pygame.key.get_pressed()

        if keys[pygame.K_w]:
            self.velocity_y = -self.speed
        if keys[pygame.K_s]:
            self.velocity_y = self.speed
        if keys[pygame.K_d]:
            self.velocity_x = self.speed
        if keys[pygame.K_a]:
            self.velocity_x = -self.speed

        if self.velocity_x != 0 and self.velocity_y != 0:  # moving diagonally
            self.velocity_x /= math.sqrt(2)
            self.velocity_y /= math.sqrt(2)

        if pygame.mouse.get_pressed() == (1, 0, 0) or keys[pygame.K_SPACE]:
            self.shoot = True
            self.is_shooting()
        else:
            self.shoot = False

    def is_shooting(self):
        if self.shoot_cooldown == 0:
            self.shoot_cooldown = SHOOT_COOLDOWN
            spawn_bullet_pos = self.pos + self.gun_barrel_offset.rotate(self.angle)
            self.bullet = Bullet(spawn_bullet_pos[0], spawn_bullet_pos[1], self.angle)
            bullet_group.add(self.bullet)
            all_sprites_group.add(self.bullet)

            shoot_sound.play()

    def move(self):
        self.pos += pygame.math.Vector2(self.velocity_x, self.velocity_y)

        # Ensure the player stays within the screen boundaries
        self.pos.x = max(0, min(self.pos.x, WIDTH))
        self.pos.y = max(0, min(self.pos.y, HEIGHT))

        self.hitbox_rect.center = self.pos
        self.rect.center = self.hitbox_rect.center

    def draw_health_bar(self, surface):
        bar_width = 100
        bar_height = 15
        fill = (self.health / self.max_health) * bar_width
        outline_rect = pygame.Rect(self.rect.centerx - bar_width / 2, self.rect.top - 20, bar_width, bar_height)
        fill_rect = pygame.Rect(self.rect.centerx - bar_width / 2, self.rect.top - 20, fill, bar_height)
        pygame.draw.rect(surface, (152, 251, 152), fill_rect)
        pygame.draw.rect(surface, (255, 255, 255), outline_rect, 2)

    def update(self):
        self.user_input()
        self.move()
        self.player_rotation()

        if self.shoot_cooldown > 0:
            self.shoot_cooldown -= 1

        if self.health_cooldown > 0:
            self.health_cooldown -= 1

        if self.health <= 0:
            self.game_over()

    def game_over(self):
        pygame.mixer.music.stop()
        gta_sound.play()
        show_death_screen()

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, angle):
        super().__init__()
        self.image = pygame.image.load("assets/bullet.png").convert_alpha()
        self.image = pygame.transform.rotozoom(self.image, 0, BULLET_SCALE)
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)
        self.x = x
        self.y = y
        self.angle = angle
        self.speed = BULLET_SPEED
        self.x_vel = math.cos(self.angle * (2*math.pi/360)) * self.speed
        self.y_vel = math.sin(self.angle * (2*math.pi/360)) * self.speed
        self.bullet_lifetime = BULLET_LIFETIME
        self.spawn_time = pygame.time.get_ticks() # gets the spesific time that the bullet was created

    def bullet_movement(self):
        self.x += self.x_vel
        self.y += self.y_vel

        self.rect.x = int(self.x)
        self.rect.y = int(self.y)

        if pygame.time.get_ticks() - self.spawn_time > self.bullet_lifetime:
            self.kill()

    def update(self):
        self.bullet_movement()

class Enemy(pygame.sprite.Sprite):
    def __init__(self, position):
        super().__init__(enemy_group, all_sprites_group)
        self.image = pygame.image.load("assets/thug.png").convert_alpha()
        self.image = pygame.transform.rotozoom(self.image, 0, 0.30)

        self.rect = self.image.get_rect()
        self.rect.center = position

        self.hitbox_rect = self.rect.inflate(-self.rect.width * 0.3, -self.rect.height * 0.3)

        self.direction = pygame.math.Vector2()
        self.velocity = pygame.math.Vector2()
        self.speed = ENEMY_SPEED

        self.position = pygame.math.Vector2(position)
        self.change_direction_interval = 1000
        self.last_change_direction_time = pygame.time.get_ticks()

        self.max_health = ENEMY_HEALTH
        self.health = self.max_health

    def random_movement(self):
        current_time = pygame.time.get_ticks()
        if current_time - self.last_change_direction_time > self.change_direction_interval:
            self.direction = pygame.math.Vector2(random.uniform(-1, 1), random.uniform(-1, 1)).normalize()
            self.velocity = self.direction * self.speed
            self.last_change_direction_time = current_time

        self.position += self.velocity

        # Ensure the enemy stays within the screen boundaries
        self.position.x = max(0, min(self.position.x, WIDTH))
        self.position.y = max(0, min(self.position.y, HEIGHT))

        self.rect.centerx = self.position.x
        self.rect.centery = self.position.y

        self.hitbox_rect.center = self.rect.center

    def draw_health_bar(self, surface):
        bar_width = 100
        bar_height = 15
        fill = (self.health / self.max_health) * bar_width
        outline_rect = pygame.Rect(self.rect.centerx - bar_width / 2, self.rect.top - 10, bar_width, bar_height)
        fill_rect = pygame.Rect(self.rect.centerx - bar_width / 2, self.rect.top - 10, fill, bar_height)
        pygame.draw.rect(surface, (255, 0, 0), fill_rect)
        pygame.draw.rect(surface, (255, 255, 255), outline_rect, 2)  
    
    def update(self):
        self.random_movement()

        # check for collisions with bullets
        hit_bullets = pygame.sprite.spritecollide(self, bullet_group, True)
        if hit_bullets:
            self.health -= 20
            print(f"Enemy hit! Current health: {self.health}")
            if self.health <= 0:
                self.kill()
                dead_sound.play()
                print("Enemy Killed!")

def show_death_screen():
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    ending1()

        info = textbutton_font(24).render("(click Enter to continue...)", True, "White")
        info_rect = info.get_rect(x=500, y=600)

        screen.fill((0, 0, 0))  # Black background
        font = pygame.font.Font("assets/Font/getfont.ttf", 100)
        text = font.render("You Are DEAD!", True, (255, 0, 0))
        text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        screen.blit(text, text_rect)
        screen.blit(info,info_rect)
        pygame.display.flip()
        clock.tick(60)
 
all_sprites_group = pygame.sprite.Group()
bullet_group = pygame.sprite.Group()
enemy_group = pygame.sprite.Group()

player = Player()

# enemies at random position
def create_enemies(num_enemies):
    for _ in range(num_enemies):
        x = random.randint(0, WIDTH)
        y = random.randint(0, HEIGHT)
        thug = Enemy((x, y))
        all_sprites_group.add(thug)

# create how many enemies
create_enemies(8)

all_sprites_group.add(player)

def check_stage_cleared():
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                sys.exit()
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if CHOICE1.checkForInput(MENU_MOUSE_POS):
                    dialogue8()

        bg = pygame.image.load('assets/Background.png')
        scaled_bg = pygame.transform.scale(bg, (1280,720))
        bg_rect = scaled_bg.get_rect(x=0,y=0)

        font = pygame.font.Font("assets/Font/ARCADECLASSIC.TTF", 50)
        text = font.render("SUCCESSFULLY   ASSASSINATE", True, (255, 255, 255))
        text_rect = text.get_rect(center=(640, 380))

        c1 = pygame.image.load('assets/cbutton.png')
        scaled_c1 = pygame.transform.scale(c1, (300,70))
        c1_rect = scaled_c1.get_rect(x=480,y=600)

        scaled_bg.blit(text, text_rect)
        screen.blit(scaled_bg, bg_rect)
        screen.blit(scaled_c1, c1_rect)

        clock.tick(60)

        MENU_MOUSE_POS = pygame.mouse.get_pos()  #detecting mouse position
        
        CHOICE1 = Button(image=pygame.image.load("assets/transparent.png"), pos=(630, 637), 
                            text_input="CONTINUE STORY", font=textbutton_font(21), base_color="white", hovering_color="#FF3131")
        
        for button in [CHOICE1]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(screen)

        pygame.display.flip()

def countdown():
    font = pygame.font.Font("assets/Font/ARCADECLASSIC.TTF", 100)
    for i in range(3, 0, -1):
        screen.blit(background, (0, 0))
        text = font.render(str(i), True, (255, 255, 255))
        text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        screen.blit(text, text_rect)
        pygame.display.flip()
        pygame.time.wait(1000)

def ending1():
    gta_sound.stop()

    pygame.mixer.music.load("assets/Audio/Ending.wav")
    pygame.mixer.music.play(-1)  # -1 means the music will loop indefinitely
    pygame.mixer.music.set_volume(0.5)

    font = pygame.font.Font('assets/Font/Cinzel.ttf', 35)
    screen = pygame.display.set_mode([1280, 720])
    timer = pygame.time.Clock()
    messages = ('Luna lost in the battle',
                'Luna is not strong enough to face this challenge',
                'She was raped by all the criminals until she died',
                'Luna lost her lover',
                'Luna lost everything',
                'She will never meet Roman again',
                'Perhaps Roman won\'t know that she\'s already dead',
                'Will Roman look for her again after this?',
                'It\'s pointless because Luna is dead',
                'HMMM',
                '...',
                '...')
    snip = font.render('', True, 'white')
    counter = 0
    speed = 1
    active_message = 0
    message = messages[active_message]

    run = True
    while run:

        timer.tick(60)
        screen.fill('black')

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
                    if active_message == 11:
                        pygame.mixer.music.stop()
                        retry()
    
        snip = font.render(message[0:counter//speed], True, 'white')
        screen.blit(snip, (180, 360))

        pygame.display.flip()

def retry():
    while True:

        timer = pygame.time.Clock()

        current  = pygame.font.Font('assets/Font/Cinzel.ttf', 50).render("YOU DESERVE A BETTER ENDING", True, "White")
        current_rect = current.get_rect(x=220,y=330)

        c1 = pygame.image.load('assets/cbutton.png')
        scaled_c1 = pygame.transform.scale(c1, (300,70))
        c1_rect = scaled_c1.get_rect(x=490,y=500)

        c2 = pygame.image.load('assets/cbutton.png')
        scaled_c2 = pygame.transform.scale(c2, (300,70))
        c2_rect = scaled_c2.get_rect(x=490,y=615)

        SCREEN.blit(scaled_c1, c1_rect)
        SCREEN.blit(scaled_c2, c2_rect)
        SCREEN.blit(current, current_rect)

        timer.tick(60)

        MENU_MOUSE_POS = pygame.mouse.get_pos()  #detecting mouse position

        CHOICE1 = Button(image=pygame.image.load("assets/transparent.png"), pos=(644,540), 
                            text_input="RETRY", font=textbutton_font(30), base_color="black", hovering_color="#FF3131")
        
        CHOICE2 = Button(image=pygame.image.load("assets/transparent.png"), pos=(644,655), 
                            text_input="QUIT", font=textbutton_font(30), base_color="black", hovering_color="#FF3131")

        for button in [CHOICE1,CHOICE2]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)

        for event in pygame.event.get():

            if event.type == pygame.QUIT: #if pressing x button on window screen
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if CHOICE1.checkForInput(MENU_MOUSE_POS):
                    print('RETRY')
                    player.reset()
                    charge()
                if CHOICE2.checkForInput(MENU_MOUSE_POS):
                    print('QUIT')
                    pygame.quit()
                    sys.exit()

            pygame.display.flip()

def charge():
    
    pygame.mixer.music.load("assets/Audio/Intense.mp3")
    pygame.mixer.music.play(-1)  # -1 means the music will loop indefinitely
    pygame.mixer.music.set_volume(0.5)

    waiting_for_key = False

    countdown()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.blit(background, (0, 0))
        
        all_sprites_group.draw(screen)
        all_sprites_group.update()

        player.draw_health_bar(screen) # Player's health Bar

        # collisions between player & enemies
        if pygame.sprite.spritecollide(player, enemy_group, False):
            if player.health_cooldown <= 0:
                player.health -= 10
                print(f"Player hit! Cirrent health: {player.health}")
                player.health_cooldown = 1000
                collision_sound.play()

        for enemy in enemy_group:
            enemy.draw_health_bar(screen)

        player.health_cooldown -= clock.get_time()

        if len(enemy_group) == 0 and not waiting_for_key:
            check_stage_cleared()
            waiting_for_key = True

        pygame.display.update()
        clock.tick(FPS)

def dialogue1v1():
    pygame.mixer.music.stop()
    
    font = pygame.font.Font('assets/Font/ARCADE.TTF', 24)
    screen = pygame.display.set_mode ([1280, 720])
    timer = pygame.time.Clock()
    messages = ('Luna : Hi Handsome!',
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

        bg = pygame.image.load('assets/Chapter2/fightback.jpg')
        scaled_bg = pygame.transform.scale(bg, (1280,720))
        bg_rect = scaled_bg.get_rect(x=0,y=0)

        lover = pygame.image.load('assets/Chapter2/loverfight.png')
        scaled_lover = pygame.transform.scale(lover, (380,400))
        lover_rect = scaled_lover.get_rect(x=480,y=200)

        textbox = pygame.image.load('assets/textboxlover.png')
        scaled_texbox = pygame.transform.scale(textbox, (850,450))
        textbox_rect = scaled_texbox.get_rect(x=220,y=410)

        SCREEN.blit(scaled_bg, bg_rect)
        PAUSE.update(SCREEN)
        PAUSE.changeColor(MENU_MOUSE_POS)
        SCREEN.blit(scaled_lover, lover_rect)
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
                        dialogue2()
    
    
        snip = font.render(message[0:counter//speed], True, 'white')
        screen.blit(snip, (295, 600))

        pygame.display.flip()

def dialogue2():

    font = pygame.font.Font('assets/Font/ARCADE.TTF', 24)
    screen = pygame.display.set_mode ([1280, 720])
    timer = pygame.time.Clock()
    messages = ('Unknown Henchman : Huhhhh... Who are you?',
                '<Henchman startled by Luna existance>',
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

        bg = pygame.image.load('assets/Chapter2/fightback.jpg')
        scaled_bg = pygame.transform.scale(bg, (1280,720))
        bg_rect = scaled_bg.get_rect(x=0,y=0)

        lover = pygame.image.load('assets/Chapter2/konco2.png')
        scaled_lover = pygame.transform.scale(lover, (350,400))
        lover_rect = scaled_lover.get_rect(x=480,y=200)

        textbox = pygame.image.load('assets/textboxlover.png')
        scaled_texbox = pygame.transform.scale(textbox, (850,450))
        textbox_rect = scaled_texbox.get_rect(x=220,y=410)

        SCREEN.blit(scaled_bg, bg_rect)
        PAUSE.update(SCREEN)
        PAUSE.changeColor(MENU_MOUSE_POS)
        SCREEN.blit(scaled_lover, lover_rect)
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
                        dialogue3()
    
    
        snip = font.render(message[0:counter//speed], True, 'white')
        screen.blit(snip, (295, 600))

        pygame.display.flip()

def dialogue3():

    font = pygame.font.Font('assets/Font/ARCADE.TTF', 24)
    screen = pygame.display.set_mode ([1280, 720])
    timer = pygame.time.Clock()
    messages = ('<Without wasting anytime, Luna shoots the henchman>',
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

        bg = pygame.image.load('assets/Chapter2/fightback.jpg')
        scaled_bg = pygame.transform.scale(bg, (1280,720))
        bg_rect = scaled_bg.get_rect(x=0,y=0)

        lover = pygame.image.load('assets/Chapter2/loverfight.png')
        scaled_lover = pygame.transform.scale(lover, (380,400))
        lover_rect = scaled_lover.get_rect(x=260,y=200)

        konco = pygame.image.load('assets/Chapter2/konco2.png')
        scaled_konco = pygame.transform.scale(konco, (350,400))
        konco_rect = scaled_konco.get_rect(x=630,y=200)

        textbox = pygame.image.load('assets/textboxlover.png')
        scaled_texbox = pygame.transform.scale(textbox, (850,450))
        textbox_rect = scaled_texbox.get_rect(x=220,y=410)

        SCREEN.blit(scaled_bg, bg_rect)
        PAUSE.update(SCREEN)
        PAUSE.changeColor(MENU_MOUSE_POS)
        SCREEN.blit(scaled_lover, lover_rect)
        SCREEN.blit(scaled_konco, konco_rect)
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
                        dialogue4()
    
    
        snip = font.render(message[0:counter//speed], True, 'white')
        screen.blit(snip, (295, 600))

        pygame.display.flip()

def dialogue4():

    font = pygame.font.Font('assets/Font/ARCADE.TTF', 24)
    screen = pygame.display.set_mode ([1280, 720])
    timer = pygame.time.Clock()
    messages = ('<BOOM> <BOOM>',
                '...')
    
    shoot_sound.play(1)
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

        bg = pygame.image.load('assets/Chapter2/fightback.jpg')
        scaled_bg = pygame.transform.scale(bg, (1280,720))
        bg_rect = scaled_bg.get_rect(x=0,y=0)

        lover = pygame.image.load('assets/Chapter2/loverfight.png')
        scaled_lover = pygame.transform.scale(lover, (380,400))
        lover_rect = scaled_lover.get_rect(x=260,y=200)

        konco = pygame.image.load('assets/Chapter2/konco2dead.png')
        scaled_konco = pygame.transform.scale(konco, (350,400))
        konco_rect = scaled_konco.get_rect(x=630,y=200)

        textbox = pygame.image.load('assets/textboxlover.png')
        scaled_texbox = pygame.transform.scale(textbox, (850,450))
        textbox_rect = scaled_texbox.get_rect(x=220,y=410)

        SCREEN.blit(scaled_bg, bg_rect)
        PAUSE.update(SCREEN)
        PAUSE.changeColor(MENU_MOUSE_POS)
        SCREEN.blit(scaled_lover, lover_rect)
        SCREEN.blit(scaled_konco, konco_rect)
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
                        dialogue5()
    
    
        snip = font.render(message[0:counter//speed], True, 'white')
        screen.blit(snip, (295, 600))

        pygame.display.flip()

def dialogue5():

    font = pygame.font.Font('assets/Font/ARCADE.TTF', 24)
    screen = pygame.display.set_mode ([1280, 720])
    timer = pygame.time.Clock()
    messages = ('Unknown Henchman 2 : HEYYYY!!!',
                'Unknown Henchman 2 : Drop the gun right now!',
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

        bg = pygame.image.load('assets/Chapter2/fightback.jpg')
        scaled_bg = pygame.transform.scale(bg, (1280,720))
        bg_rect = scaled_bg.get_rect(x=0,y=0)

        lover = pygame.image.load('assets/Chapter2/konco1.png')
        scaled_lover = pygame.transform.scale(lover, (380,400))
        lover_rect = scaled_lover.get_rect(x=450,y=200)

        textbox = pygame.image.load('assets/textboxlover.png')
        scaled_texbox = pygame.transform.scale(textbox, (850,450))
        textbox_rect = scaled_texbox.get_rect(x=220,y=410)

        SCREEN.blit(scaled_bg, bg_rect)
        PAUSE.update(SCREEN)
        PAUSE.changeColor(MENU_MOUSE_POS)
        SCREEN.blit(scaled_lover, lover_rect)
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
                        dialogue6()
    
    
        snip = font.render(message[0:counter//speed], True, 'white')
        screen.blit(snip, (295, 600))

        pygame.display.flip()

def dialogue6():

    font = pygame.font.Font('assets/Font/ARCADE.TTF', 24)
    screen = pygame.display.set_mode ([1280, 720])
    timer = pygame.time.Clock()
    messages = ('Luna : Where is Emir and Roman?',
                'Luna : Hand them over, or I\'ll end every one of you.',
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

        bg = pygame.image.load('assets/Chapter2/fightback.jpg')
        scaled_bg = pygame.transform.scale(bg, (1280,720))
        bg_rect = scaled_bg.get_rect(x=0,y=0)

        lover = pygame.image.load('assets/Chapter2/loverfight.png')
        scaled_lover = pygame.transform.scale(lover, (380,400))
        lover_rect = scaled_lover.get_rect(x=480,y=200)

        textbox = pygame.image.load('assets/textboxlover.png')
        scaled_texbox = pygame.transform.scale(textbox, (850,450))
        textbox_rect = scaled_texbox.get_rect(x=220,y=410)

        SCREEN.blit(scaled_bg, bg_rect)
        PAUSE.update(SCREEN)
        PAUSE.changeColor(MENU_MOUSE_POS)
        SCREEN.blit(scaled_lover, lover_rect)
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
                        dialogue7()
    
    
        snip = font.render(message[0:counter//speed], True, 'white')
        screen.blit(snip, (295, 600))

        pygame.display.flip()

def dialogue7():

    pygame.mixer.music.load("assets/Audio/Intense.mp3")
    pygame.mixer.music.play(-1)  # -1 means the music will loop indefinitely
    pygame.mixer.music.set_volume(0.5)

    font = pygame.font.Font('assets/Font/ARCADE.TTF', 24)
    screen = pygame.display.set_mode ([1280, 720])
    timer = pygame.time.Clock()
    messages = ('Unknown Henchman 2 : I said drop your gun, Bitc*!',
                'Luna : Why should I listen to you? I\'m not your bitc*.',
                '<Luna made the henchman pissed off>',
                '<Then the henchman called his allies to capture Luna>',
                'Unknown Henchman 2 : You better not play with us.',
                '<They slowly surrounded Luna>',
                'Luna : Back off, or I\'ll take you all down.',
                '<The henchmen ignore Luna and move closer to capture her>',
                '<Luna had no choice but to fight against all the henchmen>',
                'Luna : You all asked for this.',
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

        bg = pygame.image.load('assets/Chapter2/fightback.jpg')
        scaled_bg = pygame.transform.scale(bg, (1280,720))
        bg_rect = scaled_bg.get_rect(x=0,y=0)

        lover = pygame.image.load('assets/Chapter2/loverfight.png')
        scaled_lover = pygame.transform.scale(lover, (380,400))
        lover_rect = scaled_lover.get_rect(x=280,y=200)

        konco = pygame.image.load('assets/Chapter2/konco1.png')
        scaled_konco = pygame.transform.scale(konco, (380,400))
        konco_rect = scaled_konco.get_rect(x=630,y=200)

        textbox = pygame.image.load('assets/textboxlover.png')
        scaled_texbox = pygame.transform.scale(textbox, (850,450))
        textbox_rect = scaled_texbox.get_rect(x=220,y=410)

        SCREEN.blit(scaled_bg, bg_rect)
        PAUSE.update(SCREEN)
        PAUSE.changeColor(MENU_MOUSE_POS)
        SCREEN.blit(scaled_lover, lover_rect)
        SCREEN.blit(scaled_konco, konco_rect)
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
                        choice1()
    
    
        snip = font.render(message[0:counter//speed], True, 'white')
        screen.blit(snip, (295, 600))

        pygame.display.flip()


def choice1():
    while True:

        timer = pygame.time.Clock()

        bg = pygame.image.load('assets/Chapter2/fightbackblur.png')
        scaled_bg = pygame.transform.scale(bg, (1280,720))
        bg_rect = scaled_bg.get_rect(x=0,y=0)

        lover = pygame.image.load('assets/Chapter2/loverfight.png')
        scaled_lover = pygame.transform.scale(lover, (350,450))
        lover_rect = scaled_lover.get_rect(x=515,y=180)

        c2 = pygame.image.load('assets/cbutton.png')
        scaled_c2 = pygame.transform.scale(c2, (300,70))
        c2_rect = scaled_c2.get_rect(x=515,y=600)

        SCREEN.blit(scaled_bg, bg_rect)
        SCREEN.blit(scaled_lover, lover_rect)
        SCREEN.blit(scaled_c2, c2_rect)
        
        timer.tick(60)

        MENU_MOUSE_POS = pygame.mouse.get_pos()  #detecting mouse position
        
        CHOICE1 = Button(image=pygame.image.load("assets/transparent.png"), pos=(665, 637), 
                            text_input="CHARGE AT THEM", font=textbutton_font(21), base_color="black", hovering_color="#FF3131")

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
                    charge()
                if PAUSE.checkForInput(MENU_MOUSE_POS):
                    pausemenu()

            pygame.display.flip()

def dialogue8():
    pygame.mixer.music.stop()

    font = pygame.font.Font('assets/Font/ARCADE.TTF', 24)
    screen = pygame.display.set_mode ([1280, 720])
    timer = pygame.time.Clock()
    messages = ('Luna : Hi Handsome!',
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

        bg = pygame.image.load('assets/Chapter2/fightback.jpg')
        scaled_bg = pygame.transform.scale(bg, (1280,720))
        bg_rect = scaled_bg.get_rect(x=0,y=0)

        lover = pygame.image.load('assets/Chapter2/loverfight.png')
        scaled_lover = pygame.transform.scale(lover, (380,400))
        lover_rect = scaled_lover.get_rect(x=480,y=200)

        textbox = pygame.image.load('assets/textboxlover.png')
        scaled_texbox = pygame.transform.scale(textbox, (850,450))
        textbox_rect = scaled_texbox.get_rect(x=220,y=410)

        SCREEN.blit(scaled_bg, bg_rect)
        PAUSE.update(SCREEN)
        PAUSE.changeColor(MENU_MOUSE_POS)
        SCREEN.blit(scaled_lover, lover_rect)
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
                        dialogue8()
    
    
        snip = font.render(message[0:counter//speed], True, 'white')
        screen.blit(snip, (295, 600))

        pygame.display.flip()

charge()