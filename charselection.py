import pygame, sys
from button import Button
from main import bgmusic, main_menu


class char_select():
        def __init__(self, title, image, x1, x2, x3, y1, y2, y3):
            pygame.init()
            self.title = title
            self.x1 = x1
            self.x2 = x2
            self.x3 = x3
            self.y1 = y1
            self.y2 = y2
            self.y3 = y3
            self.image = image
            image = pygame.image.load('choosecharbg.jpg')
            self.screen = pygame.display.set_mode((800, 600))
            self.font = pygame.font.Font("ARCADECLASSIC.TTF", 30)
            self.running = True


        def run(self):
            self.char_menu(self.image)
 

        def get_font(size): 
            return pygame.font.Font("assets/font.ttf", size)

        def char_menu(self, image):
       
            pygame.display.set_caption('Character Menu')

            display = self.screen
            mc_pic = pygame.image.load('mc.png')
            bg = pygame.image.load('choosecharbg.jpg')
            size1 = pygame.transform.scale(bg, (1000,600))
            hmm = pygame.display.set_mode((1000,600))
            
            mc_pic = pygame.image.load('mc.png')
            mc_rect = mc_pic.get_rect(x=400,y=95)
            
            lover_pic = pygame.image.load('lover.png')
            lover_rect = mc_pic.get_rect(x=200,y=200)

            villain_pic = pygame.image.load('villain.png')
            villain_rect = mc_pic.get_rect(x=600,y=100)

            bg_rect = size1.get_rect(x=0,y=0)
            title = self.font.render("Choose your character", True, "White")
            title_rect = title.get_rect(x=320, y=100)
            self.screen.blit(title, title_rect)

            while self.running:
                hmm.blit(size1, bg_rect)
                display.blit(mc_pic, mc_rect)
                display.blit(lover_pic, lover_rect)
                display.blit(villain_pic, villain_rect)

                CHAR_MOUSE_POS = pygame.mouse.get_pos()

                BACK_BUTTON = Button(image=pygame.image.load("assets/transparent.png"), pos=(340, 550), 
                            text_input="QUIT", font=char_select.get_font(55), base_color="#d7fcd4", hovering_color="White")
                  
                self.screen.blit(title, title_rect)
                
                for button in [BACK_BUTTON]:
                    button.changeColor(CHAR_MOUSE_POS)
                    button.update(hmm)

                for event in pygame.event.get():

                    if event.type == pygame.QUIT: #if pressing x button on window screen
                        pygame.quit()
                        sys.exit()

                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if BACK_BUTTON.checkForInput(CHAR_MOUSE_POS):
                            main_menu()
                    pygame.display.update()
                    bgmusic.play()

charselect = char_select(title = 'Choose your character', image = pygame.image.load('choosecharbg.jpg'), x1=None, x2=None
                         , x3=None, y1=None, y2=None, y3=None)
charselect.run()
