import pygame

screen_h = 405
screen_w = 540
bg_image = pygame.image.load('pixelcell.jpg') 
screen = pygame.display.set_mode((screen_w, screen_h))                                
pygame.display.set_caption('YO1LO')

screenfade = True

#load button images
next_img = pygame.image.load('favpng_next.png').convert_alpha()

class Button():
    def __init__(self,x,y,image,scale):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image,(int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)
        self.clicked = False

    def draw(self, surface):
        action = False
        pos = pygame.mouse.get_pos()

        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True
                pygame.time.delay(10)
                fade1(screen_w,screen_h)
                pygame.quit()

            if pygame.mouse.get_pressed()[0] == 0:
                self.clicked = False
            
        surface.blit(self.image,(self.rect.x, self.rect.y))
        return action
    
next_button = Button(450, 330, next_img, 0.10)

def fade1(width, height): 
    fade = pygame.Surface((width, height))
    fade.fill((0,0,0))
    for alpha in range(0, 300):
        fade.set_alpha(alpha)
        screen.blit(fade, (0,0))
        pygame.display.update()
        pygame.time.delay(5)

def fade2(width, height): 
    fade = pygame.Surface((width, height))
    fade.fill((0,0,0))
    for alpha in range(0, 300):
        fade.set_alpha(alpha)
        screen.blit(fade, (0,0))
        pygame.display.update()
        pygame.time.delay(5)


run = True
while run :
    
    screen.fill((0,0,0))
    screen.blit(bg_image,(0,0))
    def bg_prison(image):
        size = pygame.transform.scale(image,(700,500))
        screen.blit(size,(0,0))
        bg_prison(bg_image)
        
    if next_button.draw(screen) == True:
        print('NEXT')

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()