import pygame
import sys

pygame.init()

SCREEN = pygame.display.set_mode((800,600))
pygame.display.set_caption('Menu')

BG = pygame.image.load('sunset.jpg')

def get_font(size):
    return pygame.font.Font("ARCADECLASSIC.TTF", size)

def play():
    pygame.display.set_caption('Play')

    while True:
        play_mouse_pos = pygame.mouse.get_pos()

        SCREEN.fill('black')

        PLAY_TEXT = get_font(45).render('This is the PLAY screen', True, 'White')
        PLAY_RECT = PLAY_TEXT.get_rect(center=(400, 360))

        SCREEN.blit(PLAY_TEXT, PLAY_RECT)

        PLAY_BACK = Button(image=None,pos=(400,260)
                                ,text_input="BACK", font=get_font(75), base_color="White", hovering_color="Green")

        PLAY_BACK.changeColor(play_mouse_pos) 
        PLAY_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(play_mouse_pos):
                    main_menu()

        pygame.display.update()

def main_menu():
    pygame.display.set_caption('Main Menu')

    while True:
        SCREEN.blit(BG, (0, 0))
        MENU_MOUSE_POS = pygame.mouse.get_pos() 

        MENU_TEXT = get_font(100).render("YO1LO", True,"#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(400, 100))   
        PLAY_BUTTON = Button(image=pygame.image.load("Play Rect.png"), pos=(400, 250), 
                                  text_input="PLAY", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        QUIT_BUTTON=Button(image=pygame.image.load("Quit Rect.png"), pos=(400,400),
                                   text_input="QUIT", font=get_font(75),base_color="#d7fcd4", hovering_color="White")
        
        SCREEN.blit(MENU_TEXT, MENU_RECT) 

        for button in [PLAY_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    play()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

class Button():
    def __init__(self, image, pos, text_input, font, base_color, hovering_color):
        self.image = image
        self.x_pos = pos[0]
        self.y_pos = pos[1]
        self.font = font
        self.base_color, self.hovering_color = base_color, hovering_color
        self.text_input = text_input
        self.text = self.font.render(self.text_input, True, self.base_color)
        self.font_name = 'ARCADECLASSIC.TTF'
        if self.image is None:
            self.image = self.text
        self.rect = self.image.get_rect(center = (self.x_pos, self.y_pos))
        self.text_rect = self.text.get_rect(center = (self.x_pos, self.y_pos))

    def update(self, screen):
        if self.image is not None:
            screen.blit(self.image, self.rect)
        screen.blit(self.text, self.text_rect)

    def checkForInput(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            return True
        return False
    
    def changeColor(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range (self.rect.top, self.rect.bottom):
            self.text = self.font.render(self.text_input, True, self.hovering_color)
        else:
            self.text = self.font.render(self.text_input, True, self.base_color)

main_menu()