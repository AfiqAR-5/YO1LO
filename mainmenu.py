import pygame
import sys
import config

pygame.init()
pygame.display.set_caption('Menu')

class Button:
    def __init__(self, image, pos, text_input, font, base_color, hovering_color, scale):
        pygame.init()
        self.screen = config.SCREEN
        self.font = pygame.font.Font('ARCADECLASSIC.TTF', 32)
        self.clock = pygame.time.Clock()
        self.char_selection = 3
        self.running = True
        self.choosecharacterbg = pygame.image.load('choosecharbg.jpg')
        self.image = image
        self.x_pos = pos[0]
        self.y_pos = pos[1]
        self.font = font
        self.scale = scale
        self.base_color, self.hovering_color = base_color, hovering_color
        self.text_input = text_input
        self.text = self.font.render(self.text_input, True, self.base_color)
        self.font_name = 'ARCADECLASSIC.TTF'
        if self.image is None:
            self.image = self.text
        self.rect = self.image.get_rect(center = (self.x_pos, self.y_pos))
        self.text_rect = self.text.get_rect(center = (self.x_pos, self.y_pos))
    
    def update(self, surface):
            config.SCREEN
            if self.image is not None:
                surface.blit(self.image, self.rect)
            surface.blit(self.text, self.text_rect)

    def checkForInput(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            return True
        return False
    
    def changeColor(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range (self.rect.top, self.rect.bottom):
            self.text = self.font.render(self.text_input, True, self.hovering_color)
        else:
            self.text = self.font.render(self.text_input, True, self.base_color)

    def is_pressed(self, pos, pressed):
        if self.rect.collidepoint(pos):
            if pressed[0]:
                return True
            return False
        return False
        

    def character_select(self,scale):
        char_sel = True
        choosecharacterbg = pygame.image.load('choosecharbg.jpg')
        title = self.font.render("Choose your story", True, "White")
        title_rect = title.get_rect(x=100, y=100)
        self.screen.blit(choosecharacterbg, (0,0))
        self.screen.blit(title, title_rect)

        #mc_pic = pygame.image.load('mc.png')
      

        #lover_pic = 
        #lover_rect = lover_pic.get_rect(x=300, y=250)

        #villain_pic = pygame.image.load('villain.png')
        #villain_rect = villain_pic.get_rect(x=450, y=250)

        self.scale = scale

        lover = Button(image=pygame.image.load('lover.png'), pos=(0, 0), text_input="LOVER", font=Button.get_font(45), base_color="#d7fcd4", hovering_color="White", scale=0.01)
        lover_scale = pygame.transform.scale(lover.image, (lover.image.get_size()))
        lover_rect = lover_scale.get_rect(x=0, y=0)
        
        mc = Button(image=pygame.image.load('mc.png'), pos=(400, 320), text_input="MC", font=Button.get_font(45), base_color="#d7fcd4", hovering_color="White", scale=0.01)
        mc_button = pygame.image.load('mc.png')
        mc_pic = pygame.surface.Surface(mc_button.get_size())
        mc_rect = mc_pic.get_rect(x=400, y=250)
        
        villain = Button(image=pygame.image.load('villain.png'), pos=(420, 320), text_input="VILLAIN", font=Button.get_font(45), base_color="#d7fcd4", hovering_color="White", scale=0.01)
        villain_button = pygame.image.load('villain.png')
        villain_pic = pygame.surface.Surface(villain_button.get_size())
        villain_rect = villain_pic.get_rect(x=450, y=250)


        back_button = Button(image=pygame.image.load("Play Rect.png"), pos=(400, 400), text_input="BACK", font=Button.get_font(45), base_color="#d7fcd4", hovering_color="White", scale=0.01)
        while char_sel:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    char_sel = False
                    self.running = False

            mouse_pos = pygame.mouse.get_pos()
            mouse_pressed = pygame.mouse.get_pressed()
    
            if back_button.is_pressed(mouse_pos,mouse_pressed):
                Button.main_menu()
            elif mc.is_pressed(mouse_pos,mouse_pressed):
                char_sel = False
                self.char_selection = 1
                print("Proceed to story Chap. 1...")
            elif lover.is_pressed(mouse_pos,mouse_pressed):
                char_sel = False
                self.char_selection = 2
                print("Complete Story : MC...")
            elif villain.is_pressed(mouse_pos,mouse_pressed):
                char_sel = False
                self.char_selection = 3
                print("Complete Story : MC...")
            title = self.font.render("Choose your story", True, "White")
            title_rect = title.get_rect(x=100, y=100)
            choosecharacterbg = pygame.image.load('choosecharbg.jpg')
            if back_button.image is not None:
                self.screen.blit(back_button.image, back_button.rect)
            self.screen.blit(mc.image, mc_rect)
            self.screen.blit(lover.image, lover_rect)
            self.screen.blit(villain.image, villain_rect)
            self.clock.tick(60)
        pygame.display.update()

    def play(self):

        while True:
            play_mouse_pos = pygame.mouse.get_pos()

            config.SCREEN.fill('black')
            button = Button(image=None, pos=(400, 260), text_input="BACK", font=Button.get_font(75), base_color="White", hovering_color="Green", scale = 1)
            button.character_select(scale=1)


            PLAY_BACK = Button(image=None,pos=(400,260),text_input="BACK", font=Button.get_font(75), base_color="White", hovering_color="Green", scale = 1)

            PLAY_BACK.changeColor(play_mouse_pos) 
            PLAY_BACK.update(config.SCREEN)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if PLAY_BACK.checkForInput(play_mouse_pos):
                        Button.main_menu()

            pygame.display.update()

    def get_font(size):
        return pygame.font.Font("ARCADECLASSIC.TTF", size)

    def main_menu():
        pygame.display.set_caption('Main Menu')

        while True:
            config.SCREEN.blit(config.BG, (0, 0))
            MENU_MOUSE_POS = pygame.mouse.get_pos() 

            MENU_TEXT = Button.get_font(100).render("YO1LO", True,"#b68f40")
            MENU_RECT = MENU_TEXT.get_rect(center=(400, 100))   
            PLAY_BUTTON = Button(image=pygame.image.load("Play Rect.png"), pos=(400, 250), text_input="PLAY", font=Button.get_font(75), base_color="#d7fcd4", hovering_color="White", scale = 1)
            QUIT_BUTTON=Button(image=pygame.image.load("Quit Rect.png"), pos=(400,400), text_input="QUIT", font=Button.get_font(75),base_color="#d7fcd4", hovering_color="White", scale = 1)
            
            config.SCREEN.blit(MENU_TEXT, MENU_RECT) 

            for button in [PLAY_BUTTON, QUIT_BUTTON]:
                button.changeColor(MENU_MOUSE_POS)
                button.update(config.SCREEN)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                        PLAY_BUTTON.play()
                    if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                        pygame.quit()
                        sys.exit()

            pygame.display.update()

Button.main_menu()

class Game:
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.char_selection = 3
        self.running = True
        self.font = pygame.font.Font('ARCADECLASSIC.TTF', 32)