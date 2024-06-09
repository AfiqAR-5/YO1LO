import pygame
import sys
import math
import random
from config import *
from button import Button
from settingsshoot import *

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
            self.health -= 10
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
create_enemies(5)

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
                    dialogue1()

        bg = pygame.image.load('assets/Background.png')
        scaled_bg = pygame.transform.scale(bg, (1280,720))
        bg_rect = scaled_bg.get_rect(x=0,y=0)

        font = pygame.font.Font("assets/Font/ARCADECLASSIC.TTF", 50)
        text = font.render("Mission  Complete", True, (255, 255, 255))
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
                    shootgame()
                if CHOICE2.checkForInput(MENU_MOUSE_POS):
                    print('QUIT')
                    pygame.quit()
                    sys.exit()

            pygame.display.flip()

def shootgame():

    pygame.mixer.music.load("assets/Audio/xiaolao.wav")
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

def dialogue1():
    pygame.mixer.music.stop()

    font = pygame.font.Font('assets/Font/ARCADE.TTF', 24)
    screen = pygame.display.set_mode ([1280, 720])
    timer = pygame.time.Clock()
    messages = ('Luna : FUHHHH...',
                'Luna : I don\'t know how I survive that attack.',
                'Luna : Who are these people?',
                'Luna : What do they actually want from me?',
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
                    if active_message == 4:
                        dialogue2()
    
    
        snip = font.render(message[0:counter//speed], True, 'white')
        screen.blit(snip, (295, 600))

        pygame.display.flip()

def dialogue2():
    
    font = pygame.font.Font('assets/Font/ARCADE.TTF', 24)
    screen = pygame.display.set_mode ([1280, 720])
    timer = pygame.time.Clock()
    messages = ('Suddenly...',
                '<UGH> <UGH>...',
                'UHUK UHUK...',
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

        henchman1 = pygame.image.load('assets/Chapter2/henchman1.png')
        scaled_henchman1 = pygame.transform.scale(henchman1, (330,400))
        henchman1_rect = scaled_henchman1.get_rect(x=480,y=185)
        
        textbox = pygame.image.load('assets/textboxlover.png')
        scaled_texbox = pygame.transform.scale(textbox, (850,450))
        textbox_rect = scaled_texbox.get_rect(x=220,y=410)

        SCREEN.blit(scaled_bg, bg_rect)
        PAUSE.update(SCREEN)
        PAUSE.changeColor(MENU_MOUSE_POS)
        SCREEN.blit(scaled_henchman1, henchman1_rect)
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
                        dialogue3()
    
    
        snip = font.render(message[0:counter//speed], True, 'white')
        screen.blit(snip, (295, 600))

        pygame.display.flip()

def dialogue3():
    
    font = pygame.font.Font('assets/Font/ARCADE.TTF', 24)
    screen = pygame.display.set_mode ([1280, 720])
    timer = pygame.time.Clock()
    messages = ('Luna : Ehhh...',
                'Luna : You are still alive...',
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
                        dialogue4()
    
    
        snip = font.render(message[0:counter//speed], True, 'white')
        screen.blit(snip, (295, 600))

        pygame.display.flip()

def dialogue4():
    
    font = pygame.font.Font('assets/Font/ARCADE.TTF', 24)
    screen = pygame.display.set_mode ([1280, 720])
    timer = pygame.time.Clock()
    messages = ('Luna : Who are you?',
                'Luna : What do you want from me?',
                'Survived Henchman : Eerghhh (Unable to answer)',
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
        lover_rect = scaled_lover.get_rect(x=260,y=145)
        
        henchman1 = pygame.image.load('assets/Chapter2/henchman1.png')
        scaled_henchman1 = pygame.transform.scale(henchman1, (310,400))
        henchman1_rect = scaled_henchman1.get_rect(x=680,y=185)

        textbox = pygame.image.load('assets/textboxlover.png')
        scaled_texbox = pygame.transform.scale(textbox, (850,450))
        textbox_rect = scaled_texbox.get_rect(x=220,y=410)

        SCREEN.blit(scaled_bg, bg_rect)
        PAUSE.update(SCREEN)
        PAUSE.changeColor(MENU_MOUSE_POS)
        SCREEN.blit(scaled_lover, lover_rect)
        SCREEN.blit(scaled_henchman1, henchman1_rect)
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
                        dialogue5()
    
    
        snip = font.render(message[0:counter//speed], True, 'white')
        screen.blit(snip, (295, 600))

        pygame.display.flip()

def dialogue5():

    font = pygame.font.Font('assets/Font/ARCADE.TTF', 24)
    screen = pygame.display.set_mode ([1280, 720])
    timer = pygame.time.Clock()
    messages = ('Luna : Before I finish you, you better tell me who you are?',
                '(Still waiting for an answer)',
                'Luna : I guess I\'ll give you until 3.',
                'Luna : You better be faster.',
                'Luna : 3',
                'Luna : 2',
                '(Pull the trigger of the gun)',
                'Luna : 1',
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
                    if active_message == 8:
                        dialogue6()
    
    
        snip = font.render(message[0:counter//speed], True, 'white')
        screen.blit(snip, (295, 600))

        pygame.display.flip()

def dialogue6():

    font = pygame.font.Font('assets/Font/ARCADE.TTF', 24)
    screen = pygame.display.set_mode ([1280, 720])
    timer = pygame.time.Clock()
    messages = ('Survived Henchman : EMIR... EMIR...',
                'Luna : Emir?',
                'Luna : He sent you?',
                'Survived Hencman : Ye.. Yess.. <UHUK> Yesss.. <UHUK>',
                'Luna : What does he want from me?',
                'Survived Henchman : He told us to kill you.',
                'Survived Henchman : That\'s all I know. Nothing more.',
                'Luna : FUC*!',
                'Luna : Crazy Bastard!',
                'Luna : Why does he want to kill me?',
                'Survived Henchman : I\'ll tell you again, I don\'t know.',
                'Luna : Oh, so you want to play games with me.',
                '<Placing the gun to the henchman head>',
                'Luna : Now you tell me where the fuc* he is.',
                'Luna : Before this gun blows your fuc*ing head.',
                'Survived Henchman : <Stay silent>',
                'Luna : You really want to play with me.',
                '<Grab a knife from the floor>',
                '<Stab the henchman\'s right thigh>',
                'Survived Henchman : AAAAARGGGGHHHHHHHH (Screaming Loudly)',
                'Survied Henchman : FUC*... Please, you don\'t have to this.',
                'Luna : You chose to be like this.',
                'Luna : I repeat once more, where the fuc* he is?',
                'Luna : I will not repeat it again... or else...',
                'Survived Henchman : I TOLD YOU THAT\'S ALL I KNOW!',
                'Survived Henchman : DON\'T YOU FUC*ING UNDERSTAND!',
                '<He continued to scream and curse at Luna>',
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
        lover_rect = scaled_lover.get_rect(x=260,y=145)
        
        henchman1 = pygame.image.load('assets/Chapter2/henchman1.png')
        scaled_henchman1 = pygame.transform.scale(henchman1, (310,400))
        henchman1_rect = scaled_henchman1.get_rect(x=680,y=185)

        textbox = pygame.image.load('assets/textboxlover.png')
        scaled_texbox = pygame.transform.scale(textbox, (850,450))
        textbox_rect = scaled_texbox.get_rect(x=220,y=410)

        SCREEN.blit(scaled_bg, bg_rect)
        PAUSE.update(SCREEN)
        PAUSE.changeColor(MENU_MOUSE_POS)
        SCREEN.blit(scaled_lover, lover_rect)
        SCREEN.blit(scaled_henchman1, henchman1_rect)
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
                    if active_message == 27:
                        dialogue7()
    
    
        snip = font.render(message[0:counter//speed], True, 'white')
        screen.blit(snip, (295, 600))

        pygame.display.flip()

def dialogue7():

    font = pygame.font.Font('assets/Font/ARCADE.TTF', 24)
    screen = pygame.display.set_mode ([1280, 720])
    timer = pygame.time.Clock()
    messages = ('Luna : You are really testing my patience.',
                '<Luna walked back and forth around the living room>',
                '<The henchman kept quiet as he endured the pain>',
                '<Luna looked for ideas on what to do-',
                '-to get the henchman to spill up>',
                'Luna : I\'m giving you one last chance-',
                'Luna : to answer my earlier question.',
                'Luna : Or I will use other forms of violence,-',
                'Luna : until you must live in this world with pain-',
                'Luna : and when you die-',
                'Luna : I\'ll be waiting for you-',
                'Luna : in front of the HELL to torture you again!',
                'Survived Henchman : <Stay Silent>',
                'Luna : Damn it!',
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
                    if active_message == 14:
                        choice1()
    
    
        snip = font.render(message[0:counter//speed], True, 'white')
        screen.blit(snip, (295, 600))

        pygame.display.flip()

def dialogue8():

    font = pygame.font.Font('assets/Font/ARCADE.TTF', 24)
    screen = pygame.display.set_mode ([1280, 720])
    timer = pygame.time.Clock()
    messages = ('<Luna took the knife on the floor>',
                '<Then she cut off one finger of the henchman, one by one>',
                'Survived Henchman : ARGHHHHHHHHHH (Scream In Pain)',
                'Survived Henchman : WHAT THE FUC**!',
                'Survived Henchman : My fuc*ing fingers!',
                'Survived Henchman : HAVE YOU LOST YOUR DAMN MIND?',
                'Survived Henchman : FUC*ING PSYCHOPATH!',
                'Survived Henchman : I\'m gonna kill you, FUC*ING BIT*H!',
                'Luna : HA HA HA HA HA... (Psychotic Laughter)',
                'Luna : You\'re going to kill me with what, your fuc*ing nose?',
                'Luna : You lost your damn fingers, as*hole.',
                'Luna : You can\'t even hold a thing.',
                'Survived Henchman : Grrr Grrr (Make A Dissatisfied Face)',
                'Luna : Now, you tell me, where is Emir?',
                'Survived Henchman : HUE HUE HUE BWAHAHA (Crazy Laugh)',
                'Survived Henchman : You\'re really hard to understand, aren\'t you?',
                'Survived Henchman : I DON\'T KNOW WHERE THE FUC* HE IS!',
                'Luna : You\'re still being stubborn, huh?',
                '<Luna proceeded with another method to make the henchman talk>',
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
        lover_rect = scaled_lover.get_rect(x=260,y=145)
        
        henchman1 = pygame.image.load('assets/Chapter2/henchman1.png')
        scaled_henchman1 = pygame.transform.scale(henchman1, (310,400))
        henchman1_rect = scaled_henchman1.get_rect(x=680,y=185)

        textbox = pygame.image.load('assets/textboxlover.png')
        scaled_texbox = pygame.transform.scale(textbox, (850,450))
        textbox_rect = scaled_texbox.get_rect(x=220,y=410)

        SCREEN.blit(scaled_bg, bg_rect)
        PAUSE.update(SCREEN)
        PAUSE.changeColor(MENU_MOUSE_POS)
        SCREEN.blit(scaled_lover, lover_rect)
        SCREEN.blit(scaled_henchman1, henchman1_rect)
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
                    if active_message == 19:
                        choice2()
    
    
        snip = font.render(message[0:counter//speed], True, 'white')
        screen.blit(snip, (295, 600))

        pygame.display.flip()

def dialogue9():

    font = pygame.font.Font('assets/Font/ARCADE.TTF', 24)
    screen = pygame.display.set_mode ([1280, 720])
    timer = pygame.time.Clock()
    messages = ('<Luna took a lighter from the kitchen>',
                '<She heated the knife with the lighter>',
                '<Then she returned to face the henchman>',
                'Luna : Do you see this knife?',
                'Luna : You better tell me where Emir is.',
                'Luna : Or else this knife going to be the last thing-',
                'Luna : -you see in this world.',
                'Survived Henchman : Over my DEAD BODY!',
                '<Luna then stabbed the knife into-',
                'the right eyeball of the henchman>',
                '<Then she twisted until the right eyeball-',
                'of the henchman popped out>',
                'Survived Henchman : AAARGHHHHHHH (Scream In Pain)',
                '<A lot of blood immediately flowed-',
                'from the right eye of the henchman>',
                '<Luna took the eyeball and stepped on it>',
                '<Luna wants to continue digging out his left eye>',
                'Suddenly...',
                'Survived Henchman : Ple... Pleaseee... Pleaseee Stop.',
                'Survived Henchman : I will tell you where Emir is.',
                'Luna : It would\'ve been easier if you had just told me sooner.',
                'Luna : No need to keep lying all the time.',
                'Luna : Where TF is Emir?',
                '<In his dying breath, the henchman discloses where Emir is>',
                'Survived Henchman : He\'s at a warehouse in Kiara Hills-',
                'Survived Henchman : -not too far from here.',
                'Survived Henchman : Be cautious, his henchmen are-',
                'Survived Henchman : -still plentiful there.',
                'Survived Henchman : I swear to God this time.',
                'Survived Henchman : Now, please leave me alone.',
                'Luna : Wow, look at you, giving me advice.',
                'Luna : If you weren\'t stupid from the start,-',
                '-you\'re not disabled like this.',
                'Luna : Your life is no longer worth it.',
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
        lover_rect = scaled_lover.get_rect(x=260,y=145)
        
        henchman1 = pygame.image.load('assets/Chapter2/henchman1.png')
        scaled_henchman1 = pygame.transform.scale(henchman1, (310,400))
        henchman1_rect = scaled_henchman1.get_rect(x=680,y=185)

        textbox = pygame.image.load('assets/textboxlover.png')
        scaled_texbox = pygame.transform.scale(textbox, (850,450))
        textbox_rect = scaled_texbox.get_rect(x=220,y=410)

        SCREEN.blit(scaled_bg, bg_rect)
        PAUSE.update(SCREEN)
        PAUSE.changeColor(MENU_MOUSE_POS)
        SCREEN.blit(scaled_lover, lover_rect)
        SCREEN.blit(scaled_henchman1, henchman1_rect)
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
                    if active_message == 34:
                        dialogue11()
    
    
        snip = font.render(message[0:counter//speed], True, 'white')
        screen.blit(snip, (295, 600))

        pygame.display.flip()

def dialogue11():
    
    font = pygame.font.Font('assets/Font/ARCADE.TTF', 24)
    screen = pygame.display.set_mode ([1280, 720])
    timer = pygame.time.Clock()
    messages = ('<Luna takes the gun from her waist-', 
                '-and shoots the henchman in the head>',
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

        bg = pygame.image.load('assets/Chapter2/houselover.png')
        scaled_bg = pygame.transform.scale(bg, (1280,720))
        bg_rect = scaled_bg.get_rect(x=0,y=0)

        lover = pygame.image.load('assets/Chapter2/lover3.png')
        scaled_lover = pygame.transform.scale(lover, (400,450))
        lover_rect = scaled_lover.get_rect(x=260,y=145)
        
        henchman1 = pygame.image.load('assets/Chapter2/henchman1dead.png')
        scaled_henchman1 = pygame.transform.scale(henchman1, (310,400))
        henchman1_rect = scaled_henchman1.get_rect(x=680,y=185)

        textbox = pygame.image.load('assets/textboxlover.png')
        scaled_texbox = pygame.transform.scale(textbox, (850,450))
        textbox_rect = scaled_texbox.get_rect(x=220,y=410)

        SCREEN.blit(scaled_bg, bg_rect)
        PAUSE.update(SCREEN)
        PAUSE.changeColor(MENU_MOUSE_POS)
        SCREEN.blit(scaled_lover, lover_rect)
        SCREEN.blit(scaled_henchman1, henchman1_rect)
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
                        dialogue12()
    
    
        snip = font.render(message[0:counter//speed], True, 'white')
        screen.blit(snip, (295, 600))

        pygame.display.flip()

def dialogue10():

    font = pygame.font.Font('assets/Font/ARCADE.TTF', 24)
    screen = pygame.display.set_mode ([1280, 720])
    timer = pygame.time.Clock()
    messages = ('<Luna took a machete from her store>',
                '<She lit the machete with fire>',
                '<Then she placed the machete on the face of the henchman>',
                'Survived Henchman : AAARGGGHHHHHH (Scream In Pain)',
                'Survived Henchman : It\'s hot as hell, you b1t*h!',
                'Luna : Tell me where Emir is.',
                'Luna : Before another disaster hits you.',
                'Survived Henchman : Guess what, he is in your as*hole (chuckles)',
                '<Then Luna used the machete in her hand-',
                'to cut off the right hand of the henchman>',
                'Survived Henchman : FFFFUUUCCC****....',
                'Survived Henchman : I DON\'T KNOW WHERE THE FUC* HE IS!',
                'Survived Henchman : I SWEARRR!',
                '<After that, she cut off the left hand of the henchman>',
                'Survived Henchman : ARRRGGHHHHHH (Scream In Pain)',
                'Survived Henchman : Fuc*ing Hell!',
                'Luna : You still want to be stubborn?',
                '<The henchman is half-dead>',
                '<Luna kicks his legs to see if he\'s still alive or not>',
                'Survived Henchman : I.... I do nnn... I do not know where he is.',
                'Luna : You do like to play, don\'t you?' ,   
                '<Luna proceeded with another method to make the henchman talk>',          
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
        lover_rect = scaled_lover.get_rect(x=260,y=145)
        
        henchman1 = pygame.image.load('assets/Chapter2/henchman1.png')
        scaled_henchman1 = pygame.transform.scale(henchman1, (310,400))
        henchman1_rect = scaled_henchman1.get_rect(x=680,y=185)

        textbox = pygame.image.load('assets/textboxlover.png')
        scaled_texbox = pygame.transform.scale(textbox, (850,450))
        textbox_rect = scaled_texbox.get_rect(x=220,y=410)

        SCREEN.blit(scaled_bg, bg_rect)
        PAUSE.update(SCREEN)
        PAUSE.changeColor(MENU_MOUSE_POS)
        SCREEN.blit(scaled_lover, lover_rect)
        SCREEN.blit(scaled_henchman1, henchman1_rect)
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
                    if active_message == 22:
                        choice3()
    
    
        snip = font.render(message[0:counter//speed], True, 'white')
        screen.blit(snip, (295, 600))

        pygame.display.flip()

def dialogue12():

    font = pygame.font.Font('assets/Font/ARCADE.TTF', 24)
    screen = pygame.display.set_mode ([1280, 720])
    timer = pygame.time.Clock()
    messages = ('Luna : What a mess!',
                'Luna : This house is totally trashed.',
                'Luna : Blood everywhere!',
                'Luna : Bloody Hell!',
                'Luna : I have to move these bodies into the storeroom.',
                'Luna : Emir, you\'d better wait for me.',
                '<Then Luna cleaned herself which was covered in blood>',
                '<She changes his clothes and prepares his gear-',
                'before heading to Kiara Hills>',
                '<She rests enough-',
                'and gets prepared to leave early in the morning>',
                '<In Luna\'s heart>',
                '<She is truly impatient to seek revenge against Emir>',
                '...',
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
                    if active_message == 14:
                        choice4()
    
    
        snip = font.render(message[0:counter//speed], True, 'white')
        screen.blit(snip, (295, 600))

        pygame.display.flip()

def choice1():

    while True:

        timer = pygame.time.Clock()

        current  = textbutton_font(24).render("CHOOSE THE METHOD TO MAKE HIM SPILL THE BEANS", True, "White")
        current_rect = current.get_rect(x=340,y=625)

        bg = pygame.image.load('assets/Chapter2/houseloverblur.png')
        scaled_bg = pygame.transform.scale(bg, (1280,720))
        bg_rect = scaled_bg.get_rect(x=0,y=0)

        lover = pygame.image.load('assets/Chapter2/lover3blur.png')
        lover_rect = lover.get_rect(x=425,y=100)

        textbox = pygame.image.load('assets/textboxlover.png')
        scaled_texbox = pygame.transform.scale(textbox, (850,450))
        textbox_rect = scaled_texbox.get_rect(x=200,y=410)

        c1 = pygame.image.load('assets/cbutton.png')
        scaled_c1 = pygame.transform.scale(c1, (500,70))
        c1_rect = scaled_c1.get_rect(x=400,y=150)

        c2 = pygame.image.load('assets/cbutton.png')
        scaled_c2 = pygame.transform.scale(c2, (500,70))
        c2_rect = scaled_c2.get_rect(x=400,y=300)

        c3 = pygame.image.load('assets/cbutton.png')
        scaled_c3 = pygame.transform.scale(c3, (500,70))
        c3_rect = scaled_c3.get_rect(x=400,y=450)

        SCREEN.blit(scaled_bg, bg_rect)
        SCREEN.blit(lover, lover_rect)
        SCREEN.blit(scaled_c1, c1_rect)
        SCREEN.blit(scaled_c2, c2_rect)
        SCREEN.blit(scaled_c3, c3_rect)
        SCREEN.blit(scaled_texbox, textbox_rect)
        SCREEN.blit(current, current_rect)

        timer.tick(60)

        MENU_MOUSE_POS = pygame.mouse.get_pos()  #detecting mouse position

        CHOICE1 = Button(image=pygame.image.load("assets/transparent.png"), pos=(650,190), 
                            text_input="CUT HIS FINGER", font=textbutton_font(30), base_color="black", hovering_color="#FF3131")

        CHOICE2 = Button(image=pygame.image.load("assets/transparent.png"), pos=(650, 340), 
                            text_input="REMOVE HIS EYEBALLS", font=textbutton_font(30), base_color="black", hovering_color="#FF3131")
        
        CHOICE3 = Button(image=pygame.image.load("assets/transparent.png"), pos=(650, 490), 
                            text_input="CUT RIGHT AND LEFT HAND", font=textbutton_font(30), base_color="black", hovering_color="#FF3131")

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
                    print('CUT HIS FINGER CHOOSED')
                    dialogue8()
                
                if CHOICE2.checkForInput(MENU_MOUSE_POS):
                    print('REMOVE HIS EYEBALLS CHOOSED')
                    dialogue9()

                if CHOICE3.checkForInput(MENU_MOUSE_POS):
                    print('CUT RIGHT AND LEFT HAND CHOOSED')
                    dialogue10()

                if PAUSE.checkForInput(MENU_MOUSE_POS):
                    pausemenu()

            pygame.display.flip()

def choice2():

    while True:

        timer = pygame.time.Clock()

        current  = textbutton_font(24).render("CHOOSE THE METHOD TO MAKE HIM SPILL THE BEANS", True, "White")
        current_rect = current.get_rect(x=340,y=625)

        bg = pygame.image.load('assets/Chapter2/houseloverblur.png')
        scaled_bg = pygame.transform.scale(bg, (1280,720))
        bg_rect = scaled_bg.get_rect(x=0,y=0)

        lover = pygame.image.load('assets/Chapter2/lover3blur.png')
        lover_rect = lover.get_rect(x=425,y=100)

        textbox = pygame.image.load('assets/textboxlover.png')
        scaled_texbox = pygame.transform.scale(textbox, (850,450))
        textbox_rect = scaled_texbox.get_rect(x=200,y=410)

        c2 = pygame.image.load('assets/cbutton.png')
        scaled_c2 = pygame.transform.scale(c2, (500,70))
        c2_rect = scaled_c2.get_rect(x=400,y=300)

        c3 = pygame.image.load('assets/cbutton.png')
        scaled_c3 = pygame.transform.scale(c3, (500,70))
        c3_rect = scaled_c3.get_rect(x=400,y=450)

        SCREEN.blit(scaled_bg, bg_rect)
        SCREEN.blit(lover, lover_rect)
        SCREEN.blit(scaled_c2, c2_rect)
        SCREEN.blit(scaled_c3, c3_rect)
        SCREEN.blit(scaled_texbox, textbox_rect)
        SCREEN.blit(current, current_rect)

        timer.tick(60)

        MENU_MOUSE_POS = pygame.mouse.get_pos()  #detecting mouse position

        CHOICE2 = Button(image=pygame.image.load("assets/transparent.png"), pos=(650, 340), 
                            text_input="REMOVE HIS EYEBALLS", font=textbutton_font(30), base_color="black", hovering_color="#FF3131")
        
        CHOICE3 = Button(image=pygame.image.load("assets/transparent.png"), pos=(650, 490), 
                            text_input="CUT RIGHT AND LEFT HAND", font=textbutton_font(30), base_color="black", hovering_color="#FF3131")

        PAUSE = Button(image=pygame.image.load("assets/pause.png"), pos=(50, 50), 
                            text_input="           ", font=textbutton_font(21), base_color="black", hovering_color="#FF3131")

        for button in [PAUSE,CHOICE2,CHOICE3]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)

        for event in pygame.event.get():

            if event.type == pygame.QUIT: #if pressing x button on window screen
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:                
                if CHOICE2.checkForInput(MENU_MOUSE_POS):
                    print('REMOVE HIS EYEBALLS CHOOSED')
                    dialogue9()

                if CHOICE3.checkForInput(MENU_MOUSE_POS):
                    print('CUT RIGHT AND LEFT HAND CHOOSED')
                    dialogue10()

                if PAUSE.checkForInput(MENU_MOUSE_POS):
                    pausemenu()

            pygame.display.flip()

def choice3():

    while True:

        timer = pygame.time.Clock()

        current  = textbutton_font(24).render("CHOOSE THE METHOD TO MAKE HIM SPILL THE BEANS", True, "White")
        current_rect = current.get_rect(x=340,y=625)

        bg = pygame.image.load('assets/Chapter2/houseloverblur.png')
        scaled_bg = pygame.transform.scale(bg, (1280,720))
        bg_rect = scaled_bg.get_rect(x=0,y=0)

        lover = pygame.image.load('assets/Chapter2/lover3blur.png')
        lover_rect = lover.get_rect(x=425,y=100)

        textbox = pygame.image.load('assets/textboxlover.png')
        scaled_texbox = pygame.transform.scale(textbox, (850,450))
        textbox_rect = scaled_texbox.get_rect(x=200,y=410)

        c2 = pygame.image.load('assets/cbutton.png')
        scaled_c2 = pygame.transform.scale(c2, (500,70))
        c2_rect = scaled_c2.get_rect(x=400,y=300)

        SCREEN.blit(scaled_bg, bg_rect)
        SCREEN.blit(lover, lover_rect)
        SCREEN.blit(scaled_c2, c2_rect)
        SCREEN.blit(scaled_texbox, textbox_rect)
        SCREEN.blit(current, current_rect)

        timer.tick(60)

        MENU_MOUSE_POS = pygame.mouse.get_pos()  #detecting mouse position

        CHOICE2 = Button(image=pygame.image.load("assets/transparent.png"), pos=(650, 340), 
                            text_input="REMOVE HIS EYEBALLS", font=textbutton_font(30), base_color="black", hovering_color="#FF3131")

        PAUSE = Button(image=pygame.image.load("assets/pause.png"), pos=(50, 50), 
                            text_input="           ", font=textbutton_font(21), base_color="black", hovering_color="#FF3131")

        for button in [PAUSE,CHOICE2]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)

        for event in pygame.event.get():

            if event.type == pygame.QUIT: #if pressing x button on window screen
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:                
                if CHOICE2.checkForInput(MENU_MOUSE_POS):
                    print('REMOVE HIS EYEBALLS CHOOSED')
                    dialogue9()

                if PAUSE.checkForInput(MENU_MOUSE_POS):
                    pausemenu()

            pygame.display.flip()

def choice4():
    while True:

        timer = pygame.time.Clock()

        bg = pygame.image.load('assets/Chapter2/jungleblur.png')
        scaled_bg = pygame.transform.scale(bg, (1280,720))
        bg_rect = scaled_bg.get_rect(x=0,y=0)

        lover = pygame.image.load('assets/Chapter2/lover3.png')
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
                            text_input="GO TO KIARA HILLS", font=textbutton_font(21), base_color="black", hovering_color="#FF3131")

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

        bg = pygame.image.load('assets/Chapter2/jungleblur.png')
        scaled_bg = pygame.transform.scale(bg, (1280,720))
        bg_rect = scaled_bg.get_rect(x=0,y=0)
        SCREEN.blit(scaled_bg, bg_rect)

        box = pygame.image.load('assets/Play Rect.png')
        scaled_box = pygame.transform.scale(box, (640,240))
        box_rect = scaled_box.get_rect(x=320,y=250)
        SCREEN.blit(scaled_box, box_rect)

        title = prologuefont(40).render("Chapter II ACT II", True, "White")
        title_rect = title.get_rect(x=340, y=265)
        SCREEN.blit(title, title_rect)

        head = prologuefont(22).render("Revenge Tour", True, "White")
        head_rect = head.get_rect(x=343, y=320)
        SCREEN.blit(head,head_rect)

        info = textbutton_font(19).render("Kiara Hills - Unknown Warehouse - 11:33:33 AM", True, "White")
        info_rect = title.get_rect(x=343, y=450)
        SCREEN.blit(info,info_rect)
        pygame.draw.rect(SCREEN, 'white', (343, 360, 590, 75))

        text1 = prologuefont(13).render("After being ambushed by Emir's accomplices, She now knows where Emir is located.", True, "black")
        text1_rect = text1.get_rect(x=350, y=370)
        SCREEN.blit(text1,text1_rect)

        text2 = prologuefont(13).render("Let's not forget Luna's plan to convince her lover, Roman, that Emir is the killer.", True, "black")
        text2_rect = text2.get_rect(x=350, y=390)
        SCREEN.blit(text2,text2_rect)

        text2 = prologuefont(13).render("Will this revenge tour bring about a happy ending for Luna? .....", True, "black")
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
                    dialogue13()

        pygame.display.flip()

def dialogue13():

    font = pygame.font.Font('assets/Font/ARCADE.TTF', 24)
    screen = pygame.display.set_mode ([1280, 720])
    timer = pygame.time.Clock()
    messages = ('Luna : What a mess!',
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
                    if active_message == 14:
                        choice4()
    
    
        snip = font.render(message[0:counter//speed], True, 'white')
        screen.blit(snip, (295, 600))

        pygame.display.flip()

if __name__ == "__main__":
    choice1()