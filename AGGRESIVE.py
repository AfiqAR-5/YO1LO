import pygame, sys
import math
import random
from settingshot1 import *
from button import Button
from config import *
from main import main_menu

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
trigger_sound = pygame.mixer.Sound("assets/Audio/Guntrigger.mp3")
slap_sound = pygame.mixer.Sound("assets/Audio/slap.mp3")
crying_sound = pygame.mixer.Sound("assets/Audio/crying.mp3")
evil_laugh = pygame.mixer.Sound("assets/Audio/evillaugh.mp3") 

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
        font = pygame.font.Font("assets/Font/Cinzel.ttf", 100)
        text = font.render("You Are DEAD", True, (255, 0, 0))
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

        font = pygame.font.Font("assets/Font/Cinzel.TTF", 50)
        text = font.render("SUCCESSFULLY ASSASSINATE", True, (255, 255, 255))
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

    font = pygame.font.Font('assets/Font/Cinzel.ttf', 28)
    screen = pygame.display.set_mode([1280, 720])
    timer = pygame.time.Clock()
    messages = ('Luna felt powerless to face them',
                'Luna was stabbed multiple times in her abdomen until she died',
                'After the henchmen captured Luna',
                'They told Emir that Luna was dead',
                'Roman had no idea about Luna\'s death',
                'Emir and his henchmen kept Luna\'s death a secret from Roman',
                'Afterward, Emir and his henchmen moved Luna\'s body far from the place',
                'They butchered Luna\'s body',
                'They then cooked the Luna\'s meat, making it their meal for the night',
                'That night, everyone ate the dish, including Roman',
                'They all enjoyed the dish',
                'Such a pity, Roman doesn\'t know he\'s enjoying the flesh of his lover',
                'HMMM...',
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
                    if active_message == 13:
                        pygame.mixer.music.stop()
                        retry()
    
        snip = font.render(message[0:counter//speed], True, 'white')
        screen.blit(snip, (100, 360))

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
    pygame.mixer.music.load("assets/Audio/shootscene.mp3")
    pygame.mixer.music.play(-1)  # -1 means the music will loop indefinitely
    pygame.mixer.music.set_volume(0.075)

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

    pygame.mixer.music.load("assets/Audio/Intense.mp3")
    pygame.mixer.music.play(-1)  # -1 means the music will loop indefinitely
    pygame.mixer.music.set_volume(0.25)
    
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
        lover_rect = lover.get_rect(x=450,y=50)

        textbox = pygame.image.load('assets/textboxlover.png')
        scaled_texbox = pygame.transform.scale(textbox, (850,450))
        textbox_rect = scaled_texbox.get_rect(x=220,y=410)

        SCREEN.blit(scaled_bg, bg_rect)
        PAUSE.update(SCREEN)
        PAUSE.changeColor(MENU_MOUSE_POS)
        SCREEN.blit(lover, lover_rect)
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
        lover_rect = lover.get_rect(x=450,y=70)

        textbox = pygame.image.load('assets/textboxlover.png')
        scaled_texbox = pygame.transform.scale(textbox, (850,450))
        textbox_rect = scaled_texbox.get_rect(x=220,y=410)

        SCREEN.blit(scaled_bg, bg_rect)
        PAUSE.update(SCREEN)
        PAUSE.changeColor(MENU_MOUSE_POS)
        SCREEN.blit(lover, lover_rect)
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
        lover_rect = lover.get_rect(x=450,y=50)

        textbox = pygame.image.load('assets/textboxlover.png')
        scaled_texbox = pygame.transform.scale(textbox, (850,450))
        textbox_rect = scaled_texbox.get_rect(x=220,y=410)

        SCREEN.blit(scaled_bg, bg_rect)
        PAUSE.update(SCREEN)
        PAUSE.changeColor(MENU_MOUSE_POS)
        SCREEN.blit(lover, lover_rect)
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
        lover_rect = lover.get_rect(x=470,y=80)

        c2 = pygame.image.load('assets/cbutton.png')
        scaled_c2 = pygame.transform.scale(c2, (300,70))
        c2_rect = scaled_c2.get_rect(x=515,y=600)

        SCREEN.blit(scaled_bg, bg_rect)
        SCREEN.blit(lover, lover_rect)
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

    pygame.mixer.music.load("assets/Chapter2/Chap2Act2.mp3")
    pygame.mixer.music.play(-1)  # -1 means the music will loop indefinitely
    pygame.mixer.music.set_volume(0.1)

    font = pygame.font.Font('assets/Font/ARCADE.TTF', 24)
    screen = pygame.display.set_mode ([1280, 720])
    timer = pygame.time.Clock()
    messages = ('Luna : Die you, Bastard!',
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
        lover_rect = lover.get_rect(x=450,y=50)

        textbox = pygame.image.load('assets/textboxlover.png')
        scaled_texbox = pygame.transform.scale(textbox, (850,450))
        textbox_rect = scaled_texbox.get_rect(x=220,y=410)

        SCREEN.blit(scaled_bg, bg_rect)
        PAUSE.update(SCREEN)
        PAUSE.changeColor(MENU_MOUSE_POS)
        SCREEN.blit(lover, lover_rect)
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
                        dialogue9()
    
    
        snip = font.render(message[0:counter//speed], True, 'white')
        screen.blit(snip, (295, 600))

        pygame.display.flip()

def dialogue9():

    font = pygame.font.Font('assets/Font/ARCADE.TTF', 24)
    screen = pygame.display.set_mode ([1280, 720])
    timer = pygame.time.Clock()
    messages = ('<Suddenly, someone pointed a gun at the back of Luna\'s head>',
                '...')
    
    trigger_sound.play()
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
        lover_rect = lover.get_rect(x=450,y=50)

        textbox = pygame.image.load('assets/textboxlover.png')
        scaled_texbox = pygame.transform.scale(textbox, (850,450))
        textbox_rect = scaled_texbox.get_rect(x=220,y=410)

        SCREEN.blit(scaled_bg, bg_rect)
        PAUSE.update(SCREEN)
        PAUSE.changeColor(MENU_MOUSE_POS)
        SCREEN.blit(lover, lover_rect)
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
                        dialogue10()
    
    
        snip = font.render(message[0:counter//speed], True, 'white')
        screen.blit(snip, (295, 600))

        pygame.display.flip()

def dialogue10():

    font = pygame.font.Font('assets/Font/ARCADE.TTF', 24)
    screen = pygame.display.set_mode ([1280, 720])
    timer = pygame.time.Clock()
    messages = ('Roman : Drop your gun, Luna!',
                '<It was Roman himself who pointed the gun>',
                'Luna : What are you doing Roman?',
                'Roman : I said drop your gun, honey.',
                '<Luna had to agree with Roman\'s orders>',
                'Luna : You don\'t have to do this Roman.',
                'Luna : Think wisely Roman.',
                'Roman : I\'m sorry my love, I had to this.',
                'Roman : Follow me!',
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

        mc = pygame.image.load('assets/Chapter2/mcshot22.png')
        mc_rect = mc.get_rect(x=620,y=10)

        textbox = pygame.image.load('assets/textboxlover.png')
        scaled_texbox = pygame.transform.scale(textbox, (850,450))
        textbox_rect = scaled_texbox.get_rect(x=220,y=410)

        SCREEN.blit(scaled_bg, bg_rect)
        PAUSE.update(SCREEN)
        PAUSE.changeColor(MENU_MOUSE_POS)
        SCREEN.blit(mc, mc_rect)
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
                    if active_message == 9:
                        dialogue11()
    
    
        snip = font.render(message[0:counter//speed], True, 'white')
        screen.blit(snip, (295, 600))

        pygame.display.flip()

def dialogue11():

    font = pygame.font.Font('assets/Font/ARCADE.TTF', 24)
    screen = pygame.display.set_mode ([1280, 720])
    timer = pygame.time.Clock()
    messages = ('<Roman brought Luna into the warehouse>',
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

        bg = pygame.image.load('assets/Chapter2/abanwarehouse.png')
        scaled_bg = pygame.transform.scale(bg, (1280,720))
        bg_rect = scaled_bg.get_rect(x=0,y=0)

        lover = pygame.image.load('assets/Chapter2/lovercalm.png')
        scaled_lover = pygame.transform.scale(lover, (330,400))
        lover_rect = scaled_lover.get_rect(x=280,y=200)

        mc = pygame.image.load('assets/Chapter2/mcnormal.png')
        mc_rect = mc.get_rect(x=650,y=20)

        textbox = pygame.image.load('assets/textboxlover.png')
        scaled_texbox = pygame.transform.scale(textbox, (850,450))
        textbox_rect = scaled_texbox.get_rect(x=220,y=410)

        SCREEN.blit(scaled_bg, bg_rect)
        PAUSE.update(SCREEN)
        PAUSE.changeColor(MENU_MOUSE_POS)
        SCREEN.blit(mc, mc_rect)
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
                        dialogue12()
    
    
        snip = font.render(message[0:counter//speed], True, 'white')
        screen.blit(snip, (295, 600))

        pygame.display.flip()

def dialogue12():
 
    font = pygame.font.Font('assets/Font/ARCADE.TTF', 24)
    screen = pygame.display.set_mode ([1280, 720])
    timer = pygame.time.Clock()
    messages = ('<Roman slapped Luna>',
                'Roman : LUNA, DON\'T BE STUPID!',
                'Roman : Why did you kill all those people?',
                'Roman : What if Emir knows?',
                'Roman : How do you know this place at the first place?',
                '...')
    
    slap_sound.play()
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

        bg = pygame.image.load('assets/Chapter2/abanwarehouse.png')
        scaled_bg = pygame.transform.scale(bg, (1280,720))
        bg_rect = scaled_bg.get_rect(x=0,y=0)

        mc = pygame.image.load('assets/Chapter2/mcconfused.png')
        mc_rect = mc.get_rect(x=420,y=10)

        textbox = pygame.image.load('assets/textboxlover.png')
        scaled_texbox = pygame.transform.scale(textbox, (850,450))
        textbox_rect = scaled_texbox.get_rect(x=220,y=410)

        SCREEN.blit(scaled_bg, bg_rect)
        PAUSE.update(SCREEN)
        PAUSE.changeColor(MENU_MOUSE_POS)
        SCREEN.blit(mc, mc_rect)
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
                        dialogue13()
    
    
        snip = font.render(message[0:counter//speed], True, 'white')
        screen.blit(snip, (295, 600))

        pygame.display.flip()

def dialogue13():

    font = pygame.font.Font('assets/Font/ARCADE.TTF', 24)
    screen = pygame.display.set_mode ([1280, 720])
    timer = pygame.time.Clock()
    messages = ('<Luna started crying>',
                'Luna : Do you even know what happen to me?',
                'Luna : I was almost killed by the Emir\'s henchmen, don\'t you know?',
                'Luna : That\'s why I came here.',
                'Luna : I want to tell you the truth, Roman!',
                '...')
    
    crying_sound.play(1)
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

        bg = pygame.image.load('assets/Chapter2/abanwarehouse.png')
        scaled_bg = pygame.transform.scale(bg, (1280,720))
        bg_rect = scaled_bg.get_rect(x=0,y=0)

        lover = pygame.image.load('assets/Chapter2/lovercalm.png')
        lover_rect = lover.get_rect(x=420,y=100)

        textbox = pygame.image.load('assets/textboxlover.png')
        scaled_texbox = pygame.transform.scale(textbox, (850,450))
        textbox_rect = scaled_texbox.get_rect(x=220,y=410)

        SCREEN.blit(scaled_bg, bg_rect)
        PAUSE.update(SCREEN)
        PAUSE.changeColor(MENU_MOUSE_POS)
        SCREEN.blit(lover, lover_rect)
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
                        dialogue14()
    
    
        snip = font.render(message[0:counter//speed], True, 'white')
        screen.blit(snip, (295, 600))

        pygame.display.flip()

def dialogue14():
    pygame.mixer.stop()
    font = pygame.font.Font('assets/Font/ARCADE.TTF', 24)
    screen = pygame.display.set_mode ([1280, 720])
    timer = pygame.time.Clock()
    messages = ('<Roman was very shocked by Luna\'s words>',
                '<He looked very confused>',
                'Roman : How do I know you are telling the truth?',
                'Luna : I SWEAR TO GOD, ROMAN!',
                'Luna : I\'m telling you the truth.',
                'Luna : The most important thing is that he killed your mother.',
                'Luna : Open your eyes, Roman!',
                '<Roman doesn\'t know if Luna is telling the truth or not>',
                '<He was confused about who to trust>',
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

        bg = pygame.image.load('assets/Chapter2/abanwarehouse.png')
        scaled_bg = pygame.transform.scale(bg, (1280,720))
        bg_rect = scaled_bg.get_rect(x=0,y=0)

        lover = pygame.image.load('assets/Chapter2/lovercalm.png')
        scaled_lover = pygame.transform.scale(lover, (330,400))
        lover_rect = scaled_lover.get_rect(x=280,y=200)

        mc = pygame.image.load('assets/Chapter2/mcconfused.png')
        mc_rect = mc.get_rect(x=620,y=20)

        textbox = pygame.image.load('assets/textboxlover.png')
        scaled_texbox = pygame.transform.scale(textbox, (850,450))
        textbox_rect = scaled_texbox.get_rect(x=220,y=410)

        SCREEN.blit(scaled_bg, bg_rect)
        PAUSE.update(SCREEN)
        PAUSE.changeColor(MENU_MOUSE_POS)
        SCREEN.blit(mc, mc_rect)
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
                    if active_message == 9:
                        dialogue15()
    
    
        snip = font.render(message[0:counter//speed], True, 'white')
        screen.blit(snip, (295, 600))

        pygame.display.flip()

def dialogue15():

    font = pygame.font.Font('assets/Font/ARCADE.TTF', 24)
    screen = pygame.display.set_mode ([1280, 720])
    timer = pygame.time.Clock()
    messages = ('Emir : MWAH MWAH MWAH (Evil Laugh)',
                'Emir : Don\'t trust a word this bitc* is barking, Roman!',
                '<Emir had actually heard their conversation from the beginning>',
                '<He was actually hiding behind the boxes>',
                '...')
    
    evil_laugh.play()
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

        bg = pygame.image.load('assets/Chapter2/abanwarehouse.png')
        scaled_bg = pygame.transform.scale(bg, (1280,720))
        bg_rect = scaled_bg.get_rect(x=0,y=0)

        lover = pygame.image.load('assets/Chapter2/villainnormal.png')
        lover_rect = lover.get_rect(x=485,y=-80)

        textbox = pygame.image.load('assets/textboxlover.png')
        scaled_texbox = pygame.transform.scale(textbox, (850,450))
        textbox_rect = scaled_texbox.get_rect(x=220,y=410)

        SCREEN.blit(scaled_bg, bg_rect)
        PAUSE.update(SCREEN)
        PAUSE.changeColor(MENU_MOUSE_POS)
        SCREEN.blit(lover, lover_rect)
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
                        dialogue16()
    
    
        snip = font.render(message[0:counter//speed], True, 'white')
        screen.blit(snip, (295, 600))

        pygame.display.flip()

def dialogue16():
    pygame.mixer.stop()
    font = pygame.font.Font('assets/Font/ARCADE.TTF', 24)
    screen = pygame.display.set_mode ([1280, 720])
    timer = pygame.time.Clock()
    messages = ('<Roman and Luna were very surprised by Emir\'s presence>',
                'Roman : Emir...',
                'Roman : Is this true?',
                '<Roman expects the truth from Emir>',
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

        bg = pygame.image.load('assets/Chapter2/abanwarehouse.png')
        scaled_bg = pygame.transform.scale(bg, (1280,720))
        bg_rect = scaled_bg.get_rect(x=0,y=0)

        mc = pygame.image.load('assets/Chapter2/mcnormal.png')
        mc_rect = mc.get_rect(x=450,y=20)

        textbox = pygame.image.load('assets/textboxlover.png')
        scaled_texbox = pygame.transform.scale(textbox, (850,450))
        textbox_rect = scaled_texbox.get_rect(x=220,y=410)

        SCREEN.blit(scaled_bg, bg_rect)
        PAUSE.update(SCREEN)
        PAUSE.changeColor(MENU_MOUSE_POS)
        SCREEN.blit(mc, mc_rect)
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
                        dialogue17()
    
    
        snip = font.render(message[0:counter//speed], True, 'white')
        screen.blit(snip, (295, 600))

        pygame.display.flip()

def dialogue17():
    font = pygame.font.Font('assets/Font/ARCADE.TTF', 24)
    screen = pygame.display.set_mode ([1280, 720])
    timer = pygame.time.Clock()
    messages = ('Emir : I told you, don\'t believe this bitc*!',
                'Emir : She\'s better off dead.',
                'Emir : Let me end her!',
                '<Emir looks desperate to kill Luna>',             
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

        bg = pygame.image.load('assets/Chapter2/abanwarehouse.png')
        scaled_bg = pygame.transform.scale(bg, (1280,720))
        bg_rect = scaled_bg.get_rect(x=0,y=0)

        lover = pygame.image.load('assets/Chapter2/villainnormal.png')
        lover_rect = lover.get_rect(x=485,y=-80)

        textbox = pygame.image.load('assets/textboxlover.png')
        scaled_texbox = pygame.transform.scale(textbox, (850,450))
        textbox_rect = scaled_texbox.get_rect(x=220,y=410)

        SCREEN.blit(scaled_bg, bg_rect)
        PAUSE.update(SCREEN)
        PAUSE.changeColor(MENU_MOUSE_POS)
        SCREEN.blit(lover, lover_rect)
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
                        dialogue18()
    
    
        snip = font.render(message[0:counter//speed], True, 'white')
        screen.blit(snip, (295, 600))

        pygame.display.flip()

def dialogue18():
    font = pygame.font.Font('assets/Font/ARCADE.TTF', 24)
    screen = pygame.display.set_mode ([1280, 720])
    timer = pygame.time.Clock()
    messages = ('Roman : Emir, answer my question!',
                'Roman : Don\'t you ever touch her!',
                '<Roman seemed not satisfied with Emir\'s answer>',         
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

        bg = pygame.image.load('assets/Chapter2/abanwarehouse.png')
        scaled_bg = pygame.transform.scale(bg, (1280,720))
        bg_rect = scaled_bg.get_rect(x=0,y=0)

        mc = pygame.image.load('assets/Chapter2/mcnormal.png')
        mc_rect = mc.get_rect(x=450,y=20)

        textbox = pygame.image.load('assets/textboxlover.png')
        scaled_texbox = pygame.transform.scale(textbox, (850,450))
        textbox_rect = scaled_texbox.get_rect(x=220,y=410)

        SCREEN.blit(scaled_bg, bg_rect)
        PAUSE.update(SCREEN)
        PAUSE.changeColor(MENU_MOUSE_POS)
        SCREEN.blit(mc, mc_rect)
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
                        dialogue19()
    
    
        snip = font.render(message[0:counter//speed], True, 'white')
        screen.blit(snip, (295, 600))

        pygame.display.flip()

def dialogue19():
    font = pygame.font.Font('assets/Font/ARCADE.TTF', 24)
    screen = pygame.display.set_mode ([1280, 720])
    timer = pygame.time.Clock()
    messages = ('Emir : HM.. HM.. HM..',
                'Emir : Why is it so hard for you to understand this?',
                'Emir : Don\'t be fooled by this woman\'s sweet talk.',   
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

        bg = pygame.image.load('assets/Chapter2/abanwarehouse.png')
        scaled_bg = pygame.transform.scale(bg, (1280,720))
        bg_rect = scaled_bg.get_rect(x=0,y=0)

        villain = pygame.image.load('assets/Chapter2/villainnormal.png')
        villain_rect = villain.get_rect(x=485,y=-80)

        textbox = pygame.image.load('assets/textboxlover.png')
        scaled_texbox = pygame.transform.scale(textbox, (850,450))
        textbox_rect = scaled_texbox.get_rect(x=220,y=410)

        SCREEN.blit(scaled_bg, bg_rect)
        PAUSE.update(SCREEN)
        PAUSE.changeColor(MENU_MOUSE_POS)
        SCREEN.blit(villain, villain_rect)
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
                        dialogue20()
    
    
        snip = font.render(message[0:counter//speed], True, 'white')
        screen.blit(snip, (295, 600))

        pygame.display.flip()

def dialogue20():
    font = pygame.font.Font('assets/Font/ARCADE.TTF', 24)
    screen = pygame.display.set_mode ([1280, 720])
    timer = pygame.time.Clock()
    messages = ('<Emir suddenly pulled the trigger of his gun>',  
                '<He pointed the gun at Luna>', 
                '...')
    
    trigger_sound.play()
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

        bg = pygame.image.load('assets/Chapter2/abanwarehouse.png')
        scaled_bg = pygame.transform.scale(bg, (1280,720))
        bg_rect = scaled_bg.get_rect(x=0,y=0)

        villain = pygame.image.load('assets/Chapter2/villainshot.png')
        villain_rect = villain.get_rect(x=545,y=-40)

        textbox = pygame.image.load('assets/textboxlover.png')
        scaled_texbox = pygame.transform.scale(textbox, (850,450))
        textbox_rect = scaled_texbox.get_rect(x=220,y=410)

        SCREEN.blit(scaled_bg, bg_rect)
        PAUSE.update(SCREEN)
        PAUSE.changeColor(MENU_MOUSE_POS)
        SCREEN.blit(villain, villain_rect)
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
                        dialogue21()
    
    
        snip = font.render(message[0:counter//speed], True, 'white')
        screen.blit(snip, (295, 600))

        pygame.display.flip()

def dialogue21():
    pygame.mixer.stop()
    font = pygame.font.Font('assets/Font/ARCADE.TTF', 24)
    screen = pygame.display.set_mode ([1280, 720])
    timer = pygame.time.Clock()
    messages = ('Roman : Emir, what are you doing?',   
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

        bg = pygame.image.load('assets/Chapter2/abanwarehouse.png')
        scaled_bg = pygame.transform.scale(bg, (1280,720))
        bg_rect = scaled_bg.get_rect(x=0,y=0)

        mc = pygame.image.load('assets/Chapter2/mcnormal.png')
        mc_rect = mc.get_rect(x=450,y=20)

        textbox = pygame.image.load('assets/textboxlover.png')
        scaled_texbox = pygame.transform.scale(textbox, (850,450))
        textbox_rect = scaled_texbox.get_rect(x=220,y=410)

        SCREEN.blit(scaled_bg, bg_rect)
        PAUSE.update(SCREEN)
        PAUSE.changeColor(MENU_MOUSE_POS)
        SCREEN.blit(mc, mc_rect)
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
                        dialogue22()
    
    
        snip = font.render(message[0:counter//speed], True, 'white')
        screen.blit(snip, (295, 600))

        pygame.display.flip()

def dialogue22():
    font = pygame.font.Font('assets/Font/ARCADE.TTF', 24)
    screen = pygame.display.set_mode ([1280, 720])
    timer = pygame.time.Clock()
    messages = ('<Without hesitation, Roman aimed the gun at Emir>',
                'Roman : Drop the gun, Emir!',
                'Roman : We still can discuss Emir.',
                'Emir : There is nothing to talk about Roman.',
                'Emir : What, now do you trust her more than me?',
                'Emir : SHOOT ME, ROMAN!',
                'Emir : WHAT ARE YOU WAITING FOR!',
                'Emir : ARE YOU SCARED?',
                'Emir : THERE IS NOTHING TO BE AFRAID OF!', 
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

        bg = pygame.image.load('assets/Chapter2/abanwarehouse.png')
        scaled_bg = pygame.transform.scale(bg, (1280,720))
        bg_rect = scaled_bg.get_rect(x=0,y=0)

        mc = pygame.image.load('assets/Chapter2/mcshot2.png')
        mc_rect = mc.get_rect(x=280,y=-20)

        villain = pygame.image.load('assets/Chapter2/villainnormal.png')
        villain_rect = villain.get_rect(x=680,y=-50)

        textbox = pygame.image.load('assets/textboxlover.png')
        scaled_texbox = pygame.transform.scale(textbox, (850,450))
        textbox_rect = scaled_texbox.get_rect(x=220,y=410)

        SCREEN.blit(scaled_bg, bg_rect)
        PAUSE.update(SCREEN)
        PAUSE.changeColor(MENU_MOUSE_POS)
        SCREEN.blit(mc, mc_rect)
        SCREEN.blit(villain, villain_rect)
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
                    if active_message == 9:
                        dialogue23()
    
    
        snip = font.render(message[0:counter//speed], True, 'white')
        screen.blit(snip, (295, 600))

        pygame.display.flip()

def dialogue23():
    font = pygame.font.Font('assets/Font/ARCADE.TTF', 24)
    screen = pygame.display.set_mode ([1280, 720])
    timer = pygame.time.Clock()
    messages = ('Luna : Just shoot him, Roman!',
                'Luna : This is what you want, right?',
                'Luna : Revenge for your mother.',
                '<Luna convinces Roman to shoot Emir>',
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

        bg = pygame.image.load('assets/Chapter2/abanwarehouse.png')
        scaled_bg = pygame.transform.scale(bg, (1280,720))
        bg_rect = scaled_bg.get_rect(x=0,y=0)

        lover = pygame.image.load('assets/Chapter2/lovercalm.png')
        lover_rect = lover.get_rect(x=420,y=100)

        textbox = pygame.image.load('assets/textboxlover.png')
        scaled_texbox = pygame.transform.scale(textbox, (850,450))
        textbox_rect = scaled_texbox.get_rect(x=220,y=410)

        SCREEN.blit(scaled_bg, bg_rect)
        PAUSE.update(SCREEN)
        PAUSE.changeColor(MENU_MOUSE_POS)
        SCREEN.blit(lover, lover_rect)
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
                        dialogue24()
    
        snip = font.render(message[0:counter//speed], True, 'white')
        screen.blit(snip, (295, 600))

        pygame.display.flip()

def dialogue24():
    pygame.mixer.music.stop()

    pygame.mixer.music.load("assets/Audio/Intense.mp3")
    pygame.mixer.music.play(-1)  # -1 means the music will loop indefinitely
    pygame.mixer.music.set_volume(0.3)

    font = pygame.font.Font('assets/Font/ARCADE.TTF', 24)
    screen = pygame.display.set_mode ([1280, 720])
    timer = pygame.time.Clock()
    messages = ('<BOOM> <BOOM>',
                '<Emir unleashed a shot at Roman>',
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

        bg = pygame.image.load('assets/Chapter2/abanwarehouse.png')
        scaled_bg = pygame.transform.scale(bg, (1280,720))
        bg_rect = scaled_bg.get_rect(x=0,y=0)

        mc = pygame.image.load('assets/Chapter2/mcnormaldead.png')
        scaled_mc = pygame.transform.scale(mc, (350,500))
        mc_rect = scaled_mc.get_rect(x=660,y=80)

        villain = pygame.image.load('assets/Chapter2/villainshot.png')
        villain_rect = villain.get_rect(x=290,y=-40)

        textbox = pygame.image.load('assets/textboxlover.png')
        scaled_texbox = pygame.transform.scale(textbox, (850,450))
        textbox_rect = scaled_texbox.get_rect(x=220,y=410)

        SCREEN.blit(scaled_bg, bg_rect)
        PAUSE.update(SCREEN)
        PAUSE.changeColor(MENU_MOUSE_POS)
        SCREEN.blit(scaled_mc, mc_rect)
        SCREEN.blit(villain, villain_rect)
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
    pygame.mixer.stop()
    font = pygame.font.Font('assets/Font/ARCADE.TTF', 24)
    screen = pygame.display.set_mode ([1280, 720])
    timer = pygame.time.Clock()
    messages = ('<Luna was stunned by what had happened>',
                'Luna : AAAARGHHHHHHHH!',
                'Luna : RROOOOOOOOMANNN!',
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

        bg = pygame.image.load('assets/Chapter2/abanwarehouse.png')
        scaled_bg = pygame.transform.scale(bg, (1280,720))
        bg_rect = scaled_bg.get_rect(x=0,y=0)

        lover = pygame.image.load('assets/Chapter2/lovercalm.png')
        lover_rect = lover.get_rect(x=420,y=100)

        textbox = pygame.image.load('assets/textboxlover.png')
        scaled_texbox = pygame.transform.scale(textbox, (850,450))
        textbox_rect = scaled_texbox.get_rect(x=220,y=410)

        SCREEN.blit(scaled_bg, bg_rect)
        PAUSE.update(SCREEN)
        PAUSE.changeColor(MENU_MOUSE_POS)
        SCREEN.blit(lover, lover_rect)
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
                        dialogue26()
    
    
        snip = font.render(message[0:counter//speed], True, 'white')
        screen.blit(snip, (295, 600))

        pygame.display.flip()

def dialogue26():
    font = pygame.font.Font('assets/Font/ARCADE.TTF', 24)
    screen = pygame.display.set_mode ([1280, 720])
    timer = pygame.time.Clock()
    messages = ('Luna : You have to pay for this, Emir!',
                '...')
    
    crying_sound.play(100)
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

        bg = pygame.image.load('assets/Chapter2/abanwarehouse.png')
        scaled_bg = pygame.transform.scale(bg, (1280,720))
        bg_rect = scaled_bg.get_rect(x=0,y=0)

        lover = pygame.image.load('assets/Chapter2/lovercalm.png')
        lover_rect = lover.get_rect(x=420,y=100)

        textbox = pygame.image.load('assets/textboxlover.png')
        scaled_texbox = pygame.transform.scale(textbox, (850,450))
        textbox_rect = scaled_texbox.get_rect(x=220,y=410)

        SCREEN.blit(scaled_bg, bg_rect)
        PAUSE.update(SCREEN)
        PAUSE.changeColor(MENU_MOUSE_POS)
        SCREEN.blit(lover, lover_rect)
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
                        dialogue27()
    
    
        snip = font.render(message[0:counter//speed], True, 'white')
        screen.blit(snip, (295, 600))

        pygame.display.flip()

def dialogue27():
    pygame.mixer.stop()
    font = pygame.font.Font('assets/Font/ARCADE.TTF', 24)
    screen = pygame.display.set_mode ([1280, 720])
    timer = pygame.time.Clock()
    messages = ('Emir : MWAH MWAH MWAH (Evil Laugh)',
                'Emir : You have such a foolish boyfriend.',
                'Emir : I have killed his mother, and I have also taken his life.',
                'Emir : STUPID GENES!',
                'Emir : Next, I\'ll ki....', 
                '...')
    
    evil_laugh.play(1)
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

        bg = pygame.image.load('assets/Chapter2/abanwarehouse.png')
        scaled_bg = pygame.transform.scale(bg, (1280,720))
        bg_rect = scaled_bg.get_rect(x=0,y=0)

        villain = pygame.image.load('assets/Chapter2/villainnormal.png')
        villain_rect = villain.get_rect(x=485,y=-80)

        textbox = pygame.image.load('assets/textboxlover.png')
        scaled_texbox = pygame.transform.scale(textbox, (850,450))
        textbox_rect = scaled_texbox.get_rect(x=220,y=410)

        SCREEN.blit(scaled_bg, bg_rect)
        PAUSE.update(SCREEN)
        PAUSE.changeColor(MENU_MOUSE_POS)
        SCREEN.blit(villain, villain_rect)
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
    pygame.mixer.stop()
    pygame.mixer.music.stop()
    font = pygame.font.Font('assets/Font/ARCADE.TTF', 24)
    screen = pygame.display.set_mode ([1280, 720])
    timer = pygame.time.Clock()
    messages = ('<BOOM> <BOOM>',
                '<Luna shot Emir non-stop>', 
                '...')
    
    shoot_sound.play(9)
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

        bg = pygame.image.load('assets/Chapter2/abanwarehouse.png')
        scaled_bg = pygame.transform.scale(bg, (1280,720))
        bg_rect = scaled_bg.get_rect(x=0,y=0)

        lover = pygame.image.load('assets/Chapter2/lovershoot1.png')
        lover_rect = lover.get_rect(x=380,y=30)

        textbox = pygame.image.load('assets/textboxlover.png')
        scaled_texbox = pygame.transform.scale(textbox, (850,450))
        textbox_rect = scaled_texbox.get_rect(x=220,y=410)

        SCREEN.blit(scaled_bg, bg_rect)
        PAUSE.update(SCREEN)
        PAUSE.changeColor(MENU_MOUSE_POS)
        SCREEN.blit(lover, lover_rect)
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
                        dialogue29()
    
    
        snip = font.render(message[0:counter//speed], True, 'white')
        screen.blit(snip, (295, 600))

        pygame.display.flip()   

def dialogue29():
    pygame.mixer.stop()
    font = pygame.font.Font('assets/Font/ARCADE.TTF', 24)
    screen = pygame.display.set_mode ([1280, 720])
    timer = pygame.time.Clock()
    messages = ('<Luna ended Emir\'s life there>',
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

        bg = pygame.image.load('assets/Chapter2/abanwarehouse.png')
        scaled_bg = pygame.transform.scale(bg, (1280,720))
        bg_rect = scaled_bg.get_rect(x=0,y=0)

        lover = pygame.image.load('assets/Chapter2/lovershoot1.png')
        lover_rect = lover.get_rect(x=190,y=30)

        villain = pygame.image.load('assets/Chapter2/villainnormaldead.png')
        villain_rect = villain.get_rect(x=680,y=-90)

        textbox = pygame.image.load('assets/textboxlover.png')
        scaled_texbox = pygame.transform.scale(textbox, (850,450))
        textbox_rect = scaled_texbox.get_rect(x=220,y=410)

        SCREEN.blit(scaled_bg, bg_rect)
        PAUSE.update(SCREEN)
        PAUSE.changeColor(MENU_MOUSE_POS)
        SCREEN.blit(lover, lover_rect)
        SCREEN.blit(villain, villain_rect)
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
                        dialogue30()
    
    
        snip = font.render(message[0:counter//speed], True, 'white')
        screen.blit(snip, (295, 600))

        pygame.display.flip()  

def dialogue30():   
    pygame.mixer.music.load("assets/Audio/OnlyLove.wav")
    pygame.mixer.music.play(-1)  # -1 means the music will loop indefinitely
    pygame.mixer.music.set_volume(0.15)

    font = pygame.font.Font('assets/Font/ARCADE.TTF', 24)
    screen = pygame.display.set_mode ([1280, 720])
    timer = pygame.time.Clock()
    messages = ('<After that, Luna goes to Roman\'s corpse>',
                '<Luna looked deeply into Roman\'s face>',
                'Luna : Don\'t leave me Roman...',
                'Luna : It shouldn\'t end like this...',
                'Luna : Roman, please forgive me...',
                '<Her tears continued to flow down Roman\'s face>',
                '<Luna lost the love of her life>',
                '<Luna couldn\'t control her emotions>',
                '<Luna could not accept the fate that Roman was gone>',
                '<She felt her life was useless>',
                '...')
    
    crying_sound.play(100)
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

        bg = pygame.image.load('assets/Chapter2/abanwarehouse.png')
        scaled_bg = pygame.transform.scale(bg, (1280,720))
        bg_rect = scaled_bg.get_rect(x=0,y=0)

        lover = pygame.image.load('assets/Chapter2/lovercalm.png')
        lover_rect = lover.get_rect(x=420,y=100)

        textbox = pygame.image.load('assets/textboxlover.png')
        scaled_texbox = pygame.transform.scale(textbox, (850,450))
        textbox_rect = scaled_texbox.get_rect(x=220,y=410)

        SCREEN.blit(scaled_bg, bg_rect)
        PAUSE.update(SCREEN)
        PAUSE.changeColor(MENU_MOUSE_POS)
        SCREEN.blit(lover, lover_rect)
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
                        dialogue31()
    
        snip = font.render(message[0:counter//speed], True, 'white')
        screen.blit(snip, (295, 600))

        pygame.display.flip()    

def dialogue31():
    font = pygame.font.Font('assets/Font/ARCADE.TTF', 24)
    screen = pygame.display.set_mode ([1280, 720])
    timer = pygame.time.Clock()
    messages = ('<She then took a cigarette>',
                '<She started to remember the sweetest memories with Roman>',
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

        bg = pygame.image.load('assets/Chapter2/abanwarehouse.png')
        scaled_bg = pygame.transform.scale(bg, (1280,720))
        bg_rect = scaled_bg.get_rect(x=0,y=0)

        mc = pygame.image.load('assets/Chapter2/loversmoke.png')
        mc_rect = mc.get_rect(x=400,y=80)

        textbox = pygame.image.load('assets/textboxlover.png')
        scaled_texbox = pygame.transform.scale(textbox, (850,450))
        textbox_rect = scaled_texbox.get_rect(x=220,y=410)

        SCREEN.blit(scaled_bg, bg_rect)
        PAUSE.update(SCREEN)
        PAUSE.changeColor(MENU_MOUSE_POS)
        SCREEN.blit(mc, mc_rect)
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
                        kenangan_images()
    
    
        snip = font.render(message[0:counter//speed], True, 'white')
        screen.blit(snip, (295, 600))

        pygame.display.flip() 

def kenangan_images():
    screen = pygame.display.set_mode([1280, 720])
    clock = pygame.time.Clock()


    images = [
        'assets/Chapter2/scene1.jpg',
        'assets/Chapter2/scene2.jpg',
        'assets/Chapter2/scene3.jpg',
        'assets/Chapter2/scene4.jpg',
        'assets/Chapter2/scene5.jpg',
        'assets/Chapter2/scene6.jpg',
        'assets/Chapter2/scene7.jpg',
        'assets/Chapter2/scene8.jpg',
        'assets/Chapter2/scene9.jpg',
        'assets/Chapter2/scene10.jpg',
        ]

    # Time to display each image (in milliseconds)
    current_image_index = 0

    # Function to display the current image
    def display_current_image():
        image = pygame.image.load(images[current_image_index])
        scaled_image = pygame.transform.scale(image, (720, 1100))
        screen.blit(scaled_image, (300, -180))
        pygame.display.flip()

    # Initial display of the first image
    display_current_image()

    # Loop to handle events and switch images
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    # Move to the next image if Enter is pressed
                    current_image_index += 1
                    if current_image_index < len(images):
                        display_current_image()
                    else:
                        dialogue32()  # Exit the loop if there are no more images

        clock.tick(60)

def dialogue32():

    font = pygame.font.Font('assets/Font/ARCADE.TTF', 24)
    screen = pygame.display.set_mode ([1280, 720])
    timer = pygame.time.Clock()
    messages = ('<Luna smiled remembering her memories with Roman>',
                '<But she is not strong enough to bear this pain>',
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

        bg = pygame.image.load('assets/Chapter2/abanwarehouse.png')
        scaled_bg = pygame.transform.scale(bg, (1280,720))
        bg_rect = scaled_bg.get_rect(x=0,y=0)

        mc = pygame.image.load('assets/Chapter2/loversmoke.png')
        mc_rect = mc.get_rect(x=400,y=80)

        textbox = pygame.image.load('assets/textboxlover.png')
        scaled_texbox = pygame.transform.scale(textbox, (850,450))
        textbox_rect = scaled_texbox.get_rect(x=220,y=410)

        SCREEN.blit(scaled_bg, bg_rect)
        PAUSE.update(SCREEN)
        PAUSE.changeColor(MENU_MOUSE_POS)
        SCREEN.blit(mc, mc_rect)
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
                        dialogue33()
    
    
        snip = font.render(message[0:counter//speed], True, 'white')
        screen.blit(snip, (295, 600))

        pygame.display.flip() 

def dialogue33():

    font = pygame.font.Font('assets/Font/ARCADE.TTF', 24)
    screen = pygame.display.set_mode ([1280, 720])
    timer = pygame.time.Clock()
    messages = ('<Then she put a gun to his own head>',
                '<She smiled for the last time-',
                '-and enjoyed the beauty of the world for the last time>',
                'Luna : Thank you for all your sweet memories with me Roman.',
                'Luna : I love you very much!',
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

        bg = pygame.image.load('assets/Chapter2/abanwarehouse.png')
        scaled_bg = pygame.transform.scale(bg, (1280,720))
        bg_rect = scaled_bg.get_rect(x=0,y=0)

        lover = pygame.image.load('assets/Chapter2/lovershot1.png')
        lover_rect = lover.get_rect(x=320,y=150)

        textbox = pygame.image.load('assets/textboxlover.png')
        scaled_texbox = pygame.transform.scale(textbox, (850,450))
        textbox_rect = scaled_texbox.get_rect(x=220,y=410)

        SCREEN.blit(scaled_bg, bg_rect)
        PAUSE.update(SCREEN)
        PAUSE.changeColor(MENU_MOUSE_POS)
        SCREEN.blit(lover, lover_rect)
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
                        dialogue34()
    
    
        snip = font.render(message[0:counter//speed], True, 'white')
        screen.blit(snip, (295, 600))

        pygame.display.flip() 

def dialogue34():
    pygame.mixer.stop()
    font = pygame.font.Font('assets/Font/ARCADE.TTF', 24)
    screen = pygame.display.set_mode ([1280, 720])
    timer = pygame.time.Clock()
    messages = ('<BOOM> <BOOM>',
                '<Luna killed herself>',
                '...',
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

        bg = pygame.image.load('assets/Chapter2/abanwarehouse.png')
        scaled_bg = pygame.transform.scale(bg, (1280,720))
        bg_rect = scaled_bg.get_rect(x=0,y=0)

        lover = pygame.image.load('assets/Chapter2/lovershot1dead.png')
        lover_rect = lover.get_rect(x=320,y=150)

        textbox = pygame.image.load('assets/textboxlover.png')
        scaled_texbox = pygame.transform.scale(textbox, (850,450))
        textbox_rect = scaled_texbox.get_rect(x=220,y=410)

        SCREEN.blit(scaled_bg, bg_rect)
        PAUSE.update(SCREEN)
        PAUSE.changeColor(MENU_MOUSE_POS)
        SCREEN.blit(lover, lover_rect)
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
                        bad_ending()
    
    
        snip = font.render(message[0:counter//speed], True, 'white')
        screen.blit(snip, (295, 600))

        pygame.display.flip() 

def bad_ending():
    font = pygame.font.Font('assets/Font/Cinzel.ttf', 35)
    screen = pygame.display.set_mode([1280, 720])
    timer = pygame.time.Clock()
    messages = ('Luna chose to commit suicide',
                'She lost everything',
                'She felt that she failed',
                'She can\'t accept that Roman is dead',
                'She thinks life is useless without Roman',
                'Emir is also dead',
                'She no longer has anything important in the world',
                'Maybe love stories don\'t always have happy endings',
                'A wise man once said',
                'At the end of True Love is death,',
                'And only the love that ends in death is love',
                'Only Love can hurt like this...',
                '...',
                '..',
                '.',
                'THE END',
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
                    if active_message == 16:
                        pygame.mixer.music.stop()
                        credits()
    
        snip = font.render(message[0:counter//speed], True, 'white')
        screen.blit(snip, (100, 360))

        pygame.display.flip()

def credits():
    while True:
        pygame.display.set_caption("Bad Ending")

        timer = pygame.time.Clock()

        current  = pygame.font.Font('assets/Font/Cinzel.ttf', 40).render("CONGRATULATIONS YOU HAVE UNLOCKED BAD ENDING", True, "White")
        current_rect = current.get_rect(x=70,y=330)

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
                            text_input="MAIN MENU", font=textbutton_font(30), base_color="black", hovering_color="#FF3131")
        
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
                    print('MAIN MENU')
                    main_menu()
                if CHOICE1.checkForInput(MENU_MOUSE_POS):
                    print('QUIT')
                    pygame.quit()
                    sys.exit()

            pygame.display.flip()
