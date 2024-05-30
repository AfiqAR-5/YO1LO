import pygame, sys
from sys import exit
import math
import random
from settingsshoot import *

pygame.init()

pygame.mixer.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("YO!LO")
clock = pygame.time.Clock()

# Background Sound
pygame.mixer.music.load("assets/xiaolao.wav")
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.5)

#loadsoundeffect
shoot_sound = pygame.mixer.Sound("assets/shoot_sound.wav")
collision_sound = pygame.mixer.Sound("assets/oof.wav")
dead_sound = pygame.mixer.Sound("assets/Death_sound.wav")
gta_sound = pygame.mixer.Sound("assets/gta.wav")

#backgroundimage
background = pygame.transform.scale(pygame.image.load("assets/warehouse.png").convert(), (WIDTH, HEIGHT))

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.pos = pygame.math.Vector2(PLAYER_START_X, PLAYER_START_Y)
        self.image = pygame.transform.rotozoom(pygame.image.load("assets/Player11.png").convert_alpha(), 0, PLAYER_SIZE)
        self.base_player_image = self.image
        self.hitbox_rect = self.base_player_image.get_rect(center = self.pos)
        self.rect = self.hitbox_rect.copy()
        self.speed = PLAYER_SPEED
        self.shoot = False
        self.shoot_cooldown = 0
        self.gun_barrel_offset = pygame.math.Vector2(GUN_OFFSET_X, GUN_OFFSET_Y)
        self.max_health = PLAYER_HEALTH
        self.health = self.max_health
        self.health_cooldown = 0

    def player_rotation(self):
        self.mouse_coords = pygame.mouse.get_pos()
        self.x_change_mouse_player = (self.mouse_coords[0] - WIDTH // 2)
        self.y_change_mouse_player = (self.mouse_coords[1] - HEIGHT // 2)
        self.angle = math.degrees(math.atan2(self.y_change_mouse_player, self.x_change_mouse_player))
        self.image = pygame.transform.rotate(self.base_player_image, -self.angle)
        self.rect = self.image.get_rect(center = self.hitbox_rect.center)

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

        if self.velocity_x !=0 and self.velocity_y != 0: #moving diagonally
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

        # Ensure the player statys within the screen boundaries
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
        self.image = pygame.transform.rotozoom(self.image, 0, 2)

        self.rect = self.image.get_rect()
        self.rect.center = position

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
                run = False

        screen.fill((0, 0, 0))  # Black background
        font = pygame.font.Font("assets/getfont.ttf", 50)
        text = font.render("You Are DEAD!", True, (255, 0, 0))
        text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        screen.blit(text, text_rect)
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

        popup_surface = pygame.Surface((640, 360))
        popup_surface.fill((0, 0, 0))
        popup_rect = popup_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2))

        font = pygame.font.Font("assets/ARCADECLASSIC.TTF", 50)
        text = font.render("Mission Complete!", True, (255, 255, 255))
        text_rect = text.get_rect(center=(325, 180))

        popup_surface.blit(text, text_rect)

        screen.blit(popup_surface, popup_rect)

        pygame.display.flip()

        clock.tick(60)

waiting_for_key = False
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
