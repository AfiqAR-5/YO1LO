import pygame, sys
from config import *
from button import Button
pygame.init()

class Intro:

    intro_active = True

    def __init__(self):
        self.done = False
        self.text = 'A great evening in the prison'
        self.font = pygame.font.Font('assets/ARCADE.TTF', 24)
        self.counter = 0
        self.speed = 3
        self.display = SCREEN
        self.timer = pygame.time.Clock()
    
    def checkForInput(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            return True
        return False

    def text_font(self, size):   
        return pygame.font.Font('assets/ARCADE.TTF', size)

    def Text(self):

        SKIP = Button(image=pygame.image.load("assets/next.png"), pos=(960, 330), 
                            text_input=None, font=self.font, base_color="White", hovering_color="#ba2323")

        while Intro.intro_active:
            CHAR_MOUSE_POS = pygame.mouse.get_pos()
            self.timer.tick(60)

            for button in [SKIP]:
                button.changeColor(CHAR_MOUSE_POS)
                button.update(self.display)
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if SKIP.checkForInput(CHAR_MOUSE_POS):
                        if self.done == True:
                            break

                        else:
                            self.skiptext()
                            self.done = True

            if self.counter < self.speed * len(self.text):
                self.counter += 1

            elif self.counter >= self.speed * len(self.text):
                self.done = True

            snip = self.font.render(self.text[0:self.counter//self.speed], True, 'white')
            self.display.blit(snip, (10, 310))


            Intro2().Text2()
            pygame.display.flip()

    def skiptext(self):
        text_render = self.text_font(24).render(self.text, True, 'white')
        self.display.blit(text_render, (10, 310)) 

        SKIP = Button(image=pygame.image.load("assets/next.png"), pos=(960, 330), 
                      text_input=None, font=self.font, base_color="White", hovering_color="#ba2323")

        while Intro.intro_active:
            CHAR_MOUSE_POS = pygame.mouse.get_pos()
                        
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if SKIP.checkForInput(CHAR_MOUSE_POS):
                        break

            Intro2.Text2()
            pygame.display.update()

class Intro2:

    intro2_active = True

    def __init__(self):
        self.done = False
        self.text = 'hai mc'
        self.font = pygame.font.Font('assets/ARCADE.TTF', 24)
        self.counter = 0
        self.speed = 3
        self.display = SCREEN
        self.timer = pygame.time.Clock()
    
    def checkForInput(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            return True
        return False

    def text_font(self, size):   
        return pygame.font.Font('assets/ARCADE.TTF', size)

    def Text2(self):

        SKIP = Button(image=pygame.image.load("assets/next.png"), pos=(960, 330), 
                            text_input=None, font=self.font, base_color="White", hovering_color="#ba2323")

        while Intro2.intro2_active:
            CHAR_MOUSE_POS = pygame.mouse.get_pos()
            self.timer.tick(60)

            for button in [SKIP]:
                button.changeColor(CHAR_MOUSE_POS)
                button.update(self.display)
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if SKIP.checkForInput(CHAR_MOUSE_POS):
                        if self.done:
                            pygame.quit()
                            sys.exit()
                        else:
                            pygame.quit()
                            sys.exit()

            if self.counter < self.speed * len(self.text):
                self.counter += 1

            elif self.counter >= self.speed * len(self.text):
                self.done = True

            snip = self.font.render(self.text[0:self.counter//self.speed], True, 'white')
            self.display.blit(snip, (10, 350))

            pygame.display.flip()

    def skiptext(self):
        text_render = self.text_font(24).render(self.text, True, 'white')
        self.display.blit(text_render, (10, 350)) 

        SKIP = Button(image=pygame.image.load("assets/next.png"), pos=(960, 330), 
                      text_input=None, font=self.font, base_color="White", hovering_color="#ba2323")

        while Intro2.intro2_active:
            CHAR_MOUSE_POS = pygame.mouse.get_pos()
                        
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if SKIP.checkForInput(CHAR_MOUSE_POS):
                        pygame.quit()
                        sys.exit()

            pygame.display.update()