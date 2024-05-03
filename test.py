import pygame
from menu import MainMenu

pygame.display.set_caption('YO1LO')

# Initialize the display surface
screen = pygame.display.set_mode((800,600))

class Button():
    def __init__(self,x,y,image,scale):
        self.next_img = pygame.image.load('favpng_next.png').convert_alpha()
        self.screenfade = True
        self.screen_h = 600
        self.screen_w = 900
        self.bg_image = pygame.image.load('sunset.jpg') 
        self.screen = pygame.display.set_mode((self.screen_w, self.screen_h)) 
        self.width = image.get_width()
        self.height = image.get_height()
        self.image = pygame.transform.scale(image,(int(self.width * scale), int(self.height * scale)))
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

            if pygame.mouse.get_pressed()[0] == 0:
                self.clicked = False
            
        surface.blit(self.image,(self.rect.x, self.rect.y))
        return action
    




    def fade1(self, width, height): 
        fade = pygame.Surface((width, height))
        fade.fill((0,0,0))
        for alpha in range(0, 300):
            fade.set_alpha(alpha)
            self.SCREEN.blit(fade, (0,0))
            pygame.display.update()
            pygame.time.delay(5)

    def fade2(self, width, height): 
        fade = pygame.Surface((width, height))
        fade.fill((0,0,0))
        for alpha in range(0, 300):
            fade.set_alpha(alpha)
            self.screen.blit(fade, (0,0))
            pygame.display.update()
            pygame.time.delay(5)


class StartGame:
    def __init__(self):
        self.next_img = pygame.image.load('favpng_next.png').convert_alpha()
        self.screen_h = 405
        self.screen_w = 540
        self.screen =pygame.display.set_mode((self.screen_w, self.screen_h))
        self.bg_image =pygame.image.load('sunset.jpg') 
        self.next_button = Button(450, 330, self.next_img, 0.02)

    def start(self):
        run = True
        while run :
            
            self.screen.fill((0,0,0))
            self.screen.blit(self.bg_image,(0,0))
            def bg_prison(image):
                size = pygame.transform.scale(image,(700,500))
                self.screen.blit(size,(0,0))
                bg_prison(self.bg_image)
                
            if self.next_button.draw(self.screen) == True:
                print('NEXT')

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

            pygame.display.update()

        pygame.quit()

# Call the start(self) function here
my_instance = StartGame()
my_instance.start()


